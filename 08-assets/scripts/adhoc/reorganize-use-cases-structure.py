"""
Reorganize Use Cases Structure

This script creates a new enhanced structure for the AI transformation programme
and migrates existing use case files into the appropriate locations.

Structure created:
- governance/       Programme governance documents
- planning/         Annual, quarterly, and wave planning
- pipeline/         Use case lifecycle stages (intake → deployed)
- use-cases/        Detailed specifications (existing UC-XXX folders)
- patterns/         Architecture patterns (existing PT-XXX folders)
- data/             Structured data (master, scoring, financial, operational)
- reports/          Generated views and dashboards

Usage:
    python reorganize-use-cases-structure.py [--dry-run]

Options:
    --dry-run   Show what would be created/moved without making changes
"""

import os
import shutil
import argparse
import csv
from pathlib import Path
from datetime import datetime


# =============================================================================
# STRUCTURE DEFINITION
# =============================================================================

FOLDER_STRUCTURE = {
    "governance": [
        "prioritisation-framework.md",
        "intake-process.md",
        "stage-gate-criteria.md",
        "roles-responsibilities.md",
        "review-cadence.md",
    ],
    "planning/annual/FY2025": [
        "annual-plan.md",
        "portfolio-scorecard.md",
        "investment-thesis.md",
    ],
    "planning/annual/FY2026": [],
    "planning/annual/FY2027": [],
    "planning/quarterly/FY2025-Q1": [
        "quarterly-review.md",
        "pipeline-status.md",
        "decisions.md",
    ],
    "planning/quarterly/FY2025-Q2": [],
    "planning/quarterly/FY2025-Q3": [],
    "planning/quarterly/FY2025-Q4": [],
    "planning/quarterly/FY2026-Q1": [],
    "planning/quarterly/FY2026-Q2": [],
    "planning/waves/wave-1-foundation": [
        "wave-plan.md",
        "dependencies.md",
        "success-criteria.md",
    ],
    "planning/waves/wave-2-scale": [],
    "planning/waves/wave-3-optimize": [],
    "pipeline/1-intake": [],
    "pipeline/2-assess": [],
    "pipeline/3-backlog": [],
    "pipeline/4-planned": [],
    "pipeline/5-active": [],
    "pipeline/6-deployed": [],
    "pipeline/7-retired": [],
    "use-cases": [],  # Existing UC-XXX folders will be moved here
    "patterns": [],   # Existing PT-XXX folders will be moved here
    "data/master": [
        "use-case-registry.csv",
        "pattern-catalog.csv",
        "capability-mapping.csv",
    ],
    "data/scoring": [
        "dvf-scores.csv",
        "wsjf-scores.csv",
        "strategic-alignment.csv",
        "dependency-matrix.csv",
    ],
    "data/financial": [
        "cost-estimates.csv",
        "benefit-projections.csv",
        "actuals-tracking.csv",
        "roi-analysis.csv",
    ],
    "data/operational": [],  # Existing CSV files will be moved here
    "reports": [
        "portfolio-heatmap.md",
        "dependency-graph.md",
        "resource-demand.md",
        "benefit-tracker.md",
    ],
}


# =============================================================================
# TEMPLATE CONTENT
# =============================================================================

