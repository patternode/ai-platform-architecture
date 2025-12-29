# Dependency Graph

Generated: 2025-12-06

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
| [UC-009](../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) | Platforms | [UC-004](../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md), [UC-011](../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | Yes |
| [UC-004](../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | [UC-009](../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md), Platforms | [UC-011](../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | Yes |
| [UC-001](../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | Platforms | [UC-011](../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | Yes |
| [UC-011](../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | [UC-004](../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md), [UC-001](../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | None | End |

## Risk Analysis

| Dependency Chain | Risk Level | Mitigation |
|------------------|------------|------------|
| Platform → [UC-009](../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) → [UC-004](../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | High | Parallel development |
