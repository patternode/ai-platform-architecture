# AI Platform Architecture - Copilot Instructions

## Repository Overview

This is the **AI Platform Architecture** repository for Bank of New Zealand (BNZ). It's a **documentation-only repository** with no code builds, tests, or compilation. All work involves creating, editing, and organizing markdown files, diagrams (.drawio), and spreadsheets.

**Core Purpose**: Single source of truth for BNZ AI Platform architectural artifacts, following enterprise architecture principles with complete traceability from business vision to technical implementation.

## Critical Architecture Concepts

### Layered Architecture Model

The repository follows a strict layered model that must be preserved:

```
01-MOTIVATION     → Why (strategic context, use cases, stakeholders)
02-CAPABILITIES   → What (business outcomes, vendor-agnostic)
03-BUILDING-BLOCKS → How (ABBs = logical, SBBs = physical implementations)
04-REFERENCE-ARCH → Integration (how components fit together)
05-GOVERNANCE     → Rules (ADRs, standards, compliance)
06-TECHNOLOGY     → Tools (approved tech stack, radar)
07-ROADMAP        → When (themes → epics → features → spikes)
08-ASSETS         → Support (templates, scripts, icons)
```

### ABB vs SBB (Critical Distinction)

| Aspect | ABB (Architecture Building Block) | SBB (Solution Building Block) |
|--------|-----------------------------------|-------------------------------|
| **Nature** | Logical, vendor-agnostic | Physical, vendor-specific |
| **Stability** | Stable over time | Evolves with technology |
| **Example** | "Model Registry" | "MLflow 2.x on K8s with S3 backend" |
| **Location** | `03-building-blocks/architecture-building-blocks/` | `03-building-blocks/solution-building-blocks/` |

**When creating/editing components**: Always clarify if you're working with ABBs (the WHAT) or SBBs (the HOW).

### Work Taxonomy Hierarchy

All delivery planning follows this strict hierarchy:

```
THEME (12-24 months) → EPIC (1-6 months) → FEATURE (2-6 weeks) → STORY (1-5 days) → TASK (hours)
                                        ↘ SPIKE (research, 1-2 weeks)
```

**Stories and Tasks** are tracked in Jira/Azure DevOps, not in this repository.

**Classification Examples**:
- "Establish enterprise AI governance" → THEME
- "Implement feature store" → EPIC
- "Add model versioning" → FEATURE
- "Evaluate vector databases" → SPIKE

## File Organization Rules

### Naming Conventions (Mandatory)

```
Epics:    EPIC-XXX-short-name.md
Features: FEATURE-XXX-short-name.md
Spikes:   SPIKE-XXX-short-name.md
ADRs:     ADR-XXX-decision-title.md
Use Cases: UC-XXX-use-case-title.md
Patterns: PT-XXX-pattern-name.md
```

### Where Things Go

| Content Type | Location | Template Location |
|-------------|----------|-------------------|
| Business capabilities | `02-capabilities/{domain}/` | N/A |
| Logical components (ABBs) | `03-building-blocks/architecture-building-blocks/` | Same folder |
| Physical implementations (SBBs) | `03-building-blocks/solution-building-blocks/` | Same folder |
| Architecture patterns | `03-building-blocks/patterns/` | Same folder |
| Architecture decisions | `05-governance/decisions/` | Same folder |
| Standards & runbooks | `05-governance/standards/` | Same folder |
| Delivery planning | `07-roadmap/{themes,epics,features,spikes}/` | `07-roadmap/{type}/templates/` |
| New work requests | `07-roadmap/backlog/` | Use `request-YYYY-MM-DD-description.md` |

## Traceability Requirements (Critical)

**Every architectural artifact MUST link to related artifacts**:

- **Capabilities** → Link to ABBs that realize them
- **ABBs** → Link to capabilities supported, SBB options, patterns, ADRs
- **SBBs** → Link to parent ABB, technology decisions (ADRs)
- **Epics** → Link to capabilities delivered, ABBs/SBBs involved
- **Spikes** → Link to ADRs produced, technologies evaluated

**Example**: If you create a new ABB for "Feature Store", you must:
1. Link it to the capability it supports (e.g., `02-capabilities/data/feature-management.md`)
2. Reference any related patterns (e.g., `03-building-blocks/patterns/data/feature-serving-pattern.md`)
3. List candidate SBBs (e.g., "Feast", "Tecton", "AWS SageMaker Feature Store")

## Visual Design Standards (Mandatory)

All diagrams must comply with BNZ Visual Design Standards:

**Colors** (see `05-governance/standards/visual-design/visual-design-standard.md`):
- Primary: BNZ Navy Blue (`#003087`), BNZ Orange (`#FF6B35`)
- Secondary: BNZ Light Blue (`#50E6FF`), BNZ Teal (`#00A651`)
- Text: Dark Gray (`#333333`), Medium Gray (`#666666`)

**Diagram Requirements**:
- Canvas size: 2400x1800px (16:9) or 1920x1080px
- 40-50px margins
- Include legend explaining colors, shapes, and arrows
- Typography: Helvetica for diagrams, Calibri for documents
- WCAG 2.1 AA compliance (4.5:1 contrast minimum)

## Key Workflows

### Creating New Architecture Work

