# AI Platform Capability Model

## Document Control

| Property | Value |
|----------|-------|
| **Version** | `1.0.0` |
| **Status** | `Draft` |
| **Last Updated** | `2025-12-06` |
| **Owner** | BNZ Enterprise Architecture |

---

## Overview

This document defines the complete capability model for the BNZ AI Platform. Capabilities are organized into a three-level hierarchy (L0 → L1 → L2) that describes **WHAT** the platform does in business terms, independent of **HOW** it's implemented.

### Capability Hierarchy

| Level | Description | Stability | Example |
|-------|-------------|-----------|---------|
| **L0** | Capability Domain | Very stable (years) | AI Governance |
| **L1** | Capability Group | Stable (quarters) | Risk & Compliance |
| **L2** | Specific Capability | Evolves (months) | Model Risk Assessment |

---

## Capability Domains (L0)

| L0 ID | Domain | Description | L1 Count |
|-------|--------|-------------|----------|
| CAP-L0-GOV | AI Governance | Enterprise governance, risk, and compliance for AI | 5 |
| CAP-L0-DAT | Data & Knowledge | Data management, feature engineering, and knowledge systems | 5 |
| CAP-L0-MOD | Model Lifecycle | ML model development, training, and operations | 5 |
| CAP-L0-GEN | Generative AI | LLM orchestration, RAG, and generative capabilities | 4 |
| CAP-L0-AGT | Agentic AI | Autonomous agents, multi-agent systems, and automation | 4 |
| CAP-L0-INT | Integration & Events | Real-time processing, event-driven architecture | 4 |
| CAP-L0-OBS | Observability | Monitoring, alerting, and platform visibility | 4 |
| CAP-L0-SEC | Security & Privacy | Security controls, privacy protection, access management | 4 |
| CAP-L0-EXP | Experiences | User interfaces, conversational AI, personalization | 4 |
| CAP-L0-DEV | Developer Platform | Self-service, tooling, and developer experience | 3 |

---

## Complete Capability Taxonomy

### CAP-L0-GOV: AI Governance

*Enterprise governance, risk management, and compliance for AI systems.*

#### CAP-L1-GOV-01: Model Governance

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GOV-01-01 | Model Registry | Centralized catalog of all AI/ML models with versioning and metadata | PT-001, PT-002 | ABB-GOV-001, ABB-MLO-002 |
| CAP-L2-GOV-01-02 | Model Lifecycle Management | Manage models from development through retirement | PT-001, PT-002 | ABB-MLO-004 |
| CAP-L2-GOV-01-03 | Model Approval Workflow | Multi-level approval gates for model deployment | PT-001 | ABB-GOV-003 |
| CAP-L2-GOV-01-04 | Model Versioning | Track model versions and enable rollback | PT-002, PT-010 | ABB-MLO-002, ABB-MLO-007 |

#### CAP-L1-GOV-02: Risk & Compliance

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GOV-02-01 | Model Risk Assessment | Automated risk scoring and tier classification | PT-001 | ABB-GOV-002 |
| CAP-L2-GOV-02-02 | Compliance Monitoring | Track compliance with GDPR, AML, Model Risk policies | PT-001 | ABB-GOV-005 |
| CAP-L2-GOV-02-03 | Regulatory Reporting | Generate compliance reports for regulators | PT-001 | ABB-GOV-005 |
| CAP-L2-GOV-02-04 | Policy Enforcement | Enforce governance policies through AI Gateway | PT-001 | ABB-GOV-007 |

#### CAP-L1-GOV-03: Explainability & Fairness

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GOV-03-01 | Model Explainability | Generate SHAP/LIME explanations for predictions | PT-004 | ABB-GOV-004, ABB-GOV-009 |
| CAP-L2-GOV-03-02 | Bias Detection | Detect and report bias across demographic groups | PT-004 | ABB-GOV-010, ABB-FAI-001 |
| CAP-L2-GOV-03-03 | Fairness Monitoring | Continuous fairness metrics monitoring | PT-004 | ABB-FAI-001 |
| CAP-L2-GOV-03-04 | Explanation Visualization | Visual dashboards for model explanations | PT-004 | ABB-VIS-001 |

