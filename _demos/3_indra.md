---
layout: page
title: Indra
description: A representation hypothesis for multimodal alignment
importance: 3
category: work
github: https://github.com/Jianglin954/Indra
related_publications: true
---

The Indra Representation Hypothesis asks what it means for representations from
different modalities to be *aligned*. Rather than treating alignment as a property to
be enforced by a contrastive objective, Indra frames it as a structural property that
representations of sufficiently capable models already tend toward — and makes that
structure precise enough to measure {% cite lu2025indra %}.

## The hypothesis

<!-- TODO: replace with the precise statement of the hypothesis from the paper -->

- **Alignment as structure, not as a loss term.** The hypothesis characterizes when
  two modality-specific representation spaces encode the same relational structure.
- **Measurable.** It yields a concrete diagnostic that can be applied to existing
  pretrained encoders, rather than requiring a new training run.
- **Implications for foundation models.** If the hypothesis holds, cross-modal
  alignment can be recovered post hoc, which changes how multimodal systems should be
  assembled.

## Links

- Paper: [arXiv:2604.04496](https://arxiv.org/pdf/2604.04496)
- Code: [github.com/Jianglin954/Indra](https://github.com/Jianglin954/Indra)
