# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **AI Platform Architecture** repository for Bank of New Zealand (BNZ). It serves as the single source of truth for all architectural artifacts related to the BNZ AI Platform, following industry-aligned enterprise architecture principles.

**Key Characteristic**: This is a **documentation-only repository** with no build commands, tests, or code compilation. All work involves creating, editing, and organizing markdown files and diagrams.

## Repository Purpose

- Define and maintain the complete architecture for BNZ's AI Platform
- Provide traceability from business vision through to technical implementation
- Document architectural decisions, standards, and governance processes
- Plan and track delivery through themes, epics, features, and spikes
- Serve as reference documentation for platform teams and stakeholders

## Architecture Philosophy

The repository follows a **layered architecture** approach with clear separation of concerns:

1. **Motivation (01-motivation/)** - Why the AI platform exists and what guides its development
2. **Capabilities (02-capabilities/)** - WHAT business outcomes we enable (vendor-agnostic)
3. **Building Blocks (03-building-blocks/)** - HOW we build it:
   - **ABBs (Architecture Building Blocks)** - Logical, vendor-agnostic components
   - **SBBs (Solution Building Blocks)** - Concrete, vendor-specific implementations
   - **Patterns** - Reusable solutions to common problems
4. **Governance (05-governance/)** - Architecture decisions, standards, and compliance
5. **Roadmap (07-roadmap/)** - WHEN we deliver (organized by work taxonomy)

### Critical Distinctions

**ABB vs SBB**:
- ABB = "What is needed" (e.g., "Model Registry") - stable, logical, vendor-agnostic
- SBB = "How we implement it" (e.g., "MLflow 2.x on Kubernetes with S3 backend") - specific, evolves with technology

**Work Taxonomy Hierarchy**:
```
THEME (12-24 months) → EPIC (1-6 months) → FEATURE (2-6 weeks) → SPIKE (research, 1-2 weeks)
└─ STORY (1-5 days) → TASK (hours) [tracked in Jira/Azure DevOps]
```

## Repository Structure

```
ai-platform-architecture/
├── 01-motivation/          # Strategic context and stakeholder engagement
├── 02-capabilities/        # Business capability model (L0→L1→L2 hierarchy)
├── 03-building-blocks/     # ABBs, SBBs, and architectural patterns
├── 05-governance/          # ADRs, standards, compliance, and runbooks
└── 07-roadmap/             # Themes, epics, features, spikes, and backlog
```

## Common Workflows

### When Adding New Architecture Artifacts

**Before creating new files**, always:
1. Review existing structure to avoid duplication
2. Use the appropriate template from the relevant folder
3. Maintain traceability by linking to related artifacts

**File organization rules**:
- Business capabilities → [02-capabilities/](02-capabilities/)
- Logical components (ABBs) → [03-building-blocks/architecture-building-blocks/](03-building-blocks/architecture-building-blocks/)
- Technology implementations (SBBs) → [03-building-blocks/solution-building-blocks/](03-building-blocks/solution-building-blocks/)
- Architectural patterns → [03-building-blocks/patterns/](03-building-blocks/patterns/)
- Decisions → [05-governance/decisions/](05-governance/decisions/)
- Standards → [05-governance/standards/](05-governance/standards/)
- Work planning → [07-roadmap/](07-roadmap/)

### Work Request Classification

When users request architecture work, classify it according to the work taxonomy:

| Request Type | Classification | Examples |
|--------------|----------------|----------|
| Strategic direction (12-24 months) | THEME | "Establish enterprise AI governance" |
| New capability (1-6 months) | EPIC | "Implement feature store", "Deploy LLM gateway" |
| Enhancement (2-6 weeks) | FEATURE | "Add model versioning", "Enable A/B testing" |
| Research/uncertainty (1-2 weeks) | SPIKE | "Evaluate vector databases", "RAG proof of concept" |
| Implementation work (1-5 days) | STORY | Tracked in Jira/Azure DevOps |

Place new work requests in [07-roadmap/backlog/](07-roadmap/backlog/) using filename: `request-YYYY-MM-DD-short-description.md`

### Documentation Standards

**Naming conventions**:
- Epics: `EPIC-XXX-short-name.md` (e.g., `EPIC-042-feature-store-implementation.md`)
- Features: `FEATURE-XXX-short-name.md` or `FEATURE-EPIC-SUB-short-name.md`
- Spikes: `SPIKE-XXX-short-name.md`
- ADRs: `ADR-XXX-decision-title.md`