#### CAP-L1-GOV-04: Audit & Lineage

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GOV-04-01 | Audit Trail | Immutable logging of all AI decisions and changes | PT-001 | ABB-GOV-006 |
| CAP-L2-GOV-04-02 | Data Lineage | Track data flow from source to prediction | PT-001, PT-012 | ABB-GOV-011, ABB-SEC-012 |
| CAP-L2-GOV-04-03 | Model Lineage | Track model dependencies and training data | PT-001 | ABB-GOV-011 |
| CAP-L2-GOV-04-04 | Decision Provenance | Trace how each AI decision was made | PT-001, PT-004 | ABB-GOV-006 |

#### CAP-L1-GOV-05: Cost Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GOV-05-01 | Cost Attribution | Attribute AI costs to use cases and models | PT-001 | ABB-GOV-008 |
| CAP-L2-GOV-05-02 | Budget Enforcement | Enforce cost limits and quotas | PT-007 | ABB-AGT-009 |
| CAP-L2-GOV-05-03 | Cost Optimization | Recommend cost reduction opportunities | PT-006 | ABB-OBS-005 |
| CAP-L2-GOV-05-04 | Chargeback Reporting | Generate cost allocation reports | PT-001 | ABB-GOV-008 |

---

### CAP-L0-DAT: Data & Knowledge

*Data management, feature engineering, and knowledge systems for AI/ML.*

#### CAP-L1-DAT-01: Feature Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DAT-01-01 | Offline Feature Store | Store historical features for model training | PT-003 | ABB-DAT-001, ABB-FTR-003 |
| CAP-L2-DAT-01-02 | Online Feature Store | Serve features in real-time (<10ms latency) | PT-003, PT-009 | ABB-FTR-001 |
| CAP-L2-DAT-01-03 | Feature Engineering | Transform raw data into ML features | PT-003 | ABB-FTR-002 |
| CAP-L2-DAT-01-04 | Feature Registry | Catalog features with metadata and lineage | PT-003 | ABB-DAT-001 |
| CAP-L2-DAT-01-05 | Point-in-Time Joins | Prevent data leakage in training data | PT-003 | ABB-DAT-001 |

#### CAP-L1-DAT-02: Data Storage & Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DAT-02-01 | Data Lake | Scalable storage for structured/unstructured data | PT-012 | ABB-DAT-002 |
| CAP-L2-DAT-02-02 | Data Versioning | Version control for datasets | PT-003, PT-014 | ABB-DAT-003 |
| CAP-L2-DAT-02-03 | Data Catalog | Discover and understand available data | PT-012 | ABB-DSH-001 |
| CAP-L2-DAT-02-04 | Data Quality Management | Monitor and ensure data quality | PT-003, PT-017 | ABB-OBS-009, ABB-BAT-006 |

#### CAP-L1-DAT-03: Knowledge Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DAT-03-01 | Knowledge Base | Structured storage for organizational knowledge | PT-005 | ABB-KNW-001 |
| CAP-L2-DAT-03-02 | Vector Store | Store and retrieve embeddings for semantic search | PT-005 | ABB-GEN-002 |
| CAP-L2-DAT-03-03 | Document Indexing | Process and index documents for retrieval | PT-005, PT-011 | ABB-GEN-008 |
| CAP-L2-DAT-03-04 | Knowledge Graph | Represent relationships between entities | PT-005 | ABB-KNW-001 |

