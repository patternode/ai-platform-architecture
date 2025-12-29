# AgentCore Agent Ecosystem - Solution Building Block (SBB)

## Document Control
- **Document Type:** Solution Building Block
- **Version:** 1.0.0
- **Status:** Draft
- **Created Date:** 2025-11-28
- **Last Modified:** 2025-11-28
- **Owner:** BNZ Technology | Strategy & Architecture
- **Architecture Domain:** Application
- **Implementation Phase:** Production

## 1. Solution Building Block Identification

### 1.1 Basic Information
- **SBB ID:** SBB-APP-001
- **SBB Name:** AWS Bedrock AgentCore Agent Ecosystem
- **Short Name:** AgentCore Agent Ecosystem
- **Version:** 1.0.0
- **Classification:** PaaS

### 1.2 Description
**Solution Overview:** AWS Bedrock AgentCore provides an enterprise-grade platform for deploying and operating AI agents at scale. It consists of seven modular services (Runtime, Memory, Gateway, Identity, Observability, Browser Tool, Code Interpreter) that work together to provide production-ready infrastructure for agentic AI applications.

**Procurement Type:** Cloud Service (PaaS)

**Vendor / Provider:** Amazon Web Services (AWS)

**Business Justification:** AWS AgentCore selected for its enterprise-grade security, framework-agnostic architecture (supports Strands, LangGraph, LangChain, CrewAI and custom frameworks), operational tooling, and integration with the AWS ecosystem already adopted by BNZ.

## 2. ABB Realization

### 2.1 Realized ABBs
This SBB realizes **ABB-APP-001: Agentic AI Agent** at 100% using a full implementation approach.

**Known Gaps:**
- **GAP-001:** No built-in low-code visual authoring (code-first approach)
  - **Severity:** Low
  - **Mitigation:** Low-code serves a different purpose than the high-code approach exemplified by AgentCore. Developers use Python/TypeScript SDKs; consider pairing with workflow tools.
  - **Workaround:** Use Infrastructure as Code (IaC) with reusable templates.

### 2.2 ABB Requirements Mapping
| ABB Requirement ID | Requirement Description | AgentCore Feature/Component | Compliance Status | Notes                                                               |
|--------------------|------------------------|---------------------------|-------------------|---------------------------------------------------------------------|
| FN-001 | Natural Language Understanding & Generation | Foundation Model Integration (Bedrock/external LLMs) | Full | Supports any LLM hosted via AWS Bedrock and external LLMs via APIs. |
| FN-002 | Reasoning & Decision Making | Runtime + Custom Agent Frameworks | Full | Framework-agnostic.                                                 |
| FN-003 | Memory Management | AgentCore Memory Service | Full | Dual short/long-term memory.                                        |
| FN-004 | Tool Orchestration & Integration | AgentCore Gateway (MCP support) | Full | Zero-code API transformation.                                       |
| FN-005 | Knowledge Retrieval | Custom RAG implementation via Gateway | Partial | Requires external vector database.                                  |
| FN-006 | Identity & Authorization | AgentCore Identity (Cognito, Okta, Entra ID) | Full | OAuth 2.0, SAML 2.0                                                 |
| FN-007 | Multi-turn Conversation Management | Runtime Session Isolation | Full | 8-hour sessions                                                     |
| FN-008 | Error Handling & Recovery | Observability + CloudWatch | Full | OpenTelemetry compatible                                            |

## 3. Product / Solution Specifications

### 3.1 Product Information
- **Product Name:** Amazon Bedrock AgentCore
- **Product Family:** Amazon Bedrock
- **Version:** Public Preview (as of Nov 2025)
- **Release Date:** 2025-07-16
- **Vendor:** Amazon Web Services, Inc.
- **Website:** https://aws.amazon.com/bedrock/agentcore/
- **Support Contact:** AWS Premium Support
- **Account Manager:** BNZ AWS Platform Team
- **License Model:** Pay-per-use (consumption-based)
- **License Type:** Commercial Cloud Service
- **Restrictions:** Subject to AWS Service Terms

