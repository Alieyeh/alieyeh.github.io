---
title: "Multimodal Preprocessing Pipeline"
collection: portfolio
category: software
permalink: /software/multimodal-preprocessing-pipeline/
excerpt: "Reproducible Python preprocessing pipeline for public HAR, EEG and ECG datasets with validation, reporting and command-line workflows."
---

## Overview

This public ETL-style Python pipeline downloads, transforms, harmonises and validates multimodal physiological and activity datasets for downstream machine learning experiments. It covers public HAR, EEG and ECG datasets such as PAMAP2, WISDM, EEGMMIDB and PTB-XL.

The project is designed around clear command-line stages for setup, preprocessing, validation and reporting, with Python implementations behind lightweight shell and PowerShell entrypoints.

## What It Does

- Downloads and organises public multimodal datasets
- Harmonises human activity recognition labels and schemas
- Preprocesses HAR, EEG and ECG data into analysis-ready arrays
- Generates manifests, summaries, validation reports and resource estimates
- Supports resumable preprocessing for interrupted runs
- Includes unit and smoke tests for automated verification

## Technical Highlights

- Python package structure under `src/mmprep`
- Dataset-specific preprocessing modules for HAR, EEG and ECG
- Fixed-shape `float32` outputs with aligned metadata CSVs
- Validation checks for schema integrity, metadata consistency and sample-pack outputs
- Cross-platform wrappers for Windows PowerShell and Unix-like shells

## Why It Matters

The project demonstrates research software engineering beyond one-off notebooks: repeatable processing, testable outputs, clear interfaces and enough validation for other users to understand what the pipeline produced.

This is an independent open-source project. There are plans to make the pipeline available to researchers through DPUK, but it is not currently presented as a DPUK-developed or deployed system.

## Repository

GitHub repository: [github.com/Alieyeh/Multimodal-Preprocessing-Pipeline](https://github.com/Alieyeh/Multimodal-Preprocessing-Pipeline)

**Tags:** Python, ETL, reproducible pipelines, multimodal time-series, EEG, ECG, HAR, CLI tooling, validation, automated testing