#### CAP-L1-DAT-04: Data Products

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DAT-04-01 | Data Product Catalog | Publish and discover data products | PT-012 | ABB-DSH-001 |
| CAP-L2-DAT-04-02 | Domain Data Ownership | Enable domain teams to own their data | PT-012 | ABB-DSH-002 |
| CAP-L2-DAT-04-03 | Data Contracts | Define and enforce data quality contracts | PT-012 | ABB-DSH-003 |
| CAP-L2-DAT-04-04 | Self-Serve Data Access | Enable self-service data consumption | PT-012 | ABB-DSH-002 |

#### CAP-L1-DAT-05: Data Integration

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DAT-05-01 | Data Ingestion | Ingest data from multiple sources | PT-015 | ABB-INT-003 |
| CAP-L2-DAT-05-02 | Data Transformation | Transform data for consumption | PT-016 | ABB-INT-002 |
| CAP-L2-DAT-05-03 | Schema Registry | Manage data schemas and evolution | PT-015 | ABB-INT-001 |
| CAP-L2-DAT-05-04 | Data Pipeline Orchestration | Orchestrate complex data workflows | PT-014 | ABB-BAT-001 |

---

### CAP-L0-MOD: Model Lifecycle

*ML model development, training, serving, and operations.*

#### CAP-L1-MOD-01: Model Development

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-MOD-01-01 | Model Training | Train ML models on historical data | PT-002 | ABB-MLO-001 |
| CAP-L2-MOD-01-02 | Experiment Tracking | Track experiments and hyperparameters | PT-002 | ABB-MLO-001 |
| CAP-L2-MOD-01-03 | AutoML | Automated model selection and tuning | PT-002 | ABB-MLO-001 |
| CAP-L2-MOD-01-04 | Model Validation | Validate models before deployment | PT-002 | ABB-MLO-003 |

#### CAP-L1-MOD-02: Model Serving

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-MOD-02-01 | Real-Time Inference | Sub-100ms model predictions | PT-009 | ABB-INF-001, ABB-MDL-002 |
| CAP-L2-MOD-02-02 | Batch Prediction | Large-scale batch scoring | PT-014 | ABB-BAT-001, ABB-BAT-003 |
| CAP-L2-MOD-02-03 | Model Caching | Cache predictions for performance | PT-009 | ABB-CAC-001 |
| CAP-L2-MOD-02-04 | Load Balancing | Distribute load across model replicas | PT-009 | ABB-LDB-001 |

#### CAP-L1-MOD-03: Model Operations

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-MOD-03-01 | Model Monitoring | Monitor model performance in production | PT-002, PT-017 | ABB-MLO-005 |
| CAP-L2-MOD-03-02 | Drift Detection | Detect data and concept drift | PT-017 | ABB-OBS-002, ABB-OBS-003, ABB-OBS-004 |
| CAP-L2-MOD-03-03 | Automated Retraining | Trigger retraining based on drift | PT-002 | ABB-OBS-011 |
| CAP-L2-MOD-03-04 | Model Rollback | Rollback to previous model versions | PT-002, PT-010 | ABB-MLO-007 |

#### CAP-L1-MOD-04: Model Testing

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-MOD-04-01 | A/B Testing | Compare model variants in production | PT-010 | ABB-CMP-001 |
| CAP-L2-MOD-04-02 | Champion-Challenger | Run challenger models alongside champion | PT-010 | ABB-CMP-001, ABB-CMP-002 |
| CAP-L2-MOD-04-03 | Statistical Validation | Validate results with statistical tests | PT-010 | ABB-CMP-003 |
| CAP-L2-MOD-04-04 | Model Promotion | Promote challenger to champion | PT-010 | ABB-CMP-004 |

#### CAP-L1-MOD-05: Model Optimization

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-MOD-05-01 | Model Quantization | Optimize models for inference | PT-009 | ABB-MDL-007 |
| CAP-L2-MOD-05-02 | Feature Selection | Select optimal features for models | PT-003 | ABB-FTR-002 |
| CAP-L2-MOD-05-03 | Hyperparameter Tuning | Optimize model hyperparameters | PT-002 | ABB-MLO-001 |
| CAP-L2-MOD-05-04 | Model Fallback | Handle model failures gracefully | PT-006, PT-009 | ABB-MLO-006, ABB-MDL-006 |

