# Changelog

All notable changes to the AI Platform Architecture are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

## [1.0.0] - 2025-12-12

### Added
- Initial public release
- 130 Architecture Building Blocks (ABBs)
- 21 Architectural Patterns
- Complete capability model (L0-L2)
- Governance framework including ADRs and standards
- Visual design standards for diagrams
- Work taxonomy and roadmap structure

### Changed
- Restructured repository for Git-based versioning
- Renamed files to support MkDocs static site generation
- Updated all internal hyperlinks for stability

### Infrastructure
- Added mkdocs.yml for static site generation
- Added VERSION file for semantic versioning
- Added CHANGELOG.md for change tracking

---

## Versioning Guidelines

### Repository Version (Git Tags)
- **MAJOR**: Breaking changes to ABB interfaces, capability model restructuring
- **MINOR**: New ABBs, new patterns, new capabilities (backward compatible)
- **PATCH**: Documentation fixes, clarifications, diagram updates

### Individual Artifact Versioning
Each ABB, Pattern, and major document tracks its own version in metadata:
```yaml
---
artifact_version: 1.0.0
introduced_in: v1.0.0
last_modified_in: v1.0.0
---
```

---

[Unreleased]: https://github.com/bnz/ai-platform-architecture/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bnz/ai-platform-architecture/releases/tag/v1.0.0
