---
title: "Research Data Integrity Monitoring System"
collection: portfolio
category: infrastructure
permalink: /infrastructure/file-integrity-monitoring
excerpt: "Automated monitoring system for detecting deletion, rollback and unexpected modification events in large shared research storage environments."
---

## Overview

Shared research storage can change in ways that are hard to notice: files can be deleted, overwritten, modified silently or reverted to older versions. In secure genomics and health data settings, these events affect reproducibility, auditability and trust.

This project provides scheduled monitoring for unexpected file-state changes across large directory trees.

## My Contribution

- Designed and implemented a Python scanning approach for large research storage areas.
- Recorded file metadata and fingerprints to compare storage state across scan runs.
- Built detection logic for deletion, modification, rollback and timestamp anomalies.
- Integrated monitoring into scheduled workflows for routine operational checks.
- Produced structured outputs that support follow-up, triage and audit conversations.

## Architecture

- Python scanning engine for traversal, metadata capture and comparison
- SQLite state store for file fingerprints and historical metadata
- Scheduled automation with `n8n`
- JSON and CSV reporting for operational review

## Impact

The system gives data and infrastructure teams a practical way to detect unexpected dataset changes and maintain confidence in shared research repositories.

**Tags:** Python, SQLite, n8n, data integrity, monitoring, research infrastructure, metadata, automation