---

### CAP-L0-GEN: Generative AI

*Large language model orchestration, RAG, and generative capabilities.*

#### CAP-L1-GEN-01: LLM Orchestration

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GEN-01-01 | LLM Gateway | Unified access to multiple LLM providers | PT-006 | ABB-GEN-001 |
| CAP-L2-GEN-01-02 | Multi-Model Routing | Route requests to optimal model | PT-006 | ABB-RTE-001 |
| CAP-L2-GEN-01-03 | Cost-Based Routing | Optimize model selection by cost | PT-006 | ABB-RTE-002 |
| CAP-L2-GEN-01-04 | Latency-Based Routing | Route based on latency requirements | PT-006 | ABB-RTE-003 |
| CAP-L2-GEN-01-05 | Capability-Based Routing | Route based on model capabilities | PT-006 | ABB-RTE-004 |

#### CAP-L1-GEN-02: Retrieval-Augmented Generation

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GEN-02-01 | Semantic Search | Vector-based document retrieval | PT-005 | ABB-GEN-003 |
| CAP-L2-GEN-02-02 | Hybrid Search | Combine keyword and semantic search | PT-005 | ABB-GEN-005 |
| CAP-L2-GEN-02-03 | Document Reranking | Rerank retrieved documents for relevance | PT-005 | ABB-GEN-006 |
| CAP-L2-GEN-02-04 | Query Rewriting | Reformulate queries for better retrieval | PT-005 | ABB-GEN-010 |
| CAP-L2-GEN-02-05 | Citation Generation | Attribute sources in LLM responses | PT-005 | ABB-GEN-009 |

#### CAP-L1-GEN-03: Content Generation

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GEN-03-01 | Text Generation | Generate natural language text | PT-005, PT-007 | ABB-GEN-001 |
| CAP-L2-GEN-03-02 | Summarization | Summarize documents and conversations | PT-013 | ABB-CNV-007 |
| CAP-L2-GEN-03-03 | Natural Language Generation | Convert structured data to text | PT-004 | ABB-NLG-001 |
| CAP-L2-GEN-03-04 | Self-Critique | Evaluate and refine generated content | PT-005 | ABB-GEN-007 |

#### CAP-L1-GEN-04: Document Intelligence

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-GEN-04-01 | Document Classification | Categorize documents by type | PT-011 | ABB-DOC-001 |
| CAP-L2-GEN-04-02 | OCR & Text Extraction | Extract text from images/scans | PT-011 | ABB-DOC-002 |
| CAP-L2-GEN-04-03 | Entity Extraction | Extract entities from documents | PT-011 | ABB-NLP-001 |
| CAP-L2-GEN-04-04 | Document Forensics | Detect document tampering | PT-011 | ABB-DOC-003 |
| CAP-L2-GEN-04-05 | Document Processing Pipeline | End-to-end document processing | PT-011 | ABB-GEN-008 |

---

### CAP-L0-AGT: Agentic AI

*Autonomous agents, multi-agent systems, and intelligent automation.*

#### CAP-L1-AGT-01: Agent Core

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-AGT-01-01 | Agent Orchestration | Coordinate agent execution | PT-007, PT-008 | ABB-AGT-001 |
| CAP-L2-AGT-01-02 | Tool Integration | Enable agents to use tools/APIs | PT-007 | ABB-AGT-002 |
| CAP-L2-AGT-01-03 | Agent Memory | Short and long-term agent memory | PT-007 | ABB-AGT-003 |
| CAP-L2-AGT-01-04 | Task Planning | Break complex goals into steps | PT-007 | ABB-AGT-004 |
| CAP-L2-AGT-01-05 | Plan Execution | Execute planned actions | PT-007 | ABB-AGT-005 |