### 3.2 Technical Specifications

**AgentCore Runtime:**
- Execution Model: Serverless (Firecracker microVMs)
- Session Duration: Up to 8 hours
- Isolation: Complete session-level isolation
- Scaling: Automatic based on demand
- Supported Frameworks: Strands, LangChain, LangGraph, CrewAI, Custom
- Supported Languages: Python, TypeScript, JavaScript

**AgentCore Memory:**
- Short-term Memory: Session-based context (up to 8 hours)
- Long-term Memory: Persistent cross-session storage
- API Access: REST APIs and SDKs
- Storage Backend: AWS managed service

**AgentCore Gateway:**
- Protocol Support: Model Context Protocol (MCP), REST, GraphQL
- Tool Transformation: Zero-code API to MCP tool conversion
- AWS Integrations: Native access to 200+ AWS services
- Third-party Connectors: Salesforce, ServiceNow, Slack, GitHub, Microsoft M365

**AgentCore Identity:**
- Supported IdPs: Amazon Cognito, Microsoft Entra ID, Okta, SAML 2.0, Custom OIDC
- Authentication Patterns: OAuth 2.0 Authorization Code, OAuth 2.0 Client Credentials
- Token Management: Automatic refresh and lifecycle

**AgentCore Observability:**
- Telemetry Standard: OpenTelemetry
- CloudWatch Integration: Yes
- Metrics: Latency, Token usage, Tool invocations, Error rates
- Tracing: Distributed tracing with X-Ray compatible
- Dashboards: Pre-built CloudWatch dashboards

**Cloud Specifications:**
- Provider: AWS
- Supported Regions: us-east-1, us-west-2, eu-west-1 (TBC)
- Availability Zones: Multi-AZ deployment
- Deployment Options: Public, VPC-only, Private endpoints (PrivateLink)

### 3.3 Deployment Architecture
- **Deployment Model:** Cloud
- **Deployment Pattern:** Serverless + Managed Services

**Architecture Layers:**
1. **Presentation Layer:** Custom web/mobile apps, API clients
2. **AgentCore Services Layer:** Runtime (serverless agent execution), Gateway (MCP tool integration), Memory (persistent storage), Identity (auth/authz), Observability (monitoring), Browser Tool (web automation), Code Interpreter (sandboxed execution)
3. **Foundation Models Layer:** Amazon Bedrock models, External LLM APIs
4. **External Integrations Layer:** Enterprise APIs, AWS Services, SaaS applications

**Infrastructure as Code:**
- Tool: Terraform
- Repository: TBD
- Version: 1.2.0

## 4. Implemented Functionality

### 4.1 Features & Capabilities

**Core Features:**

| Feature ID | Feature Name | Description | ABB Mapping | Status  | Configuration Required |
|------------|--------------|-------------|-------------|---------|------------------------|
| FE-001 | AgentCore Runtime | Secure serverless execution environment with 8-hour session support | FN-002, FN-007 | TBC [1] | Yes |
| FE-002 | AgentCore Memory | Dual short-term and long-term memory with API access | FN-003 | TBC [1] | Yes |
| FE-003 | AgentCore Gateway | MCP-based tool integration with zero-code API transformation | FN-004 | TBC [1] | Yes |
| FE-004 | AgentCore Identity | Enterprise identity management with multiple IdP support | FN-006 | TBC [1] | Yes |
| FE-005 | AgentCore Observability | OpenTelemetry-based monitoring with CloudWatch dashboards | FN-008 | TBC [1] | Yes |

**Notes:** [1] Depends on NAB MSB compliance approval.

**Optional Features:**
- **FE-OPT-001: AgentCore Browser Tool** - Serverless browser runtime for web automation (Enabled)
- **FE-OPT-002: AgentCore Code Interpreter** - Sandboxed Python code execution (Enabled)

