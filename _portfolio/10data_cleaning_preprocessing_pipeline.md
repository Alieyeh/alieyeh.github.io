---
title: "Mentored Project: Automated Pre-Processing Pipeline for Tabular Health Data"
collection: portfolio
category: software
permalink: /software/data-cleaning-preprocessing-pipeline
excerpt: "Mentoring contribution to an intern project on configuration-driven preprocessing for reproducible cleaning of multimodal tabular health data."
slidesurl: /files/presentations/data_cleaning_preprocessing_pipeline.pdf
---

## Overview

This project was led by Ms Adeoye and carried out by Saad Kiyani as an intern project. My role was as a mentor, supporting the work as it developed within the DPUK Data Portal context.

The pipeline addresses a common problem in health data science: cohort extracts often contain numerical, categorical, date, time, multi-option and free-text fields in the same table, with missing codes, inconsistent labels and mixed formats. If these are cleaned by hand, decisions can become hard to repeat, audit or explain.

## Project Approach

The pipeline uses a configuration-driven approach:

- A YAML file defines the expected columns, data types, aliases, ranges, missing-value codes and validation rules.
- The same input and configuration produce the same cleaned output.
- The output shape is controlled by the reviewed configuration rather than whatever happens to appear in a single extract.
- Config errors, missing columns and unrecognised options produce warnings or failures instead of silent skips.
- Each run records an audit trail, including configuration hash, code version, library versions, row counts, data dictionary and fitted parameters.
- A scaffolding step drafts the configuration from the raw data, but human review is required before release.

## My Role

I did not lead or develop the pipeline. My contribution was mentoring and feedback, with a focus on keeping the project aligned with reproducibility, auditability and secure research data practice.

## Why It Matters

The project shows the value of turning data cleaning into a documented, reviewable and repeatable process. That is especially important in secure research environments where users need to understand how an analysis-ready table was produced, not only receive the cleaned data.

Project showcase: [Automated pre-processing pipeline for multimodal tabular health data](/files/presentations/data_cleaning_preprocessing_pipeline.pdf)

**Tags:** mentoring, Python, YAML, data cleaning, preprocessing, reproducible pipelines, audit trail, tabular health data, DPUK Data Portal