#### CAP-L1-AGT-02: Agent Intelligence

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-AGT-02-01 | Self-Reflection | Evaluate and adjust strategies | PT-007 | ABB-AGT-006 |
| CAP-L2-AGT-02-02 | Multi-Step Reasoning | Logical inference across steps | PT-007 | ABB-AGT-001 |
| CAP-L2-AGT-02-03 | Learning from Feedback | Improve via user corrections | PT-007 | ABB-AGT-006 |
| CAP-L2-AGT-02-04 | Proactive Suggestions | Anticipate user needs | PT-007 | ABB-AGT-001 |

#### CAP-L1-AGT-03: Multi-Agent Systems

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-AGT-03-01 | Inter-Agent Communication | Message passing between agents | PT-008 | ABB-AGT-007 |
| CAP-L2-AGT-03-02 | Agent Specialization | Domain-specific expert agents | PT-008 | ABB-AGT-001 |
| CAP-L2-AGT-03-03 | Result Aggregation | Combine outputs from multiple agents | PT-008 | ABB-AGT-005 |
| CAP-L2-AGT-03-04 | Conflict Resolution | Handle disagreements between agents | PT-008 | ABB-AGT-006 |

#### CAP-L1-AGT-04: Agent Governance

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-AGT-04-01 | Human-in-the-Loop | Approval gates for high-risk actions | PT-007 | ABB-AGT-008 |
| CAP-L2-AGT-04-02 | Agent Cost Monitoring | Track token and API costs | PT-007 | ABB-AGT-009 |
| CAP-L2-AGT-04-03 | Agent Versioning | Version control for agent configs | PT-007 | ABB-AGT-010 |
| CAP-L2-AGT-04-04 | Agent Audit Trail | Log all agent decisions and actions | PT-007 | ABB-GOV-006 |

---

### CAP-L0-INT: Integration & Events

*Real-time processing, event-driven architecture, and system integration.*

#### CAP-L1-INT-01: Event Processing

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-INT-01-01 | Event Streaming | Publish/subscribe event model | PT-015 | ABB-INT-001 |
| CAP-L2-INT-01-02 | Event Sourcing | Immutable event stream as truth | PT-015 | ABB-INT-001 |
| CAP-L2-INT-01-03 | Event Replay | Replay events for recovery/testing | PT-015 | ABB-INT-006 |
| CAP-L2-INT-01-04 | Dead Letter Handling | Handle failed message processing | PT-015 | ABB-INT-005 |

#### CAP-L1-INT-02: Stream Processing

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-INT-02-01 | Real-Time Feature Computation | Compute features from streams | PT-016 | ABB-INT-002 |
| CAP-L2-INT-02-02 | Windowed Aggregations | Tumbling, sliding, session windows | PT-016 | ABB-INT-002 |
| CAP-L2-INT-02-03 | Pattern Detection | Identify complex event patterns | PT-016 | ABB-INT-002 |
| CAP-L2-INT-02-04 | Stream Joins | Correlate multiple data streams | PT-016 | ABB-INT-002 |

#### CAP-L1-INT-03: API Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-INT-03-01 | API Gateway | Central API access and routing | PT-001 | ABB-API-001 |
| CAP-L2-INT-03-02 | Rate Limiting | Enforce API rate limits | PT-001 | ABB-API-001 |
| CAP-L2-INT-03-03 | API Versioning | Manage API versions | PT-001 | ABB-API-001 |
| CAP-L2-INT-03-04 | API Analytics | Track API usage and performance | PT-017 | ABB-API-001 |

#### CAP-L1-INT-04: Batch Processing

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-INT-04-01 | Batch Orchestration | Orchestrate batch workflows | PT-014 | ABB-BAT-001 |
| CAP-L2-INT-04-02 | Distributed Processing | Parallelize across nodes | PT-014 | ABB-BAT-003 |
| CAP-L2-INT-04-03 | Incremental Processing | Process only changed data | PT-014 | ABB-BAT-007 |
| CAP-L2-INT-04-04 | Checkpoint & Resume | Recover from batch failures | PT-014 | ABB-BAT-001 |