**Custom Extensions:**
- **EX-001: BNZ Knowledge Integration**
  - Description: Custom RAG (vector and graph) pipeline with BNZ knowledge sources
  - Developer: BNZ AI Platform Team
  - Maintenance: BNZ AI Platform Team
  - Repository: TBD

### 4.2 Performance Characteristics

**Measured Metrics:**

To be decided.

**Benchmarks:**

To be decided.

**SLA Compliance:**

To be decided / confirmed.

## 5. Integration & Interfaces

### 5.1 Implemented Interfaces

**Provided Interfaces:**

| Interface ID | Interface Name | Type | Endpoint | Authentication | Rate Limits |
|--------------|----------------|------|----------|----------------|-------------|
| IF-001 | Agent Invocation API | HTTPS REST | https://runtime.agentcore.{region}.amazonaws.com/v1/invoke | AWS IAM Signature V4 | 1000 req/s, 10K concurrent |
| IF-002 | Memory Management API | HTTPS REST | https://memory.agentcore.{region}.amazonaws.com/v1/ | AWS IAM | Standard AWS limits |
| IF-003 | Gateway MCP Endpoint | HTTPS REST / MCP | https://gateway.agentcore.{region}.amazonaws.com/mcp/ | AWS IAM + OAuth 2.0 | Dynamic |

**Interface Details:**
- **IF-001:** OpenAPI 3.0 specification TBC
- **IF-002:** Operations: store_memory, retrieve_memory, search_memory, delete_memory
- **IF-003:** Tools dynamically registered via MCP protocol

**Required Interfaces:**

| Interface ID | Interface Name | Type | Provider | Models/Protocols |
|--------------|----------------|------|----------|------------------|
| IF-REQ-001 | Foundation Model API | HTTPS REST | Amazon Bedrock / External LLMs | Claude 3.5 Sonnet, GPT-4, Custom models |
| IF-REQ-002 | Identity Provider | OAuth 2.0 / SAML 2.0 | Amazon Cognito / Entra ID | OAuth 2.0 Authorization Code, SAML 2.0 |

### 5.2 Integration Patterns Implemented

**Serverless Agent Execution:**
- Protocol: HTTPS REST
- Implementation: Event-driven agent invocation via API Gateway
- Error Handling: Automatic retries with exponential backoff (max 3 retries, 1000ms initial delay)

**MCP Tool Orchestration:**
- Protocol: Model Context Protocol (MCP)
- Implementation: Gateway transforms APIs to MCP tools, agents invoke via standard protocol
- Message Format: JSON-RPC 2.0 over HTTPS

**Asynchronous Memory Operations:**
- Protocol: HTTPS REST
- Implementation: Non-blocking memory storage and retrieval
- Consistency Model: Eventually consistent

### 5.3 Data Integration

**Data Sources:**

The nature of the data sources will depend on the specific use cases implemented by BNZ using AgentCore. 
Below are example data sources that could be integrated.

| Source ID | Source Name | Integration Method | Connector | Frequency | Data Volume |
|-----------|-------------|-------------------|-----------|-----------|-------------|
| DS-001 | BNZ Knowledge Base (SharePoint) | API | Custom Microsoft Graph connector via Gateway | Real-time | TBD         |
| DS-002 | Customer Data Platform (Salesforce) | API | Salesforce REST API via Gateway | On-demand | TBD         |

**Data Targets:**

| Target ID | Target Name | Integration Method | Frequency | Data Entities |
|-----------|-------------|-------------------|-----------|---------------|
| DT-001 | CloudWatch Logs | Stream | Real-time | Agent conversations, Tool invocations, Errors |

## 6. Security Implementation

### 6.1 Security Controls

**Authentication:**
- Methods: AWS IAM, OAuth 2.0, SAML 2.0
- Primary Method: AWS IAM
- Identity Providers: Amazon Cognito, Microsoft Entra ID, Okta
- MFA: Enabled (TOTP, WebAuthn)

**Authorization:**
- Model: IAM Policies + Resource-based policies
- Fine-grained Access: Per-agent, per-tool, per-memory namespace
- Enforcement Point: AWS IAM Policy Engine

