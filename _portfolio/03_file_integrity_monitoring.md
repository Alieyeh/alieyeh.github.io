---
title: "Research Data Integrity Monitoring System"
collection: portfolio
category: infrastructure
permalink: /portfolio/file-integrity-monitoring/
excerpt: "Automated monitoring system for detecting file deletion, rollback and corruption events in large research storage systems."
---

## Research Data Integrity Monitoring System

Large research data repositories can occasionally experience unexpected issues such as files disappearing, reverting to older versions, or being modified without traceability. In a secure research environment handling large-scale genomics and health datasets, these issues can have serious implications for reproducibility, auditing, and research reliability.

To address this, I designed and implemented a **file integrity monitoring system** capable of detecting anomalous changes across very large directory trees.

The system automatically scans storage environments and records file metadata and content fingerprints, enabling detection of unexpected changes such as file deletion, rollback to previous versions, or silent modification.

### Key Features

- Detection of:
  - deleted files
  - file content changes
  - version rollbacks
  - modification timestamp anomalies

- Designed to scale to **multi-terabyte research storage systems**

- Efficient scanning using:
  - metadata-first traversal
  - partial hashing for large files
  - parallel hashing workers

- Automated monitoring through scheduled workflows

### System Architecture

The system integrates three main components:

**Python scanning engine**

- Traverses directory trees
- records metadata and fingerprints
- compares results to previous scan state

**Workflow automation**

- scheduled monitoring using `n8n`
- execution orchestration
- alert and report generation

**State tracking**

- SQLite database stores file fingerprints and metadata history

This architecture allows efficient monitoring of large storage systems without excessive compute or disk overhead.

### Technical Stack

- Python
- SQLite
- n8n workflow automation
- JSON/CSV reporting
- parallel hashing and metadata-first scanning

### Impact

This system provides an automated way to detect unexpected changes in research data environments, improving:

- traceability
- data reliability
- governance auditing
- operational monitoring

It is particularly useful in large research platforms where datasets are shared across many teams and infrastructure changes may otherwise go unnoticed.

### Repository

GitHub repository:  
**github.com/Alieyeh/file_integrity_check**
