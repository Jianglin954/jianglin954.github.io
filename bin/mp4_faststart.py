#!/usr/bin/env python3
"""Move an MP4's `moov` atom in front of `mdat` so it can stream progressively.

Browsers cannot start playback until they have read `moov`. When `moov` sits at
the end of the file, the player must first fetch the tail (or, where range
requests are unavailable, the whole file), which shows up as a video that never
starts and a play button that appears to do nothing.

This is a pure-Python equivalent of `qt-faststart` / `ffmpeg -movflags +faststart`,
for machines with no ffmpeg. Chunk offset tables (`stco`/`co64`) are rewritten by
the number of bytes the media data shifts.

Usage:
    python3 bin/mp4_faststart.py assets/video/demo_video.mp4 [more.mp4 ...]

Files already in faststart order are left untouched. Rewrites in place via a
temporary file, so an interrupted run cannot leave a half-written video behind.
"""

import os
import struct
import sys
import tempfile

CONTAINER_ATOMS = {b"moov", b"trak", b"mdia", b"minf", b"stbl", b"edts", b"udta"}


def parse_boxes(data, start=0, end=None):
    """Yield (type, offset, header_size, size) for boxes in a bytes buffer."""
    if end is None:
        end = len(data)
    pos = start
    while pos < end - 8:
        size = struct.unpack(">I", data[pos : pos + 4])[0]
        box_type = bytes(data[pos + 4 : pos + 8])  # bytes(), so bytearray slices hash
        header_size = 8
        if size == 1:
            size = struct.unpack(">Q", data[pos + 8 : pos + 16])[0]
            header_size = 16
        elif size == 0:
            size = end - pos
        if size < header_size:
            return
        yield box_type, pos, header_size, size
        pos += size


def shift_chunk_offsets(moov, delta):
    """Return `moov` with every stco/co64 entry moved by `delta` bytes."""
    buf = bytearray(moov)

    def walk(start, end):
        for box, off, hsize, size in parse_boxes(buf, start, end):
            if box in CONTAINER_ATOMS:
                walk(off + hsize, off + size)
            elif box in (b"stco", b"co64"):
                body = off + hsize + 4  # skip version/flags
                count = struct.unpack(">I", buf[body : body + 4])[0]
                entry = body + 4
                width = 4 if box == b"stco" else 8
                fmt = ">I" if box == b"stco" else ">Q"
                for i in range(count):
                    at = entry + i * width
                    value = struct.unpack(fmt, buf[at : at + width])[0] + delta
                    if box == b"stco" and value > 0xFFFFFFFF:
                        raise ValueError(
                            "chunk offset overflows 32-bit stco; needs co64 conversion"
                        )
                    buf[at : at + width] = struct.pack(fmt, value)

    walk(0, len(buf))
    return bytes(buf)


def faststart(path):
    with open(path, "rb") as fh:
        data = fh.read()

    boxes = list(parse_boxes(data))
    order = [box.decode("latin1") for box, _, _, _ in boxes]
    if not any(b == b"moov" for b, _, _, _ in boxes):
        return "no moov atom, skipped ({})".format(" ".join(order))
    if not any(b == b"mdat" for b, _, _, _ in boxes):
        return "no mdat atom, skipped ({})".format(" ".join(order))

    moov_index = next(i for i, (b, _, _, _) in enumerate(boxes) if b == b"moov")
    mdat_index = next(i for i, (b, _, _, _) in enumerate(boxes) if b == b"mdat")
    if moov_index < mdat_index:
        return "already faststart ({})".format(" ".join(order))

    _, moov_off, _, moov_size = boxes[moov_index]
    moov = shift_chunk_offsets(data[moov_off : moov_off + moov_size], moov_size)

    # ftyp must stay first; moov goes immediately after it, everything else keeps
    # its original order. Only bytes after the insertion point move, by moov_size.
    head = b""
    rest = []
    for i, (box, off, _, size) in enumerate(boxes):
        chunk = data[off : off + size]
        if i == moov_index:
            continue
        if box == b"ftyp" and not head:
            head = chunk
        else:
            rest.append(chunk)

    out_dir = os.path.dirname(os.path.abspath(path))
    mode = os.stat(path).st_mode & 0o7777
    fd, tmp = tempfile.mkstemp(dir=out_dir, suffix=".faststart.mp4")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(head)
            fh.write(moov)
            for chunk in rest:
                fh.write(chunk)
        os.chmod(tmp, mode)  # mkstemp creates 0600; keep the original permissions
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    new_order = [b.decode("latin1") for b, _, _, _ in parse_boxes(open(path, "rb").read())]
    return "{} -> {}".format(" ".join(order), " ".join(new_order))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for target in sys.argv[1:]:
        print("{}: {}".format(target, faststart(target)))