def get_template_content(filename: str, base_path: Path) -> str:
    """Generate template content for new files."""

    templates = {
        # Governance templates
        "prioritisation-framework.md": """# Prioritisation Framework

## Overview

This document defines the methodology for scoring and prioritising AI use cases
within the BNZ AI Transformation Programme.

## Scoring Methodology

### Stage 1: DVF Pre-Filter (Desirability, Viability, Feasibility)

All incoming use cases are assessed against three dimensions:

| Dimension | Question | Score Range |
|-----------|----------|-------------|
| **Desirability** | Do customers/users want this? | 1-3 |
| **Viability** | Does it make business sense? | 1-3 |
| **Feasibility** | Can we build it? | 1-3 |

**Pass threshold**: DVF composite score ≥ 6/9

### Stage 2: WSJF Prioritisation (Weighted Shortest Job First)

Use cases passing DVF are ranked using WSJF:

```
WSJF = (User Value + Time Criticality + Risk Reduction) / Job Size
```

| Factor | Description | Scale |
|--------|-------------|-------|
| User/Business Value | Revenue, cost savings, experience improvement | 1-10 |
| Time Criticality | Regulatory deadline, competitive pressure, decay | 1-10 |
| Risk Reduction/Opportunity Enablement | Platform enablement, risk mitigation | 1-10 |
| Job Size | Effort estimate (T-shirt: S=2, M=5, L=8, XL=13) | 2-13 |

### Stage 3: Strategic Alignment

Final prioritisation considers alignment with annual strategic themes:
- Theme weight × WSJF score = Final Priority Score

## Decision Authority

| Decision | Authority | Forum |
|----------|-----------|-------|
| DVF assessment | Use Case Owner + Architecture | Weekly intake |
| WSJF scoring | Programme Office | Quarterly review |
| Wave commitment | Executive Sponsor | Annual planning |
| Reprioritisation | Architecture Review Board | Quarterly review |

## Related Documents

- [Intake Process](intake-process.md)
- [Stage Gate Criteria](stage-gate-criteria.md)
- [Review Cadence](review-cadence.md)
""",

        "intake-process.md": """# Use Case Intake Process

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
""",

        "stage-gate-criteria.md": """# Stage Gate Criteria

## Overview

Use cases progress through defined stages with explicit criteria for advancement.

## Stage Definitions

### Gate 1: Intake → Assess

**Criteria:**
- [ ] Submission complete (all required fields)
- [ ] Business sponsor identified
- [ ] No duplicate of existing use case
- [ ] Within programme scope

**Artifacts:** Intake form complete

---

### Gate 2: Assess → Backlog

**Criteria:**
- [ ] DVF score ≥ 6/9
- [ ] Architecture patterns identified
- [ ] No blocking dependencies
- [ ] Rough cost estimate available

**Artifacts:** DVF scorecard, pattern mapping

---

### Gate 3: Backlog → Planned

**Criteria:**
- [ ] WSJF score calculated
- [ ] Ranked in top N for wave capacity
- [ ] Resources identified (not committed)
- [ ] Executive sponsor approval

**Artifacts:** WSJF score, wave assignment

---

### Gate 4: Planned → Active

**Criteria:**
- [ ] Detailed delivery plan approved
- [ ] Resources committed
- [ ] Dependencies resolved or mitigated
- [ ] Success metrics defined

**Artifacts:** Delivery plan, resource plan, success criteria

---

### Gate 5: Active → Deployed

**Criteria:**
- [ ] Solution deployed to production
- [ ] User acceptance complete
- [ ] Operational handover complete
- [ ] Benefits baseline established

**Artifacts:** Deployment sign-off, operational runbook

---

### Gate 6: Deployed → Benefits Realised

**Criteria:**
- [ ] Benefits measured at 3/6/12 months
- [ ] ROI calculated vs business case
- [ ] Lessons learned documented

**Artifacts:** Benefits realisation report

## Stage Regression

Use cases may move backwards if:
- Dependencies become blocked
- Resources are reallocated
- Strategic priorities change
- Technical blockers emerge

All regressions must be documented in quarterly decisions.
""",

        "roles-responsibilities.md": """# Roles and Responsibilities

## Overview

RACI matrix for AI Transformation Programme prioritisation activities.

## Key Roles

| Role | Description |
|------|-------------|
| **Executive Sponsor** | Budget holder, final prioritisation authority |
| **Programme Director** | Day-to-day programme management |
| **Architecture Lead** | Technical feasibility, pattern selection |
| **Use Case Owner** | Business case, benefits realisation |
| **Enterprise Architect** | Assigned architect per use case |
| **Programme Office** | Scoring, tracking, reporting |

## RACI Matrix

| Activity | Exec Sponsor | Programme Dir | Arch Lead | UC Owner | EA | PMO |
|----------|:------------:|:-------------:|:---------:|:--------:|:--:|:---:|
| Annual planning | A | R | C | I | I | C |
| Quarterly review | A | R | C | C | I | R |
| DVF assessment | I | I | A | R | R | C |
| WSJF scoring | A | C | C | C | I | R |
| Wave commitment | A | R | C | I | I | C |
| Intake triage | I | A | R | C | C | R |
| Benefits tracking | A | C | I | R | I | R |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

## Decision Forums

| Forum | Frequency | Chair | Purpose |
|-------|-----------|-------|---------|
| Intake Review | Weekly | Programme Dir | Triage new submissions |
| Architecture Review | Fortnightly | Arch Lead | Technical assessment |
| Quarterly Review | Quarterly | Exec Sponsor | Reprioritisation |
| Annual Planning | Annual | Exec Sponsor | Strategic priorities |
""",

        "review-cadence.md": """# Review Cadence

## Overview

Defines the rhythm of planning and review activities for the AI Transformation Programme.

## Annual Cycle (Financial Year)

| Month | Activity | Output |
|-------|----------|--------|
| **October** | Strategic direction setting | Investment thesis draft |
| **November** | Portfolio scoring & ranking | Annual plan draft |
| **December** | Budget allocation & wave planning | Annual plan final |
| **January** | Wave 1 kickoff (new FY) | Delivery commences |

## Quarterly Cycle

| Week | Activity | Owner | Output |
|------|----------|-------|--------|
| **1** | Collect delivery status | PMO | Pipeline status |
| **2** | Score new intake items | EA + UC Owner | DVF scores |
| **3** | Re-rank backlog | PMO + Arch Lead | Updated WSJF |
| **4** | Executive review & decisions | Exec Sponsor | Decisions log |

### Quarterly Review Agenda

1. **Delivery progress** (30 min)
   - Active use cases status
   - Blockers and risks
   - Resource utilisation

2. **Pipeline health** (20 min)
   - Intake volume and quality
   - Stage distribution
   - Aging items

3. **Reprioritisation** (40 min)
   - New high-priority items
   - Deprioritisation candidates
   - Wave adjustments

4. **Decisions & actions** (30 min)
   - Document all changes
   - Assign owners
   - Communicate outcomes

## Monthly Check-in

| Activity | Frequency | Duration |
|----------|-----------|----------|
| Intake triage | Weekly | 30 min |
| Delivery standup | Weekly | 30 min |
| Architecture review | Fortnightly | 1 hour |
| Stakeholder update | Monthly | 30 min |

## Calendar Template

```
         Q1              Q2              Q3              Q4
    ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
    │ Review  │     │ Review  │     │ Review  │     │ Review  │
    │ Week 4  │     │ Week 4  │     │ Week 4  │     │ + Annual│
    └─────────┘     └─────────┘     └─────────┘     │ Planning│
                                                     └─────────┘
```
""",

        # Planning templates
        "annual-plan.md": """# Annual Plan - {fy}

## Executive Summary

[High-level summary of the year's AI transformation priorities]

## Strategic Context

### Business Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

### Technology Themes
1. [Theme 1]
2. [Theme 2]
3. [Theme 3]

## Portfolio Overview

| Metric | Value |
|--------|-------|
| Total use cases | XX |
| Planned for delivery | XX |
| Estimated investment | $X.XM |
| Expected benefits | $X.XM |

## Wave Allocation

### Wave 1: Foundation (Q1-Q3)
| UC ID | Name | Investment | Expected Benefit |
|-------|------|------------|------------------|
| UC-XXX | [Name] | $XXXk | $X.XM |

### Wave 2: Scale (Q4-Q3+1)
[To be confirmed at Q2 review]

### Wave 3: Optimise (Q4+1 onwards)
[To be confirmed at Q4 review]

## Resource Plan

| Capability | Q1 | Q2 | Q3 | Q4 |
|------------|----|----|----|----|
| Data Engineering | X FTE | X FTE | X FTE | X FTE |
| ML Engineering | X FTE | X FTE | X FTE | X FTE |
| Architecture | X FTE | X FTE | X FTE | X FTE |

## Risk & Dependencies

| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | H/M/L | [Mitigation] |

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Use cases deployed | X | Count |
| Benefits realised | $XM | Financial tracking |
| Platform adoption | X% | Usage metrics |

## Approval

| Role | Name | Date |
|------|------|------|
| Executive Sponsor | | |
| Programme Director | | |
| Architecture Lead | | |
""",

        "portfolio-scorecard.md": """# Portfolio Scorecard - {fy}

## Scoring Summary

Generated: {date}

### DVF Distribution

| Score Range | Count | % of Portfolio |
|-------------|-------|----------------|
| 7-9 (High) | XX | XX% |
| 5-6 (Medium) | XX | XX% |
| 1-4 (Low) | XX | XX% |

### WSJF Rankings

| Rank | UC ID | Name | WSJF Score | Recommended Wave |
|------|-------|------|------------|------------------|
| 1 | UC-XXX | [Name] | XX.X | Wave 1 |
| 2 | UC-XXX | [Name] | XX.X | Wave 1 |
| ... | | | | |

### Strategic Alignment

| Theme | Use Cases Aligned | % of Portfolio |
|-------|-------------------|----------------|
| [Theme 1] | XX | XX% |
| [Theme 2] | XX | XX% |

## Category Distribution

| Category | Count | Total Value |
|----------|-------|-------------|
| Customer & Relationship | XX | $X.XM |
| Risk Management | XX | $X.XM |
| Operations | XX | $X.XM |
| Data & Analytics | XX | $X.XM |

## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]
""",

        "investment-thesis.md": """# Investment Thesis - {fy}

## Why Now?

[Strategic context for AI investment this year]

## Where to Play

### Priority Domains
1. **[Domain 1]** - [Rationale]
2. **[Domain 2]** - [Rationale]
3. **[Domain 3]** - [Rationale]

### Deprioritised Areas
- [Area] - [Reason]

## How to Win

### Capability Investments
| Capability | Investment | Expected Outcome |
|------------|------------|------------------|
| [Capability 1] | $XXXk | [Outcome] |

### Platform Bets
| Platform | Investment | Enables |
|----------|------------|---------|
| [Platform 1] | $XXXk | X use cases |

## Financial Model

| Metric | FY25 | FY26 | FY27 |
|--------|------|------|------|
| Investment | $X.XM | $X.XM | $X.XM |
| Run rate benefit | $X.XM | $X.XM | $X.XM |
| Cumulative ROI | X% | X% | X% |

## Risk Appetite

| Risk Type | Appetite | Rationale |
|-----------|----------|-----------|
| Technology | Medium | Proven patterns, some innovation |
| Execution | Low | Strong governance required |
| Regulatory | Very Low | Compliance non-negotiable |

## Success Definition

By end of {fy}, success means:
1. [Measurable outcome 1]
2. [Measurable outcome 2]
3. [Measurable outcome 3]
""",

        "quarterly-review.md": """# Quarterly Review - {quarter}

## Review Date
{date}

## Attendees
- [Name] - [Role]

---

## 1. Delivery Progress

### Active Use Cases

| UC ID | Name | Status | % Complete | On Track |
|-------|------|--------|------------|----------|
| UC-XXX | [Name] | [Status] | XX% | Yes/No |

### Key Achievements
- [Achievement 1]
- [Achievement 2]

### Blockers & Risks
| Issue | Impact | Owner | Resolution |
|-------|--------|-------|------------|
| [Issue] | H/M/L | [Name] | [Action] |

---

## 2. Pipeline Health

### Stage Distribution

| Stage | Count | Change vs Last Qtr |
|-------|-------|-------------------|
| Intake | XX | +/- X |
| Assess | XX | +/- X |
| Backlog | XX | +/- X |
| Planned | XX | +/- X |
| Active | XX | +/- X |
| Deployed | XX | +/- X |

### New Intake Items
| ID | Name | Sponsor | Initial DVF |
|----|------|---------|-------------|
| INTAKE-XXX | [Name] | [Sponsor] | X/9 |

---

## 3. Reprioritisation

### Promoted (moved up in priority)
| UC ID | From | To | Reason |
|-------|------|----|----|
| UC-XXX | Backlog | Planned | [Reason] |

### Demoted (moved down in priority)
| UC ID | From | To | Reason |
|-------|------|----|----|
| UC-XXX | Planned | Backlog | [Reason] |

### Retired
| UC ID | Reason |
|-------|--------|
| UC-XXX | [Reason] |

---

## 4. Decisions

| # | Decision | Owner | Due Date |
|---|----------|-------|----------|
| 1 | [Decision] | [Name] | [Date] |

---

## 5. Next Quarter Focus

1. [Focus area 1]
2. [Focus area 2]
3. [Focus area 3]

---

## Approval

| Role | Name | Approved |
|------|------|----------|
| Executive Sponsor | | ☐ |
| Programme Director | | ☐ |
""",

        "pipeline-status.md": """# Pipeline Status - {quarter}

Generated: {date}

## Summary

| Metric | Value | Trend |
|--------|-------|-------|
| Total in pipeline | XX | → |
| Intake this quarter | XX | ↑ |
| Deployed this quarter | XX | → |
| Avg time in backlog | XX days | ↓ |

## Stage Detail

### 1-Intake
| ID | Name | Submitted | Days in Stage |
|----|------|-----------|---------------|
| INTAKE-XXX | [Name] | YYYY-MM-DD | X |

### 2-Assess
| UC ID | Name | DVF Score | Assessor |
|-------|------|-----------|----------|
| UC-XXX | [Name] | X/9 | [Name] |

### 3-Backlog
| UC ID | Name | WSJF | Wave Target |
|-------|------|------|-------------|
| UC-XXX | [Name] | XX.X | Wave X |

### 4-Planned
| UC ID | Name | Wave | Start Date |
|-------|------|------|------------|
| UC-XXX | [Name] | Wave X | YYYY-MM-DD |

### 5-Active
| UC ID | Name | Phase | % Complete | ETA |
|-------|------|-------|------------|-----|
| UC-XXX | [Name] | [Phase] | XX% | YYYY-MM-DD |

### 6-Deployed
| UC ID | Name | Go-Live | Benefits Status |
|-------|------|---------|-----------------|
| UC-XXX | [Name] | YYYY-MM-DD | Tracking |

## Aging Analysis

| Stage | < 30 days | 30-60 days | 60-90 days | > 90 days |
|-------|-----------|------------|------------|-----------|
| Intake | X | X | X | X |
| Assess | X | X | X | X |
| Backlog | X | X | X | X |
""",

        "decisions.md": """# Quarterly Decisions - {quarter}

## Decision Log

### Decision 1
- **Date:** YYYY-MM-DD
- **Decision:** [Description]
- **Rationale:** [Why this decision was made]
- **Impact:** [What changes as a result]
- **Owner:** [Name]

---

### Decision 2
- **Date:** YYYY-MM-DD
- **Decision:** [Description]
- **Rationale:** [Why this decision was made]
- **Impact:** [What changes as a result]
- **Owner:** [Name]

---

## Priority Changes

| UC ID | Previous Priority | New Priority | Reason |
|-------|-------------------|--------------|--------|
| UC-XXX | X | Y | [Reason] |

## Wave Adjustments

| UC ID | Previous Wave | New Wave | Reason |
|-------|---------------|----------|--------|
| UC-XXX | Wave X | Wave Y | [Reason] |

## Resource Reallocations

| From | To | Amount | Reason |
|------|-----|--------|--------|
| [Project] | [Project] | X FTE | [Reason] |

---

## Approved By

| Role | Name | Date |
|------|------|------|
| Executive Sponsor | | |
""",

        "wave-plan.md": """# Wave Plan - {wave}

## Wave Overview

| Attribute | Value |
|-----------|-------|
| Wave Name | {wave} |
| Duration | QX YYYY - QX YYYY |
| Total Investment | $X.XM |
| Expected Benefits | $X.XM annually |

## Strategic Objective

[What this wave aims to achieve and why these use cases are grouped together]

## Use Cases in Wave

| Priority | UC ID | Name | Investment | Benefit | Dependencies |
|----------|-------|------|------------|---------|--------------|
| 1 | UC-XXX | [Name] | $XXXk | $X.XM | None |
| 2 | UC-XXX | [Name] | $XXXk | $X.XM | UC-XXX |

## Timeline

```
        Month 1-3       Month 4-6       Month 7-9
        ─────────       ─────────       ─────────
UC-XXX  ████████████
UC-XXX      ████████████████████
UC-XXX              ████████████████████████████
```

## Resource Requirements

| Role | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 |
|------|----|----|----|----|----|----|----|----|----|
| Data Engineer | X | X | X | X | X | X | X | X | X |
| ML Engineer | X | X | X | X | X | X | X | X | X |
| Architect | X | X | X | X | X | X | X | X | X |

## Dependencies

### Internal Dependencies
| Dependency | Required By | Status |
|------------|-------------|--------|
| [Platform/capability] | UC-XXX | ✅/⏳/❌ |

### External Dependencies
| Dependency | Required By | Owner | Status |
|------------|-------------|-------|--------|
| [External system] | UC-XXX | [Team] | ✅/⏳/❌ |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Action] |

## Success Criteria

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Use cases deployed | X | Count |
| On-time delivery | >80% | Schedule variance |
| Benefits realised | $XM | Financial tracking |
""",

        "dependencies.md": """# Wave Dependencies - {wave}

## Dependency Matrix

### Use Case to Use Case

|  | UC-001 | UC-004 | UC-006 | UC-009 | UC-011 |
|--|--------|--------|--------|--------|--------|
| UC-001 | - | | | | |
| UC-004 | | - | | ← | |
| UC-006 | | | - | ← | |
| UC-009 | | | | - | |
| UC-011 | | ← | | | - |

**Legend:** ← depends on (row depends on column)

### Use Case to Platform

| UC ID | Feature Store | MLOps | RAG Platform | Governance |
|-------|---------------|-------|--------------|------------|
| UC-001 | Required | Required | Required | Required |
| UC-004 | Required | Required | | Required |

### Use Case to External System

| UC ID | Core Banking | Data Lake | CRM | External API |
|-------|--------------|-----------|-----|--------------|
| UC-001 | Read | Read | Read/Write | |
| UC-004 | Read | Read | | Credit Bureau |

## Critical Path

```
Platform Foundation
        │
        ├──► UC-009 (Data Products) ──► UC-004 (Credit Risk)
        │                                    │
        │                                    ▼
        └──► UC-001 (Partnership Banking)   UC-011 (Fincrime)
                    │
                    ▼
              UC-006 (Personalisation)
```

## Dependency Risks

| Dependency | Risk | Impact | Mitigation |
|------------|------|--------|------------|
| [Dependency] | [Risk description] | H/M/L | [Action] |
""",

        "success-criteria.md": """# Success Criteria - {wave}

## Wave Success Definition

This wave will be considered successful if:

1. **Delivery:** X of Y planned use cases deployed to production
2. **Quality:** All deployments meet production readiness criteria
3. **Adoption:** >X% of target users actively using within 3 months
4. **Benefits:** Benefits tracking established for all deployed use cases

## Use Case Success Metrics

### UC-XXX: [Name]

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| [Metric 1] | X | Y | 3 months |
| [Metric 2] | X | Y | 6 months |

### UC-XXX: [Name]

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| [Metric 1] | X | Y | 3 months |
| [Metric 2] | X | Y | 6 months |

## Platform Success Metrics

| Platform Capability | Metric | Target |
|---------------------|--------|--------|
| Feature Store | Latency p99 | <10ms |
| MLOps | Deployment frequency | Weekly |
| Governance | Model registry coverage | 100% |

## Measurement Plan

| Metric | Data Source | Frequency | Owner |
|--------|-------------|-----------|-------|
| [Metric] | [Source] | [Frequency] | [Name] |

## Review Schedule

| Milestone | Date | Review Type |
|-----------|------|-------------|
| Wave kickoff | YYYY-MM-DD | Baseline confirmation |
| Mid-wave | YYYY-MM-DD | Progress check |
| Wave end | YYYY-MM-DD | Success assessment |
| +3 months | YYYY-MM-DD | Benefits realisation |
| +6 months | YYYY-MM-DD | Benefits realisation |
""",

        # Report templates
        "portfolio-heatmap.md": """# Portfolio Heatmap

Generated: {date}

## Value vs Complexity Matrix

```
    HIGH VALUE
         │
         │   ★ UC-004      ★ UC-001
         │   ★ UC-011      ★ UC-006
         │
         │   ★ UC-009      ★ UC-010
         │   ★ UC-014
         │
    LOW VALUE
         └──────────────────────────────
              LOW COMPLEXITY    HIGH COMPLEXITY
```

**Legend:**
- ★ Wave 1 candidates
- ○ Wave 2 candidates
- · Backlog

## Quadrant Summary

### Quick Wins (High Value, Low Complexity)
| UC ID | Name | WSJF |
|-------|------|------|
| UC-XXX | [Name] | XX.X |

### Strategic Bets (High Value, High Complexity)
| UC ID | Name | WSJF |
|-------|------|------|
| UC-XXX | [Name] | XX.X |

### Fill-ins (Low Value, Low Complexity)
| UC ID | Name | WSJF |
|-------|------|------|
| UC-XXX | [Name] | XX.X |

### Reconsider (Low Value, High Complexity)
| UC ID | Name | WSJF |
|-------|------|------|
| UC-XXX | [Name] | XX.X |

## Recommendations

1. [Recommendation based on heatmap analysis]
""",

        "dependency-graph.md": """# Dependency Graph

Generated: {date}

## Visual Dependency Map

```
                    ┌─────────────────┐
                    │   PLATFORMS     │
                    │  (Foundation)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐         ┌─────────┐         ┌─────────┐
   │ UC-009  │         │ UC-004  │         │ UC-001  │
   │  Data   │         │ Credit  │         │ Partner │
   │Products │         │  Risk   │         │ Banking │
   └────┬────┘         └────┬────┘         └────┬────┘
        │                   │                   │
        │                   ▼                   │
        │              ┌─────────┐              │
        └─────────────►│ UC-011  │◄─────────────┘
                       │Fincrime │
                       └─────────┘
```

## Dependency Table

| UC ID | Depends On | Depended By | Critical Path |
|-------|------------|-------------|---------------|
| UC-009 | Platforms | UC-004, UC-011 | Yes |
| UC-004 | UC-009, Platforms | UC-011 | Yes |
| UC-001 | Platforms | UC-011 | Yes |
| UC-011 | UC-004, UC-001 | None | End |

## Risk Analysis

| Dependency Chain | Risk Level | Mitigation |
|------------------|------------|------------|
| Platform → UC-009 → UC-004 | High | Parallel development |
""",

        "resource-demand.md": """# Resource Demand

Generated: {date}

## Demand Forecast

### By Quarter

| Role | Q1 | Q2 | Q3 | Q4 | Total FTE-Quarters |
|------|----|----|----|----|-------------------|
| Data Engineer | X | X | X | X | XX |
| ML Engineer | X | X | X | X | XX |
| Platform Engineer | X | X | X | X | XX |
| Enterprise Architect | X | X | X | X | XX |
| **Total** | **X** | **X** | **X** | **X** | **XX** |

### By Use Case

| UC ID | Name | Data Eng | ML Eng | Platform | Arch |
|-------|------|----------|--------|----------|------|
| UC-XXX | [Name] | X | X | X | X |

## Capacity Analysis

| Role | Available | Demand | Gap |
|------|-----------|--------|-----|
| Data Engineer | X | X | +/- X |
| ML Engineer | X | X | +/- X |

## Recommendations

1. [Capacity recommendation]
""",

        "benefit-tracker.md": """# Benefits Tracker

Generated: {date}

## Benefits Summary

| Metric | Target | Actual | Variance |
|--------|--------|--------|----------|
| Total annual benefit | $X.XM | $X.XM | +/- X% |
| Use cases tracking | XX | XX | +/- X |
| On-track for target | XX% | | |

## By Use Case

### Deployed & Tracking

| UC ID | Name | Target Benefit | Actual (YTD) | Status |
|-------|------|----------------|--------------|--------|
| UC-XXX | [Name] | $X.XM | $X.XM | 🟢/🟡/🔴 |

### Deployed, Not Yet Tracking

| UC ID | Name | Target Benefit | Tracking Start |
|-------|------|----------------|----------------|
| UC-XXX | [Name] | $X.XM | YYYY-MM-DD |

## Benefit Categories

| Category | Target | Actual | % Achieved |
|----------|--------|--------|------------|
| Revenue increase | $X.XM | $X.XM | XX% |
| Cost reduction | $X.XM | $X.XM | XX% |
| Risk reduction | $X.XM | $X.XM | XX% |

## Lessons Learned

| UC ID | Learning | Application |
|-------|----------|-------------|
| UC-XXX | [Learning] | [How to apply] |
""",
    }

    # Handle parameterised templates
    today = datetime.now()
    fy = f"FY{today.year + 1}" if today.month >= 7 else f"FY{today.year}"
    quarter = f"FY{today.year}-Q{(today.month - 1) // 3 + 1}"

    if filename in templates:
        content = templates[filename]
        content = content.replace("{date}", today.strftime("%Y-%m-%d"))
        content = content.replace("{fy}", fy)
        content = content.replace("{quarter}", quarter)
        content = content.replace("{wave}", "Wave 1 - Foundation")
        return content

    return None


