---
layout: page
title: demos
permalink: /demos/
nav: true
nav_order: 1
---

<!-- ── Demo 1 (autoplays on load) ──────────────────────────── -->
<div class="demo-item">
  <div class="caption">
    During my internship with the <a href="https://amazon.jobs/content/en/teams/agi">Amazon AGI Foundations Team</a>, I worked on an interactive video world model: a video diffusion model that generates future frames conditioned on the incoming action, so the world can be steered step by step rather than sampled in one shot.
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

<!-- ── Demo 2 (placeholder — replace path, poster and caption) ─ -->
<div class="demo-item">
  <div class="caption">
    Project Two Title @ <a href="#">Affiliation</a>.
  </div>
  <div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
      {%
        include video.liquid
        path="assets/video/clip_00_web_crf26.mp4"
        poster="assets/img/video_posters/clip_00_web_crf26.jpg"
        class="img-fluid rounded z-depth-1"
        preload="metadata"
        controls=true
        muted=true
        loop=true
        playsinline=true
      %}
    </div>
  </div>
</div>

<hr class="demo-divider" />

<!-- ── Demo 3 ─────────────────────────────────────────────── -->
<div class="demo-item">
  <div class="caption">
    During my internship with the <a href="https://research.adobe.com/">Adobe Research Team</a>, I worked on quality-controllable visual retrieval (<a href="https://arxiv.org/pdf/2602.21175">ICLR 2026</a>): a lightweight language model refines a short query at a requested aesthetic and relevance level, so the quality of what CLIP-based retrieves is steered through words alone rather than by retraining the computationally expensive retrieval model. See <a href="https://jianglin954.github.io/QCQC/">[Webpage]</a> and <a href="https://jianglin954.github.io/QCQC/demo/index.html">[Live Demo]</a> for details.
  </div>
  <div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
      {%
        include video.liquid
        path="assets/video/demo_video.mp4"
        poster="assets/img/video_posters/demo_video.jpg"
        class="img-fluid rounded z-depth-1"
        preload="metadata"
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
</style>

<script>
  // Only the demo closest to the middle of the viewport plays; the rest stay
  // paused on their poster, so the browser never decodes more than one clip.
  (function () {
    const videos = Array.from(document.querySelectorAll(".demo-item video"));
    if (!videos.length || !("IntersectionObserver" in window)) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    const MIN_VISIBLE = 0.25;
    const ratios = new Map(videos.map((video) => [video, 0]));
    let active = null;

    function activate(video) {
      if (active === video) return;
      active = video; // set first, so the pauses below aren't read as user intent
      videos.forEach((other) => {
        if (other !== video && !other.paused) other.pause();
      });
      if (!video.dataset.userPaused) {
        const started = video.play();
        if (started) started.catch(function () {});
      }
    }

    function deactivate() {
      if (!active) return;
      const leaving = active;
      active = null;
      leaving.pause();
      delete leaving.dataset.userPaused; // a manual pause only lasts while in view
    }

    videos.forEach((video) => {
      video.addEventListener("pause", () => {
        if (video === active && !video.ended) video.dataset.userPaused = "1";
      });
      video.addEventListener("play", () => {
        delete video.dataset.userPaused;
        activate(video);
      });
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => ratios.set(entry.target, entry.intersectionRatio));

        let best = null;
        let bestRatio = 0;
        ratios.forEach((ratio, video) => {
          if (ratio > bestRatio) {
            bestRatio = ratio;
            best = video;
          }
        });

        if (best && bestRatio >= MIN_VISIBLE) activate(best);
        else deactivate();
      },
      { threshold: [0, 0.1, 0.25, 0.5, 0.75, 1] }
    );

    videos.forEach((video) => observer.observe(video));
  })();
</script>
