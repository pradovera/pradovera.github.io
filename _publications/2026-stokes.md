---
title: "Accelerating droplet-laden Stokes flow simulations with hierarchical surrogate modeling"
collection: publications
permalink: /publication/2026-stokes
excerpt: 'We present a surrogate modeling strategy for Stokes flows with liquid roplets suspended in a carrier fluid. Our approach is based on a multi-fidelity framework. At the lowest fidelity, droplets are treated as passive tracers, neglecting their influence on the ambient flow field. Building on this approximation, we derive a PDE that represents the current modeling error. This error equation is then solved approximately to correct the flow field and the procedure is iterated. Two fidelities are employed in an alternating fashion: Stokes flow in the absence of droplets and flow around a single droplet in free space. By systematically combining these models, the method captures droplet-flow, droplet-boundary, and droplet-droplet interactions. In this work, the framework is developed and validated for circular, non-deforming droplets in two spatial dimensions. The geometric self-similarity of the droplets allows us to construct an efficient offline-online strategy based on the reuse of precomputed single-droplet solutions. Extensions to deformable droplets are also discussed. Numerical experiments demonstrate the accuracy and efficiency of the proposed surrogate in a variety of tests, including scenarios with up to 10,000 droplets. Notably, we show that the proposed surrogate achieves substantially reduced computational cost compared to fully resolved multi-fluid simulations with state-of-the-art software.'
year: '2027'
status: 'Published'
venue: 'Comput. Methods Appl. Mech. Eng. 464'
author: '**Davide Pradovera**, Thomas Frachon, and Sara Zahedi'
doi: '10.1016/j.cma.2026.119487'
paperurl: 'https://arxiv.org/abs/2607.03301'
label: "main"
---