def get_csv_template(filename: str) -> str:
    """Generate CSV template content."""

    templates = {
        "use-case-registry.csv": """use_case_id,name,stage,wave,fy_quarter,dvf_score,wsjf_score,strategic_theme,category,owner,last_review,next_milestone,status
UC-001,Partnership Banking,5-active,wave-1,FY2026-Q1,8,24.5,Customer Experience,Customer & Relationship Management,Shawn Cawood,2025-12-01,Go-live,On Track
UC-002,Finance,3-backlog,wave-2,,7,18.2,Operational Excellence,Finance & Accounting,Brian Stapleton,2025-12-01,Wave 2 planning,Pending
UC-003,Analytics and Reporting,3-backlog,wave-2,,7,17.8,Data & Analytics,Data & Analytics,Tracey Davis,2025-12-01,Wave 2 planning,Pending
UC-004,Credit Risk,5-active,wave-1,FY2026-Q1,9,28.0,Risk Management,Risk Management,Paul Furkert,2025-12-01,Go-live,On Track
UC-005,Lending Ops,3-backlog,wave-2,,7,16.5,Operational Excellence,Lending & Credit Operations,Paul Furkert,2025-12-01,Wave 2 planning,Pending
UC-006,HyperPersonalization,5-active,wave-1,FY2026-Q2,8,22.0,Customer Experience,Marketing & Personalization,Corina Elama,2025-12-01,Development,On Track
UC-007,Contact Centre,3-backlog,wave-2,,7,15.8,Customer Experience,Customer Service & Support,Dan Barratt,2025-12-01,Wave 2 planning,Pending
UC-008,Security AI,3-backlog,wave-2,,8,19.5,Risk Management,Cybersecurity & Threat Detection,Francis Kataino,2025-12-01,Wave 2 planning,Pending
UC-009,Data Products,5-active,wave-1,FY2026-Q1,8,26.0,Data & Analytics,Data & Analytics,Tracey Davis,2025-12-01,Go-live,On Track
UC-010,SDLC,3-backlog,wave-2,,7,14.2,Operational Excellence,Software Development,Glenn Bellam,2025-12-01,Wave 2 planning,Pending
UC-011,Fincrime,5-active,wave-1,FY2026-Q2,9,25.5,Risk Management,Compliance & Financial Crime,Michael Lomas,2025-12-01,Development,On Track""",

        "pattern-catalog.csv": """pattern_id,name,category,description,use_case_count,maturity,documentation_status
PT-001,Enterprise AI Governance,Governance,Comprehensive governance framework for AI systems,24,Defined,Complete
PT-002,MLOps Level 2+,Operations,Automated ML pipeline with CI/CD and monitoring,12,Developing,Complete
PT-003,Feature Store Dual-Store,Data,Online/offline feature serving with low latency,8,Defined,Complete
PT-004,ML Model Explainability,Governance,SHAP/LIME explainability for regulatory compliance,7,Defined,Complete
PT-005,Self-Reflective RAG,AI Pattern,RAG with reflection and hybrid search,8,Developing,Complete
PT-006,Multi-Model Routing,AI Pattern,Intelligent routing across multiple LLMs,6,Initial,Complete
PT-007,Agentic AI Pattern,AI Pattern,Autonomous agents with planning and reflection,12,Developing,Complete
PT-008,Multi-Agent Orchestration,AI Pattern,Coordination of multiple specialized agents,2,Initial,Complete
PT-009,Real-Time ML Scoring,Inference,Sub-second ML inference for production,10,Defined,Complete
PT-010,Champion/Challenger Testing,Operations,A/B testing framework for model comparison,3,Developing,Complete
PT-011,Intelligent Document Processing,AI Pattern,Multi-modal document extraction and processing,5,Developing,Complete
PT-012,Data Mesh Pattern,Data,Federated data product ownership,4,Initial,Complete
PT-013,Conversational AI,AI Pattern,Multi-turn dialogue management,2,Developing,Complete
PT-014,Batch Prediction Pattern,Inference,Large-scale batch inference pipelines,4,Defined,Complete
PT-015,Event-Driven Architecture,Integration,Real-time event streaming and processing,5,Defined,Complete
PT-016,Stream Processing,Data,Continuous data stream processing,2,Developing,Complete
PT-017,Observability and Monitoring,Operations,Full-stack observability with OpenTelemetry,24,Defined,Complete
PT-018,Security and Privacy,Security,Privacy-preserving AI and security controls,8,Defined,Complete""",

        "capability-mapping.csv": """use_case_id,use_case_name,l0_capability,l1_capability,l2_capability,capability_id
UC-001,Partnership Banking,Customer Management,Relationship Management,Customer Insights,CAP-CM-RM-01
UC-001,Partnership Banking,Customer Management,Relationship Management,Meeting Preparation,CAP-CM-RM-02
UC-004,Credit Risk,Risk Management,Credit Risk,Credit Assessment,CAP-RM-CR-01
UC-004,Credit Risk,Risk Management,Credit Risk,Portfolio Monitoring,CAP-RM-CR-02
UC-009,Data Products,Data & Analytics,Data Management,Data Product Creation,CAP-DA-DM-01
UC-011,Fincrime,Risk Management,Financial Crime,Transaction Monitoring,CAP-RM-FC-01
UC-011,Fincrime,Risk Management,Financial Crime,KYC/AML,CAP-RM-FC-02""",

        "dvf-scores.csv": """use_case_id,use_case_name,desirability,viability,feasibility,dvf_total,assessment_date,assessor,notes
UC-001,Partnership Banking,3,3,2,8,2025-10-15,Shawn Cawood,Strong business pull; technical complexity moderate
UC-002,Finance,2,3,2,7,2025-10-15,Brian Stapleton,Clear value; depends on data quality
UC-003,Analytics and Reporting,2,3,2,7,2025-10-15,Tracey Davis,Broad applicability; integration complexity
UC-004,Credit Risk,3,3,3,9,2025-10-15,Paul Furkert,Regulatory driver; proven patterns exist
UC-005,Lending Ops,2,3,2,7,2025-10-15,Paul Furkert,Process efficiency gains clear
UC-006,HyperPersonalization,3,2,3,8,2025-10-15,Corina Elama,High customer impact; platform dependency
UC-007,Contact Centre,3,2,2,7,2025-10-15,Dan Barratt,Strong user need; vendor integration
UC-008,Security AI,3,3,2,8,2025-10-15,Francis Kataino,Critical capability; specialized skills needed
UC-009,Data Products,3,3,2,8,2025-10-15,Tracey Davis,Platform enabler; foundational
UC-010,SDLC,2,3,2,7,2025-10-15,Glenn Bellam,Developer productivity; adoption risk
UC-011,Fincrime,3,3,3,9,2025-10-15,Michael Lomas,Regulatory mandate; high urgency""",

        "wsjf-scores.csv": """use_case_id,use_case_name,user_value,time_criticality,risk_reduction,job_size,wsjf_score,ranking,wave_recommendation,scoring_date,notes
UC-004,Credit Risk,9,8,9,8,28.0,1,wave-1,2025-11-01,Regulatory driver + high value
UC-009,Data Products,8,7,9,8,26.0,2,wave-1,2025-11-01,Platform enabler for multiple UCs
UC-011,Fincrime,9,9,8,8,25.5,3,wave-1,2025-11-01,Regulatory mandate
UC-001,Partnership Banking,8,6,7,8,24.5,4,wave-1,2025-11-01,Revenue opportunity
UC-006,HyperPersonalization,8,6,6,8,22.0,5,wave-1,2025-11-01,Customer experience differentiator
UC-008,Security AI,8,7,9,10,19.5,6,wave-2,2025-11-01,Critical but complex
UC-002,Finance,7,6,6,8,18.2,7,wave-2,2025-11-01,Efficiency gains
UC-003,Analytics and Reporting,7,5,6,8,17.8,8,wave-2,2025-11-01,Democratization of data
UC-005,Lending Ops,7,5,5,8,16.5,9,wave-2,2025-11-01,Process efficiency
UC-007,Contact Centre,7,5,5,8,15.8,10,wave-2,2025-11-01,Customer service improvement
UC-010,SDLC,6,4,5,8,14.2,11,wave-2,2025-11-01,Developer productivity""",

        "strategic-alignment.csv": """use_case_id,use_case_name,theme_customer_experience,theme_operational_excellence,theme_risk_management,theme_data_analytics,primary_theme,alignment_score,strategic_priority
UC-001,Partnership Banking,5,2,2,3,Customer Experience,5,High
UC-002,Finance,1,5,2,3,Operational Excellence,5,Medium
UC-003,Analytics and Reporting,2,3,1,5,Data & Analytics,5,Medium
UC-004,Credit Risk,2,3,5,3,Risk Management,5,Critical
UC-005,Lending Ops,3,5,2,2,Operational Excellence,5,Medium
UC-006,HyperPersonalization,5,2,1,3,Customer Experience,5,High
UC-007,Contact Centre,5,4,1,2,Customer Experience,5,Medium
UC-008,Security AI,1,3,5,2,Risk Management,5,High
UC-009,Data Products,2,4,2,5,Data & Analytics,5,High
UC-010,SDLC,1,5,2,2,Operational Excellence,5,Medium
UC-011,Fincrime,1,3,5,2,Risk Management,5,Critical""",

        "dependency-matrix.csv": """use_case_id,depends_on_uc,dependency_type,strength,notes
UC-001,UC-009,data,strong,Requires data products for customer features
UC-004,UC-009,data,strong,Requires data products for credit features
UC-006,UC-001,feature,medium,Leverages partnership banking insights
UC-006,UC-009,data,strong,Requires real-time customer features
UC-011,UC-004,model,medium,Uses credit risk scoring outputs
UC-011,UC-009,data,strong,Requires transaction data products
UC-007,UC-001,feature,weak,Can use customer context from partnership
UC-003,UC-009,data,strong,Built on data product foundation
UC-002,UC-009,data,strong,Financial data products required""",

        "cost-estimates.csv": """use_case_id,use_case_name,platform_cost,development_cost,integration_cost,operational_cost_annual,total_implementation,contingency_pct,total_with_contingency,estimate_date,confidence
UC-001,Partnership Banking,150000,300000,100000,75000,550000,20,660000,2025-11-01,Medium
UC-004,Credit Risk,200000,400000,150000,100000,750000,15,862500,2025-11-01,High
UC-006,HyperPersonalization,150000,350000,100000,80000,600000,20,720000,2025-11-01,Medium
UC-009,Data Products,300000,250000,100000,120000,650000,15,747500,2025-11-01,High
UC-011,Fincrime,200000,350000,150000,90000,700000,15,805000,2025-11-01,High""",

        "benefit-projections.csv": """use_case_id,use_case_name,benefit_type,year_1,year_2,year_3,npv_3yr,measurement_method,confidence,assumptions
UC-001,Partnership Banking,Revenue,500000,1500000,2500000,3800000,CRM attribution,Medium,10% conversion improvement
UC-001,Partnership Banking,Cost Reduction,100000,200000,250000,470000,Time tracking,High,30% prep time reduction
UC-004,Credit Risk,Risk Reduction,1000000,2000000,3000000,5100000,Loss analysis,High,15% default reduction
UC-004,Credit Risk,Cost Reduction,200000,400000,500000,940000,Process efficiency,High,40% faster decisions
UC-006,HyperPersonalization,Revenue,300000,900000,1500000,2300000,Campaign attribution,Medium,15% conversion lift
UC-009,Data Products,Cost Reduction,400000,800000,1000000,1880000,Engineering efficiency,High,50% faster data delivery
UC-011,Fincrime,Risk Reduction,800000,1500000,2000000,3650000,Regulatory fines avoided,High,Compliance improvement
UC-011,Fincrime,Cost Reduction,300000,500000,600000,1190000,Investigation efficiency,High,40% faster investigations""",

        "actuals-tracking.csv": """use_case_id,use_case_name,metric,period,target,actual,variance_pct,status,notes
UC-004,Credit Risk,Decision time reduction,2025-Q4,40%,35%,-12.5,Yellow,Ramping up adoption
UC-004,Credit Risk,Default rate improvement,2025-Q4,5%,4.2%,-16,Yellow,Early stage measurement
UC-009,Data Products,Data product delivery time,2025-Q4,50%,55%,10,Green,Exceeding target
UC-009,Data Products,Data quality score,2025-Q4,95%,96.2%,1.3,Green,Strong performance""",

        "roi-analysis.csv": """use_case_id,use_case_name,total_investment,year_1_benefit,year_2_benefit,year_3_benefit,total_benefit_3yr,roi_3yr_pct,payback_months,irr_pct,status
UC-001,Partnership Banking,660000,600000,1700000,2750000,5050000,665,9,185,Projected
UC-004,Credit Risk,862500,1200000,2400000,3500000,7100000,723,7,210,Projected
UC-006,HyperPersonalization,720000,300000,900000,1500000,2700000,275,16,95,Projected
UC-009,Data Products,747500,400000,800000,1000000,2200000,194,14,72,Projected
UC-011,Fincrime,805000,1100000,2000000,2600000,5700000,608,8,195,Projected""",
    }

    return templates.get(filename, "")


