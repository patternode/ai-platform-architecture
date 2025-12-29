# Architecture Building Block (ABB) Template

## Document Control

| Property | Value |
|----------|-------|
| **ABB ID** | `ABB-XXX-001` (e.g., ABB-GEN-001, ABB-GOV-001) |
| **ABB Name** | [Name of Architecture Building Block] |
| **Version** | `1.0.0` |
| **Status** | `Draft` / `Review` / `Approved` |
| **Created Date** | `YYYY-MM-DD` |
| **Last Modified** | `YYYY-MM-DD` |
| **Owner** | BNZ Enterprise Architecture |
| **Category** | `GenAI` / `ML` / `Data` / `Governance` / `Security` / `Integration` / `Observability` |

---

## 1. ABB Overview

### 1.1 Definition

**ABB Name**: [Full descriptive name]

**Short Name**: [Abbreviated name for diagrams]

**Category**: [Select from: GenAI, ML, Data, Governance, Security, Integration, Observability, Infrastructure]

**Description**:
[2-3 sentence description of what this ABB provides. Remember: ABBs are vendor-agnostic logical components that describe WHAT is needed, not HOW it is implemented.]

### 1.2 Purpose and Rationale

**Business Purpose**:
[Why does the business need this building block? What business outcomes does it enable?]

**Technical Purpose**:
[What technical capability does this ABB provide to the AI platform?]

**Key Responsibilities**:
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

### 1.3 Scope

**In Scope**:
- [What this ABB includes]
- [Functionality it provides]
- [Boundaries of responsibility]

**Out of Scope**:
- [What this ABB does NOT include]
- [Responsibilities that belong to other ABBs]

---

## 2. Functional Specification

### 2.1 Core Capabilities

| Capability ID | Capability Name | Description | Priority |
|---------------|-----------------|-------------|----------|
| CAP-001 | [Capability Name] | [Description] | Must Have |
| CAP-002 | [Capability Name] | [Description] | Must Have |
| CAP-003 | [Capability Name] | [Description] | Should Have |
| CAP-004 | [Capability Name] | [Description] | Could Have |

### 2.2 Functional Requirements

**Primary Functions**:

| Requirement ID | Requirement | Acceptance Criteria |
|----------------|-------------|---------------------|
| FR-001 | [Requirement description] | [How to verify] |
| FR-002 | [Requirement description] | [How to verify] |
| FR-003 | [Requirement description] | [How to verify] |

### 2.3 Non-Functional Requirements

| Category | Requirement | Target | Rationale |
|----------|-------------|--------|-----------|
| **Performance** | [e.g., Response time] | [e.g., < 100ms p99] | [Why this target] |
| **Scalability** | [e.g., Concurrent requests] | [e.g., 10,000 req/sec] | [Why this target] |
| **Availability** | [e.g., Uptime] | [e.g., 99.9%] | [Why this target] |
| **Security** | [e.g., Encryption] | [e.g., TLS 1.3, AES-256] | [Compliance requirement] |
| **Compliance** | [e.g., Data residency] | [e.g., NZ/AU only] | [Regulatory requirement] |

---

## 3. Integration Specification

### 3.1 Dependencies

**Upstream Dependencies** (ABBs this building block depends on):

| ABB ID | ABB Name | Dependency Type | Description |
|--------|----------|-----------------|-------------|
| ABB-XXX-001 | [ABB Name] | Required / Optional | [How this ABB uses it] |

**Downstream Consumers** (ABBs that depend on this building block):

| ABB ID | ABB Name | Dependency Type | Description |
|--------|----------|-----------------|-------------|
| ABB-XXX-002 | [ABB Name] | Required / Optional | [How they use this ABB] |

### 3.2 Interfaces

**Input Interfaces**:

| Interface ID | Interface Name | Protocol | Data Format | Description |
|--------------|----------------|----------|-------------|-------------|
| IF-IN-001 | [Interface Name] | REST/gRPC/Kafka | JSON/Protobuf/Avro | [Description] |

**Output Interfaces**:

| Interface ID | Interface Name | Protocol | Data Format | Description |
|--------------|----------------|----------|-------------|-------------|
| IF-OUT-001 | [Interface Name] | REST/gRPC/Kafka | JSON/Protobuf/Avro | [Description] |

### 3.3 Data Contracts

**Input Data**:
```yaml
# Example input schema
input_schema:
  type: object
  properties:
    field1:
      type: string
      description: "[Description]"
    field2:
      type: number
      description: "[Description]"
  required:
    - field1
```

**Output Data**:
```yaml
# Example output schema
output_schema:
  type: object
  properties:
    result:
      type: string
      description: "[Description]"
    metadata:
      type: object
      description: "[Description]"
```

---

