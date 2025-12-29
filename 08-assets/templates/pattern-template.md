# AI Architecture Pattern Template

## Document Control

| Property | Value |
|----------|-------|
| **Pattern ID** | `PT-XXX` (e.g., PT-001) |
| **Pattern Name** | [Name of Pattern] |
| **Version** | `1.0.0` |
| **Status** | `Draft` / `Review` / `Approved` |
| **Created Date** | `YYYY-MM-DD` |
| **Last Modified** | `YYYY-MM-DD` |
| **Owner** | BNZ Enterprise Architecture |
| **Pattern Category** | `GenAI` / `ML Prediction` / `Document Intelligence` / `Real-Time` / `Data` / `Governance` / `Agent` |
| **Maturity Level** | `Mature` / `Emerging` / `Early` / `Experimental` |

---

## 1. Pattern Overview

### 1.1 Pattern Name and Classification

**Pattern Name**: [Full descriptive name]

**Short Name**: [Abbreviated name for diagrams]

**Pattern Category**: [Select from: GenAI, ML Prediction, Document Intelligence, Real-Time, Data, Governance, Agent, Cross-Cutting]

**Pattern Type**: [Select from: Integration, Processing, Storage, Orchestration, Security, etc.]

### 1.2 Intent and Context

**Intent Statement**:
[One-sentence description of what this pattern does]

**Problem Statement**:
[Describe the business or technical problem this pattern solves]

**Context**:
[When and where is this pattern applicable? What are the typical scenarios?]

**Forces**:
[What are the competing concerns and trade-offs this pattern addresses?]
- Force 1: [e.g., Need for real-time processing vs. cost constraints]
- Force 2: [e.g., Accuracy requirements vs. latency requirements]
- Force 3: [e.g., Flexibility vs. complexity]

### 1.3 Pattern Maturity and Industry Adoption

**Maturity Level**: [Mature / Emerging / Early / Experimental]

**Industry Adoption**:
- **Adoption Rate**: [e.g., 75% of enterprises in financial services]
- **Reference Implementations**: [List 2-3 known implementations]
- **Timeframe**: [e.g., Mainstream since 2024, Expected mainstream by 2026]

**Standards Alignment**:
- [List relevant standards, e.g., SAFe, TOGAF, ISO standards]

---

## 2. Architecture Specification

### 2.1 Architecture Building Blocks (ABBs)

**Primary ABBs** (Core components required):

| ABB ID | ABB Name | Purpose in Pattern | Criticality |
|--------|----------|-------------------|-------------|
| ABB-XXX-001 | [ABB Name] | [Role in pattern] | Critical / High / Medium |
| ABB-XXX-002 | [ABB Name] | [Role in pattern] | Critical / High / Medium |
| ABB-XXX-003 | [ABB Name] | [Role in pattern] | Critical / High / Medium |

**Supporting ABBs** (Optional or scenario-specific):

| ABB ID | ABB Name | Purpose in Pattern | When Required |
|--------|----------|-------------------|---------------|
| ABB-XXX-004 | [ABB Name] | [Role in pattern] | [Conditions when needed] |

**Cross-Cutting ABBs** (Always required):

| ABB ID | ABB Name | Purpose |
|--------|----------|---------|
| ABB-GOV-001 | AI Governance Platform | Compliance, risk management, audit |
| ABB-SEC-001 | Security & Identity | Authentication, authorization, encryption |
| ABB-OBS-001 | Observability Platform | Monitoring, logging, alerting |

### 2.2 Pattern Structure