**Data Protection:**
- Encryption at Rest: AES-256-GCM with AWS KMS (Customer Managed Keys)
- Encryption in Transit: TLS 1.3 with AWS Certificate Manager
- Data Isolation: Complete session isolation via Firecracker microVMs, VPC isolation with private endpoints

**Security Monitoring:**
- Audit & Security Logging: Enabled
- Log Aggregation: CloudWatch Logs
- Retention Period: 90 days (adjustable)
- SIEM Integration: BNZ Splunk (forwards Authentication, Authorization failures, Tool invocations, Data access)

**Vulnerability Management:**
- Infrastructure: AWS responsibility for patching
- Application: BNZ responsibility for custom agent code scanning

**Compliance:**
- Frameworks: SOC 2, ISO 27001, PCI-DSS (infrastructure)
- AWS Compliance Reports: Available via AWS Artifact

### 6.2 Security Architecture

**Network Security:**
- Deployment Options: Public endpoints with IAM authentication, VPC-only endpoints, AWS PrivateLink for private connectivity
- Network Isolation: VPC with security groups and NACLs

**Application Security:**
- Input Validation: AWS WAF rules for API Gateway
- Prompt Injection Protection: Custom validation logic in agent code
- Secrets Management: AWS Secrets Manager for API keys and credentials

## 7. Operational Characteristics

### 7.1 Deployment & Configuration

**CI/CD Pipeline:**
- Tool: GitHub Actions
- Pipeline URL: TBD
- Build Frequency: On commit to main branch
- Deployment Frequency: TBD

**Deployment Automation:**
- Automation Level: Fully Automated
- Deployment Tool: Terraform + AWS CDK
- Rollback Capability: Yes (< 5 minutes with blue-green deployment)

**Configuration Management:**
- Config Location: AWS Systems Manager Parameter Store
- Config Format: JSON
- Environment Configs: Dev, Test, Staging, Production
- Secrets Management: AWS Secrets Manager
- Config Validation: Automated via pre-deployment hooks

### 7.2 Monitoring & Observability

**Observability Platform:** AWS CloudWatch + X-Ray

**Metrics:**
- Collection Interval: 1 minute
- Retention Period: 15 months
- Key Metrics:
  - Agent Invocation Latency (Warning: 500ms, Critical: 2000ms)
  - Error Rate (Warning: 1%, Critical: 5%)
  - Token Consumption (Warning: 80% of budget, Critical: 95% of budget)

**Logging:**
- Log Aggregation: CloudWatch Logs
- Log Level: INFO (Production), DEBUG (Dev)
- Log Retention: 90 days
- Structured Logging: Yes (JSON format)

**Tracing:**
- Distributed Tracing: Yes (AWS X-Ray)
- Trace Sampling: 5% (production), 100% (dev)

**Alerting:**
- Alerting Tool: CloudWatch Alarms + PagerDuty
- Alert Channels: Email, PagerDuty, Slack
- Escalation Policy: L2 Platform Team → L3 AWS Support
- On-Call Rotation: Weekly

**Dashboards:**
- AgentCore Operations Dashboard (CloudWatch)
- URL: TBD
- Metrics: Invocations, Latency, Errors, Token usage

### 7.3 Backup & Recovery

**Backup:**
- Agent Configurations: Version controlled in Git (on every commit)
- Memory Data: Continuous replication, AWS managed (cross-AZ), encrypted, retention per data classification policy

**Recovery:**
- RPO: 5 minutes (agent memory)
- RTO: 30 minutes (full service restoration)
- Recovery Procedures: TBD
- Disaster Recovery Plan: Multi-region failover (us-east-1 → us-west-2)
- Failover Capability: Manual
- Last DR Test: Not yet completed

### 7.4 Maintenance & Support

**Maintenance:**
- Infrastructure: AWS managed (patching and updates)
- Application: BNZ responsibility (agent code and configurations)

**Support Model:** Hybrid (AWS + BNZ)

