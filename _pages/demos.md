---
layout: page
title: demos
permalink: /demos/
description: Interactive Video World Model — Amazon AGI Foundations.
nav: true
nav_order: 1
---

During my Applied Scientist internship with the
<a href="https://amazon.jobs/content/en/teams/agi">Amazon AGI Foundations</a> team
(Summer 2026), I worked on an interactive video world model: a video diffusion model
that generates future frames conditioned on the incoming action, so the world can be
steered step by step rather than sampled in one shot.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {%
      include video.liquid
      path="assets/video/clip_00_web_crf26.mp4"
      class="img-fluid rounded z-depth-1"
      controls=true
      autoplay=true
      muted=true
      loop=true
      playsinline=true
    %}
  </div>
</div>
<div class="caption">
  An action-controlled rollout from the video world model.
</div>

- **Data and pipeline.** Built a large-scale Unreal Engine video dataset and the
  accompanying training pipeline for action-controlled video generation.
- **Scaling.** Scaled training from a 1.3B to a 14B bidirectional video diffusion model
  on 32 NVIDIA B200 GPUs.
- **Causal rollout.** Transformed the bidirectional model into a causal architecture so
  frames can be generated autoregressively, which is what makes the model interactive.
- **Fast inference.** Applied few-step diffusion distillation to accelerate sampling.
