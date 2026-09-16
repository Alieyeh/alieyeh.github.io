---
title: "DPUK Omics Metadata Atlas and Feasibility Tool"
collection: portfolio
category: infrastructure
permalink: /infrastructure/omics-metadata-discovery
excerpt: "A scoped research software and metadata infrastructure project for non-disclosive omics dataset discovery, feasibility assessment and governance-aware catalogue development."
slidesurl: /files/presentations/Amarachi_Njoku_Showcase_Presentation.pptx
---

## Overview

Large research platforms often hold valuable genomics and multi-omics datasets, but the information needed to assess them can be scattered across documentation, file manifests, project records, public pages, file headers and informal notes.

That creates a practical barrier for researchers: before applying for access, they need to know whether a dataset exists, what assay and file types it contains, whether the technical context fits their method, what governance constraints apply, and where the metadata is still incomplete.

This project scopes a DPUK Omics Metadata Atlas: a FAIR, non-disclosive metadata catalogue and discovery prototype for dementia omics datasets. The focus is dataset-level and aggregate technical metadata, not participant-level values.

The same thinking is reflected in my published Real World Data Science guide on genomic dataset selection, which sets out a five-pillar framework for evaluating discovery, governance, assay choice, cohort context and quality-control readiness.

## Project Scope

The improved 12-week intern plan turns a broad idea into a realistic research software build. The target output is a minimum viable metadata product rather than an over-extended all-modality platform.

The planned scope includes:

- A high-level inventory of available DPUK omics records, with blocked or unavailable sources logged clearly.
- Deeper pilot extraction for 5-8 representative datasets across two priority modalities.
- A standards-aligned metadata profile covering discovery, technical context, governance, provenance, quality and interoperability fields.
- A reproducible ingestion and validation workflow that records source, extraction method, confidence, review status and last updated date for each field.
- A queryable catalogue with search, filters, dataset detail pages, completeness views, gap reports and non-disclosive exports.
- An evaluation pack covering coverage, extraction accuracy, metadata completeness, usability and performance.
- A JOSS-ready research software paper package, conference abstract and handover materials.

## My Contribution

- Reframed the project from an ambitious all-modality build into a focused, deliverable research software plan.
- Defined the metadata model around cohorts, datasets, experiments, file sets, quality summaries, publications, provenance and standards mappings.
- Set out the feasibility workflow researchers need before formal access applications.
- Specified the technical architecture for curation, validation, database loading, API access and dashboard exploration.
- Built the intern delivery plan with weekly gates, acceptance criteria, risk controls, paper evidence and role-relevant outputs.
- Kept NLP and LLM-assisted extraction as optional support, with manual review and field-level provenance as the authoritative route.

## Technical Design

The following is the planned implementation stack for the supervised intern project. I designed the project scope, architecture, delivery gates and acceptance criteria; these components are intended to be built and evaluated by the intern during the 12-week placement rather than representing software I have already implemented:

- Python package and CLI for ingestion, validation and reproducible catalogue builds
- Pydantic models and JSON schema for executable metadata definitions
- PostgreSQL database with indexed search and JSONB support for modality-specific fields
- SQLAlchemy and Alembic for database models and migrations
- FastAPI service with OpenAPI documentation for reusable catalogue access
- Streamlit or Dash dashboard for rapid delivery of the researcher-facing discovery interface
- Docker Compose, pytest, GitHub Actions and MkDocs or Sphinx documentation for maintainability and paper readiness

The metadata profile is aligned where practical with GA4GH ExpMeta, Bioschemas Dataset, RO-Crate and ELIXIR metadata guidance, while staying realistic for DPUK governance and available source material.

## Phase 1 Implementation

Phase 1 was delivered as an intern project by Amarachi Njoku under my project leadership. The showcase presentation documents a metadata standardisation pipeline that turns fragmented omics descriptions into validated, Gen3-ready metadata.

The Phase 1 work:

- Catalogued the available picture across five omics data types.
- Fully standardised three data types end to end as a proof of method.
- Used a common metadata spine with modality-specific extensions.
- Applied Pydantic validation, controlled vocabularies and explicit handling of unknown values.
- Carried provenance, confidence and transformation notes with the metadata rather than hiding uncertainty.
- Reported completeness for the pilot outputs, including 96.6% for genotyping, 100% for methylation and 82.1% for GWAS, with essential fields complete across the pilot.

Phase 1 showcase: [Building an Omics Data Discovery Pipeline](/files/presentations/Amarachi_Njoku_Showcase_Presentation.pptx)

## Feasibility Workflow

The tool is designed to help a researcher answer the questions that usually come before an access request:

- Which cohorts have data for this modality or assay type?
- Are the file formats, genome build, platform or processing details suitable for the planned analysis?
- Is only high-level, non-disclosive information being shown?
- Which fields are verified, candidate, missing or blocked?
- What source supports each metadata field?
- Which datasets are worth pursuing through formal governance routes?

This makes the tool useful both for researchers and for data stewards. Researchers get a clearer pre-application view, while the platform can see where metadata quality needs improvement.

## Discovery Views

The planned dashboard focuses on four decision-support views:

- Search and filter table for cohort, modality, assay, file format and access-route discovery
- Dataset detail page showing canonical metadata, provenance, caveats and missing fields
- Cohort by modality heatmap showing availability and metadata completeness
- Metadata gap report ranking missing required fields and low-completeness datasets

The API documentation is treated as part of the product, so future developers and data stewards can reuse the catalogue beyond the first dashboard.

## Status

Project plan completed and Phase 1 proof of method delivered through a supervised intern project. The current next step is to connect automated storage discovery to the standardisation workflow, load standardised metadata into the shared discovery system and extend the method across remaining data types.

**Tags:** metadata, Python, PostgreSQL, FastAPI, Pydantic, FAIR data, dataset discovery, omics, governance, provenance, Trusted Research Environments, research software