## 4. Quality Attributes

### 4.1 Performance Characteristics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Latency (p50) | [Target] | [How measured] |
| Latency (p99) | [Target] | [How measured] |
| Throughput | [Target] | [How measured] |
| Error Rate | [Target] | [How measured] |

### 4.2 Reliability Requirements

| Attribute | Requirement | Recovery Strategy |
|-----------|-------------|-------------------|
| Availability | [e.g., 99.9%] | [e.g., Active-passive failover] |
| Durability | [e.g., 99.999999999%] | [e.g., Multi-region replication] |
| Recovery Time (RTO) | [e.g., < 15 minutes] | [Recovery procedure] |
| Recovery Point (RPO) | [e.g., < 1 minute] | [Backup strategy] |

### 4.3 Security Requirements

| Security Control | Requirement | Implementation Guidance |
|-----------------|-------------|------------------------|
| Authentication | [Requirement] | [Guidance] |
| Authorization | [Requirement] | [Guidance] |
| Encryption at Rest | [Requirement] | [Guidance] |
| Encryption in Transit | [Requirement] | [Guidance] |
| Audit Logging | [Requirement] | [Guidance] |

---

## 5. Governance

### 5.1 Ownership and Accountability

| Role | Responsibility | Contact |
|------|----------------|---------|
| Architecture Owner | Strategic direction, design decisions | [Team/Person] |
| Technical Owner | Implementation, maintenance | [Team/Person] |
| Operations Owner | Day-to-day operations, monitoring | [Team/Person] |

### 5.2 Lifecycle Management

| Phase | Activities | Exit Criteria |
|-------|-----------|---------------|
| Design | Requirements gathering, architecture design | Architecture approved |
| Build | SBB selection, implementation | Testing complete |
| Deploy | Production deployment, integration | Production validated |
| Operate | Monitoring, maintenance, support | Ongoing |
| Retire | Migration, decommissioning | Replacement deployed |

### 5.3 Change Management

**Change Categories**:
- **Minor**: Configuration changes, bug fixes (no approval required)
- **Standard**: Feature additions, SBB upgrades (team approval)
- **Major**: Interface changes, capability additions (architecture board approval)

---

## 6. Solution Building Block Options

### 6.1 Candidate SBBs

**Note**: This section lists potential technology implementations. See individual SBB documents for detailed specifications.

| SBB ID | SBB Name | Vendor | Deployment Model | Maturity | Recommendation |
|--------|----------|--------|------------------|----------|----------------|
| SBB-XXX-001 | [SBB Name] | [Vendor] | SaaS/PaaS/Self-Managed | Mature/Emerging | Recommended / Alternative / Not Recommended |
| SBB-XXX-002 | [SBB Name] | [Vendor] | SaaS/PaaS/Self-Managed | Mature/Emerging | Recommended / Alternative / Not Recommended |
| SBB-XXX-003 | [SBB Name] | Open Source | Self-Managed | Mature/Emerging | Recommended / Alternative / Not Recommended |

### 6.2 Selection Criteria

| Criterion | Weight | SBB-001 Score | SBB-002 Score | SBB-003 Score |
|-----------|--------|---------------|---------------|---------------|
| Functionality | 30% | [1-5] | [1-5] | [1-5] |
| Performance | 20% | [1-5] | [1-5] | [1-5] |
| Cost | 15% | [1-5] | [1-5] | [1-5] |
| Integration | 15% | [1-5] | [1-5] | [1-5] |
| Support | 10% | [1-5] | [1-5] | [1-5] |
| Security | 10% | [1-5] | [1-5] | [1-5] |
| **Weighted Total** | 100% | [Total] | [Total] | [Total] |

---

## 7. Traceability

### 7.1 Capability Mapping

| Capability ID | Capability Name | Level | How This ABB Supports |
|---------------|-----------------|-------|----------------------|
| CAP-L1-XXX | [Capability] | L1 | [Description] |
| CAP-L2-XXX | [Capability] | L2 | [Description] |

### 7.2 Pattern Usage

| Pattern ID | Pattern Name | Role in Pattern |
|------------|--------------|-----------------|
| PT-XXX | [Pattern Name] | Primary / Supporting / Cross-cutting |

### 7.3 Use Case Support

| Use Case ID | Use Case Name | How This ABB Supports |
|-------------|---------------|----------------------|
| UC-XXX | [Use Case Name] | [Description] |

---

## 8. References

### 8.1 Related Documents

- [Link to related ABBs]
- [Link to SBB specifications]
- [Link to patterns that use this ABB]
- [Link to ADRs related to this ABB]

### 8.2 External References

- [Industry standards]
- [Vendor documentation]
- [Best practice guides]

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

---

## Appendix B: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Author] | Initial version |
