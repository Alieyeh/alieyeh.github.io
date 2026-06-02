---
title: "Polygenic Risk Score Pipeline on SLURM HPC"
category: research
excerpt: "PRS workflow engineering for scalable, documented and reproducible cohort-level execution in secure HPC environments."
collection: portfolio
permalink: /research/prs-pipeline
---

<br/><img src="/images/prsflow.jpg" alt="Polygenic risk score workflow">

## Overview

Polygenic risk score analyses can be difficult to run consistently at cohort scale, especially inside secure HPC environments where reproducibility, documentation, resource use and output validation all matter.

This project improves the execution strategy and usability of a PRS workflow for dementia and psychiatric disease research.

## My Contribution

- Reviewed workflow bottlenecks and reworked execution patterns for SLURM.
- Improved job configuration, parallelisation and resource-aware execution.
- Developed a Nextflow-oriented version using containerised execution patterns, PLINK and Python/R support scripts.
- Improved documentation so non-specialist researchers could run and check analyses more independently.
- Tested and debugged workflow updates with attention to runtime, output validation and reproducibility.

## Outcome

Earlier optimisation work reduced large-cohort runtime from weeks to hours in practical use cases. Current work focuses on testing, debugging and documenting the workflow before wider deployment inside the secure research platform.

## Technical Scope

- SLURM job orchestration
- Nextflow-style workflow design
- Containerised execution patterns
- PLINK and PRS tooling
- Python and R support scripts
- Output validation and researcher guidance

**Tags:** SLURM, Linux, Nextflow, containers, Python, R, PLINK, PRS, reproducible workflows, genomics
