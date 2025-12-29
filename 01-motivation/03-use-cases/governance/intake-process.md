# Use Case Intake Process

## Overview

This document defines how new AI use cases enter the transformation programme pipeline.

## Intake Channels

1. **Strategic initiatives** - Top-down from executive/strategy
2. **Business requests** - Bottom-up from business units
3. **Technology enablement** - Platform capabilities seeking use cases
4. **External drivers** - Regulatory, competitive, market changes

## Submission Requirements

New use cases must provide:

| Field | Required | Description |
|-------|----------|-------------|
| Name | Yes | Short descriptive name |
| Problem statement | Yes | What problem does this solve? |
| Proposed solution | Yes | High-level AI approach |
| Business sponsor | Yes | Executive owner |
| Estimated value | Yes | Qualitative (H/M/L) or quantitative |
| Target users | Yes | Who benefits? |
| Data requirements | No | Key data sources needed |
| Constraints | No | Regulatory, technical, timing |

## Intake Workflow

```
Submission → Initial Review → DVF Assessment → Backlog/Reject
    │              │                │               │
    │         (48 hrs)          (1 week)        Decision
    │              │                │           documented
    │              ▼                ▼               │
    └──────► pipeline/1-intake → pipeline/2-assess ─┘
```

## Submission Template

New intake items should be created in `pipeline/1-intake/` using filename:
`INTAKE-YYYY-MM-DD-short-name.md`

## SLA

| Stage | Target Duration |
|-------|-----------------|
| Initial review | 48 hours |
| DVF assessment | 1 week |
| Backlog placement | 2 weeks from submission |