# =============================================================================
# FILE OPERATIONS
# =============================================================================

def create_folder_structure(base_path: Path, dry_run: bool = False) -> dict:
    """Create the new folder structure."""
    results = {
        'folders_created': [],
        'files_created': [],
        'errors': []
    }

    print("\n" + "=" * 60)
    print("CREATING FOLDER STRUCTURE")
    print("=" * 60 + "\n")

    for folder, files in FOLDER_STRUCTURE.items():
        folder_path = base_path / folder

        # Create folder
        if not folder_path.exists():
            if dry_run:
                print(f"  [DRY RUN] Would create folder: {folder}")
            else:
                try:
                    folder_path.mkdir(parents=True, exist_ok=True)
                    print(f"  Created folder: {folder}")
                    results['folders_created'].append(folder_path)
                except Exception as e:
                    print(f"  [ERROR] Failed to create {folder}: {e}")
                    results['errors'].append((folder_path, str(e)))
        else:
            print(f"  [EXISTS] Folder: {folder}")

        # Create template files
        for filename in files:
            file_path = folder_path / filename
            if not file_path.exists():
                if dry_run:
                    print(f"    [DRY RUN] Would create file: {filename}")
                else:
                    try:
                        # Get template content
                        if filename.endswith('.csv'):
                            content = get_csv_template(filename)
                        else:
                            content = get_template_content(filename, base_path)

                        if content:
                            file_path.write_text(content, encoding='utf-8')
                            print(f"    Created file: {filename}")
                            results['files_created'].append(file_path)
                        else:
                            # Create empty placeholder
                            file_path.write_text(f"# {filename}\n\nTODO: Add content\n", encoding='utf-8')
                            print(f"    Created placeholder: {filename}")
                            results['files_created'].append(file_path)
                    except Exception as e:
                        print(f"    [ERROR] Failed to create {filename}: {e}")
                        results['errors'].append((file_path, str(e)))
            else:
                print(f"    [EXISTS] File: {filename}")

    return results