---

### CAP-L0-OBS: Observability

*Monitoring, alerting, and platform visibility.*

#### CAP-L1-OBS-01: Platform Monitoring

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-OBS-01-01 | Metrics Collection | Collect platform metrics | PT-017 | ABB-OBS-001 |
| CAP-L2-OBS-01-02 | Log Aggregation | Centralize logs from all services | PT-017 | ABB-OBS-001 |
| CAP-L2-OBS-01-03 | Distributed Tracing | Trace requests across services | PT-017 | ABB-OBS-001 |
| CAP-L2-OBS-01-04 | Alerting | Alert on anomalies and SLA violations | PT-017 | ABB-OBS-007 |

#### CAP-L1-OBS-02: Model Monitoring

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-OBS-02-01 | Performance Monitoring | Track accuracy, latency, throughput | PT-017 | ABB-OBS-001 |
| CAP-L2-OBS-02-02 | Data Drift Detection | Detect input distribution changes | PT-017 | ABB-OBS-002 |
| CAP-L2-OBS-02-03 | Prediction Drift Detection | Detect output distribution changes | PT-017 | ABB-OBS-003 |
| CAP-L2-OBS-02-04 | Concept Drift Detection | Detect relationship changes | PT-017 | ABB-OBS-004 |

#### CAP-L1-OBS-03: Business Monitoring

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-OBS-03-01 | Business Metrics | Link model to business outcomes | PT-017 | ABB-OBS-008 |
| CAP-L2-OBS-03-02 | Cost Tracking | Track infrastructure costs | PT-017 | ABB-OBS-005 |
| CAP-L2-OBS-03-03 | Latency Monitoring | Track inference latency | PT-017 | ABB-OBS-006 |
| CAP-L2-OBS-03-04 | GenAI Quality Monitoring | Monitor LLM output quality | PT-017 | ABB-OBS-010 |

#### CAP-L1-OBS-04: Dashboards & Reporting

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-OBS-04-01 | Operational Dashboards | Real-time operational health | PT-017 | ABB-OBS-012 |
| CAP-L2-OBS-04-02 | Executive Dashboards | High-level platform visibility | PT-017 | ABB-OBS-012 |
| CAP-L2-OBS-04-03 | Custom Reporting | Ad-hoc reporting capabilities | PT-017 | ABB-OBS-012 |
| CAP-L2-OBS-04-04 | Root Cause Analysis | Investigate performance issues | PT-017 | ABB-OBS-001 |

---

### CAP-L0-SEC: Security & Privacy

*Security controls, privacy protection, and access management.*

#### CAP-L1-SEC-01: Access Control

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-SEC-01-01 | Authentication | Verify user/service identity | PT-018 | ABB-SEC-002 |
| CAP-L2-SEC-01-02 | Authorization | Role-based access control | PT-018 | ABB-SEC-002 |
| CAP-L2-SEC-01-03 | Identity Management | Manage identities and permissions | PT-018 | ABB-SEC-002 |
| CAP-L2-SEC-01-04 | Secrets Management | Secure credential storage | PT-018 | ABB-SEC-007 |

#### CAP-L1-SEC-02: Data Protection

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-SEC-02-01 | Encryption at Rest | Encrypt stored data | PT-018 | ABB-SEC-001 |
| CAP-L2-SEC-02-02 | Encryption in Transit | Encrypt data in motion | PT-018 | ABB-SEC-001 |
| CAP-L2-SEC-02-03 | Data Masking | Mask sensitive data | PT-018 | ABB-SEC-003 |
| CAP-L2-SEC-02-04 | PII Detection | Detect personally identifiable info | PT-018 | ABB-SEC-003 |

