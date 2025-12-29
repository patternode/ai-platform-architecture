# AI Platform Implementation Roadmap

> Indicative roadmap for BNZ AI Platform capabilities delivery across Q4 FY25 - Q4 FY26

---

## Document Information

| Attribute | Value |
|-----------|-------|
| **Status** | Draft |
| **Classification** | Confidential |
| **Period** | Q4 FY25 - Q4 FY26 (Aug 2025 - Sept 2026) |
| **Last Updated** | 2025-12-03 |
| **Owner** | BNZ Strategy & Architecture Team |
| **Note** | Indicative, to be refined via QPS planning for Q2 |

---

## Contents

- [Overview](#overview)
- [Roadmap Phases](#roadmap-phases)
- [Capability Domains](#capability-domains)
  - [Agents](#1-agents-capability)
  - [Models](#2-models-capability)
  - [Knowledge](#3-knowledge-capability)
- [Technology Platforms](#technology-platforms)
- [Key Milestones](#key-milestones)
- [Dependencies and Decision Points](#dependencies-and-decision-points)
- [Strategic Themes](#strategic-themes)
- [Related Artifacts](#related-artifacts)

---

## Overview

This roadmap defines the phased delivery of BNZ's AI Platform capabilities over a 14-month period, organized into three major capability domains (Agents, Models, Knowledge) with supporting technology platforms.

### Roadmap Structure

The roadmap follows a **progressive maturity model**:

```
Phase 1: Foundation (Q4 FY25 - Q1 FY26)
  ↓
Phase 2: Production Readiness (Q2 FY26)
  ↓
Phase 3: Enterprise Integration (Q3-Q4 FY26)
```

---

## Roadmap Phases

### Phase 1: Foundation (Q4 FY25 - Q1 FY26)
**Timeline**: Aug 2025 - Dec 2025

**Objectives**:
- Define target state architectures for Agents and Knowledge
- Make critical technology direction decisions
- Establish foundational platforms and workbenches
- Begin infrastructure setup

**Key Outcomes**:
- Agent capabilities and UI foundation established
- High/Low code direction decided
- SageMaker Workbench operational for DD&A
- Knowledge target state defined
- Vector and Graph database directions confirmed
- AgentCore and Copilot Studio MVP ready

---

### Phase 2: Production Readiness (Q2 FY26)
**Timeline**: Jan 2026 - Mar 2026

**Objectives**:
- Move core platforms to production readiness
- Enable foundation models for agent use
- Deploy vector RAG capabilities
- Establish enterprise integration patterns

**Key Outcomes**:
- AgentCore and Copilot Studio production ready
- Agents target state endorsed
- Foundation models (LLMs) available to agents
- Vector RAG available to agents
- APIs, integration and gateways operational
- Knowledge target state (safe data leverage) endorsed

---

### Phase 3: Enterprise Integration (Q3-Q4 FY26)
**Timeline**: Apr 2026 - Sept 2026

**Objectives**:
- Enable agents to consume enterprise data
- Integrate custom BNZ models with agent platform
- Deploy graph database and advanced RAG
- Scale infrastructure and observability

**Key Outcomes**:
- Agents can use enterprise data and foundation models
- Graph/RAG available to agents
- Custom models available to agents
- Model uplift for agent integration complete
- Full technology platform operational
- Engineering and AI operations practices mature

---

## Capability Domains

### 1. Agents Capability

**Duration**: Q4 FY25 - Q4 FY26 (Full roadmap period)

**Capability Reference**: [02-capabilities/agents/](../02-capabilities/)

#### Q4 FY25 (Aug-Sep 2025)
- **Agent capabilities and Agent UI foundation**
  - Initial agent framework setup
  - UI components for agent interaction
- **High / Low code direction decision**
  - Strategic decision on agent development approach
  - Impact: Determines tooling and platform choices

#### Q1 FY26 (Oct-Dec 2025)
- **Agents target state definition complete**
  - Architecture documented
  - Reference patterns established
- **AgentCore and Copilot Studio MVP**
  - Initial agent orchestration capabilities
  - Microsoft Copilot Studio integration

#### Q2 FY26 (Jan-Mar 2026)
- **AgentCore and Copilot Studio Production ready**
  - Production-grade infrastructure
  - SLAs defined and met
- **Agents target state endorsed**
  - Architecture review board approval
  - Governance framework approved

#### Q3 FY26 (Apr-Jun 2026)
- **Agents can use enterprise data and foundation models**
  - Integration with enterprise data sources
  - LLM orchestration operational
  - Secure data access patterns

#### Q4 FY26 (Jul-Sep 2026)
- **Agents can use custom models**
  - Integration with BNZ-specific models
  - Custom model serving endpoints
  - Agent-to-model orchestration

---

### 2. Models Capability

**Duration**: Q4 FY25 - Q4 FY26 (Multiple concurrent workstreams)

**Capability Reference**: [02-capabilities/models/](../02-capabilities/)

#### Model Management Workstream

**Foundation Models Timeline**:
- **Q1 FY26**: Models target state definition complete
- **Q2 FY26**: Foundation models (LLMs) available to agents
- **Q4 FY26**: Custom models available to agents

**Model Uplift Releases**:
- **R1 - Foundation** (Q2 FY26)
  - Basic model registry and serving
  - Initial LLM access
- **R2 - Publishing into BDH (no AI)** (Q3 FY26)
  - Model metadata publishing
  - Integration with Bank Data Hub
- **R3 - TBD** (Q4 FY26)
  - Agent integration capabilities
- **R4 - TBD** (Q4 FY26)
  - Advanced agent-model orchestration

#### BNZ-Specific Models Workstream

**SageMaker Workbench** (for DD&A / Data Science use only):
- **Q4 FY25**: Initial deployment
  - Workbench setup for data science teams
  - Basic model development capabilities

**Model Serving Evolution**:
- **Q1-Q2 FY26**: Uplift for limited production use / Scoping for AI use
  - Production deployment patterns
  - Model versioning and governance
- **Q3 FY26**: Uplift for use outside analytics (e.g., fraud via PEGA)
  - Cross-platform model serving
  - Integration with PEGA workflows
- **Q4 FY26**: Uplift for agent integration (agents using custom BNZ models)
  - Agent-to-model APIs
  - Custom model orchestration

#### Supporting Capabilities (Continuous)
- **Model Serving**: Ongoing throughout roadmap
- **Model Hosting**: Ongoing throughout roadmap
- **Model Observability**: Ongoing throughout roadmap

---

### 3. Knowledge Capability

**Duration**: Q4 FY25 - Q4 FY26 (Multiple parallel initiatives)

**Capability Reference**: [02-capabilities/knowledge/](../02-capabilities/)

#### Semantic Modeling & Data Access

**Q4 FY25**:
- **Knowledge capabilities defined (draft)**
  - Initial knowledge architecture
  - Semantic layer design

**Q1 FY26**:
- **Knowledge target state definition complete**
  - Knowledge target state (safe leverage of data by agents)
  - Data governance for AI established
  - Semantic management framework

**Q2-Q4 FY26**:
- **Knowledge target state endorsed**
  - Architecture approved
  - Ongoing refinement and implementation

#### Graph Database Workstream

**Q4 FY25**:
- **Graph database direction (Need)**
  - Technology evaluation initiated
  - Use case definition

**Q1-Q2 FY26**:
- **Graph Database options**
  - Vendor evaluation (NeoJ and alternatives)
  - POC and testing

**Q2-Q3 FY26**:
- **Graph/RAG available to agents - NeoJ Procurement and Deployment**
  - NeoJ deployment (pending procurement)
  - Graph-based RAG patterns
  - Integration with agent platform

#### Vector Database Workstream

**Q4 FY25**:
- **Vector Database confirmation**
  - Technology selection finalized
  - Architecture designed

**Q4 FY25 - Q2 FY26**:
- **MongoDb implementation (for Technology / Enterprise Simplification)**
  - MongoDB vector search deployment
  - Enterprise integration patterns

**Q2 FY26**:
- **Uplift for vector embeddings**
  - Embedding pipeline established
  - Vector search optimization
- **Vector RAG available to agents**
  - Vector-based retrieval
  - Agent integration complete

#### Data Sources and Targets

**Q4 FY25 onwards**:
- **Data Sources and Data Targets (agent consumption of enterprise data)**
  - Data projection capabilities
  - Semantic management (ontology, taxonomy, knowledge graphs)
  - Data lineage and governance

---

## Technology Platforms

**Horizontal capabilities supporting all domains**

### Integration Platform
**Timeline**: Q1-Q2 FY26

**Capabilities**:
- APIs, integration and gateways
- Enterprise service bus
- API management

**Milestone**: Technology platform target state for AI endorsed (Q2 FY26)

---

### Security Platform
**Timeline**: Q1-Q4 FY26

**Capabilities**:
- **Q1-Q3 FY26**: Agents, applications and workflows (PEGA), User experience and engagement
  - Identity and access management for agents
  - Application security controls
  - Workflow security (PEGA integration)
- **Q1-Q4 FY26**: Security risk, controls and identity
  - Security governance
  - Risk assessment framework
  - Identity management

---

### Data Platform
**Timeline**: Q4 FY25 - Q4 FY26 (Continuous)

**Capabilities**:
- Data sources and data targets
- Agent consumption of enterprise data
- Semantic management (ontology, taxonomy, knowledge graphs)
- Data governance for AI
- Data lineage and cataloging

---

### Infrastructure Platform
**Timeline**: Q4 FY25 - Q3 FY26

**Capabilities**:
- Agent frameworks
- Agent discovery and orchestration
- Memory management
- Observability and monitoring
- Tool discovery and registry
- Hosting and scaling infrastructure

---

### Engineering Platform
**Timeline**: Q1-Q3 FY26

**Capabilities**:
- Engineering and AI operations practices
- MLOps and AIOps
- Governance frameworks
- Observability and monitoring
- CI/CD pipelines for AI

---

## Key Milestones

### Q4 FY25 Milestones (Aug-Sep 2025)

| Milestone | Domain | Description | Status |
|-----------|--------|-------------|--------|
| Agent capabilities foundation | Agents | Initial agent framework and UI | Planned |
| High/Low code direction | Agents | Strategic decision on development approach | Dependency |
| SageMaker Workbench deployed | Models | DD&A workbench operational | Planned |
| Knowledge capabilities defined | Knowledge | Draft knowledge architecture | Planned |
| Vector Database confirmed | Knowledge | Technology selection finalized | Dependency |
| Graph database direction | Knowledge | Evaluation decision | Dependency |

---

### Q1 FY26 Milestones (Oct-Dec 2025)

| Milestone | Domain | Description | Status |
|-----------|--------|-------------|--------|
| Agents target state defined | Agents | Complete architecture documentation | Planned |
| AgentCore and Copilot Studio MVP | Agents | MVP ready for testing | Planned |
| Models target state defined | Models | Model platform architecture complete | Planned |
| Knowledge target state defined | Knowledge | Safe data leverage architecture | Planned |

---

### Q2 FY26 Milestones (Jan-Mar 2026)

| Milestone | Domain | Description | Status |
|-----------|--------|-------------|--------|
| AgentCore Production Ready | Agents | Production-grade agent platform | Planned |
| Agents target state endorsed | Agents | Architecture approved | Planned |
| Foundation models available | Models | LLMs accessible to agents (R1) | Planned |
| Vector RAG available | Knowledge | Vector-based retrieval operational | Planned |
| Technology platform endorsed | Platforms | AI platform architecture approved | Planned |

---

### Q3 FY26 Milestones (Apr-Jun 2026)

| Milestone | Domain | Description | Status |
|-----------|--------|-------------|--------|
| Agents use enterprise data | Agents | Secure enterprise data access | Planned |
| Models in BDH | Models | Model publishing to Bank Data Hub (R2) | Planned |
| Graph/RAG available | Knowledge | Graph-based retrieval operational | Planned |
| PEGA model integration | Models | Fraud models in PEGA workflows | Planned |

---

### Q4 FY26 Milestones (Jul-Sep 2026)

| Milestone | Domain | Description | Status |
|-----------|--------|-------------|--------|
| Agents use custom models | Agents | BNZ models integrated with agents | Planned |
| Custom models platform (R3/R4) | Models | Full agent-model orchestration | Planned |
| Knowledge target state mature | Knowledge | Complete knowledge platform | Planned |

---

## Dependencies and Decision Points

### Critical Decisions (Q4 FY25)

| Decision | Impact | Timeline | Owner |
|----------|--------|----------|-------|
| **High/Low code direction** | Determines agent development tooling and platforms | Q4 FY25 | Architecture Team |
| **Graph database selection** | Affects knowledge graph implementation approach | Q4 FY25 | Architecture Team |
| **Vector database confirmation** | Finalizes vector RAG architecture | Q4 FY25 | Architecture Team |

### Key Dependencies

**Agents Domain Dependencies**:
- ✓ Agent capabilities definition → Agent target state
- ✓ Agent target state → Production deployment
- ✓ Foundation models availability → Agents can use LLMs
- ✓ Knowledge platform → Agents can use enterprise data
- ✓ Custom models platform → Agents can use BNZ models

**Models Domain Dependencies**:
- ✓ Model target state definition → Foundation models deployment
- ✓ R1 Foundation → R2 BDH Publishing → R3/R4 Agent Integration
- ✓ SageMaker workbench → Production model serving
- ✓ Model governance → Production deployment

**Knowledge Domain Dependencies**:
- ✓ Knowledge capabilities defined → Target state definition
- ✓ Vector DB confirmation → Vector RAG deployment
- ✓ Graph DB direction → Graph RAG deployment
- ✓ Knowledge target state → Safe agent data access

**Technology Platform Dependencies**:
- ✓ Infrastructure platform → All agent capabilities
- ✓ Security platform → Production deployments
- ✓ Integration platform → Enterprise data access
- ✓ Engineering platform → Operational maturity

---

## Strategic Themes

### Theme 1: Foundation and Discovery (Q4 FY25 - Q1 FY26)
**Strategic Focus**: Establish foundational capabilities and make critical technology decisions

**Key Activities**:
- Define target state architectures
- Make technology selection decisions
- Deploy workbenches and dev environments
- Establish governance frameworks
- Build initial infrastructure

**Success Criteria**:
- All target states defined and documented
- Critical technology decisions made
- MVP platforms operational
- Governance processes established

**Related Work**:
- Link to Theme document: `07-roadmap/themes/foundation-and-discovery.md` (to be created)

---

### Theme 2: Production Readiness and Integration (Q2 FY26)
**Strategic Focus**: Move core platforms to production and enable enterprise integration

**Key Activities**:
- Production-harden agent platforms
- Deploy foundation models
- Enable vector RAG
- Establish API gateways
- Implement security controls
- Endorse target state architectures

**Success Criteria**:
- Production SLAs met
- Foundation models accessible
- Vector RAG operational
- Security controls approved
- Architecture endorsed by review board

**Related Work**:
- Link to Theme document: `07-roadmap/themes/production-readiness.md` (to be created)

---

### Theme 3: Enterprise Scale and Custom Integration (Q3-Q4 FY26)
**Strategic Focus**: Enable enterprise-wide adoption and custom model integration

**Key Activities**:
- Enable agents to consume enterprise data
- Deploy graph database and advanced RAG
- Integrate custom BNZ models
- Scale infrastructure
- Mature observability
- Expand to cross-platform use cases (PEGA)

**Success Criteria**:
- Agents accessing enterprise data securely
- Custom models integrated
- Graph RAG operational
- Cross-platform integration (PEGA) working
- Full technology platform operational
- Production at scale

**Related Work**:
- Link to Theme document: `07-roadmap/themes/enterprise-scale.md` (to be created)

---

## Related Artifacts

### Capabilities
- [Agents Capabilities](../02-capabilities/agents/) - Agent capability definitions
- [Models Capabilities](../02-capabilities/models/) - Model management capabilities
- [Knowledge Capabilities](../02-capabilities/knowledge/) - Knowledge and data capabilities

### Architecture Building Blocks
- [Agent Orchestrator ABB](../03-building-blocks/architecture-building-blocks/) - Logical agent components
- [Model Registry ABB](../03-building-blocks/architecture-building-blocks/) - Model management
- [Vector Store ABB](../03-building-blocks/architecture-building-blocks/) - Vector database abstraction
- [Graph Store ABB](../03-building-blocks/architecture-building-blocks/) - Graph database abstraction

### Solution Building Blocks
- [AgentCore SBB](../03-building-blocks/solution-building-blocks/) - AgentCore implementation
- [Copilot Studio SBB](../03-building-blocks/solution-building-blocks/) - Microsoft Copilot Studio
- [SageMaker SBB](../03-building-blocks/solution-building-blocks/) - AWS SageMaker workbench
- [MongoDB Vector Search SBB](../03-building-blocks/solution-building-blocks/) - MongoDB vector implementation
- [NeoJ SBB](../03-building-blocks/solution-building-blocks/) - NeoJ graph database

### Governance
- [ADR: High/Low Code Direction](../05-governance/decisions/) - Agent development approach (pending)
- [ADR: Vector Database Selection](../05-governance/decisions/) - Vector DB technology choice (pending)
- [ADR: Graph Database Selection](../05-governance/decisions/) - Graph DB technology choice (pending)
- [AI Governance Framework](../05-governance/standards/) - Governance standards for AI

### Epics (To Be Created)
- `EPIC-XXX: AgentCore and Copilot Studio Production Deployment`
- `EPIC-XXX: Foundation Models Integration Platform`
- `EPIC-XXX: Vector RAG Implementation`
- `EPIC-XXX: Graph Database Deployment`
- `EPIC-XXX: Custom Models Platform for Agents`
- `EPIC-XXX: Enterprise Data Access for Agents`
- `EPIC-XXX: SageMaker Workbench Production Deployment`
- `EPIC-XXX: Model Uplift Program (R1-R4)`

---

## Roadmap Governance

### Review Cycle
- **Monthly**: Progress review against milestones
- **Quarterly**: QPS planning alignment and refinement
- **Next Review**: Q2 planning (to refine this indicative roadmap)

### Change Management
- Changes to milestone dates require Architecture Team approval
- Changes to capability scope require Architecture Review Board approval
- Technology decisions require ADR documentation

### Stakeholders
- **Owner**: BNZ Strategy & Architecture Team
- **Approver**: Architecture Review Board
- **Contributors**: Platform teams, Product owners, Engineering leads
- **Informed**: Business stakeholders, Executive sponsors

---

## Appendix

### Glossary of Terms

| Term | Definition |
|------|------------|
| **AgentCore** | BNZ's agent orchestration platform |
| **Copilot Studio** | Microsoft's agent development platform |
| **RAG** | Retrieval-Augmented Generation - pattern for enhancing LLM responses with external knowledge |
| **SageMaker** | AWS machine learning platform for model development |
| **BDH** | Bank Data Hub - BNZ's central data platform |
| **PEGA** | BNZ's workflow and decisioning platform |
| **DD&A** | Data, Digital & Analytics team |
| **NeoJ** | Graph database technology |
| **R1, R2, R3, R4** | Release stages for model platform uplift |

### References
- [AI Platform Architecture README](../README.md)
- [Capability Model](../02-capabilities/README.md)
- [Work Taxonomy Guide](./README.md)
- [Visual Design Standards](../05-governance/standards/visual-design/visual-design-standard.md)

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-12-03 | Claude Code | Initial roadmap documentation from PNG analysis |

**Status**: Draft
**Next Update**: Q2 FY26 (following QPS planning refinement)