| Tier | Team | Response Time | Coverage |
|------|------|---------------|----------|
| L1 | BNZ Service Desk | 15 minutes | 24x7 |
| L2 | BNZ AI Platform Team | 1 hour | Business hours |
| L3 | AWS Premium Support | 4 hours (critical) | 24x7 |

**AWS Support:** Enterprise level, Technical Account Manager contact

## 8. Dependencies

### 8.1 Technology Dependencies

**AWS Services:**

| Service | Purpose | Criticality |
|---------|---------|-------------|
| Amazon Bedrock | Foundation model access (Claude, Titan models) | Critical |
| AWS Lambda | Serverless compute for custom integrations | High |
| Amazon CloudWatch | Monitoring and logging | High |
| AWS IAM | Authentication and authorization | Critical |
| AWS Secrets Manager | Secrets and credentials management | High |

**External Dependencies:**
- Foundation Models (Anthropic Claude, OpenAI GPT-4) - Critical
  - Fallback: Multi-model support for redundancy

### 8.2 Infrastructure Dependencies

**Compute:** AWS Serverless (Firecracker microVMs) with automatic scaling

**Network:**
- VPC: BNZ AI Platform VPC
- Subnets: Private subnets with NAT Gateway for outbound
- Security Groups: Agent-SG, Gateway-SG

**Storage:**
- Object Storage: S3 for artifacts and logs
- Database: Managed by AgentCore Memory service

## 9. Cost Information

### 9.1 Acquisition Costs

Not yet determined. Will include:

- Any upfront Costs
- Implementation Costs
  - Consulting Services
  - Training
  - etc.
  
### 9.2 Operational Costs

Operational costs are based on estimated usage patterns for a medium-sized deployment. Use cases have not yet been 
identified, so rough estimates in the table below are needed.

**Monthly Estimates:**

| Cost Category | Monthly Cost                          |
|---------------|---------------------------------------|
| Runtime | TBD (100K invocations/month)          |
| Memory | TBD (1M memories stored)             |
| Gateway | TBD (50K tool invocations)           |
| Identity | TBD (token requests)                 |
| Observability | TBD (CloudWatch metrics and logs)    |
| Foundation Models | TBD (token consumption - variable) |
| **Total Monthly** | **TBD**                            |

**Annual Estimate:** TBD base + variable model costs

**Cost Optimization Strategies:**
- Caching frequently used responses
- Memory pruning and archival
- Right-sizing session durations
- Reserved capacity for predictable workloads (when available in GA)

### 9.3 TCO Analysis

TCO analysis will be completed post-implementation when actual usage data is available.

- TCO Period: 3 years
- Year 1: TBC (implementation + operational)
- Year 2-3: TBC / year
- **Total 3-Year TCO: TBC**
- Cost per Conversation: TBC (estimated)
- Cost per Agent Hour: TBC

## 10. Capacity & Scalability

### 10.1 Current Capacity
- Concurrent Agents: TBC
- Peak Concurrent: TBC
- Conversations per Day: TBC
- Average Session Duration: TBC minutes

**Deployment Sizing:**
- **Small:** 100 concurrent agents, 5K conversations/day
- **Medium:** 1,000 concurrent agents, 50K conversations/day
- **Large:** 10,000+ concurrent agents, 500K+ conversations/day

### 10.2 Scalability Plan

**Scaling Approach:**
- Serverless Scaling: Enabled
- Scaling Trigger: Automatic based on invocations
- Scale Out Time: < 1 second

**Capacity Forecasting:**
- **Year 2026:** TBC conversations/day, TBC concurrent agents, estimated cost TBC / month

## 11. Testing & Quality Assurance

### 11.1 Testing Strategy

The testing strategy for the AWS AgentCore implementation includes:

**Unit Testing:**
- Coverage Target: 80%
- Coverage Actual: TBC
- Framework: pytest / TBC

**Integration Testing:**
- Coverage: 65%
- Framework: pytest + moto (AWS mocking) / TPC
- Environment: Dedicated AWS test account