def migrate_existing_files(base_path: Path, dry_run: bool = False) -> dict:
    """Migrate existing files to new structure."""
    results = {
        'moved': [],
        'skipped': [],
        'errors': []
    }

    print("\n" + "=" * 60)
    print("MIGRATING EXISTING FILES")
    print("=" * 60 + "\n")

    # Define migration rules
    migrations = [
        # UC-XXX folders → use-cases/
        {
            'pattern': 'UC-*',
            'source': base_path / 'use-case-prioritisation',
            'dest': base_path / 'use-case-prioritisation' / 'use-cases',
            'type': 'folder'
        },
        # PT-XXX folders → patterns/ (already in patterns/)
        # Existing CSV files → data/operational/
        {
            'pattern': 'use-case-*.csv',
            'source': base_path / 'use-case-prioritisation' / 'data',
            'dest': base_path / 'use-case-prioritisation' / 'data' / 'operational',
            'type': 'file'
        },
        {
            'pattern': 'scenario-*.csv',
            'source': base_path / 'use-case-prioritisation' / 'data',
            'dest': base_path / 'use-case-prioritisation' / 'data' / 'operational',
            'type': 'file'
        },
        {
            'pattern': 'solution-*.csv',
            'source': base_path / 'use-case-prioritisation' / 'data',
            'dest': base_path / 'use-case-prioritisation' / 'data' / 'operational',
            'type': 'file'
        },
        {
            'pattern': 'ai-*.csv',
            'source': base_path / 'use-case-prioritisation' / 'data',
            'dest': base_path / 'use-case-prioritisation' / 'data' / 'operational',
            'type': 'file'
        },
    ]

    for migration in migrations:
        source_dir = migration['source']
        dest_dir = migration['dest']
        pattern = migration['pattern']
        item_type = migration['type']

        if not source_dir.exists():
            print(f"  [SKIP] Source not found: {source_dir}")
            continue

        # Ensure destination exists
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)

        # Find matching items
        import glob
        matches = list(source_dir.glob(pattern))

        for item in matches:
            # Skip if already in destination
            if str(dest_dir) in str(item):
                continue

            dest_path = dest_dir / item.name

            if dest_path.exists():
                print(f"  [SKIP] Already exists: {item.name}")
                results['skipped'].append((item, dest_path))
                continue

            if dry_run:
                print(f"  [DRY RUN] Would move: {item.name} -> {dest_dir.name}/")
                results['moved'].append((item, dest_path))
            else:
                try:
                    shutil.move(str(item), str(dest_path))
                    print(f"  Moved: {item.name} -> {dest_dir.name}/")
                    results['moved'].append((item, dest_path))
                except Exception as e:
                    print(f"  [ERROR] Failed to move {item.name}: {e}")
                    results['errors'].append((item, str(e)))

    return results


