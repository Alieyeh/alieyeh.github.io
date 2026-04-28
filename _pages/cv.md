---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Professional Summary
======

Genomic data scientist specialising in reproducible bioinformatics, secure research data infrastructure and applied biomedical data science. My work spans genomics ingest and provisioning, metadata systems, statistical genetics, workflow engineering, and practical tools for researchers working with sensitive health and omics data.

I combine a computer engineering background with MSc training in health data science and genomics, allowing me to work across software design, HPC workflows, data governance, statistical analysis and researcher-facing documentation.

---

Current Role
======

**Genomic Data Scientist**  
Dementias Platform UK (DPUK), Swansea University  
2023 - Present

**Secure Data Infrastructure and Platform Development**
- Designed and implemented genomics ingest and provisioning workflows within a dementia-focused Trusted Research Environment.
- Developed metadata and tagging structures to improve dataset classification, discovery and feasibility assessment.
- Built QC, validation and privacy-aware handling processes for onboarding genomics and multi-omics datasets.
- Supported governed data provisioning workflows aligned with secure research principles.
- Contributed to database, dashboard and visualisation work for researcher-facing feasibility and discovery tools.
- Authored documentation and SOP-style guidance for repeatable data onboarding and provisioning processes.

**Workflow Engineering and HPC**
- Developed and maintained reproducible genomics workflows for secure Linux and SLURM-based environments.
- Improved polygenic risk score pipeline execution through parallelisation, resource-aware configuration and clearer documentation.
- Used containerised execution patterns with Singularity and Docker to support reproducibility.
- Implemented automated integrity monitoring to detect unexpected file changes or version drift in shared research storage.

**Applied Genomics and Machine Learning**
- Worked on statistical genetics and genomic analysis workflows across large cohort datasets.
- Developed exploratory multi-omic approaches for dementia subtyping and patient stratification research.
- Contributed to privacy-aware evaluation and governance thinking for AI models in sensitive health data settings.

**Leadership and Knowledge Exchange**
- Supervising intern work on omics metadata discovery infrastructure.
- Delivered and contributed to training materials on HPC usage, workflow execution and secure data handling.
- Collaborated with researchers, governance specialists, clinicians and infrastructure engineers to translate research needs into practical workflows.

---

Previous Experience
======

**Data Scientist - Human Genetics, GSK**

2023

- Performed region-based association analyses using UK Biobank whole-genome sequencing data.
- Developed Python-based annotation and processing workflows for rare non-coding genomic regions.
- Integrated Python and REGENIE workflows into HPC-based statistical genetics analyses.
- Worked within a regulated pharmaceutical research environment alongside geneticists and computational scientists.

**Health Data Scientist - Clinical Machine Learning Research**

2021 - 2022

- Developed machine learning models for clinical outcome prediction using hospital patient datasets.
- Performed feature engineering, model evaluation and interpretation under appropriate research governance.
- Contributed to manuscript preparation for a peer-reviewed COVID-19 mortality prediction study.

---

Education
======

**MSc Health Data Science (Genomics)**

University of Exeter, 2022 - 2023
- Thesis in collaboration with GSK: using human genetic data to inform drug discovery through annotation strategies and region-based association testing.

**BSc Computer Engineering**

Iran University of Science and Technology, 2016 - 2021
- Thesis: disease prediction using symptom-disease network modelling and probabilistic inference software.

---

Technical Expertise
======

**Workflow and Infrastructure**
- Linux environments, HPC with SLURM, Docker, Singularity
- Reproducible workflow design with Nextflow/Snakemake-style orchestration
- Genomics ingest, QC, metadata standardisation and governed provisioning
- Trusted Research Environments and secure research workflows

**Genomics and Statistical Genetics**
- Polygenic risk scores, region-based association testing and variant annotation
- Whole-genome sequencing and cohort-scale genomics workflows
- PLINK, bcftools, QCtool, REGENIE and related genomics tooling
- Multi-omics integration concepts and exploratory analysis

**Machine Learning and Data Science**
- scikit-learn, PyTorch, pandas, numpy and R
- Classification, clustering, feature engineering and model evaluation
- Survival analysis and clinical prediction modelling experience
- Privacy-aware evaluation in sensitive health data settings

**Software and Data Engineering**
- Python, R, SQL, Bash, Java
- PostgreSQL, relational database design and ER modelling
- Streamlit, Plotly, Matplotlib and dashboard-oriented communication
- Git, testing, documentation and research software packaging

---

Publications and Reports
======
<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

---

Conference Posters and Talks
======
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html  %}
{% endfor %}</ul>

---

Service and Professional Contributions
======
- Contributor to internal training materials on secure genomics workflows and HPC usage.
- Contributor to policy-oriented work on AI risk and responsible data science in secure environments.
- Author of educational material on selecting appropriate genomics datasets for research use cases.
- ONS Safe Researcher accredited.
