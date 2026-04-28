---
title: "Research Data Integrity Monitoring System"
collection: portfolio
category: infrastructure
permalink: /infrastructure/file-integrity-monitoring
excerpt: "Automated monitoring system for detecting file deletion, rollback and unexpected modification events in large research storage environments."
---

## Overview

Large shared research storage environments can experience unexpected changes: files may be deleted, overwritten, silently modified or reverted to older versions. In secure genomics and health-data settings, these events affect reproducibility, auditability and trust.

This project provides automated monitoring for unexpected file-state changes across large directory trees.

## My Contribution

- Designed and implemented a Python-based scanning approach for large research storage areas.
- Recorded file metadata and fingerprints to support comparison across scan runs.
- Built detection logic for deletion, modification, rollback and timestamp anomalies.
- Integrated monitoring into scheduled workflows for regular operational checks.
- Produced structured reports to support follow-up and audit conversations.

## Architecture

- Python scanning engine for traversal, metadata capture and comparison.
- SQLite state store for file fingerprints and historical metadata.
- Scheduled automation with `n8n`.
- JSON/CSV-style reporting for operational review.

## Impact

The system gives infrastructure and data teams a practical way to detect unexpected dataset changes, improving operational monitoring and confidence in shared research repositories.

**Tags:** Python, SQLite, n8n, data integrity, monitoring, research infrastructure, metadata, automation
