# AI Use Cases - Transformation Programme

## Overview

This folder contains all artifacts for the BNZ AI Transformation Programme use cases, including specifications, prioritisation data, and planning documents.

## Structure

```
use-cases/
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
├── model/                # Structured data
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
            │         │         │         │         │          │
        DVF Pass   WSJF Rank  Wave     Delivery  Go-Live   Measured
         (≥6/9)     (Top N)   Commit   Complete
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
