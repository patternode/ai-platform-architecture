# Contributing to AI Platform Architecture

This guide explains how to contribute to the AI Platform Architecture repository.

## Overview

This repository follows a structured governance model to ensure quality and consistency of architecture artifacts. All changes should be proposed via pull requests and reviewed according to the processes defined in `06-governance/`.

## Contribution Process

### 1. Before You Start

- Review the relevant architecture principles in `02-principles/`
- Check existing ADRs in `06-governance/decisions/` to understand past decisions
- Familiarize yourself with the templates in `09-assets/templates/`

### 2. Making Changes

#### Small Changes (Documentation fixes, clarifications)
1. Create a branch from `main`
2. Make your changes
3. Submit a pull request

#### Significant Changes (New capabilities, ABBs, SBBs, ADRs)
1. Discuss with the architecture team first
2. Use the appropriate template from `09-assets/templates/`
3. Create a branch from `main`
4. Make your changes following the template structure
5. Ensure all traceability links are updated
6. Submit a pull request with detailed description

### 3. Pull Request Guidelines

**PR Title Format:**
- `[CAPABILITY]` - New or updated capability definition
- `[ABB]` - Architecture Building Block changes
- `[SBB]` - Solution Building Block changes
- `[ADR]` - Architecture Decision Record
- `[PATTERN]` - Architecture pattern
- `[DOCS]` - Documentation updates

**PR Description Should Include:**
- What changed and why
- Which artifacts are affected
- Links to related work items or epics
- Any dependencies or impacts

### 4. Review Process

See `06-governance/review-process.md` for detailed review criteria.

**Review Levels:**
- **Minor changes** (documentation fixes): Single reviewer approval
- **Moderate changes** (capability updates, ABB/SBB additions): Architecture lead approval
- **Major changes** (new principles, significant ADRs): Architecture review board approval

## File Organization

### When Creating New Files

1. **Use Templates**: Always start with the appropriate template from `09-assets/templates/`
2. **Follow Naming Conventions**: See `06-governance/standards/naming-conventions.md`
3. **Maintain Traceability**: Update cross-reference matrices when adding new artifacts
4. **Update Catalogs**: Add entries to relevant catalog files (e.g., `abb-catalog.md`, `sbb-catalog.md`)

### Folder Structure

Place new files in the appropriate folder:
- Business capabilities → `03-capabilities/`
- Logical components → `04-building-blocks/architecture-building-blocks/`
- Technology implementations → `04-building-blocks/solution-building-blocks/`
- Reusable patterns → `04-building-blocks/patterns/`
- Architecture views → `05-reference-architecture/`
- Decisions → `06-governance/decisions/`
- Standards → `06-governance/standards/`
- Work planning → `08-roadmap/`

## Architecture Artifact Types

### Capabilities
Define WHAT business outcomes the platform enables. Keep them vendor-agnostic and stable.

### Architecture Building Blocks (ABBs)
Define WHAT logical components are needed. Keep them vendor-agnostic and reusable.

### Solution Building Blocks (SBBs)
Define HOW we implement with specific technologies. Include concrete details like versions, configurations, and deployment patterns.

### Patterns
Document proven solutions to recurring problems. Reference the ABBs and SBBs used.

### Architecture Decision Records (ADRs)
Document significant decisions with context, options considered, and rationale. Use the ADR template and follow the lifecycle (proposed → accepted → superseded).

## Standards Compliance

All contributions must comply with:
- Architecture principles in `02-principles/`
- Standards in `06-governance/standards/`
- Security requirements in `02-principles/security-principles.md`
- Data principles in `02-principles/data-principles.md`

## Questions or Issues?

- Architecture questions: Contact the platform architecture team
- Process questions: See `06-governance/architecture-governance.md`
- Technical questions: See relevant ABB/SBB documentation

## License

Internal use only. All rights reserved.