def create_readme(base_path: Path, dry_run: bool = False) -> bool:
    """Create main README for the new structure."""

    readme_content = """# AI Use Cases - Transformation Programme

## Overview

This folder contains all artifacts for the BNZ AI Transformation Programme use cases,
including specifications, prioritisation data, and planning documents.

## Structure

```
use-case-prioritisation/
├── governance/           # Programme governance & methodology
│   ├── prioritisation-framework.md
│   ├── intake-process.md
│   ├── stage-gate-criteria.md
│   ├── roles-responsibilities.md
│   └── review-cadence.md
│
├── planning/             # Planning cycles
│   ├── annual/           # Annual plans by FY
│   ├── quarterly/        # Quarterly reviews
│   └── waves/            # Delivery wave plans
│
├── pipeline/             # Use case lifecycle stages
│   ├── 1-intake/         # New ideas (unscored)
│   ├── 2-assess/         # Under DVF assessment
│   ├── 3-backlog/        # Scored, awaiting prioritisation
│   ├── 4-planned/        # Committed to a wave
│   ├── 5-active/         # Currently in delivery
│   ├── 6-deployed/       # Live in production
│   └── 7-retired/        # Decommissioned
│
├── use-cases/            # Detailed specifications
│   └── UC-XXX/           # Individual use case folders
│
├── patterns/             # Architecture patterns (PT-XXX)
│
├── data/                 # Structured data
│   ├── master/           # Source of truth registries
│   ├── scoring/          # Prioritisation scores
│   ├── financial/        # Cost & benefit tracking
│   └── operational/      # Detailed operational data
│
└── reports/              # Generated views & dashboards
```

## Quick Links

### Governance
- [Prioritisation Framework](governance/prioritisation-framework.md)
- [Intake Process](governance/intake-process.md)
- [Stage Gate Criteria](governance/stage-gate-criteria.md)

### Planning
- [Current Annual Plan](planning/annual/FY2026/annual-plan.md)
- [Latest Quarterly Review](planning/quarterly/)
- [Wave 1 Plan](planning/waves/wave-1-foundation/wave-plan.md)

### Data
- [Use Case Registry](data/master/use-case-registry.csv)
- [WSJF Scores](data/scoring/wsjf-scores.csv)
- [DVF Scores](data/scoring/dvf-scores.csv)

## Use Case Lifecycle

```
INTAKE → ASSESS → BACKLOG → PLANNED → ACTIVE → DEPLOYED → BENEFITS
   │        │         │         │         │         │          │
   │    DVF Pass   WSJF Rank  Wave     Delivery  Go-Live   Measured
   │    (≥6/9)     (Top N)   Commit   Complete
```

## Key Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Total use cases | 24 | - |
| Wave 1 committed | 5 | 5 |
| In active delivery | 5 | 5 |
| Deployed | 0 | 5 (by Q3 FY26) |

## Review Schedule

| Review | Frequency | Next Date |
|--------|-----------|-----------|
| Intake triage | Weekly | Every Monday |
| Quarterly review | Quarterly | End of quarter |
| Annual planning | Annual | October |

## Contact

- **Programme Director:** [Name]
- **Architecture Lead:** [Name]
- **Programme Office:** [Email]
"""

    readme_path = base_path / 'use-case-prioritisation' / 'README.md'

    if dry_run:
        print(f"\n[DRY RUN] Would create README at: {readme_path}")
        return True

    try:
        readme_path.write_text(readme_content, encoding='utf-8')
        print(f"\nCreated README: {readme_path}")
        return True
    except Exception as e:
        print(f"\n[ERROR] Failed to create README: {e}")
        return False


