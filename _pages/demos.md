---
layout: page
title: demos
permalink: /demos/
nav: true
nav_order: 1
---

<!-- ── Demo 1 (autoplays on load) ──────────────────────────── -->
<div class="demo-item" id="video-world-model">
  <div class="caption">
    During my internship at <a href="https://amazon.jobs/content/en/teams/agi">Amazon AGI Foundations</a>, I worked on an interactive video world model: a video diffusion model that generates future frames conditioned on the incoming action, so the world can be steered step by step rather than sampled in one shot.
  </div>
  <div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
      {%
        include video.liquid
        path="assets/video/clip_00_web_crf26.mp4"
        poster="assets/img/video_posters/clip_00_web_crf26.jpg"
        class="img-fluid rounded z-depth-1"
        preload="metadata"
        autoplay=true
        controls=true
        muted=true
        loop=true
        playsinline=true
      %}
    </div>
  </div>
</div>

<hr class="demo-divider" />

<!-- ── Demo 2 (before/after slider) ───────────────────────── -->
<div class="demo-item" id="restore-r1">
  <div class="caption">
    During my internship at <a href="https://aws.amazon.com/">Amazon</a>, I worked on Restore-R1 (<a href="https://openaccess.thecvf.com/content/CVPR2026F/papers/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.pdf">CVPR 2026</a>): an image restoration agent that judges a degraded photo with a multimodal LLM and learns, through reinforcement learning, which restoration tools to call and in what order.
  </div>
  <div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
      <figure class="image-compare" style="--pos: 0%; --hide: 100%; --fade: 0">
        <div class="image-compare-strip rounded z-depth-1">
          <div class="image-compare-panel" style="flex-grow: 0.625">
            <img
              src="{{ 'assets/img/039_LQ.png' | relative_url }}"
              width="640"
              height="1024"
              loading="lazy"
              decoding="async"
              alt="Degraded input: a lightning storm shot through heavy rain streaks and sensor noise."
            />
            <div class="image-compare-reveal">
              <img
                src="{{ 'assets/img/039_ours.png' | relative_url }}"
                width="640"
                height="1024"
                loading="lazy"
                decoding="async"
                alt="Restore-R1 output: the same lightning photograph with the rain streaks and noise removed."
              />
            </div>
            <div class="image-compare-line" aria-hidden="true"><span class="image-compare-grip"></span></div>
          </div>
          <div class="image-compare-panel" style="flex-grow: 1.0">
            <img
              src="{{ 'assets/img/093_LQ.png' | relative_url }}"
              width="1024"
              height="1024"
              loading="lazy"
              decoding="async"
              alt="Degraded input: a glass skyscraper obscured by rain streaks and sensor noise."
            />
            <div class="image-compare-reveal">
              <img
                src="{{ 'assets/img/093_ours.png' | relative_url }}"
                width="1024"
                height="1024"
                loading="lazy"
                decoding="async"
                alt="Restore-R1 output: the same skyscraper with the rain streaks and noise removed."
              />
            </div>
            <div class="image-compare-line" aria-hidden="true"><span class="image-compare-grip"></span></div>
          </div>
          <span class="image-compare-tag image-compare-tag-left">Restore-R1</span>
          <span class="image-compare-tag image-compare-tag-right">Low quality</span>
          <input
            class="image-compare-range"
            type="range"
            min="0"
            max="100"
            step="0.1"
            value="0"
            aria-label="Drag right to reveal the restored images"
          />
        </div>
        <figcaption class="caption">Drag the slider to reveal the restored images.</figcaption>
      </figure>
    </div>
  </div>
</div>

<hr class="demo-divider" />

