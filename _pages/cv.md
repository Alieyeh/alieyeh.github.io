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
Genomic Data Scientist specialising in secure, scalable health data systems within Trusted Research Environments (TREs). My work spans genomics pipeline engineering, metadata-driven data infrastructure, statistical genetics, and applied machine learning. I focus on building reproducible, governance-aware platforms that enable researchers to move from raw cohort data to reliable analytical outputs efficiently and responsibly.

I combine a background in computer engineering with advanced training in health data science and genomics, allowing me to operate across system architecture, workflow orchestration, statistical modelling, and secure data governance.

---

Current Role
======

**Genomic Data Scientist**  
Dementias Platform UK (DPUK), Swansea University  
2023 – Present  

**Secure Data Infrastructure & Platform Development**
- Contributed to the design and implementation of a scalable genomics ingest and provisioning framework within a national dementia Trusted Research Environment.
- Developed metadata-driven discovery tools to standardise cohort description and improve cross-dataset comparability.
- Implemented structured QC and privacy screening procedures to support responsible onboarding of multi-modal genomic datasets.
- Designed governed data provisioning workflows aligned with Five Safes principles.

**Workflow Engineering & HPC Optimisation**
- Developed and maintained reproducible genomics workflows using Snakemake/Nextflow-style orchestration.
- Optimised Polygenic Risk Score (PRS) pipeline execution on SLURM-based HPC systems, reducing runtime and improving accessibility for non-specialist researchers.
- Implemented containerised execution environments (Singularity/Docker) to ensure cross-platform reproducibility.

**Applied Genomics & Machine Learning**
- Performed region-based association analyses and statistical genetics workflows on large-scale cohorts (e.g., UK Biobank and dementia-focused datasets).
- Designed semi-supervised multi-omic integration approaches for dementia subtyping research.
- Developed privacy-aware evaluation strategies for machine learning models operating on sensitive health data.

**AI Risk & Governance**
- Contributed to a DARE UK–funded initiative examining AI model release risks within TRE environments.
- Evaluated privacy attack vectors (e.g., membership and attribute inference risks) and mitigation strategies.
- Supported practical recommendations for safe AI deployment within secure research platforms.

**Leadership & Mentorship**
- Serving as project lead for a genomics metadata curation and discovery initiative, supervising an intern.
- Contributed to internal training materials and HPC usage guidance for researchers.

---

Previous Experience
======

**Data Scientist – Human Genetics (GSK, complementary role)**  
2021 – 2022  

- Worked on human genetic data applications for drug discovery.
- Conducted annotation and region-based association analyses on large-scale genomic datasets.
- Supported translational research by integrating genetic evidence into target prioritisation workflows.

**Data Scientist – Health Research Project**  
2020 – 2021  

- Developed machine learning models for clinical risk prediction in hospitalised patients.
- Applied survival modelling, decision trees, and rule-mining approaches to structured hospital datasets.
- Contributed to analysis of COVID-19 outcomes in high-risk populations.

**Software & Backend Development (Early Career Roles)**  
2017 – 2019  

- Developed backend systems and database-driven applications.
- Designed relational database schemas and implemented RESTful API-style architectures.
- Gained experience in production-oriented software engineering and structured system design.

---

Education
======

**MSc Health Data Science (Genomics specialisation)**  
University of Exeter, 2022–2023  
- Thesis (in collaboration with GSK): Using human genetic data to inform drug discovery through annotation strategies and region-based association testing.

**BSc Computer Engineering**  
Iran University of Science and Technology, 2016–2021  
- Thesis: Disease prediction using symptom–disease network modelling and probabilistic inference software.

---

Technical Expertise
======

**Workflow & Infrastructure**
- Linux environments, HPC (SLURM), containerisation (Singularity/Docker)
- Reproducible pipeline design (Snakemake, Nextflow-style orchestration)
- Structured data ingest, metadata standardisation, QC automation
- Secure research computing and governed data access frameworks

**Genomics & Statistical Genetics**
- Polygenic Risk Scores (PRS), region-based association tests
- Large-scale cohort analysis (e.g., UK Biobank-scale workflows)
- Multi-omics integration strategies
- Genomic QC and preprocessing toolchains

**Machine Learning & Data Science**
- Semi-supervised learning
- Survival modelling and classification models
- Privacy attack simulation (membership/attribute inference)
- Model evaluation under governance constraints

**Software & Data Engineering**
- Python (pandas, numpy, scikit-learn, PyTorch)
- R for statistical genetics workflows
- SQL and relational database design (ER modelling)
- RESTful design principles
- Unit testing and performance-aware system design

---

Publications & Reports
======
<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

---

Conference Posters & Talks
======
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html  %}
{% endfor %}</ul>

---

Service & Professional Contributions
======
- Contributor to internal training materials on secure genomics workflows and HPC usage.
- Contributor to policy-oriented work on AI risk and responsible data science in secure environments.
- Author of educational material on selecting appropriate genomics datasets for research use cases.
