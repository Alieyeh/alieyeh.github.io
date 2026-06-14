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
- Extended an existing imaging-only provisioning system to support genomics, updating its MinIO-backed storage, dataset tagging and project-approval controls.
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
- Developed and compared dementia classifiers using Random Forest, SVM, XGBoost and neural-network approaches under different privacy controls, including AI-SDC safe wrappers and synthetic-data variants.
- Ran membership inference, LiRA/likelihood, worst-case, attribute and structural privacy attacks, and prototyped a Concrete-ML homomorphic-encryption route.
- Used the technical findings to contribute to DARE UK recommendations on safe AI development, model release and synthetic data in sensitive health environments.

**Collaboration and knowledge exchange**
- Collaborate with researchers, clinicians, epidemiologists, governance specialists and infrastructure engineers to translate research needs into practical workflows.
- Supervise intern work on omics metadata discovery infrastructure.
- Produced the HPC training component of the [DPUK Induction for Approved Users](https://dataciseopenlearning.org/courses/dementias-platform-uk-induction-approved-users/), supporting practical use of secure research computing and reproducible workflow execution.
- Published a Real World Data Science guide giving researchers a practical framework for selecting genomic datasets responsibly and efficiently.

---

Previous Experience
======

**Human Genetics Data Science Placement, GSK**

2023

- Developed a Python and pandas workflow to annotate chromosome-scale UK Biobank WGS variants against the Ensembl GRCh38 Regulatory Build.
- Prepared regulatory annotations and rare-variant masks for two-step REGENIE region-based association testing across binary and quantitative traits on GSK HPC.
- Analysed association outputs by regulatory element, allele-frequency threshold, phenotype and effect direction, producing summary tables, forest plots and Manhattan plots.
- Used SQL to compare significant non-coding region signals with existing WES/GWAS evidence and linked regions to nearby protein-coding genes.
- Delivered annotation catalogues, association results and visualisations, and prepared a technical report and final presentation for the GSK Human Genetics team.

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
- Industry-linked thesis with GSK Human Genetics: annotated UK Biobank WGS rare non-coding variants using the Ensembl GRCh38 Regulatory Build and ran REGENIE region-based association tests to explore gene-phenotype evidence for drug discovery.

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
- SLURM, Nextflow-style workflow design, Snakemake, Docker, Singularity, n8n, MinIO, ETL and reproducible pipeline development

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
- Training author for the HPC component of the [DPUK Induction for Approved Users](https://dataciseopenlearning.org/courses/dementias-platform-uk-induction-approved-users/).
- Technical contributor and co-author on DARE UK work covering AI privacy attacks, safe model release, synthetic data and responsible AI development in secure environments.
- Author of a published Real World Data Science guide on selecting appropriate genomic datasets for research use cases.
- ONS Safe Researcher accredited.
