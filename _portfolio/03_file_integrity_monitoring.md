---
title: "Research Data Integrity Monitoring System"
collection: portfolio
category: infrastructure
permalink: /infrastructure/file-integrity-monitoring
excerpt: "Two operational architectures for detecting deletion, reversion, movement and unexpected modification across large secure research storage environments."
---

## Overview

Shared research storage can change in ways that are hard to notice: files can be deleted, overwritten, modified silently or reverted to older versions. In secure genomics and health data settings, these events affect reproducibility, auditability and trust.

This project provides scheduled monitoring for unexpected file and directory state changes across large directory trees. It has two implementations: an original Python scanner orchestrated with `n8n`, and a newer Python-only package that replaces the external workflow while retaining the same operational purpose.

## My Contribution

- Designed and implemented a Python scanning approach for large research storage areas.
- Built the original scheduled implementation with Python, SQLite and `n8n`.
- Re-engineered the workflow as a standalone, installable Python package and CLI with no runtime dependencies or internet calls.
- Recorded file and directory metadata, sampled fingerprints and bounded history in SQLite to compare storage state across runs.
- Built risk-ranked detection for deletion, modification, moves, renames, timestamp anomalies and exact or metadata-supported version reversion.
- Added configurable exclusions, internal repeat and weekly scheduling, tests, transactional state updates and offline operator reports.

## Original n8n Architecture

- Python scanning engine for traversal, metadata capture and comparison
- SQLite state store for file fingerprints and historical metadata
- Scheduled automation with `n8n`
- JSON and CSV reporting for operational review

## Python-Only Architecture

- Installable `file-watch` package and CLI using only the Python standard library at runtime
- Single pruned `os.scandir` traversal with metadata-first mode for very large TRE shares
- Optional sampled fingerprints, parallel fingerprint jobs and explicit visibility of files without fingerprint coverage
- Batched SQLite upserts and one transaction per completed baseline to avoid partial state
- Direct file and directory baselines, including empty-directory monitoring
- Offline HTML, text, CSV and compact JSON reports with stable risk-ranked event types
- Platform scheduling, internal interval scheduling or a pure-Python weekly loop
- Unit and workflow tests, deployment guidance and performance documentation

## Impact

The two versions demonstrate both workflow integration and subsequent architectural simplification. The Python-only implementation removes the external orchestration dependency while adding a packaged interface, richer event classification, deployment controls and operator-focused reporting suitable for secure offline environments.

## Repository

- [Python-only implementation](https://github.com/Alieyeh/File_Integrity_Check/tree/python-only)

**Tags:** Python, SQLite, n8n, CLI, data integrity, monitoring, research infrastructure, metadata, automation, testing, Trusted Research Environments