**Traceability requirements**:
Every architectural artifact must link to related artifacts above and below in the hierarchy. For example:
- Capabilities → ABBs that realize them
- ABBs → Capabilities supported, SBB options, patterns, ADRs
- Epics → Capabilities delivered, ABBs/SBBs involved
- Spikes → ADRs produced, technologies evaluated

### Visual Design Standards

**Critical requirement**: All diagrams and visual artifacts MUST follow the BNZ Visual Design Standards defined in [05-governance/standards/visual-design/visual-design-standard.md](05-governance/standards/visual-design/visual-design-standard.md).

**Key visual standards**:
- **Primary colors**: BNZ Navy Blue (#003087), BNZ Orange (#FF6B35), BNZ Light Blue (#50E6FF), BNZ Teal (#00A651)
- **Typography**: Calibri for documents/presentations, Helvetica for diagrams
- **Diagram canvas**: 2400x1800px (16:9) or 1920x1080px with 40-50px margins
- **Accessibility**: WCAG 2.1 AA compliance (4.5:1 contrast ratio minimum)
- **Legend requirement**: Every diagram must include a legend explaining colors, shapes, and arrow types

## Contribution Process

### Pull Request Guidelines

**PR title format**:
- `[CAPABILITY]` - New or updated capability definition
- `[ABB]` - Architecture Building Block changes
- `[SBB]` - Solution Building Block changes
- `[ADR]` - Architecture Decision Record
- `[PATTERN]` - Architecture pattern
- `[DOCS]` - Documentation updates

**Review levels** (see [CONTRIBUTING.md](CONTRIBUTING.md)):
- Minor changes (documentation fixes): Single reviewer approval
- Moderate changes (capability updates, ABB/SBB additions): Architecture lead approval
- Major changes (new principles, significant ADRs): Architecture review board approval

### Architecture Decision Records (ADRs)

When documenting significant decisions:
1. Use the ADR template from [05-governance/decisions/](05-governance/decisions/)
2. Include: context, options considered, decision made, consequences
3. Link to related capabilities, ABBs, SBBs, and patterns
4. Follow lifecycle: proposed → accepted → superseded

## Key Architecture Patterns

**Capability Maturity Model** (0-5 scale):
- 0 = None
- 1 = Initial (ad-hoc, manual)
- 2 = Developing (repeatable, some automation)
- 3 = Defined (standardized, consistent)
- 4 = Managed (measured, SLAs tracked)
- 5 = Optimizing (continuous improvement, data-driven)

**Traceability Flow**:
```
Vision → Principles → Capabilities → ABBs → SBBs → Patterns
  ↓                                              ↓
Themes → Epics → Features/Spikes        Reference Architecture
  ↓                                              ↓
Stories/Tasks                            Governed by ADRs & Standards
```

## Important Files to Reference

- [README.md](README.md) - Comprehensive repository guide with roadmap details
- [CONTRIBUTING.md](CONTRIBUTING.md) - Detailed contribution guidelines and PR process
- [glossary.md](glossary.md) - Common terms and definitions (ABB, SBB, ADR, etc.)
- [02-capabilities/README.md](02-capabilities/README.md) - Capability model overview
- [07-roadmap/README.md](07-roadmap/README.md) - Work taxonomy and organization guide
- [05-governance/standards/visual-design/visual-design-standard.md](05-governance/standards/visual-design/visual-design-standard.md) - Mandatory visual standards

## Important Notes

- **No code builds**: This repository contains only documentation (markdown, diagrams). There are no build commands, linting, or test execution needed.
- **Templates over creation**: ALWAYS prefer using existing templates rather than creating documents from scratch.
- **Traceability is mandatory**: Every artifact must link to related artifacts to maintain the architecture's integrity.
- **Visual standards are enforced**: All diagrams must comply with BNZ branding guidelines.
- **Governance approval required**: Significant changes require architecture team or board approval.
- **Keep backlog organized**: New work requests start in `07-roadmap/backlog/` and are triaged by the architecture team.

## Repository Metadata

- **Organization**: Bank of New Zealand (BNZ)
- **Team**: Strategy & Architecture
- **License**: Internal use only
- **Primary audience**: Platform architects, product owners, engineering teams, business stakeholders
