# Capabilities

> Business capabilities enabled by the AI Platform

---

## Overview

This folder contains the business capability model for the AI Platform. Capabilities define **WHAT** the platform does in business terms, independent of **HOW** it's implemented. They are organized hierarchically and remain stable over time, evolving slowly as business needs change.

### Purpose

- Define platform capabilities from a business perspective
- Map capabilities to Architecture Building Blocks (ABBs)
- Track capability maturity and investment priorities
- Provide traceability from business outcomes to technical implementation

### Audience

- Product owners
- Business stakeholders
- Platform architects
- Delivery teams

---

## Capability Model

The capability model is organized into **L0 → L1 → L2** levels:

| Level | Description | Example |
|-------|-------------|---------|
| **L0** | Capability Domain | Models, Agents, Knowledge |
| **L1** | Capability Group | Model Development, Model Serving |
| **L2** | Specific Capability | Model Training, Real-time Inference |

---

## Capability Domains (L0)

### 🤖 Agents
AI agents that can autonomously perform tasks, make decisions, and interact with systems and users.

- **agentic-ai/** - Common agent mechanisms and frameworks
- **low-code/** - Low-code agent development capabilities
- **high-code/** - High-code agent development capabilities

### 🧠 Models
Machine learning and AI model lifecycle management from development through production.

- **model-development/** - Experimentation, training, and model creation
- **model-serving/** - Real-time and batch inference capabilities
- **llm-orchestration/** - LLM gateway, prompt management, RAG, and agent coordination

### 📚 Knowledge
Data and knowledge management for AI/ML workloads.

- **data-management/** - Feature stores, embeddings, data access, and lineage

### 🛡️ Governance
AI governance, compliance, and responsible AI practices.

- Contains capabilities for model approval, bias detection, compliance tracking, and audit trails

### 📊 Observability
Platform and model observability, monitoring, and performance tracking.

- Contains capabilities for metrics collection, logging, drift detection, and alerting

### 👥 Experiences and Engagement
User experiences and stakeholder engagement capabilities.

- Contains capabilities for user interfaces, collaboration, and feedback mechanisms

### 🛠️ Practices
Development practices and platform tooling.

- **developer-experience/** - Self-service portals, SDKs, documentation, and developer tools

---

## Capability Structure

Each capability area follows a consistent structure:

```
capability-name/
├── overview.md           # Capability description and scope
├── sub-capabilities.md   # L2 breakdown of specific capabilities
└── abb-mapping.md        # Links to ABBs that realize this capability
```

### File Descriptions

| File | Purpose | Content |
|------|---------|---------|
| `overview.md` | Defines the capability | Business context, scope, stakeholders, success metrics |
| `sub-capabilities.md` | Lists L2 capabilities | Detailed breakdown of specific capabilities with descriptions |
| `abb-mapping.md` | Traceability matrix | Maps capabilities to Architecture Building Blocks (ABBs) |

---

## Capability Maturity Levels

Each capability is assessed against a maturity model:

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **0 - None** | Not available | Capability does not exist |
| **1 - Initial** | Ad-hoc | Manual, inconsistent, reactive |
| **2 - Developing** | Repeatable | Some automation, documented processes |
| **3 - Defined** | Standardized | Well-defined, consistent, proactive |
| **4 - Managed** | Measured | Quantitatively managed, SLAs tracked |
| **5 - Optimizing** | Continuous improvement | Data-driven optimization, innovation |

Maturity levels are tracked in `capability-model.md` and visualized in `capability-map.md`.

---

## Key Artifacts

### Top-Level Files

| File | Description |
|------|-------------|
| `capability-model.md` | Complete capability taxonomy (L0/L1/L2) with descriptions |
| `capability-map.md` | Visual capability map with maturity heat map and investment priorities |

---

## Usage Guidelines

### When to Update Capabilities

- **Quarterly reviews** to assess maturity progression
- **New business requirements** that introduce new capabilities
- **Strategic pivots** that change capability priorities
- **Governance approval required** for significant changes

### How to Add a New Capability

1. Discuss with architecture team to validate business need
2. Determine capability level (L0/L1/L2) and placement
3. Create folder structure following the template
4. Document overview, sub-capabilities, and ABB mappings
5. Update `capability-model.md` and `capability-map.md`
6. Submit PR with [CAPABILITY] tag

### Traceability

Capabilities link to implementation through this chain:

```
Capability → ABB (04-building-blocks/architecture-building-blocks/)
         → SBB (04-building-blocks/solution-building-blocks/)
         → Implementation (code repositories)
```

---

## Governance

### Update Frequency

- **Quarterly**: Maturity assessment and priority review
- **As-needed**: New capabilities or significant changes
- **Approval required**: Architecture review board for L0/L1 changes

### Change Process

1. Propose change via PR with detailed justification
2. Architecture team review
3. Stakeholder validation for business alignment
4. Update related ABB mappings
5. Communicate changes to affected teams

---

## Related Artifacts

- **Vision**: `01-vision/business-capabilities.md` - High-level capability overview
- **ABBs**: `04-building-blocks/architecture-building-blocks/` - Technical components
- **Roadmap**: `08-roadmap/` - Capability delivery timeline
- **Reference Architecture**: `05-reference-architecture/` - How capabilities compose

---

## Templates

Use the capability template when creating new capability documentation:

- `09-assets/templates/capability-template.md`

---

*For questions about capabilities or to propose changes, contact the Platform Architecture team.*
