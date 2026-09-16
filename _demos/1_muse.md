---
layout: page
title: MUSE
description: A unified agentic harness for multimodal large language models
importance: 1
category: work
github: https://github.com/Jianglin954/MUSE
---

MUSE is a unified agentic harness for multimodal large language models. Instead of
wiring a new scaffold for every task, MUSE gives an MLLM a single interface through
which it can perceive, call tools, and act — so the same harness carries over across
perception, reasoning, and generation workloads.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {%
      include video.liquid
      path="assets/video/clip_00_web_crf26.mp4"
      class="img-fluid rounded z-depth-1"
      controls=true
      muted=true
      loop=true
    %}
  </div>
</div>
<div class="caption">
    MUSE in action: the harness drives an MLLM through a multi-step task end to end.
</div>

## What it does

<!-- TODO: replace with the actual capability list from the paper -->

- **One harness, many tasks.** A single agent loop covers tool use, multi-step
  perception, and long-horizon reasoning, rather than one bespoke scaffold per benchmark.
- **Model-agnostic.** The harness sits above the MLLM, so swapping the underlying
  model does not require rewriting the agent logic.
- **Inspectable traces.** Every step the agent takes is recorded, which makes failure
  cases easy to replay and diagnose.

## Links

- Paper: [arXiv:2606.03005](https://arxiv.org/abs/2606.03005)
- Code: [github.com/Jianglin954/MUSE](https://github.com/Jianglin954/MUSE)

Jianglin Lu, Hailing Wang, Xu Ma, Qihua Dong, Mingyuan Zhang, Yizhou Wang, Yun Fu.
*MUSE: A Unified Agentic Harness for MLLMs.* arXiv, 2026.
