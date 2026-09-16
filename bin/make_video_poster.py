#!/usr/bin/env python3
"""Grab the first frame of a video as a JPEG poster.

No ffmpeg required: renders the frame in headless Chrome, then downscales with PIL.

Usage:
    python3 bin/make_video_poster.py assets/video/clip_00_web_crf26.mp4 [more.mp4 ...]

Writes assets/img/video_posters/<basename>.jpg (max width 960px).
"""

import os
import shutil
import struct
import subprocess
import sys
import tempfile

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "assets", "img", "video_posters")
SEEK_SECONDS = 0.05
MAX_WIDTH = 960
JPEG_QUALITY = 82


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("error: no Chrome/Chromium binary found")


def iter_boxes(fh, start, end):
    """Yield (type, offset, header_size, size) for each MP4 box in [start, end)."""
    pos = start
    while pos < end - 8:
        fh.seek(pos)
        header = fh.read(8)
        if len(header) < 8:
            return
        size = struct.unpack(">I", header[:4])[0]
        box_type = header[4:8]
        header_size = 8
        if size == 1:  # 64-bit extended size
            size = struct.unpack(">Q", fh.read(8))[0]
            header_size = 16
        elif size == 0:  # box runs to end of file
            size = end - pos
        if size < header_size:
            return
        yield box_type, pos, header_size, size
        pos += size


def video_size(path):
    """Read display width/height from the MP4 track header.

    Walks the box tree rather than scanning bytes, because `moov` may sit after
    `mdat` (a non-faststart file), and a byte scan would then match junk inside
    the media data.
    """
    total = os.path.getsize(path)
    with open(path, "rb") as fh:
        for box, off, hsize, size in iter_boxes(fh, 0, total):
            if box != b"moov":
                continue
            for box2, off2, hsize2, size2 in iter_boxes(fh, off + hsize, off + size):
                if box2 != b"trak":
                    continue
                for box3, off3, hsize3, size3 in iter_boxes(fh, off2 + hsize2, off2 + size2):
                    if box3 != b"tkhd":
                        continue
                    fh.seek(off3 + hsize3)
                    body = fh.read(size3 - hsize3)
                    version = body[0]
                    # flags + (creation, modification, track id, reserved, duration)
                    skip = 4 + (32 if version == 1 else 20)
                    skip += 8 + 2 + 2 + 2 + 2 + 36  # reserved, layer, group, volume, matrix
                    w, h = struct.unpack(">II", body[skip : skip + 8])
                    w, h = w >> 16, h >> 16
                    if w and h:  # skip audio/subtitle tracks, which report 0x0
                        return w, h
    return 1920, 1080


def capture(chrome, video_path, width, height, png_out):
    page = """<!doctype html>
<html><body style="margin:0;padding:0;background:#000;overflow:hidden">
<video id="v" src="{src}" width="{w}" height="{h}" muted preload="auto"
       style="display:block;width:{w}px;height:{h}px"></video>
<script>
  const v = document.getElementById('v');
  v.addEventListener('loadeddata', () => {{ v.currentTime = {t}; }});
</script>
</body></html>
""".format(src="file://" + video_path, w=width, h=height, t=SEEK_SECONDS)

    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "frame.html")
        with open(html, "w") as fh:
            fh.write(page)
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--no-sandbox",
                "--disable-gpu",
                "--hide-scrollbars",
                "--allow-file-access-from-files",
                "--autoplay-policy=no-user-gesture-required",
                "--window-size={},{}".format(width, height),
                "--virtual-time-budget=15000",
                "--screenshot=" + png_out,
                "file://" + html,
            ],
            check=True,
            capture_output=True,
        )


def main(paths):
    chrome = find_chrome()
    os.makedirs(OUT_DIR, exist_ok=True)
    for rel in paths:
        src = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
        if not os.path.exists(src):
            sys.exit("error: no such video: " + src)
        w, h = video_size(src)
        stem = os.path.splitext(os.path.basename(src))[0]
        dst = os.path.join(OUT_DIR, stem + ".jpg")
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "frame.png")
            capture(chrome, src, w, h, png)
            img = Image.open(png).convert("RGB")
            if img.width > MAX_WIDTH:
                img = img.resize(
                    (MAX_WIDTH, round(img.height * MAX_WIDTH / img.width)),
                    Image.LANCZOS,
                )
            img.save(dst, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
        print(
            "{} -> {} ({}x{}, {:.0f} KB)".format(
                rel, os.path.relpath(dst, REPO), img.width, img.height,
                os.path.getsize(dst) / 1024,
            )
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
