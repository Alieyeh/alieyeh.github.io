---
title: "Rare Non-Coding Variant Analysis for Drug Discovery"
collection: portfolio
category: research
permalink: /research/genetics-drug-discovery
excerpt: "UK Biobank WGS project annotating rare non-coding regulatory variants and testing aggregate associations with binary and quantitative traits."
---

## Overview

This completed MSc industry placement with GSK Human Genetics investigated whether rare non-coding regulatory variants could provide useful gene-phenotype evidence for drug discovery.

The project used UK Biobank whole-genome sequencing data and the Ensembl GRCh38 Regulatory Build. Rare variants were grouped by regulatory function, tested for aggregate association with binary and quantitative traits, and compared with existing WES and GWAS evidence.

## My Contribution

- Developed and tested a Python and pandas workflow to annotate chromosome-scale UK Biobank WGS variant files against the Ensembl GRCh38 Regulatory Build.
- Processed large variant files in chunks, applied the supplied quality-exclusion list, and produced filtered and reformatted annotation catalogues.
- Quantified annotation coverage, regulatory-element distributions and overlaps across enhancers, promoters, CTCF-binding sites, transcription-factor binding sites and open-chromatin regions.
- Converted the annotations into REGENIE inputs and ran two-step region-based association tests for 31 binary and 45 quantitative traits on the GSK HPC environment.
- Used rare-variant masks across multiple allele-frequency thresholds and analysed significant outputs by regulatory class, phenotype and effect direction.
- Linked significant regions to nearby protein-coding genes and used SQL to cross-reference the results with existing WES and GWAS gene-trait evidence.
- Produced summary tables, forest plots, Manhattan plots and an evidence package for review by the GSK Human Genetics team.

## Technical Approach

- **Annotation:** Python, pandas, chromosome-level processing and Ensembl GRCh38 regulatory features
- **Association testing:** REGENIE step 1 and step 2, binary and quantitative traits, rare-variant masks and batch execution
- **Evidence integration:** nearest-gene mapping and SQL queries against available WES/GWAS evidence
- **Analysis:** summary statistics, regulatory-element overlap analysis, forest plots and Manhattan plots
- **Infrastructure:** Linux HPC, Bash scripts and large genomic file handling

## Delivery and Judgement

The original scope included a second annotation catalogue. When REGENIE runtimes and the wider analysis proved more demanding than expected, I worked with my supervisors to prioritise a complete Ensembl-based annotation, association-testing and GWAS-mapping workflow over a broader set of unfinished outputs.

The completed deliverables included the annotation catalogue, filtered datasets, REGENIE outputs, significant-association tables, nearest-gene information, GWAS mappings, summary statistics and visualisations, alongside a technical report and final presentation prepared for GSK.

## Interpretation

The work produced exploratory evidence about rare non-coding regulatory regions and their relationship with common traits. The project did not treat preliminary signals as confirmed drug targets. Conditional analysis, stronger variant-to-gene mapping and replication would be required before making causal or novel-association claims.

## Repository

Anonymised analysis code: [github.com/Alieyeh/UKB-analysis](https://github.com/Alieyeh/UKB-analysis)

**Tags:** WGS, UK Biobank, rare non-coding variants, regulatory genomics, Ensembl Regulatory Build, REGENIE, region-based association testing, Python, pandas, Bash, SQL, HPC, statistical genetics, drug discovery
