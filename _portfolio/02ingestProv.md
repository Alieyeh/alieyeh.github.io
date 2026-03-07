---
title: "Secure Genomics Ingest & Provisioning Framework (TRE)"
category: infrastructure
excerpt: "End-to-end framework for onboarding, QC, metadata standardisation and secure provisioning of cohort-scale genomics data in a Trusted Research Environment."
permalink: /infrastructure/ingest-and-provisioning
collection: portfolio
---
<br/><img src='/images/datacheckgenome.jpg'>"
---

**Problem:** Cohort-scale genomics datasets require rigorous QC, consistent structure and governed access to be usable across teams within a Trusted Research Environment.

**What I did:**
- Designed a reusable ingest and provisioning framework covering discovery → QC → organisation standards → controlled provisioning  
- Implemented reproducible, containerised workflows to support consistent execution across compute environments  
- Developed metadata standardisation practices to improve discoverability and downstream usability

### Internal Researcher-Facing Tooling

As part of the genomics ingest and provisioning workflow, I developed internal Streamlit-based interfaces to:

- Facilitate dataset provisioning within the TRE
- Support structured data release workflows
- Enable controlled interaction with harmonised metadata outputs

These tools were designed for internal use and are not publicly available.

**Impact:** Reduced manual onboarding effort, improved reproducibility and analysis readiness, and accelerated time-to-analysis for downstream research teams.

**Tags:** Python · Linux · Streamlit · MinIO · Bash Scripting · genomics tooling (e.g., PLINK/bcftools/QCtool)