**Performance Testing:**
- Tool: Locust / TPC
- Last Test Date: 2025-10-15
- Test Scenario: Sustained load with 5,000 concurrent users for 1 hour
- Result: TBC

## 12. Diagrams & Visual Models

### 12.1 Physical Deployment Diagram
- **Diagram Type:** Physical Deployment Diagram
- **Diagram Format:** UML Deployment / AWS Architecture
- **Diagram File:** SBB-APP-001-Deployment-v1.0.0.drawio
- **Description:** Shows actual AWS AgentCore deployment architecture

**Deployment Elements:**

**Primary Region: ap-southeast-2 (Sydney)**
- Availability Zones: ap-southeast-2a, ap-southeast-2b, ap-southeast-2c
- Components: AgentCore Runtime (Serverless), AgentCore Memory (Managed), AgentCore Gateway (Managed), AgentCore Identity (Managed), AgentCore Observability (Managed), CloudWatch Logs & Metrics, S3 (Artifacts)

**DR Region: us-west-2 (Oregon)**
- Availability Zones: us-west-2a, us-west-2b
- Components: AgentCore Runtime (Standby), CloudWatch Logs (Replicated)

### 12.2 Component Implementation Diagram
- **Diagram Type:** Component Implementation Diagram
- **Diagram Format:** C4 Container
- **Diagram File:** SBB-APP-001-Components-v1.0.0.drawio
- **Description:** Shows AgentCore components and technology stack

**Key Containers:**
- **Agent Application:** Python 3.11 + LangGraph, deployed to AgentCore Runtime (Serverless)
- **AgentCore Runtime:** AWS Managed (Firecracker microVMs) - Agent execution, Session isolation, Scaling
- **AgentCore Memory:** AWS Managed Service - Short-term memory, Long-term memory, Retrieval
- **AgentCore Gateway:** AWS Managed (MCP implementation) - Tool transformation, API integration, OAuth handling

#### Component Inventory

**Table 12.2.1: Component Definitions**

| Component ID | Component Name | Layer | Technology Stack | Description |
|--------------|----------------|-------|------------------|-------------|
| CM-001 | Agent Implementation | Agent Application (Customer Code) | Python 3.11+, LangGraph 0.2.40+, LangChain (optional), CrewAI (optional) | Custom agent code implementing multi-agent orchestration, reasoning logic, and tool integration |
| CM-002 | Agent Configuration | Agent Application (Customer Code) | YAML/JSON config files | Configuration for model selection (Bedrock), memory settings, tool bindings, security policies, and observability settings |
| CM-003 | Custom Tools | Agent Application (Customer Code) | Python/TypeScript, MCP-compliant | Business logic tools, API wrappers, data access tools, integration adapters implementing MCP protocol |
| CM-004 | Deployment Package | Agent Application (Customer Code) | Docker, AWS CDK/Terraform, AWS CodePipeline | Container image and Infrastructure as Code (IaC) for CI/CD deployment automation |
| CM-005 | AgentCore Runtime | AgentCore Managed Components | Firecracker microVMs | Serverless agent execution environment providing isolated execution, fast startup (125ms), resource controls, and multi-tenancy safety |
| CM-006 | AgentCore Memory | AgentCore Managed Components | In-memory (short-term), DynamoDB (long-term) | Dual architecture memory system for conversation history, state persistence, and vector search (KNN) |
| CM-007 | AgentCore Gateway | AgentCore Managed Components | MCP server + client | Tool orchestration layer providing MCP protocol support, tool discovery, request routing, and result aggregation |
| CM-008 | AgentCore Identity | AgentCore Managed Components | AWS IAM, OAuth 2.0, SAML 2.0 | Authentication and authorization service with enterprise IdP integration, RBAC policies, and session management |
| CM-009 | Browser Tool | AgentCore Managed Components | Headless Chromium, sandboxed execution | Web automation tool for page rendering, JavaScript execution, and screenshot capture |
| CM-010 | Code Interpreter | AgentCore Managed Components | Python sandbox (NumPy, Pandas) | Sandboxed code execution environment for dynamic scripting, data analysis, and file processing |
| CM-011 | AgentCore Observability | AgentCore Managed Components | OpenTelemetry, CloudWatch Logs, CloudWatch Metrics, X-Ray | Monitoring and tracing service providing distributed tracing, performance metrics, log aggregation, and custom dashboards |
| CM-012 | AgentCore Control Plane | AgentCore Managed Components | AWS managed service | Platform management service for lifecycle management, resource provisioning, configuration updates, health monitoring, and auto-scaling |
| CM-013 | Amazon Bedrock | External Services & Integrations | AWS Bedrock API | Foundation model service providing access to Claude, GPT-4, and other LLMs |
| CM-014 | Enterprise IdP | External Services & Integrations | Microsoft Entra ID, Okta | Enterprise identity provider for SSO and user authentication |
| CM-015 | External APIs | External Services & Integrations | REST/SOAP APIs | Third-party business systems including Salesforce CRM and ServiceNow ITSM |
| CM-016 | Data Sources | External Services & Integrations | Amazon S3, RDS, DynamoDB | Data storage and retrieval services for agent knowledge and state |
| CM-017 | Monitoring Stack | External Services & Integrations | CloudWatch, X-Ray | AWS observability infrastructure for centralized logging and tracing |

