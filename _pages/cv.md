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

Health and genomics data scientist with a computer engineering background and experience building Python workflows, validation tooling, metadata systems and reproducible pipelines for complex biomedical datasets in secure research environments.

My work covers genomics ingest, QC, metadata harmonisation, data integrity monitoring, PRS workflows, statistical genetics, governed provisioning, applied machine learning and researcher-facing documentation. I am strongest where scientific requirements, infrastructure constraints and governance expectations need to become practical, reliable data workflows.

---

Current Role
======

**Genomic Data Scientist**  
Dementias Platform UK (DPUK), Swansea University  
2023 - Present

**Genomic data systems and secure infrastructure**
- Design and maintain genomics ingest, QC, metadata harmonisation and provisioning workflows for WGS, array, methylation and multi-omics datasets.
- Build validation scripts and operational checks for file structure, metadata completeness, privacy readiness and analysis readiness.
- Develop metadata frameworks, tagging systems and discovery structures that make heterogeneous omics datasets easier to find, compare and use.
- Support governed provisioning workflows that connect dataset discovery, quality checking, access approvals and secure downstream analysis.
- Produce SOP-style documentation and researcher guidance to support traceability and reproducible use of platform workflows.

**Workflow engineering and bioinformatics**
- Develop reproducible workflows for secure Linux and SLURM-based environments using Python, R, containers and Nextflow-style orchestration.
- Improve polygenic risk score workflow execution through SLURM parallelisation, containerised execution patterns, PLINK and Python/R support scripts.
- Test and debug workflow updates before wider deployment, with attention to runtime, output validation, usability and reproducibility.
- Implement automated integrity monitoring to detect unexpected file deletion, modification, rollback or version drift in shared research storage.

**Applied genomics and data science**
- Work on statistical genetics and WGS analysis workflows across cohort-scale datasets.
- Develop exploratory multi-omic approaches for dementia subtyping and patient stratification research.
- Contribute to privacy-aware evaluation and governance thinking for AI models in sensitive health data settings.

**Collaboration and knowledge exchange**
- Collaborate with researchers, clinicians, epidemiologists, governance specialists and infrastructure engineers to translate research needs into practical workflows.
- Supervise intern work on omics metadata discovery infrastructure.
- Deliver and contribute to training materials on HPC usage, workflow execution, output checking and secure data handling.
- Published a Real World Data Science guide giving researchers a practical framework for selecting genomic datasets responsibly and efficiently.

---

Previous Experience
======

**Data Scientist - Human Genetics, GSK**

2023

- Performed region-based association analyses using UK Biobank whole-genome sequencing data.
- Developed Python-based annotation and processing workflows for rare non-coding genomic regions.
- Integrated Python and REGENIE workflows into HPC-based statistical genetics analyses.
- Supported QC, interpretation and communication of statistical genetics outputs in a regulated pharmaceutical research setting.

**Health Data Scientist - Clinical Machine Learning Research**

2021 - 2022

- Developed machine learning models for predicting in-hospital mortality in COVID-19 patients with diabetes using structured hospital datasets.
- Performed feature engineering, classification modelling, model evaluation and performance analysis under ethical approval.
- Co-authored a peer-reviewed publication in the Journal of Diabetes and Metabolic Disorders.

---

Education
======

**MSc Health Data Science, Genomics**

University of Exeter, 2022 - 2023
- Thesis in collaboration with GSK: using human genetic data to inform drug discovery through annotation strategies and region-based association testing.

**BSc Computer Engineering**

Iran University of Science and Technology, 2016 - 2021
- Thesis: disease prediction using symptom-disease network modelling and probabilistic inference software.

---

Technical Expertise
======

**Programming and engineering**
- Python, R, SQL, Bash, Java, C/C++, Git, Linux, CLI wrappers, package development and automated scripting

**Bioinformatics and statistical genetics**
- WGS, rare variant annotation, PRS, GWAS, region-based association testing, PLINK, bcftools, REGENIE, GATK and QCtool

**Workflows and infrastructure**
- SLURM, Nextflow-style workflow design, Snakemake, Docker, Singularity, n8n, MinIO and reproducible pipeline development

**Data systems and governance**
- PostgreSQL, SQL Server, MongoDB, ER modelling, metadata schemas, dataset tagging, Trusted Research Environments and disclosure control

**Analysis and visualisation**
- pandas, scipy, scikit-learn, PyTorch, Streamlit, R Shiny, PowerBI, Plotly, matplotlib and seaborn

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
- Contributor to training materials on secure genomics workflows, HPC usage and output checking.
- Contributor to policy-oriented work on AI risk and responsible data science in secure environments.
- Author of a published Real World Data Science guide on selecting appropriate genomic datasets for research use cases.
- ONS Safe Researcher accredited.