#### CAP-L1-SEC-03: Privacy Engineering

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-SEC-03-01 | Differential Privacy | Add noise to protect privacy | PT-018 | ABB-SEC-008 |
| CAP-L2-SEC-03-02 | Federated Learning | Train without centralizing data | PT-018 | ABB-SEC-009 |
| CAP-L2-SEC-03-03 | Homomorphic Encryption | Compute on encrypted data | PT-018 | ABB-SEC-010 |
| CAP-L2-SEC-03-04 | Secure Multi-Party Computation | Secure cross-party computation | PT-018 | ABB-SEC-011 |

#### CAP-L1-SEC-04: Security Operations

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-SEC-04-01 | Threat Detection | Detect security threats | PT-018 | ABB-SEC-005 |
| CAP-L2-SEC-04-02 | Adversarial Testing | Test against adversarial attacks | PT-018 | ABB-SEC-014 |
| CAP-L2-SEC-04-03 | Model Watermarking | Protect model IP | PT-018 | ABB-SEC-013 |
| CAP-L2-SEC-04-04 | Security Audit Logging | Log security events | PT-018 | ABB-SEC-005 |

---

### CAP-L0-EXP: Experiences

*User interfaces, conversational AI, and personalization.*

#### CAP-L1-EXP-01: Conversational AI

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-EXP-01-01 | Intent Classification | Understand user intent | PT-013 | ABB-CNV-002 |
| CAP-L2-EXP-01-02 | Entity Extraction | Extract entities from text | PT-013 | ABB-CNV-006 |
| CAP-L2-EXP-01-03 | Response Generation | Generate natural responses | PT-013 | ABB-CNV-003 |
| CAP-L2-EXP-01-04 | Conversation Management | Maintain multi-turn context | PT-013 | ABB-CNV-001 |
| CAP-L2-EXP-01-05 | Sentiment Analysis | Detect user sentiment | PT-013 | ABB-CNV-005 |

#### CAP-L1-EXP-02: Channel Management

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-EXP-02-01 | Multi-Channel Support | Web, mobile, voice, messaging | PT-013 | ABB-CNV-008 |
| CAP-L2-EXP-02-02 | Human Handoff | Escalate to human agents | PT-013 | ABB-CNV-004 |
| CAP-L2-EXP-02-03 | Conversation Summarization | Summarize conversation history | PT-013 | ABB-CNV-007 |
| CAP-L2-EXP-02-04 | Context Preservation | Maintain context across channels | PT-013 | ABB-CNV-001 |

#### CAP-L1-EXP-03: Personalization

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-EXP-03-01 | Real-Time Personalization | Personalize in real-time | PT-009 | ABB-FTR-001 |
| CAP-L2-EXP-03-02 | Recommendation Engine | Generate recommendations | PT-009 | ABB-INF-001 |
| CAP-L2-EXP-03-03 | Next-Best-Action | Determine optimal next action | PT-009 | ABB-INF-001 |
| CAP-L2-EXP-03-04 | Dynamic Content | Personalize content dynamically | PT-009 | ABB-INF-001 |

#### CAP-L1-EXP-04: User Assistance

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-EXP-04-01 | AI Assistant | Context-aware AI assistance | PT-007, PT-013 | ABB-AGT-001 |
| CAP-L2-EXP-04-02 | Query Understanding | Understand complex queries | PT-005 | ABB-GEN-004 |
| CAP-L2-EXP-04-03 | Proactive Insights | Surface relevant insights | PT-007 | ABB-AGT-001 |
| CAP-L2-EXP-04-04 | Self-Service Analytics | Enable user-driven analysis | PT-005 | ABB-KNW-001 |

---

### CAP-L0-DEV: Developer Platform

*Self-service capabilities, tooling, and developer experience.*

#### CAP-L1-DEV-01: Self-Service Platform

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DEV-01-01 | Model Deployment Portal | Self-service model deployment | PT-002 | ABB-MLO-004 |
| CAP-L2-DEV-01-02 | Feature Store Access | Self-service feature access | PT-003 | ABB-DAT-001 |
| CAP-L2-DEV-01-03 | Experiment Environment | Self-service experimentation | PT-002 | ABB-MLO-001 |
| CAP-L2-DEV-01-04 | Agent Development | Self-service agent creation | PT-007 | ABB-AGT-001 |

