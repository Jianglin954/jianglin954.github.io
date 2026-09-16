---
layout: page
title: Restore-R1
description: Image restoration agents trained with MLLM perceptual feedback
importance: 2
category: work
---

Restore-R1 treats image restoration as an agentic decision problem rather than a
single feed-forward mapping. A restoration agent is trained with reinforcement
learning, and the reward signal comes from a multimodal LLM acting as a perceptual
critic — so the agent optimizes for what actually looks restored, not just for
pixel-space distance.

## Approach

<!-- TODO: replace with the actual method description and figures from the paper -->

- **MLLM perceptual feedback.** A multimodal LLM scores restoration quality, giving a
  reward that tracks perceptual judgment more closely than PSNR-style metrics.
- **Reinforcement learning over restoration steps.** The agent chooses how to restore,
  which lets it spend effort where degradation is actually severe.
- **Efficiency as a first-class goal.** The policy is trained to reach good
  restorations without exhausting a fixed heavy pipeline on every input.

Add before/after result figures here — drop the images into `assets/img/` and use:

{% raw %}

```html
<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/restore_before.jpg" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/restore_after.jpg" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">Left: degraded input. Right: Restore-R1 output.</div>
```

{% endraw %}

## Links

- Paper: [CVPR 2026 open access](https://openaccess.thecvf.com/content/CVPR2026F/papers/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.pdf)

Jianglin Lu, Yuanwei Wu, Ziyi Zhao, Hongcheng Wang, Felix Jimenez, Abrar Majeedi, Yun Fu.
*Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with
Multimodal LLM Perceptual Feedback.* CVPR, 2026.