**Architectural Diagram**: See [PATTERN-XXX-Architecture-v1.0.0.drawio](#diagram-templates)

**Component Interaction Flow**:
```
[Component A] → [Component B] → [Component C]
    ↓               ↓               ↓
[Supporting Service 1]  [Supporting Service 2]
    ↓
[Final Output]
```

**Key Interactions**:
1. **[Interaction 1]**: [Component A] sends [data/request] to [Component B]
   - Protocol: [REST, gRPC, messaging, etc.]
   - Data Format: [JSON, Protobuf, etc.]
   - Latency Target: [e.g., < 100ms]

2. **[Interaction 2]**: [Component B] processes and forwards to [Component C]
   - Processing Type: [Synchronous/Asynchronous]
   - Error Handling: [Retry logic, circuit breaker, etc.]

3. **[Interaction 3]**: [Final output routing]
   - Delivery Mechanism: [How results are delivered]

### 2.3 Data Flow

**Data Sources**:
- [Source 1]: [Description, format, volume]
- [Source 2]: [Description, format, volume]

**Data Transformations**:
1. **[Transformation 1]**: [Input format → Output format]
2. **[Transformation 2]**: [Processing description]

**Data Sinks**:
- [Sink 1]: [Destination, format, retention]
- [Sink 2]: [Destination, format, retention]

**Data Governance**:
- **Classification**: [Public / Internal / Confidential / Restricted]
- **Retention**: [Retention period and policy]
- **Lineage**: [How data lineage is tracked]
- **Quality**: [Data quality checks applied]

### 2.4 Interface Specifications

**Inbound Interfaces** (Inputs to pattern):

| Interface ID | Interface Name | Type | Protocol | Data Format | SLA |
|--------------|---------------|------|----------|-------------|-----|
| IF-IN-001 | [Interface name] | [API/Message/Event] | [REST/gRPC/Kafka] | [JSON/Protobuf] | [Latency/Throughput] |

**Outbound Interfaces** (Outputs from pattern):

| Interface ID | Interface Name | Type | Protocol | Data Format | SLA |
|--------------|---------------|------|----------|-------------|-----|
| IF-OUT-001 | [Interface name] | [API/Message/Event] | [REST/gRPC/Kafka] | [JSON/Protobuf] | [Latency/Throughput] |

**Internal Interfaces** (Between ABBs within pattern):

| Interface ID | Source ABB | Target ABB | Protocol | Purpose |
|--------------|-----------|-----------|----------|---------|
| IF-INT-001 | ABB-XXX-001 | ABB-XXX-002 | [Protocol] | [Purpose] |


## 3. Pattern Variants and Options

### 3.1 Pattern Variations

**Variant 1: [Name]**
- **When to Use**: [Specific scenarios]
- **Key Differences**: [How it differs from base pattern]
- **Trade-offs**: [What you gain/lose]

**Variant 2: [Name]**
- **When to Use**: [Specific scenarios]
- **Key Differences**: [How it differs from base pattern]
- **Trade-offs**: [What you gain/lose]

### 3.2 Composition with Other Patterns

**Commonly Combined With**:

| Pattern | Integration Point | Combined Benefit |
|---------|------------------|------------------|
| [Pattern A] | [How they connect] | [Why combine them] |
| [Pattern B] | [How they connect] | [Why combine them] |

**Anti-Patterns** (What NOT to do):
- **Anti-Pattern 1**: [Description]
  - **Why Problematic**: [Issues it causes]
  - **Better Approach**: [Alternative solution]

---

## 4. References and Resources

### 4.1 Related Patterns

| Pattern ID | Pattern Name | Relationship | Reference |
|-----------|-------------|--------------|-----------|
| PATTERN-XXX | [Name] | Depends on / Used with / Alternative to | [Link] |

### 4.2 Related ABBs

| ABB ID | ABB Name | Document Link |
|--------|----------|---------------|
| ABB-XXX-001 | [Name] | [Link to ABB document] |

### 4.3 Standards and Guidelines

- [Standard 1]: [Link or reference]
- [Standard 2]: [Link or reference]

### 4.4 External References

**Industry Research**:
- [Author/Organization]: [Title] - [URL]
- [Author/Organization]: [Title] - [URL]

**Technology Documentation**:
- [Technology]: [Official documentation URL]
- [Technology]: [Official documentation URL]

**Vendor Resources**:
- [Vendor]: [Resource description] - [URL]

---

## 5. Diagram Templates

**Required Diagrams** (to be created using draw.io templates):

1. **[PATTERN-XXX-Architecture-v1.0.0.drawio]**: High-level architecture showing ABBs and their relationships
2. **[PATTERN-XXX-Data-Flow-v1.0.0.drawio]**: Data flow through the pattern

See [Draw.io Diagram Templates](#diagram-templates) section for templates.

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

---

## Appendix B: Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Name] | Initial version |

---

## Appendix C: Review and Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Pattern Author** | [Name] | | |
| **Enterprise Architect** | [Name] | | |
| **Security Architect** | [Name] | | |
| **TAF** | [Name] | | |