**Table 12.2.2: Component Relationships**

| Link ID | Source Component | Target Component | Link Type | Protocol/Technology | Description |
|---------|-----------------|------------------|-----------|---------------------|-------------|
| LK-001 | Agent Implementation (CM-001) | AgentCore Runtime (CM-005) | Deployment | Python SDK, Docker | Customer agent code is deployed to and executed within the AgentCore Runtime environment |
| LK-002 | AgentCore Runtime (CM-005) | AgentCore Memory (CM-006) | Component Dependency | AWS SDK (internal) | Runtime accesses Memory service for conversation history and state retrieval |
| LK-003 | AgentCore Runtime (CM-005) | AgentCore Gateway (CM-007) | Component Dependency | MCP protocol | Runtime invokes Gateway to execute tool calls and integrate with external systems |
| LK-004 | AgentCore Runtime (CM-005) | AgentCore Identity (CM-008) | Component Dependency | AWS IAM, OAuth 2.0 | Runtime validates authentication tokens and enforces authorization policies |
| LK-005 | AgentCore Runtime (CM-005) | AgentCore Observability (CM-011) | Telemetry Flow | OpenTelemetry | Runtime emits traces, metrics, and logs to Observability service for monitoring |
| LK-006 | AgentCore Gateway (CM-007) | Browser Tool (CM-009) | Component Dependency | MCP protocol | Gateway routes web automation requests to Browser Tool |
| LK-007 | AgentCore Gateway (CM-007) | Code Interpreter (CM-010) | Component Dependency | MCP protocol | Gateway routes code execution requests to Code Interpreter |
| LK-008 | AgentCore Gateway (CM-007) | External APIs (CM-015) | Integration | REST/SOAP, HTTPS | Gateway orchestrates calls to third-party APIs (Salesforce, ServiceNow) |
| LK-009 | AgentCore Runtime (CM-005) | Amazon Bedrock (CM-013) | Integration | AWS Bedrock API | Runtime invokes foundation models for language understanding and generation |
| LK-010 | AgentCore Identity (CM-008) | Enterprise IdP (CM-014) | Integration | SAML 2.0, OAuth 2.0 | Identity service federates authentication to enterprise SSO providers |
| LK-011 | AgentCore Memory (CM-006) | Data Sources (CM-016) | Data Access | AWS SDK | Memory service persists long-term data to DynamoDB and S3 |
| LK-012 | AgentCore Observability (CM-011) | Monitoring Stack (CM-017) | Telemetry Flow | OpenTelemetry, CloudWatch API | Observability service forwards telemetry to CloudWatch and X-Ray |
| LK-013 | Custom Tools (CM-003) | AgentCore Gateway (CM-007) | Registration | MCP protocol | Custom tools register with Gateway using MCP protocol for discovery and invocation |
| LK-014 | AgentCore Control Plane (CM-012) | AgentCore Runtime (CM-005) | Management | AWS Control API | Control Plane manages Runtime lifecycle, provisioning, and scaling |
| LK-015 | Agent Configuration (CM-002) | AgentCore Runtime (CM-005) | Configuration | YAML/JSON, AWS SDK | Configuration files define agent behavior and are loaded by Runtime at initialization |