def print_summary(structure_results: dict, migration_results: dict, dry_run: bool):
    """Print summary of all operations."""

    print("\n" + "=" * 60)
    print("SUMMARY" + (" (DRY RUN)" if dry_run else ""))
    print("=" * 60)

    print("\nStructure Creation:")
    print(f"  Folders created:  {len(structure_results['folders_created'])}")
    print(f"  Files created:    {len(structure_results['files_created'])}")
    print(f"  Errors:           {len(structure_results['errors'])}")

    print("\nFile Migration:")
    print(f"  Items moved:      {len(migration_results['moved'])}")
    print(f"  Items skipped:    {len(migration_results['skipped'])}")
    print(f"  Errors:           {len(migration_results['errors'])}")

    total_errors = len(structure_results['errors']) + len(migration_results['errors'])
    if total_errors > 0:
        print("\nErrors encountered:")
        for path, error in structure_results['errors'] + migration_results['errors']:
            print(f"  - {path}: {error}")

    print("\n" + "=" * 60)
    if dry_run:
        print("DRY RUN COMPLETE - No changes were made")
        print("Run without --dry-run to apply changes")
    else:
        print("REORGANIZATION COMPLETE")
    print("=" * 60)


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Reorganize use cases into enhanced transformation programme structure'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    args = parser.parse_args()

    # Define paths
    repo_root = Path(__file__).parent.parent.parent.parent
    base_path = repo_root / '01-motivation' / '03-use-cases'

    print("=" * 60)
    print("Reorganize Use Cases Structure")
    print("=" * 60)
    print(f"Repository root: {repo_root}")
    print(f"Target path:     {base_path}")
    print(f"Mode:            {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 60)

    # Validate paths
    if not base_path.exists():
        print(f"ERROR: Base path does not exist: {base_path}")
        return 1

    # Create new folder structure
    structure_results = create_folder_structure(
        base_path / 'use-case-prioritisation',
        dry_run=args.dry_run
    )

    # Migrate existing files
    migration_results = migrate_existing_files(base_path, dry_run=args.dry_run)

    # Create README
    create_readme(base_path, dry_run=args.dry_run)

    # Print summary
    print_summary(structure_results, migration_results, args.dry_run)

    return 0 if not (structure_results['errors'] or migration_results['errors']) else 1


if __name__ == '__main__':
    exit(main())
