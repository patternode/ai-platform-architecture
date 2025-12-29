# Wave Dependencies - Wave 1 - Foundation

## Dependency Matrix

### Use Case to Use Case

|  | [UC-001](../../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | [UC-004](../../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | [UC-006](../../../use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) | [UC-009](../../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) | [UC-011](../../../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) |
|--|--------|--------|--------|--------|--------|
| [UC-001](../../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | - | | | | |
| [UC-004](../../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | | - | | ← | |
| [UC-006](../../../use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) | | | - | ← | |
| [UC-009](../../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) | | | | - | |
| [UC-011](../../../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | | ← | | | - |

**Legend:** ← depends on (row depends on column)

### Use Case to Platform

| UC ID | Feature Store | MLOps | RAG Platform | Governance |
|-------|---------------|-------|--------------|------------|
| [UC-001](../../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | Required | Required | Required | Required |
| [UC-004](../../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | Required | Required | | Required |

### Use Case to External System

| UC ID | Core Banking | Data Lake | CRM | External API |
|-------|--------------|-----------|-----|--------------|
| [UC-001](../../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | Read | Read | Read/Write | |
| [UC-004](../../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | Read | Read | | Credit Bureau |

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