<!-- ── Demo 3 ─────────────────────────────────────────────── -->
<div class="demo-item">
  <div class="caption">
    During my internship at <a href="https://research.adobe.com/">Adobe Research</a>, I worked on quality-controllable visual retrieval (<a href="https://arxiv.org/pdf/2602.21175">ICLR 2026</a>): a lightweight language model refines a short query at a requested aesthetic and relevance level, so the quality of what CLIP-based retrieves is steered through words alone rather than by retraining the computationally expensive retrieval model. See <a href="https://jianglin954.github.io/QCQC/">[Webpage]</a> and <a href="https://jianglin954.github.io/QCQC/demo/index.html">[Live Demo]</a> for details.
  </div>
  <div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
      {%
        include video.liquid
        path="assets/video/demo_video.mp4"
        poster="assets/img/video_posters/demo_video.jpg"
        class="img-fluid rounded z-depth-1"
        preload="metadata"
        autoplay=true
        controls=true
        muted=true
        loop=true
        playsinline=true
      %}
    </div>
  </div>
</div>

<style>
  .demo-item {
    margin-bottom: 0.5rem;
    scroll-margin-top: 66px; /* the theme only sets this on headings; clears the fixed navbar */
  }
  .demo-item .caption {
    margin-bottom: 0.75rem;
  }
  .demo-item figure {
    margin-bottom: 0;
  }
  .demo-divider {
    margin: 2.5rem auto;
    width: 83.333%; /* aligns with the col-sm-10 video column */
    border: 0;
    border-top: 1px solid var(--global-divider-color);
    opacity: 0.6;
  }

  /* Before/after slider. --pos is how much of the restored image is revealed. */
  .image-compare {
    margin: 0;
  }
  /* One strip, one slider: the panels butt up against each other with no gap and
     share a single --pos, so both wipes move together. */
  .image-compare-strip {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    gap: 0;
    overflow: hidden;
    line-height: 0;
    touch-action: pan-y; /* a vertical swipe still scrolls the page */
    -webkit-user-select: none;
    user-select: none;
  }
  .image-compare-strip:focus-within {
    outline: 2px solid var(--global-theme-color);
    outline-offset: 2px;
  }
  .image-compare-panel {
    position: relative;
    flex-basis: 0; /* widths come from flex-grow, i.e. from each pair's aspect ratio */
    min-width: 240px; /* below this the two stack instead of getting unreadably narrow */
  }
  .image-compare-strip img {
    display: block;
    width: 100%;
    height: auto;
  }
  .image-compare-reveal {
    position: absolute;
    inset: 0;
    /* Deliberately no arithmetic here: jekyll-minifier, which only runs for
       JEKYLL_ENV=production, rewrites the "--" of a custom property inside an
       arithmetic expression into two minus signs and the declaration is dropped.
       JS hands us finished values instead. */
    clip-path: inset(0 var(--hide) 0 0);
  }
  .image-compare-line {
    position: absolute;
    top: 0;
    bottom: 0;
    left: var(--pos);
    width: 2px;
    margin-left: -1px;
    background: #fff;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.6);
    pointer-events: none;
    /* At rest the second panel's line would land on the seam and read as a gutter
       between the photos, so the wipes only appear once you engage the slider. */
    opacity: var(--fade);
    transition: opacity 0.15s ease;
  }
  .image-compare-strip:hover .image-compare-line,
  .image-compare-strip:focus-within .image-compare-line {
    opacity: 1;
  }
  .image-compare-grip {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2.25rem;
    height: 2.25rem;
    transform: translate(-50%, -50%);
    border: 2px solid #fff;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.35);
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.6);
  }
  .image-compare-grip::before,
  .image-compare-grip::after {
    content: "";
    position: absolute;
    top: 50%;
    width: 0;
    height: 0;
    border-top: 5px solid transparent;
    border-bottom: 5px solid transparent;
    transform: translateY(-50%);
  }
  .image-compare-grip::before {
    left: 0.45rem;
    border-right: 6px solid #fff;
  }
  .image-compare-grip::after {
    right: 0.45rem;
    border-left: 6px solid #fff;
  }
  .image-compare-tag {
    position: absolute;
    top: 0.5rem;
    padding: 0.1rem 0.45rem;
    border-radius: 0.2rem;
    background: rgba(0, 0, 0, 0.55);
    color: #fff;
    font-size: 0.7rem;
    line-height: 1.6;
    letter-spacing: 0.02em;
    pointer-events: none;
  }
  .image-compare-tag-left {
    left: 0.5rem;
    /* nothing is revealed at position 0, so fade this label in as the drag starts */
    opacity: var(--fade);
  }
  .image-compare-tag-right {
    right: 0.5rem;
  }
  /* An invisible full-size range gives us drag, touch and keyboard for free. */
  .image-compare-range {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    opacity: 0;
    cursor: ew-resize;
    -webkit-appearance: none;
    appearance: none;
    background: transparent;
  }
  .image-compare-range::-webkit-slider-runnable-track {
    height: 100%;
  }
  .image-compare-range::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 2.5rem;
    height: 100%;
    border: 0;
  }
  .image-compare-range::-moz-range-track {
    height: 100%;
  }
  .image-compare-range::-moz-range-thumb {
    width: 2.5rem;
    height: 100%;
    border: 0;
    border-radius: 0;
  }