#### CAP-L1-DEV-02: Developer Tooling

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DEV-02-01 | SDKs & Libraries | Client libraries for platform | All | Multiple |
| CAP-L2-DEV-02-02 | API Documentation | Interactive API documentation | All | ABB-API-001 |
| CAP-L2-DEV-02-03 | Code Templates | Starter templates and examples | All | Multiple |
| CAP-L2-DEV-02-04 | CLI Tools | Command-line interfaces | All | Multiple |

#### CAP-L1-DEV-03: Platform Operations

| L2 ID | Capability | Description | Patterns | ABBs |
|-------|------------|-------------|----------|------|
| CAP-L2-DEV-03-01 | CI/CD for ML | Continuous integration for ML | PT-002 | ABB-MLO-004 |
| CAP-L2-DEV-03-02 | Infrastructure as Code | Declarative infrastructure | PT-002 | ABB-MLO-004 |
| CAP-L2-DEV-03-03 | Feature Flags | Control feature rollout | PT-010 | ABB-MLO-009 |
| CAP-L2-DEV-03-04 | Environment Management | Manage dev/test/prod environments | PT-002 | ABB-MLO-004 |

---

## Capability Summary

### Totals by Level

| Level | Count |
|-------|-------|
| L0 Domains | 10 |
| L1 Groups | 42 |
| L2 Capabilities | 168 |

### Capabilities by Domain

| Domain | L1 Groups | L2 Capabilities |
|--------|-----------|-----------------|
| AI Governance | 5 | 20 |
| Data & Knowledge | 5 | 21 |
| Model Lifecycle | 5 | 20 |
| Generative AI | 4 | 18 |
| Agentic AI | 4 | 17 |
| Integration & Events | 4 | 16 |
| Observability | 4 | 16 |
| Security & Privacy | 4 | 16 |
| Experiences | 4 | 17 |
| Developer Platform | 3 | 12 |

---

## Pattern Coverage

| Pattern | Primary Capability Domains |
|---------|---------------------------|
| PT-001 Enterprise AI Governance | CAP-L0-GOV |
| PT-002 MLOps Level 2+ | CAP-L0-MOD, CAP-L0-DEV |
| PT-003 Feature Store | CAP-L0-DAT |
| PT-004 Explainability | CAP-L0-GOV |
| PT-005 RAG | CAP-L0-GEN, CAP-L0-DAT |
| PT-006 Multi-Model Routing | CAP-L0-GEN |
| PT-007 Agentic AI | CAP-L0-AGT |
| PT-008 Multi-Agent Orchestration | CAP-L0-AGT |
| PT-009 Real-Time Scoring | CAP-L0-MOD, CAP-L0-INT |
| PT-010 Champion-Challenger | CAP-L0-MOD |
| PT-011 IDP | CAP-L0-GEN |
| PT-012 Data Mesh | CAP-L0-DAT |
| PT-013 Conversational AI | CAP-L0-EXP |
| PT-014 Batch Prediction | CAP-L0-MOD, CAP-L0-INT |
| PT-015 Event-Driven | CAP-L0-INT |
| PT-016 Stream Processing | CAP-L0-INT |
| PT-017 Observability | CAP-L0-OBS |
| PT-018 Security & Privacy | CAP-L0-SEC |

---

## Related Documents

- [Capability Map](capability-map.md) - Visual capability heat map
- [ABB Index](../03-building-blocks/architecture-building-blocks/README.md) - Architecture Building Blocks
- [Pattern Catalog](../03-building-blocks/patterns/README.md) - Architectural Patterns
- [Use Cases](../01-motivation/03-use-cases/use-cases/README.md) - Business Use Cases

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-06 | BNZ Enterprise Architecture | Initial capability model creation |
