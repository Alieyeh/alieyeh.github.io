---
title: "Multimodal Preprocessing Pipeline"
collection: portfolio
category: software
permalink: /software/multimodal-preprocessing-pipeline/
excerpt: "Reproducible Python pipeline for downloading, harmonising, preprocessing, validating and reporting on multimodal time-series datasets for downstream machine learning use."
---

## Multimodal Preprocessing Pipeline

A reproducible preprocessing pipeline for multimodal physiological and activity datasets, covering PAMAP2, WISDM, EEGMMIDB, PTB-XL and optional mHealth data.

The project separates setup, preprocessing, validation and reporting into clear command-line stages, with Python implementations behind lightweight shell and PowerShell entrypoints.

### What It Does

- Downloads and organises public multimodal datasets
- Harmonises human activity recognition labels and schemas
- Preprocesses HAR, EEG and ECG data into analysis-ready arrays
- Generates manifests, summaries, validation reports and resource estimates
- Supports resumable preprocessing for interrupted runs
- Includes unit and smoke tests for automated verification

### Technical Highlights

- Python package structure under `src/mmprep`
- Dataset-specific preprocessing modules for HAR, EEG and ECG
- Fixed-shape `float32` outputs with aligned metadata CSVs
- Validation checks for schema integrity, metadata consistency and sample-pack outputs
- Cross-platform wrappers for Windows PowerShell and Unix-like shells

### Repository

GitHub repository:  
[github.com/Alieyeh/Multimodal-Preprocessing-Pipeline](https://github.com/Alieyeh/Multimodal-Preprocessing-Pipeline)

**Tags:** Python, reproducible pipelines, multimodal time-series, EEG, ECG, HAR, data validation, automated testing