### 12.3 Data Flow Implementation Diagram
- **Diagram Type:** Sequence Diagram
- **Diagram File:** SBB-APP-001-DataFlow-v1.0.0.drawio
- **Description:** Shows actual data flow for agent invocation

**Sequence Flow:**

| Step | From | To | Action | Protocol |
|------|------|----|---------|---------|
| 1 | User Application | API Gateway | POST /invoke with user query | HTTPS |
| 2 | API Gateway | AgentCore Runtime | Invoke agent with session context | AWS SDK |
| 3 | AgentCore Runtime | AgentCore Memory | Retrieve relevant memories | HTTPS REST |
| 4 | AgentCore Runtime | Amazon Bedrock | Invoke Claude 3.5 Sonnet with context | HTTPS REST |
| 5 | AgentCore Runtime | AgentCore Gateway | Invoke tools via MCP | MCP over HTTPS |
| 6 | AgentCore Gateway | External API | Execute tool action | HTTPS REST |
| 7 | AgentCore Runtime | AgentCore Memory | Store conversation and learnings | HTTPS REST |
| 8 | AgentCore Runtime | User Application | Return agent response | HTTPS (via API Gateway) |

## 13. Migration & Transition

### 13.1 Migration Strategy
This is a **greenfield implementation** with phased rollout:

| Phase | Duration | Scope | Users |
|-------|----------|-------|-------|
| Pilot (Phase 1) | 3 months | Single use case (IT Helpdesk agent) | 100 |
| Expansion (Phase 2) | 6 months | Additional 3 use cases | 1,000 |
| Enterprise (Phase 3) | Ongoing | Platform for all agentic AI use cases | All employees + customers |

## 14. Vendor Management

### 14.1 Vendor Information
- **Vendor Name:** Amazon Web Services, Inc.
- **Vendor Type:** Cloud Provider
- **Account ID:** 123456789012
- **Organization ID:** o-xxxxxxxxxx
- **Account Manager:** AWS Enterprise Account Team
- **Technical Account Manager:** AWS TAM

**Support Details:**
- Support Tier: Enterprise
- Support Hours: 24x7
- Support Portal: https://console.aws.amazon.com/support/
- Support Email: aws-support@amazon.com

## 15. Known Issues & Limitations

### 15.1 Known Issues

| Issue ID | Severity | Description | Impact | Workaround | Resolution ETA |
|----------|----------|-------------|--------|------------|----------------|
| ISSUE-001 | Low | Preview service - GA date not announced | Potential API changes before GA | Monitor AWS announcements, use IaC for easy updates | Q1 2026 (expected GA) |

### 15.2 Limitations

**Functional Limitations:**
- **No built-in low-code visual authoring**
  - Impact: Requires developers with Python/TypeScript skills
  - Mitigation: Developer training, reusable templates

**Regional Limitations:**
- **Limited region availability (3 regions in preview)**
  - Impact: Data residency considerations for some regions
  - Mitigation: Multi-region strategy, await GA for expanded regions

## 16. Lessons Learned

### 16.1 Implementation Lessons

This section will be completed post-implementation.

- What Went Well
- What Could Improve
- Recommendations

## 17. Related Documents
- ABB-APP-001: Agentic AI Agent (Architecture Building Block)
- SBB-APP-002: Microsoft Copilot Studio Agent (Alternative Implementation)
- Architecture Decision Record: ADR-2025-042 (Agent Platform Selection)
