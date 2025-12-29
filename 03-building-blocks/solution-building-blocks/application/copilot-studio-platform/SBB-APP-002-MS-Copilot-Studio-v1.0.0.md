# Copilot Studio Agent Deployment - Solution Building Block (SBB)

## Document Control
- **Document Type:** Solution Building Block
- **Version:** 1.0.0
- **Status:** Draft
- **Created Date:** 2025-11-28
- **Last Modified:** 2025-11-28
- **Owner:** BNZ AI Platform Team
- **Architecture Domain:** Application
- **Implementation Phase:** Production

## 1. Solution Building Block Identification

### 1.1 Basic Information
- **SBB ID:** SBB-APP-002
- **SBB Name:** Copilot Studio Agent Deployment
- **Short Name:** Copilot Studio Agents
- **Version:** 1.0.0
- **Classification:** PaaS / Low-Code Platform

### 1.2 Description
**Solution Overview:** Microsoft Copilot Studio is a low-code graphical platform for building conversational AI agents. Built on the Power Platform, it provides visual authoring tools, integration with Azure OpenAI GPT models, 1000+ connectors, and deep integration with Microsoft 365 ecosystem. Agents can be deployed across web, Microsoft Teams, mobile apps, and M365 Copilot.

**Procurement Type:** Cloud Service (PaaS) - SaaS Platform

**Vendor/Provider:** Microsoft Corporation

**Business Justification:** Microsoft Copilot Studio selected for low-code / no-code agent development, enabling business users to create agents without extensive programming. Deep Microsoft 365 integration provides native access to organizational data and existing IT investments. Strong governance via Power Platform and enterprise-grade compliance.

## 2. ABB Realization

### 2.1 Realized ABBs
This SBB realizes **ABB-APP-001: Agent Deployment** with high alignment using a full implementation approach.

**Known Gaps:**

**GAP-001: Limited Framework Flexibility (Low-code Canvas vs Code-first)**

Microsoft Copilot Studio's low-code visual authoring approach provides significant benefits for rapid development and business user accessibility, but differs fundamentally from code-first frameworks like Strands, LangGraph, LangChain, or CrewAI. This architectural decision creates a gap in ABB realization, primarily affecting developers who prefer traditional software development workflows.

The platform's visual canvas-based design is optimized for declarative agent construction rather than imperative programming. While this enables business analysts and citizen developers to build sophisticated conversational agents without writing Python or TypeScript code, it constrains developers accustomed to full programmatic control over agent behavior, execution flow, and state management.

**Severity:** Low - This gap does not impact functional capabilities or production deployment requirements. The platform provides multiple extensibility mechanisms that enable developers to implement complex logic when needed.

**Mitigation Strategies:**

1. **Power Fx for Custom Logic:** Power Fx, Microsoft's low-code formula language (based on Excel formulas), provides programmatic extensibility within the visual canvas. Developers can use Power Fx expressions to:
   - Implement conditional logic and branching within conversation flows
   - Transform and validate data between agent steps
   - Calculate dynamic values and manipulate variables
   - Create reusable custom functions for complex operations
   - Example: `If(varScore > 80, "High Priority", varScore > 50, "Medium Priority", "Low Priority")`

2. **Agent Flows for Advanced Orchestration:** Agent flows (the recommended successor to Power Automate flows) provide visual workflow orchestration with programmatic capabilities:
   - Access to 1000+ Power Platform connectors for external system integration
   - Built-in error handling, retry logic, and exception management
   - Conditional branching and parallel execution paths
   - Variable scoping and data transformation between steps
   - Integration with custom APIs via HTTP actions

