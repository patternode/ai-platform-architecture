# Prioritisation Framework

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