</style>

<script>
  // Only the most visible demo plays; the rest stay paused on their poster, so the
  // browser never decodes more than one clip at a time.
  (function () {
    const videos = Array.from(document.querySelectorAll(".demo-item video"));
    if (!videos.length || !("IntersectionObserver" in window)) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    const MIN_VISIBLE = 0.25;
    const ratios = new Map(videos.map((video) => [video, 0]));
    let active = null;

    function mostVisible() {
      let best = null;
      let bestRatio = 0;
      ratios.forEach((ratio, video) => {
        if (ratio > bestRatio) {
          bestRatio = ratio;
          best = video;
        }
      });
      return bestRatio >= MIN_VISIBLE ? best : null;
    }

    // Visibility is the single source of truth: recompute the winner, pause everyone
    // else. More than one video carries the autoplay attribute, and those play events
    // land after the first observer callback, so this has to be re-runnable.
    function apply() {
      const want = mostVisible();
      active = want; // set first, so the pauses below aren't read as user intent
      videos.forEach((video) => {
        if (video !== want && !video.paused) video.pause();
      });
      if (want && want.paused && !want.dataset.userPaused) {
        const started = want.play();
        if (started) started.catch(function () {});
      }
    }

    videos.forEach((video) => {
      video.addEventListener("pause", () => {
        if (video === active && !video.ended) video.dataset.userPaused = "1";
      });
      video.addEventListener("play", () => {
        delete video.dataset.userPaused;
        if (video !== active) apply(); // autoplay on an off-screen demo, or a stray play
      });
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          ratios.set(entry.target, entry.intersectionRatio);
          // a manual pause only lasts while the demo is on screen
          if (entry.intersectionRatio < MIN_VISIBLE) delete entry.target.dataset.userPaused;
        });
        apply();
      },
      { threshold: [0, 0.1, 0.25, 0.5, 0.75, 1] }
    );

    videos.forEach((video) => observer.observe(video));
  })();
</script>

<script>
  // Before/after slider: the range input drives --pos, which clips the top image.
  (function () {
    document.querySelectorAll(".image-compare").forEach(function (widget) {
      const range = widget.querySelector(".image-compare-range");
      if (!range) return;
      const sync = function () {
        const pos = Number(range.value);
        widget.style.setProperty("--pos", pos + "%"); // where the wipe line sits
        widget.style.setProperty("--hide", 100 - pos + "%"); // how much to clip away
        widget.style.setProperty("--fade", Math.min(1, pos / 12.5)); // label/line fade-in
      };
      range.addEventListener("input", sync);
      sync(); // soft reloads restore the old value, so seed --pos from the input
    });
  })();
</script>