1. **Classify the request**: Theme, Epic, Feature, or Spike?
2. **Check for existing work**: Search `07-roadmap/` to avoid duplication
3. **Use appropriate template**: Copy from `07-roadmap/{type}/templates/`
4. **Add traceability links**: Connect to capabilities, ABBs, SBBs, ADRs
5. **Follow naming convention**: `{TYPE}-XXX-descriptive-name.md`

### Adding an Architecture Decision (ADR)

1. Use template from `05-governance/decisions/`
2. Include: Context, Options Considered, Decision, Consequences
3. Link to affected capabilities, ABBs, SBBs, patterns
4. Mark status: `proposed`, `accepted`, `superseded`
5. Assign ADR number sequentially (check existing ADRs)

### Working with Use Cases

Use cases live in `01-motivation/03-use-cases/use-case-prioritisation/`:

**Structure**:
```
use-cases/
├── UC-XXX/               # Individual use case folder
│   ├── README.md         # Use case specification
│   ├── blueprint.drawio  # Architecture diagram
│   └── sequence.drawio   # Sequence diagram
├── data/master/          # Source of truth CSVs
├── patterns/             # Architecture patterns (PT-XXX)
└── scripts/              # Python automation scripts
```

**Python Scripts Available** (`08-assets/scripts/use-cases/`):
- `organize_use_cases.py` - Organize files into UC-XXX folders
- `generate_use_cases.py` - Generate use case markdown from templates
- `create_prioritization_spreadsheet.py` - Generate prioritization sheets

**PowerShell Scripts Available** (`08-assets/scripts/use-cases/`):
- `convert-use-cases-to-docx.ps1` - Convert markdown to Word with high-fidelity round-trip

**Run scripts from repository root**:
```powershell
# Python scripts
python 08-assets\scripts\use-cases\use-case-prioritisation\organize_use_cases.py

# Word conversion (requires Pandoc)
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Validate  # Test round-trip
```

### PR Title Format

```
[CAPABILITY] - New or updated capability definition
[ABB]        - Architecture Building Block changes
[SBB]        - Solution Building Block changes
[ADR]        - Architecture Decision Record
[PATTERN]    - Architecture pattern
[DOCS]       - Documentation updates
```

## Essential Commands

**No build or test commands** - this is a documentation repository.

**Common operations**:
```powershell
# Search for existing ADRs
Get-ChildItem -Path "05-governance\decisions" -Filter "ADR-*.md"

# Find all epics
Get-ChildItem -Path "07-roadmap\epics" -Filter "EPIC-*.md"

# Run use case organization script
python 08-assets\scripts\use-cases\use-case-prioritisation\organize_use_cases.py

# Convert use cases to Word (requires Pandoc: choco install pandoc)
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -UseCaseId "UC-019"  # Single use case
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Validate            # Test round-trip quality

# Export draw.io diagrams to PNG
python 01-motivation\03-use-cases\use-case-prioritisation\scripts\export-drawio-to-png.py
```

## What NOT to Do

❌ **Don't** create ABBs with vendor-specific technologies (that's an SBB)
❌ **Don't** skip traceability links between artifacts
❌ **Don't** violate BNZ visual design standards for diagrams
❌ **Don't** create work items in wrong taxonomy level (e.g., calling a feature an epic)
❌ **Don't** create files without using existing templates
❌ **Don't** put implementation stories in this repo (use Jira/Azure DevOps)
❌ **Don't** modify glossary terms without architecture team approval

## Key Reference Files

When in doubt, consult these files:
- **Repository guide**: `README.md` (comprehensive structure overview)
- **Claude guidance**: `CLAUDE.md` (detailed agent instructions)
- **Contribution process**: `CONTRIBUTING.md` (PR guidelines, review process)
- **Terminology**: `glossary.md` (definitions of ABB, SBB, ADR, etc.)
- **Visual standards**: `05-governance/standards/visual-design/visual-design-standard.md`
- **Work taxonomy**: `07-roadmap/README.md` (how to organize delivery work)
- **Capability model**: `02-capabilities/README.md` (capability maturity levels)

## Capability Maturity Model

All capabilities are scored 0-5:
- **0** = None
- **1** = Initial (ad-hoc, manual)
- **2** = Developing (repeatable, some automation)
- **3** = Defined (standardized, consistent)
- **4** = Managed (measured, SLAs tracked)
- **5** = Optimizing (continuous improvement, data-driven)

When proposing new work, reference current capability maturity and target state.

## Approval Requirements

| Change Type | Approval Needed |
|-------------|----------------|
| Documentation fixes, clarifications | Single reviewer |
| Capability updates, ABB/SBB additions | Architecture lead |
| New principles, significant ADRs | Architecture review board |
| Visual design standard changes | Architecture practice approval |

## Special Notes

- **No code execution**: This is pure documentation - if you need to run Python scripts, they're for automation only
- **Draw.io files**: Edit `.drawio` files; export to PNG is optional and handled by scripts
- **Excel/CSV files**: Use case prioritization data lives in `01-motivation/03-use-cases/use-case-prioritisation/data/`
- **Templates are mandatory**: Always use existing templates rather than creating from scratch
- **Vendor neutrality**: Keep capabilities and ABBs vendor-agnostic; vendor specifics go in SBBs only
