---
title: "Polygenic Risk Score Pipeline on SLURM HPC"
category: research
excerpt: "Re-architected and documented a PRS workflow for scalable, reproducible execution across large cohort datasets in a secure research environment."
collection: portfolio
permalink: /research/prs-pipeline
---

<br/><img src="/images/prsflow.jpg" alt="Polygenic risk score workflow">

## Overview

Polygenic risk score analyses can be difficult for research teams to run consistently at cohort scale, particularly in secure HPC environments where reproducibility, documentation and resource use all matter.

This project improved the execution strategy and usability of a PRS workflow for dementia and psychiatric disease research.

## My Contribution

- Reviewed the existing workflow and identified bottlenecks in HPC execution.
- Reworked job configuration and parallelisation patterns for SLURM.
- Improved documentation so non-specialist researchers could run analyses more independently.
- Supported migration toward more reproducible workflow orchestration.
- Validated outputs to preserve consistency while improving runtime.

## Outcome

The changes reduced large-cohort runtime from days or weeks to hours in practical use cases, while improving usability and reproducibility for researchers working inside the secure platform.

## Technical Scope

- SLURM job orchestration
- Containerised execution patterns
- PRS workflow documentation
- PLINK and related genomics tools
- Python/R support scripts
- Nextflow-oriented workflow design

**Tags:** SLURM, Linux, Nextflow, containers, Python, R, PLINK, PRS, reproducible workflows, genomics