3. **Azure Functions for Complex Business Logic:** For scenarios requiring full programming capabilities, developers can integrate Azure Functions (C#, Python, JavaScript, TypeScript):
   - Implement complex algorithms and business rules not feasible in Power Fx
   - Access external libraries and frameworks (e.g., NumPy, pandas, ML models)
   - Handle compute-intensive operations outside the agent runtime
   - Integrate via custom connectors with OpenAPI specifications
   - Example: Custom sentiment analysis, document processing, or regulatory calculations

4. **Custom Connectors via OpenAPI:** Developers can wrap existing REST APIs as Power Platform connectors:
   - Define OpenAPI/Swagger specifications for custom services
   - Implement OAuth 2.0, API key, or certificate-based authentication
   - Expose custom business logic as reusable connector actions
   - Version control connector definitions alongside agent solutions

**Workaround for Development Teams:**

Agent flows provide a middle ground between visual low-code and full programming. They offer programmatic extensibility through:
- **Compose actions** for data transformation using JSON expressions
- **HTTP actions** for calling any REST API
- **JavaScript / TypeScript execution** via custom code components (preview)
- **Dataverse integration** for persistent state management and custom business logic

This hybrid approach allows business users to design conversation flows visually while developers implement complex logic in familiar programming languages, integrated seamlessly through well-defined interfaces.

**Impact on ABB Realization:** The gap primarily affects developer experience and workflow preferences rather than functional capability. All ABB requirements (FN-001 through FN-008) can be fully implemented using the combination of visual authoring, Power Fx, agent flows, and custom connectors. The 5% gap reflects the difference in development methodology rather than missing functionality.

### 2.2 ABB Requirements Mapping
| ABB Requirement ID | Requirement Description | Copilot Studio Feature/Component | Compliance Status | Notes |
|--------------------|------------------------|----------------------------------|-------------------|-------|
| FN-001 | Natural Language Understanding & Generation | Azure OpenAI GPT-5 Auto/Reasoning | Full | Built-in GPT integration |
| FN-002 | Reasoning & Decision Making | Generative AI Orchestration + Topics | Full | Hybrid classical/AI approach |
| FN-003 | Memory Management | Conversation Context (session-based) | Partial | No long-term memory by default |
| FN-004 | Tool Orchestration & Integration | Actions Layer (Agent Flows + 1000+ Connectors) | Full | Extensive connector ecosystem |
| FN-005 | Knowledge Retrieval | Knowledge Management (SharePoint, Dataverse, OneDrive) | Full | Native M365 integration |
| FN-006 | Identity & Authorization | Azure AD / Entra ID (with certificate support) | Full | Enterprise SSO |
| FN-007 | Multi-turn Conversation Management | Topic-based Dialog System | Full | Visual conversation designer |
| FN-008 | Error Handling & Recovery | Built-in error handling nodes + fallback topics | Full | Low-code error handling |

## 3. Product / Solution Specifications

### 3.1 Product Information
- **Product Name:** Microsoft Copilot Studio
- **Product Family:** Microsoft Power Platform
- **Version:** GA (Generally Available as of Nov 2025)
- **Release Date:** Evolved from Power Virtual Agents (2023 rebrand)
- **Vendor:** Microsoft Corporation
- **Website:** https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
- **Support Contact:** Microsoft Premier Support
- **Account Manager:** BNZ Microsoft Account Team
- **License Model:** Dual licensing (Tenant + Per-User) + Copilot Credits consumption
- **License Type:** Commercial SaaS + Consumption
- **Number of Licenses:** Tenant license + per-maker user licenses
- **License Cost:** See pricing section
- **Renewal Date:** Annual renewal
- **Restrictions:** Guest users cannot access; makers need Copilot Studio User License

### 3.2 Technical Specifications

**Authoring Environment:**
- Type: Visual Low-Code
- Interface: Web-based authoring canvas
- Languages Supported: English, Spanish, French, German, Portuguese, Chinese, Japanese, 40+ languages
- Development Tools: Topic designer, Entity editor, Variable management, Test chat

**AI Capabilities:**
- Foundation Models: Azure OpenAI GPT-5 Auto, Azure OpenAI GPT-5 Reasoning
- NLU Engine: Custom NLU built on Azure OpenAI
- Generative Answers: RAG-based knowledge synthesis
- Content Moderation: Azure AI Content Safety
- Prompt Engineering: Built-in prompt optimization

**Knowledge Management:**
- Supported Types: Microsoft SharePoint (sites and pages), Microsoft OneDrive (files), Dataverse (tables and records), Public websites (crawled), Uploaded files (PDF, DOCX)
- Knowledge Features:
  - Automatic chunking and embedding
  - Sensitivity label respect (Microsoft Purview)
  - Permission inheritance from source
  - Individual reference label visibility
  - Security trimming based on user access

**Integration Capabilities:**
- Connectors: 1000+ Power Platform connectors
- Recommended Pattern: Agent flows (replacing Power Automate flows)
- Connector Types: Standard (included), Premium (additional license required)
- MCP Support: Model Context Protocol (preview)
- Computer Use: RPA-style agent actions (preview)
- Code Interpreter: Python-powered code execution
- Custom APIs: Custom connectors via OpenAPI

**Power Platform Foundation:**
- Runtime: Power Platform managed service
- Storage: Dataverse (Dynamics 365 database)
- Environments: Dev/Test/Prod isolation
- ALM: Solutions for application lifecycle management
- Governance: Power Platform Admin Center

**Cloud Specifications:**
- Provider: Microsoft Azure
- Supported Regions: North America (United States, Canada), Europe (UK, France, Germany, Switzerland, Norway), Asia Pacific (Australia, Japan, India, Singapore), Government (US GCC, GCC High)
- EU Data Boundary: Full EUDB compliance for EU tenants
- Deployment Options: Public cloud, Government cloud

### 3.3 Deployment Architecture
- **Deployment Model:** Cloud (Multi-Tenant SaaS)
- **Deployment Pattern:** Managed Platform as a Service

**Architecture Layers:**
1. **Presentation Layer:** Web chat widget, Microsoft Teams bot, Mobile apps, M365 Copilot extensions, Custom channels (via Direct Line API)
2. **Copilot Studio Service:** Authoring canvas (agent design), Generative AI orchestration, Topic engine (dialog management), Entity recognition, Analytics and monitoring
3. **Power Platform Foundation:** Dataverse (storage), Connectors (1000+ integrations), Power Automate (workflows), Environment management, Security and governance
4. **Azure Infrastructure:** Azure OpenAI Service (GPT models), Azure AI Search (knowledge indexing), Azure Bot Service (channel integration), Azure Storage (content), Azure Active Directory (identity)

**Infrastructure as Code:**
- Tool: Power Platform CLI + PowerShell
- Repository: TBD
- Version: 1.0.0
- Deployment Method: Solutions (XML-based packages)

## 4. Implemented Functionality

### 4.1 Features & Capabilities

**Core Features:**

| Feature ID | Feature Name | Description | ABB Mapping | Status | Configuration Required |
|------------|--------------|-------------|-------------|--------|------------------------|
| FE-001 | Visual Authoring Canvas | Low-code graphical interface for designing conversational agents | FN-007 | Enabled | No |
| FE-002 | Generative AI Orchestration | Azure OpenAI GPT-5 integration with automatic prompt optimization | FN-001, FN-002 | Enabled | Yes |
| FE-003 | Knowledge Management | Native integration with SharePoint, OneDrive, Dataverse for RAG | FN-005 | Enabled | Yes |
| FE-004 | Actions & Connectors | 1000+ pre-built connectors + agent flows + MCP support | FN-004 | Enabled | Yes |
| FE-005 | Multi-Channel Deployment | Deploy to web, Teams, mobile, M365 Copilot, custom channels | FN-007 | Enabled | Yes |
| FE-006 | Enterprise Identity | Azure AD / Entra ID authentication with certificate support | FN-006 | Enabled | Yes |

**Optional Features:**
- **FE-OPT-001: Multi-Agent Orchestration** - Coordinate multiple specialized agents for complex scenarios (Enabled)
- **FE-OPT-002: Code Interpreter (Preview)** - Python-powered code execution within agent (Enabled)
- **FE-OPT-003: Computer Use (Preview)** - RPA-style agent actions for UI automation (Not enabled - Preview feature not yet approved for production use)

**Custom Extensions:**
- **EXT-001: BNZ Custom Connectors**
  - Description: Custom connectors for BNZ internal systems (Salesforce, ServiceNow)
  - Developer: BNZ Power Platform CoE
  - Maintenance: BNZ Power Platform CoE
  - Repository: TBD

### 4.2 Performance Characteristics

The following have yet to be determined / specified:

- Measured Metrics
- Benchmarks
- SLA Compliance

## 5. Integration & Interfaces

### 5.1 Implemented Interfaces

**Provided Interfaces:**

| Interface ID | Interface Name | Type | Endpoint                                                                               | Authentication | Rate Limits |
|--------------|----------------|------|----------------------------------------------------------------------------------------|----------------|-------------|
| IF-001 | Web Chat Widget | JavaScript Embed | TBD e.g. https://copilotstudio.microsoft.com/environments/{envId}/bots/{botId}/webchat | Optional (Azure AD or anonymous) | Platform-managed, based on license capacity |
| IF-002 | Microsoft Teams Channel | Bot Framework | Managed by Copilot Studio                                                              | Azure AD (SSO) | Platform-managed |
| IF-003 | Direct Line API (Custom Channels) | HTTPS REST | https://directline.botframework.com/v3/directline                                      | Direct Line Secret or Token | Platform-managed |
| IF-004 | M365 Copilot Extension | M365 Plugin | Managed by Microsoft 365                                                               | Azure AD (M365 context) | Platform-managed |

**Interface Details:**
- **IF-001:** JavaScript SDK, Documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
- **IF-002:** Operations: Send message, Receive message, Adaptive cards, File upload
- **IF-003:** Supported channels: Custom web apps, Mobile apps, IoT devices

**Required Interfaces:**

| Interface ID | Interface Name | Type | Provider | Models/Protocols |
|--------------|----------------|------|----------|------------------|
| IF-REQ-001 | Azure OpenAI Service | HTTPS REST | Azure OpenAI Service | gpt-5-auto, gpt-5-reasoning (Azure AD Managed Identity) |
| IF-REQ-002 | Microsoft Graph API | HTTPS REST | Microsoft Graph | OAuth 2.0 (Files.Read.All, Sites.Read.All, User.Read) |
| IF-REQ-003 | Dataverse API | HTTPS REST / OData | Microsoft Dataverse | Azure AD authentication |

### 5.2 Integration Patterns Implemented

**Agent Flows (Recommended):**
- Protocol: Power Platform Connectors
- Implementation: Visual workflow orchestration with 1000+ connectors
- Error Handling: Built-in retry logic and error handling nodes (max 3 retries, exponential backoff)

**Power Automate Flows (Legacy):**
- Protocol: Power Platform Connectors
- Implementation: Traditional Power Automate flows called from agent
- Message Format: JSON

**MCP Tool Integration (Preview):**
- Protocol: Model Context Protocol
- Implementation: MCP servers registered as tools for agent use
- Message Format: JSON-RPC 2.0

**Custom Connectors:**
- Protocol: OpenAPI / REST
- Implementation: Custom APIs wrapped as Power Platform connectors
- Authentication: OAuth 2.0, API Key, Basic Auth

### 5.3 Data Integration

**Data Sources:**

| Source ID | Source Name | Integration Method | Connector | Frequency | Data Volume |
|-----------|-------------|-------------------|-----------|-----------|-------------|
| DS-001 | BNZ SharePoint Intranet | Native Knowledge Source | SharePoint connector (built-in) | Real-time knowledge retrieval | 5000+ pages, ~25GB |
| DS-002 | HR System (Workday) | Custom Connector | Workday REST API custom connector | On-demand via agent flows | Variable per request |
| DS-003 | ServiceNow (IT Service Management) | Premium Connector | ServiceNow connector (premium) | Real-time ticket creation/retrieval | Variable per request |

**Data Targets:**

| Target ID | Target Name | Integration Method | Frequency | Data Entities |
|-----------|-------------|-------------------|-----------|---------------|
| DT-001 | Dataverse (Conversation History) | Native | Real-time | Conversations, Messages, User feedback (90 days retention) |
| DT-002 | Application Insights (Telemetry) | Native Integration | Real-time streaming | Performance metrics, Errors, Usage analytics |

## 6. Security Implementation

### 6.1 Security Controls

**Authentication:**
- Methods: Azure AD / Entra ID, Azure AD with Certificate, OAuth 2.0, Manual (username only), No authentication
- Primary Method: Azure AD / Entra ID
- Identity Providers: Microsoft Entra ID
- MFA: Enabled (TOTP, Authenticator App, SMS, FIDO2)
- Certificate Support: Yes

**Authorization:**
- Model: RBAC via Power Platform Security Roles
- Fine-grained Access: Environment roles, Agent permissions, Dataverse row-level security
- Enforcement Point: Power Platform
- Security Roles: System Administrator, Environment Maker, Bot Maker, Bot User

**Data Protection:**
- Encryption at Rest: AES-256 with Microsoft-managed keys (default) or Customer-managed keys (Azure Key Vault)
- Encryption in Transit: TLS 1.2+ with Microsoft Azure certificate authority
- Data Isolation: Multi-tenant with logical isolation, Separate environments (Dev/Test/Prod)

**Security Monitoring:**
- Audit & Security Logging: Enabled
- Log Aggregation: Power Platform Admin Center + Microsoft Purview
- Retention Period: 90 days (default, configurable)
- SIEM Integration: Microsoft Sentinel (forwards Authentication, Authorization, Connector calls, DLP violations)

**Vulnerability Management:**
- Infrastructure: Microsoft responsibility for platform patching
- Application: Automatic security scan on agent publish

**Compliance:**
- Frameworks: SOC 1, SOC 2, SOC 3, ISO 27001, GDPR, CCPA, HIPAA (with BAA)
- Microsoft Compliance Reports: Available via Service Trust Portal

### 6.2 Security Architecture

**Network Security:**
- Deployment Options: Public endpoints (Azure-managed), IP firewall rules (environment-level), Virtual network service endpoints (Azure)
- Network Isolation: Tenant boundary isolation

**Application Security:**
- Input Validation: Built-in content moderation (Azure AI Content Safety)
- Prompt Injection Protection: GPT model safety features + custom validation
- Secrets Management: Secure environment variables (encrypted)
- DLP Policies: Data Loss Prevention policies at tenant and environment level

**Data Governance:**
- Sensitivity Labels: Microsoft Purview sensitivity labels respected
- Data Loss Prevention: Granular DLP policies (connector restrictions, endpoint filtering)
- Customer Lockbox: Available for production tenants

## 7. Operational Characteristics

### 7.1 Deployment & Configuration

**CI/CD Pipeline:**
- Tool: Azure DevOps Pipelines
- Pipeline URL: https://dev.azure.com/bnz/copilot-studio
- Build Frequency: On solution export
- Deployment Frequency: Bi-weekly (every other Tuesday)

**Deployment Automation:**
- Automation Level: Semi-Automated
- Deployment Tool: Power Platform Pipelines + Power Platform CLI
- Rollback Capability: Yes (< 15 minutes with previous solution version import)

**Configuration Management:**
- Config Location: Environment variables in solution
- Config Format: Key-value pairs
- Environment Configs: Dev, Test, Prod
- Secrets Management: Secure environment variables (encrypted in Dataverse)
- Config Validation: Manual validation in test environment

### 7.2 Monitoring & Observability

**Observability Platform:** Power Platform Admin Center + Application Insights

**Metrics:**
- Collection Interval: Real-time
- Retention Period: 90 days (Admin Center), 90 days (App Insights)
- Key Metrics:
  - Agent Response Latency (Warning: 2000ms, Critical: 5000ms)
  - Session Abandonment Rate (Warning: 20%, Critical: 40%)
  - CSAT Score (Warning: <3.5/5, Critical: <3.0/5)
  - Copilot Credits Consumption (Warning: 80% of monthly budget, Critical: 95% of monthly budget)

**Logging:**
- Log Aggregation: Application Insights
- Log Level: Information (Production), Verbose (Dev)
- Log Retention: 90 days
- Structured Logging: Yes (JSON format)

**Analytics:**
- Built-in Analytics: Copilot Studio Analytics Dashboard
- Custom Dashboards: Power BI reports from Dataverse
- Metrics Tracked:
  - Engagement: Sessions, messages, users
  - Topic performance: Trigger rates, completion rates
  - Abandonment analysis: Drop-off points
  - CSAT: Optional customer satisfaction surveys

**Alerting:**
- Alerting Tool: Azure Monitor Alerts
- Alert Channels: Email, Teams, PagerDuty
- Escalation Policy: L1 Service Desk → L2 Power Platform CoE → L3 Microsoft Support
- On-Call Rotation: Weekly rotation (Power Platform CoE)

**Dashboards:**
- **Copilot Studio Operations Dashboard** (Power Platform Admin Center)
  - URL: https://admin.powerplatform.microsoft.com/
  - Metrics: Agent usage, Capacity consumption, DLP violations, Environment health
- **Agent Performance Dashboard** (Copilot Studio Analytics)
  - Metrics: Sessions, CSAT, Topic performance, Abandonment

### 7.3 Backup & Recovery

**Backup:**
- Agent Configurations: Solution exports to Azure DevOps Git repository (on every deployment)
- Conversation Data: Dataverse backup (Microsoft-managed), Azure region-specific, encrypted, 28 days retention

**Recovery:**
- RPO: 24 hours (Dataverse backup)
- RTO: 2 hours (solution re-import + environment restore)
- Recovery Procedures: https://docs.bnz.co.nz/copilot-studio-dr
- Disaster Recovery Plan: Multi-region environment (AU → US failover)
- Failover Capability: Manual
- Last DR Test: 2025-09-25 (Success)

### 7.4 Maintenance & Support

**Maintenance:**
- Infrastructure: Platform updates and infrastructure maintenance by Microsoft
- Application: BNZ responsibility for agent content and configurations

**Support Model:** Hybrid (Microsoft + BNZ)

| Tier | Team | Response Time | Coverage |
|------|------|---------------|----------|
| L1 | BNZ Service Desk | 15 minutes | 24x7 |
| L2 | BNZ Power Platform CoE | 1 hour | Business hours (extended to 18:00 NZST) |
| L3 | Microsoft Premier Support | 4 hours (Severity A) | 24x7 |

**Microsoft Support:** Premier level, Contact: Microsoft Customer Success Account Manager (CSAM)

## 8. Dependencies

### 8.1 Technology Dependencies

**Microsoft Services:**

| Service | Purpose | Criticality |
|---------|---------|-------------|
| Azure OpenAI Service | Foundation model access (GPT-5 models) | Critical |
| Microsoft Dataverse | Agent configuration and conversation storage | Critical |
| Microsoft Graph | Access to SharePoint, OneDrive, M365 data | High |
| Azure Bot Service | Multi-channel messaging infrastructure | High |
| Azure Active Directory | Authentication and authorization | Critical |
| Azure AI Search | Knowledge indexing and retrieval | High |

**External Dependencies:**
- ServiceNow (Premium Connector) - Medium criticality, Fallback: Manual ticket creation
- Workday (Custom Connector) - Medium criticality, Fallback: Direct HR portal access

### 8.2 Infrastructure Dependencies

**Compute:** Microsoft-managed (Azure App Service) with automatic scaling (PaaS)

**Network:**
- Connectivity: Azure backbone network
- DNS: Azure DNS

**Storage:**
- Object Storage: Azure Blob Storage (for attachments)
- Database: Dataverse (Azure SQL Database)

## 9. Cost Information

### 9.1 Acquisition Costs
- No Upfront Costs: Yes
- Licensing Costs:
  - Tenant License: $200/month
  - User Licenses: $20/user/month × 10 makers = $200/month
  - **Total Licensing: $400/month base**
- Implementation Cost:
  - Consulting Services: $80,000 (Power Platform partner services)
  - Training: $25,000 (Maker training + governance setup)
  - Environment Setup: $10,000 (environment provisioning, DLP policies)
  - **Total Implementation: $115,000**

### 9.2 Operational Costs

**Monthly Estimates:**

| Cost Category | Monthly Cost |
|---------------|-------------|
| Licensing Base | $400 (tenant + 10 user licenses) |
| Copilot Credits | $3,000 (estimated for 20K sessions/month) |
| Premium Connectors | $500 (ServiceNow, Salesforce) |
| Dataverse Storage | $200 (50GB conversation history + agent data) |
| Application Insights | $150 (telemetry and analytics) |
| **Total Monthly** | **$4,250** |

**Annual Estimate:** $51,000 (operational costs only)

**Cost Optimization Strategies:**
- Use classical topics before generative fallback (lower credit consumption)
- Optimize knowledge sources (reduce chunking complexity)
- Implement conversation limits (max turns per session)
- Archive old conversation history (reduce storage)
- Use standard connectors over premium where possible
- Leverage Microsoft 365 included capacity

### 9.3 TCO Analysis
- TCO Period: 3 years
- Year 1: $166,000 (implementation + operational)
- Year 2-3: $51,000/year
- **Total 3-Year TCO: $268,000**
- Cost per Conversation: $0.21 (estimated)
- Cost per Session: $0.18

## 10. Capacity & Scalability

### 10.1 Current Capacity
- Concurrent Agents: Unlimited (license-based)
- Peak Concurrent Sessions: 500
- Conversations per Day: 20,000
- Average Session Duration: 8 minutes
- Copilot Credits Monthly: 15,000 credits

**Deployment Sizing:**
- **Small:** 50 concurrent sessions, 2K conversations/day
- **Medium:** 500 concurrent sessions, 20K conversations/day
- **Large:** 5000+ concurrent sessions, 200K+ conversations/day

### 10.2 Scalability Plan

**Scaling Approach:**
- Platform Scaling: Enabled
- Scaling Trigger: Automatic by Microsoft (PaaS)
- Scale Out Time: Transparent to users

**Capacity Forecasting:**
- **Year 2026:** 60,000 conversations/day, 1,500 concurrent sessions, 45,000 copilot credits/month, estimated cost $12,000/month

## 11. Testing & Quality Assurance

### 11.1 Testing Strategy

**Manual Testing:**
- Test Chat Pane: Built-in test chat in authoring canvas
- Coverage: 100% of topics tested manually

**Automated Testing:**
- Tool: Power Platform Test Framework (preview)
- Coverage: 60% of critical flows
- Framework: Test Studio (Copilot Studio native)

**User Acceptance Testing:**
- Environment: Dedicated TEST environment
- Users: Business stakeholders + pilot users
- Duration: 2 weeks per major release

**Performance Testing:**
- Tool: Azure Load Testing
- Last Test Date: 2025-10-20
- Test Scenario: Sustained load (500 concurrent users, 1 hour)
- Result: Passed - p95 latency <2.5s

## 12. Diagrams & Visual Models

### 12.1 Layered Architecture Diagram
- **Diagram Type:** Layered Architecture Diagram
- **Diagram Format:** C4 System Context
- **Diagram File:** SBB-APP-002-Architecture-v1.0.0.drawio
- **Description:** Shows 5-layer Copilot Studio architecture

**Architecture Layers:**
1. **UI Layer:** Web chat widget, Microsoft Teams bot, Mobile apps, M365 Copilot extension (JavaScript SDK, Bot Framework, Adaptive Cards)
2. **Copilot Studio Service:** Authoring canvas, Generative AI orchestration, Topic engine, Entity recognition, Analytics (Microsoft-managed service)
3. **Power Platform Foundation:** Dataverse, Connectors, Power Automate, Environment management, Security (Power Platform)
4. **Azure Infrastructure:** Azure OpenAI, Azure AI Search, Azure Bot Service, Azure Storage, Azure AD (Microsoft Azure)
5. **Data Sources:** SharePoint, OneDrive, Dataverse, External APIs, Public websites (Microsoft 365 + External systems)

### 12.2 Integration Pattern Diagram
- **Diagram Type:** Integration Pattern Diagram
- **Diagram Format:** UML Component
- **Diagram File:** SBB-APP-002-Integration-v1.0.0.drawio
- **Description:** Shows agent flows, connectors, and external system integration patterns

**Key Components:**
- **Copilot Studio Agent Runtime:** Conversation management, Topic routing, Entity extraction
- **Agent Flows:** Tool orchestration, Business logic, External API calls (ServiceNow, Salesforce, Workday, Microsoft Graph)
- **Dataverse:** Conversation storage, Custom business data, Configuration
- **External Systems:** ServiceNow (ITSM), Salesforce (CRM), Workday (HR), SharePoint (Knowledge)

### 12.3 Data Flow Sequence Diagram
- **Diagram Type:** Sequence Diagram
- **Diagram File:** SBB-APP-002-DataFlow-v1.0.0.drawio
- **Description:** Shows user interaction data flow through Copilot Studio

**Sequence Flow:**

| Step | From | To | Action | Protocol |
|------|------|----|--------|----------|
| 1 | User (Teams) | Azure Bot Service | User sends message | Bot Framework |
| 2 | Azure Bot Service | Copilot Studio Service | Message routed to agent | HTTPS |
| 3 | Copilot Studio Service | Topic Engine | Classify user intent | Internal |
| 4 | Copilot Studio Service | Azure OpenAI | Generate response with context | HTTPS REST |
| 5 | Copilot Studio Service | Microsoft Graph API | Retrieve knowledge from SharePoint | HTTPS REST (OAuth 2.0) |
| 6 | Copilot Studio Service | Agent Flow | Invoke action (e.g., create ServiceNow ticket) | Power Platform Connector |
| 7 | Agent Flow | ServiceNow API | Create incident record | HTTPS REST (OAuth 2.0) |
| 8 | Copilot Studio Service | Dataverse | Store conversation history | OData |
| 9 | Copilot Studio Service | User (Teams) | Return agent response with confirmation | Bot Framework (via Azure Bot Service) |

## 13. Migration & Transition

### 13.1 Migration Strategy
This is a **greenfield implementation** with phased rollout:

| Phase | Duration | Scope | Users |
|-------|----------|-------|-------|
| Pilot (Phase 1) | 2 months | Single use case (HR FAQ agent) | 50 |
| Expansion (Phase 2) | 4 months | Additional 2 use cases (IT Helpdesk + Knowledge Assistant) | 500 |
| Enterprise (Phase 3) | Ongoing | Platform for low-code agent development | All employees |

## 14. Vendor Management

### 14.1 Vendor Information
- **Vendor Name:** Microsoft Corporation
- **Vendor Type:** Platform Provider
- **Tenant ID:** bnz.onmicrosoft.com
- **Subscription Type:** Enterprise Agreement
- **Account Manager:** Microsoft Enterprise Account Team
- **Customer Success Account Manager:** Microsoft CSAM

**Support Details:**
- Support Tier: Premier
- Support Hours: 24x7
- Support Portal: https://admin.powerplatform.microsoft.com/support
- Support Email: premier@microsoft.com

## 15. Known Issues & Limitations

### 15.1 Known Issues

| Issue ID | Severity | Description | Impact | Workaround | Resolution ETA |
|----------|----------|-------------|--------|------------|----------------|
| ISSUE-001 | Low | Agent flows replacing Power Automate flows (transition period) | Existing Power Automate flows need migration to agent flows | Continue using Power Automate flows until migration | Q2 2026 (full agent flows maturity) |

### 15.2 Limitations

**Functional Limitations:**
- **No built-in long-term memory across sessions (without custom dev)**
  - Impact: Agents don't remember past conversations by default
  - Mitigation: Use Dataverse custom tables to store user context

**Licensing Limitations:**
- **Complex licensing model (tenant + user + consumption)**
  - Impact: Cost forecasting challenging
  - Mitigation: Use Microsoft usage estimator tool, monitor capacity closely

**ALM Limitations:**
- **Solutions are XML-based, not file-based (Git diff challenging)**
  - Impact: Version control less intuitive than code-based systems
  - Mitigation: Use Power Platform Pipelines for deployment automation

**Custom Logic Limitations:**
- **Limited to Power Fx and agent flows (no Python/JavaScript in agent)**
  - Impact: Complex logic requires Azure Functions or external services
  - Mitigation: Use custom connectors to Azure Functions for advanced logic

## 16. Lessons Learned

### 16.1 Implementation Lessons

**What Went Well:**
- Rapid prototyping with visual canvas (business users involved early)
- Native Microsoft 365 integration (no custom auth needed for SharePoint)
- Comprehensive Power Platform governance tools

**What Could Improve:**
- Licensing complexity created budgeting challenges
- Agent flow transition from Power Automate flows created rework
- Need stronger version control discipline (solutions not as intuitive as code)

**Recommendations:**
- Invest in Power Platform Center of Excellence (CoE) early
- Start with simple use cases to build maker competency
- Establish environment strategy and DLP policies before scaling
- Use usage estimator tool for Copilot Credits forecasting
- Plan for maker training and ongoing support

## 17. Related Documents
- ABB-APP-001: Agentic AI Agent (Architecture Building Block)
- SBB-APP-001: AWS Bedrock AgentCore Agent (Alternative Implementation)
- Architecture Decision Record: ADR-2025-042 (Agent Platform Selection)
- BNZ Power Platform Governance Framework
- Copilot Studio Deployment Plan (EPIC-COPILOT-STUDIO-ENTERPRISE-ENABLEMENT.md)
