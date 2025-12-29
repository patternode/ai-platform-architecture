# Data & Information Protection - Target State Architecture (TSA) v0.2

## Document Information
- **Document**: Data and Information Protection TSA v0.2
- **Authors**: Francis Kaitano, Glenn Ballam, Hugh Walcott, John Marshall, Tracey Davis
- **Date**: August 2025 v0.2
- **Responsible Heads of Architecture**: Tanya Boelema, Angus Cotton
- **Enterprise Owners**:
  - Richard Boxall, Chief Information Security Officer
  - Kate Skinner, Executive – Digital, Data & Analytics
  - Paul Norman, Executive – Chief Information Officer

---

## Slide 1: Title Page - Data & Information Protection - Target State Modernisation Roadmap

This document presents BNZ's Target State Architecture for Data & Information Protection, establishing the strategy, process, technology and practice for safe, reliable, trusted and compliant data and information. The document is marked as CONFIDENTIAL and represents a comprehensive modernisation roadmap for the organisation.

---

## Slide 2: Table of Contents

The document is structured across six main sections:
- **Executive Summary**: High-level overview of the initiative
- **1. Platform Scope**: Platform scope, definition and business purpose
- **2. Current State**: Current state landscape and key pain points
- **3. Platform Target State**: Vision and architecture for the future state
- **4. Roadmap**: Implementation timeline and approach
- **5. Risk Overview of Current State**: Analysis of existing risks
- **6. Focus Areas**: Key technical and strategic focus areas
- **Appendices**: Supporting documentation and detailed definitions

---

## Slide 3: Executive Summary Section Divider

This slide introduces the Executive Summary section, providing a high-level overview of the Data & Information Protection modernisation initiative against BNZ's signature starfield background.

---

## Slide 4: Executive Summary - Modernisation Roadmap Overview

### Key Components:

**Definition**: Data & Information Protection encompasses the strategy, process, technology and practice for safe, reliable, trusted and compliant data and information, enabling BNZ to move faster, operate safer and lead with confidence in a digital first, regulated world.

**Scope & Context**: Effective Data & Information Protection requires deep integration across the entire technology ecosystem, not within the boundaries of any single platform.

**Transformation Approach**: An evolution from reactive, siloed cybersecurity practices to a unified model that embeds governance, security, and technology across platforms and teams, using a technology-enabled phase as a bridge to build operational maturity.

**Current State - BMI View**: BMI is represented in technologies across other platforms in BNZ, rather than in Data & Information Protection itself.

**NAB Alignment**: NAB haven't adopted Data & Information Protection as a platform, however the approach is similar in building protection with capabilities from other platforms. BNZ & NAB are targeting similar outcomes.

### Modernisation Pathway:
1. **Cyber Security Led**: Focused on threat defence, monitoring & incident response
2. **Technology Enabled**: Embedded protection in platforms & architecture
3. **Enterprise Trust & Resilience**: Unified governance, security & technology with automation and strategic alignment

### Key Strategic Actions:
- Re-use capabilities in existing technologies across platforms to uplift Data & Information Protection capability
- Define and communicate standards, patterns & tools for consistent protection practices
- Apply DataSecOps to embed automated protection continuously across the lifecycle
- Introduce Data & Information Protection Observability for real-time visibility
- Introduce Automation in detection & response to rapidly identify and mitigate threats
- Look for efficiency gains in AI that can improve Data & Information Protection

---

## Slide 5: Data & Information Protection Overview

### Challenges & Issues:
**Fragmented Foundations & Inconsistent Practices**: Legacy tools and siloed operations have led to inconsistent policy enforcement, missing Zero Trust capabilities, and low data protection maturity.

**Governance & Visibility**: Fragmented tooling and lack of integration limit end-to-end observability, with gaps in unstructured data protection and access controls.

**Operating Model & Capability Maturity**: The organisation lacks a fit-for-purpose model with fragmented risk ownership and constrained investment.

**Culture & Communication**: Data & Information Protection uplift is seen as a productivity barrier with limited business-led dialogue and unclear stewardship roles.

### Target State Overview:
**Key Points**:
- **Interface Layer**: Defining how to engage platform support and delivery services
- **CoE Services Layer**: Provides a platform service catalogue for delivery of configuration changes, recommendations and insights
- **DIP Control Layer**: Catalogue of governed risk mitigations, including policies, standards, training and support
- **Application Support Layer**: Technologies responsible for implementing configuration changes

### Technical Focus Areas:

**Uplift**:
- Zero Trust Architecture – shift from implicit trust to verify every access
- Event-driven & Decoupled Systems Security – strengthening system resilience
- Synthetic Data & Data Simulation – for testing and training (AI)
- Data Detection & Response Uplift – proactive detection and response
- Data Security Posture & Configuration - automation of capabilities for identifying exposures
- Channel Loss Prevention Uplift - strengthening breadth and coverage

**Future Focused**:
- AI Readiness – prepare to safely adopt and scale AI technologies
- Privacy-enhancing technologies – trusted execution environments
- Post Quantum cryptography – vulnerability mitigation for traditional encryption
- AI Opportunities – understand how AI can enhance Data & Information protection
- Data Sovereignty & cross border compliance – enable geo-fencing and data residency
- Resilience against ransomware & data tampering – confidential computing and immutable storage

---

## Slide 6: Section 1 - Platform Scope

This slide introduces Section 1 of the document, which covers the platform scope, definition and business purpose of the Data & Information Protection initiative.

---

## Slide 7: Definition & Platform Context

### Core Definition:
Data & Information Protection is the strategy, process, technology and practice for safe, reliable, trusted and compliant data and information. Effective Data & Information Protection requires deep integration with where data lives and moves – across the entire technology ecosystem, not within the boundaries of any single platform.

### Platform Architecture Context:
The diagram shows Data & Information Protection as a central capability that integrates with multiple other platform capabilities:
- **Cyber Threat Intelligence, Detection & Response**
- **Data & Analytics**
- **Enterprise Information Management**
- **Enterprise Interfaces API, Events & Integration**
- **Infrastructure Foundations**

### Supporting Platforms:
- **Application & Infrastructure Protection**
- **Customer Platforms** (Customer & Party Management, Customer Identity & Access Management, Customer & Party Lifecycle Management)
- **AI**
- **Colleague Identity & Access Management**
- **Customer & Colleague Digital**
- **FinCrime**

---

## Slide 8: Value Chain & Capabilities

### Value Chain Components:
The value chain describes the activity and capabilities that allow BNZ to achieve Data & Information Protection:

**1. Data Discovery & Classification**:
- Classification
- Data Business Rules Management & Refinement
- Data Catalog
- Data Lineage

**2. Protection Controls**:
- Access & Entitlement Management
- Backup
- Data Channel & Loss Protection
- Data Encryption
- Engineering Automation & Orchestration
- Masking & Tokenisation
- Ransomware Protection
- Secure Posture & Configuration

**3. Governance & Assurance**:
- Awareness Training
- Continuous Improvement
- Data Patterns, Principles & Guardrails
- Metrics, Reporting & Analytics
- Policy Management
- Privacy & AI Trust Oversight
- Process & Workflow Optimisation
- Risk & Compliance Management
- Consent Management

**4. Transfer, Storage & Destruction**:
- Archiving & Retention
- Data Transformation
- Destruction & Disposal
- Movement & Exchange
- Storage
- Versioning & Batching

**5. Detection, Response & Recovery**:
- Behavioural & Activity Monitoring
- Data Breach Analysis & Response
- Data Incident Playbooks
- Data Quality
- Data Recovery & Restoration
- Data Threat Monitoring & Orchestration
- Data Vulnerability & Exposure Management
- Forensics Analysis & Investigation
- Performance Monitoring

---

## Slide 9: Data & Information Protection Platform Context

### Strategic Framework:
The strategy, process and technology for safe, reliable, trusted and compliant data and information.

### Four Pillars:

**Strategic Drivers (the 'why')**:
- Customer confidence & trust
- Business continuity & resilience
- Compliance & regulator expectations

**Personas (the 'who')**:
- Customers
- Colleagues
- Party – Prospects, Partners, Regulators, Vendors etc

**Governance (the 'what')**:
- Regulations
- Risk Management
- Policies & Standards
- Controls

**Security (the 'how')**:
- Access Enablement
- Protection
- Detection & Response
- Operational resilience

### Scope Dimensions:
- **All data types** → **Across the whole lifecycle** → **Everywhere data & information lives and moves** → **Continuously** → **Through automation & orchestration**

---

## Slide 10: Data & Information Protection Break Down

### Five Key Areas:

**Data Types**: All data formats including structured data, unstructured data across operational and analytical systems and processes.

**Data Lifecycle**: Protection across the data lifecycle – Capture, Process, Retain, Distribute, Dispose.

**Security Coverage**: Protection of data in use, during transmission (in transit) and while stored (at rest), across all environments.

**Risk Informed**: Embedded, automated controls to deliver continuous security, assurance to meet compliance obligations and standards.

**Resilient Access**: Ensuring appropriate availability & access to data and information as and when it is required, without compromising its integrity.

---

## Slide 11: Security Perspective (The How)

### Security Architecture Overview:
This diagram illustrates the comprehensive security perspective covering the entire data ecosystem at BNZ.

### Key Security Components:
1. **Non Human**: AI, APIs, Microservices, system-system, cloud endpoint APIs
2. **Party**: Prospects, Partners, Regulatory bodies, vendors
3. **Identity & Trust**: Covers human, non-human entities including secret management, privilege access
4. **DataSecOps**: Automation of security controls across DataOps and managed pipelines
5. **Inventory, Visibility, Risk, Assurance**: Detection and Response are continuous across journey touchpoints
6. **User, Entity Behavioural Analytics (EUBA)**: Covers insider risk and threats for data usage

### Data Flow Stages:
- **Acquire** → **Provide** → **Consume** → **Produce**
- Central **Data @ BNZ** hub with Access, Movement, Storage, Curate, Data Quality, Metadata Management, Discover, and Lineage capabilities

### Security Layers:
- Data Detection & Response
- DataSecOps
- Data Security Risk & Assurance
- Inventory & Visibility
- Encryption & Ransomware Protection
- Secure Data & Posture Configuration

---

## Slide 12: Stakeholder Engagement & Accountability

### Organizational Structure:
The diagram shows the comprehensive stakeholder network involved in Data & Information Protection, organized by enterprise owners and their respective teams.

### Enterprise Owners:
- **Paul Norman**: Executive – Chief Information Officer
- **Kate Skinner**: Executive – Digital, Data & Analytics
- **Sam Perkins**: Executive – Chief Risk Officer
- **Karna Luke**: Executive – Customer Products & Services

### Key Leadership Roles:
- **Technology Architecture Forum (TAF)**: Paul Norman
- **GM – Core Infrastructure**: Nic Olivier
- **GM – Chief Information Security Officer**: Richard Boxall
- **GM Technology – Digital, Data & AI**: Lee Challoner-Miles

### Supporting Architecture and Management:
- **Heads of Architecture**: Tanya Boelema, Angus Cotton, Kim Arnold
- **Enterprise Architects**: Including specialists in Customer, Cybersecurity, Engineering & App Integration, IEM, Infrastructure, FinCrime, and Data & Analytics
- **Platform Managers**: Multiple managers across different technology domains

---

## Slide 13: Section 2 - Current State

This slide introduces Section 2 of the document, focusing on the current state landscape and key pain points in BNZ's Data & Information Protection capabilities.

---

## Slide 14: Current State – Overview

### Technology Distribution Across Platforms:
The current state shows Data & Information Protection capabilities are distributed across many platforms and technologies rather than being centralized.

### Platform Breakdown:
- **Data & Analytics**: 20 technologies, 16 capabilities
- **Enterprise Information Management**: 11 technologies, 13 capabilities
- **Enterprise Interfaces API's, Events & Integration**: 6 technologies, 7 capabilities
- **Engineering & Automation**: 8 technologies, 36 capabilities
- **Operational Observability**: 3 technologies, 6 capabilities

### Technology Lifecycle Status:
Technologies are categorized by lifecycle status:
- **Innovate** (Purple)
- **Encourage** (Green)
- **Contain** (Yellow)
- **Exit** (Red)

### Current Challenges:
- **36 DIP Capabilities** spread across **90+ Technologies**
- The platform as currently represented does not adequately cover Data & Information Protection at BNZ
- Note: This analysis is incomplete - there are more technologies and platforms to be identified and catalogued

---

## Slide 15: Current State Interactive Dashboard

This slide references an interactive dashboard/report that visualizes the technologies across BNZ platforms used to deliver Data & Information Protection. The dashboard allows filtering by:
- **Platform**: Data & Analytics (and others)
- **Technology**: All technologies
- **Value Chain**: All value chain components
- **Capabilities**: All capabilities

The dashboard shows a detailed matrix mapping technologies to value chain capabilities including:
- Transfer, Storage & Destruction
- Protection Controls
- Governance & Assurance
- Detection, Response & Recovery

---

## Slide 16: Current State Challenges

### Four Key Challenge Areas:

**Fragmented Foundations & Inconsistent Practices**:
- Legacy tools lack architectural and technical fitness for modern use cases
- Disparate workflows, tools and operating models across domains
- Inconsistent application of policy across technologies
- Lack of standardised protection guardrails and enforcement patterns
- Zero Trust data protection foundational capabilities are missing
- EIM protections are unevenly distributed across systems & lifecycle stages
- Low maturity enterprise level data detection & response logic

**Operating Model & Capability Maturity**:
- Operating model is not fit for purpose (DataSecOps, automation, policy)
- Capabilities lack breadth and depth to address excessive and emerging risks
- Conflicting understanding of risks related to data & information protection across the organisation and responsibility for mitigation (e.g. RSK-166 & 171)
- Investment in uplift constrained by prioritisation, resources, and funding
- Change Management issues when rolling out DLP and authentication changes
- Achieving balance between need to protect and need to enable
- Lack of investment and commitment to uplift within the organisation

**Governance & Visibility**:
- Poor end-to-end observability due to fragmented tooling and context sharing
- Gaps for unstructured data in malware protection (outside O365), document disposal and assurance
- Inadequate performance monitoring and governance of document protections
- Unclear data retention and disposal linked to customer lifecycle events
- Limited integration with data catalogue at design time
- Identity and authorisation gaps: unclear access and role-based controls

**Culture & Communication**:
- Perception that Data & Information Protection uplift restricts productivity, leading to push back
- Technology-led conversations mean not leading uplift discussions from business and customer value perspective
- Lack of data stewardship training and role clarity
- Need for broader communication to build understanding and confidence

---

## Slide 17: Section 3 - Platform Target State

This slide introduces Section 3, which outlines the platform target state vision and architecture for Data & Information Protection.

---

## Slide 18: Data & Information Protection Modernisation

### Transformation Journey:
From Defence to Confidence: Transforming Data & Information Protection into Enterprise Trust & Resilience.

### Three-Phase Evolution:

**1. Cybersecurity-Led**:
- **Focus**: Threat defence, monitoring and incident response
- **Industry Trends**: Historic - Rooted in perimeter defence and reactive models; still relevant but evolving
- **Drivers**: Threat landscape, regulatory pressure, need for resilience and proactive breach readiness
- **Key Shifts**: Manual to Automated Controls, Reactive to proactive, Perimeter to identity/data-centric, Siloed to integrated
- **Strategic Value**: Strong foundation for protection, but limited in agility with digital transformation

**2. Technology Enabled**:
- **Focus**: Embedded protection in platforms & architecture
- **Industry Trends**: Transitional - Supports modern architectures and automation; needs governance integration to mature
- **Drivers**: Cloud adoption, automation, agile development, platform modernisation
- **Key Shifts**: Introduces DevSecOps, Automates compliance, Enables real-time monitoring
- **Strategic Value**: Bridges the gap between security and operations; supports scale, agility & cloud first approaches

**3. Enterprise Trust & Resilience**:
- **Focus**: Unified governance, security, and technology with automation, visibility and strategic alignment
- **Industry Trends**: Future-facing - Aligns with trends like zero trust, open banking, AI-driven, automated compliance risk, detection and response
- **Drivers**: Hostile Threat landscape, regulatory compliance, digital transformation, trust and transparency
- **Key Shifts**: Cross-functional ownership, Continuous assurance, Trust and transparency as outcomes, Resilience
- **Strategic Value**: Aligns protection with business value and risk appetite. Focused on enabling and protecting

---

## Slide 19: Operating Model Shifts

### Transformation Areas:
From Defence to Confidence: Transforming Data & Information Protection into Enterprise Trust & Resilience.

### Nine Key Transformation Dimensions:

**Customer Centricity**: Internal focus on protecting systems and data → External focus on earning trust through transparency and ethical data use

**Governance Shift**: Isolated within technology/security, with limited visibility across the enterprise → Involve the whole business in trust and resilience, not just technology teams

**Strategic Alignment**: Security focused on protecting assets and meeting compliance → Trust and resilience part of business strategy and innovation

**Scope Expansion**: Focus on technical threats, like malware and unauthorised access → Beyond technical threats, to include disruptions, ethics and privacy

**Leadership Involvement**: CISO/Security teams lead, with limited business input → Shared accountability across senior leaders

**Cultural Transformation**: Security is seen as a blocker or compliance checkbox → Build a culture where everyone trusts, values and protects data & information

**Capability Enhancement**: Reliance on traditional tools like firewalls, antivirus and access controls → Expand to use advanced tools like data lineage and digital ethics frameworks

**Architecture Evolution**: Security is added after systems are built ("bolt-on") → Select and design systems with trust and resilience from the start

**Redefined Metrics**: Metrics focus on technical indicators (e.g. number of incidents, patching rates) → Measure trust and resilience, not just technical issues

---

## Slide 20: Uplift Themes

### Seven Strategic Uplift Themes:

**Zero Trust by Design**: Ensure access is granted only when identity, context, and risk are verified—minimising exposure and strengthening resilience.

**Continuous Compliance**: Embed automated governance and monitoring to maintain real-time assurance and reduce reliance on manual audits.

**Privacy First Architecture**: Design systems with privacy embedded from the outset, ensuring responsible data use and regulatory alignment.

**Secure Data Usage**: Enable secure data processing and analytics without compromising sensitive information - unlocking value while protecting trust.

**Culture & Capability**: Foster a security-aware culture through training, leadership alignment, and integration into operating models.

**DataSecOps Driven**: Use practices which embed automated security, trust, compliance, workflows and guardrails by design and continuously into every stage of the data lifecycle.

**Exceptional Colleague Experiences**: Delivering premium user experience, where data and information protection is applied 'just in time', lowering friction and toil.

---

## Slide 21: Data & Information Protection – BNZ Vision

### Vision Statement:
Enabling BNZ to move faster, operate safer and lead with confidence in a digital first, regulated world.

### Five Strategic Transformations:

**From Cyber-centric to Enterprise Enablement**:
- Build a policy translation layer to convert business protection needs into scalable, platform-specific enforcement
- Enable cross-platform visibility and orchestration to align protection with enterprise priorities and delivery pipelines

**From Tech Uplift to Secure-by-Design**:
- Leverage existing investment in cyber, cloud transformation and data platform modernisation to embed native protection capabilities
- Make data protection a default part of platform engineering, not an afterthought

**From Reactive to Proactive Control**:
- Embed automated protection into the design and deployment lifecycle—ensuring controls are integrated from the start, not retrofitted
- Introduce automated response workflows to detect and act on anomalies across platforms

**From Independent to Collaborative Delivery**:
- Shift to an enterprise shared responsibility model, enabling teams to own protection outcomes with the right support
- Equip and incentivise teams to prioritise secure configuration and data protection outcomes – not just functional delivery

**From Siloed to Orchestrated Governance**:
- Implement federated governance with shared standards and automation tools—empowering platform teams with guardrails, not gates
- Establish a Centre of Enablement to co-ordinate enterprise-wide protection, trust and resilience

---

## Slide 22: Target State Architecture

### Layered Architecture Model:

**Customer Layer**: Platform owners who, through training and insights, can access DIP services via the interface layer.

**Interface Layer**: Defining how to engage data and information protection platform support and delivery services.

**CoE Services Layer**: Defines the services available, from prepared patterns, guardrails, to the delivery of configuration changes, recommendations and insights.

**DIP Control Layer**: Catalogue of governed risk mitigations, including policies, standards, training and support.

**Application Support Layer**: Representing the technologies responsible for implementing the configuration changes.

### Service Flow:
- **Service Desk** → **Events** → **Observability feeds** → **Insights** → **Training**
- **DIP Service Requests** → **DIP Business Events** → **Analytics & Orchestration** → **Self Serve Metrics & Dashboards**
- **Data & Information Protection Guardrails & Patterns** → **Detection & Response Engineering** → **DIP Managed Delivery Pipeline** → **Configuration** → **Governance and Assurance Services**
- **Policies Standards** → **Policy & Compliance as Code** → **DIP Technical Control Catalogue** → **Defence Posture Optimisation** → **Training and Support**

### Implementation Layer:
**Domain Managed and Owned DIP Applications & IT Components**

---

## Slide 23: Section 4 - Roadmap

This slide introduces Section 4, which details the implementation roadmap and timeline for achieving the target state Data & Information Protection architecture.

---

## Slide 24: Indicative Roadmap

### Roadmap Overview:
Indicating the actions needed to evolve the operating model from cybersecurity-led to a trust and resilience driven enterprise approach.

### Timeline: FY26 - FY29+

### Six Key Workstreams:

**Establish Cross-functional Governance**:
- Form a cross-functional steering group including security, risk, legal, data and business leaders
- Align governance with enterprise risk and strategic planning
- Define clear roles and shared accountability across leadership

**Redesign Strategy & Architecture**:
- Update strategy to embed trust, ethics, and resilience as core principles
- Apply trust-by-design and resilience-by-design in architecture and solution development
- Align architecture decision with business outcomes and stakeholder expectations

**Build Foundation & Scale Capabilities**:
- Re-use existing (and invest, where required) tools for privacy engineering, data lineage, trust scoring & resilience modelling
- Develop secure-by-design & zero trust architectures
- Enable proactive risk sensing and adaptive response capabilities

**Create a Centre of Enablement (CoE)**:
- Establish CoE to drive adoption and capability uplift across teams
- Provide toolkits, frameworks, and best practices for trust and resilience
- Act as a hub for training, coaching and community building

**Modernise Policies & Processes**:
- Revise policies to reflect trust, privacy and resilience goals
- Embed trust into business continuity, incident response, and third-party risk management
- Ensure procurement and vendor onboarding include trust and privacy criteria

**Drive Cultural & Behavioural Change**:
- Launch training and awareness programs on data stewardship and trust
- Promote a culture of transparency, accountability and ethical data use
- Recognise and reward behaviours that support enterprise trust and resilience

**Define & Track Metrics**:
- Introduce KPIs for trust, data integrity, resilience maturity, and stakeholder confidence
- Use dashboards to monitor and communicate performance across the enterprise
- Link metrics to business value and strategic outcomes

---

## Slide 25: Planned Uplift Roadmap

### Investment Timeline: FY25 - FY28+

### Three Programme Categories:

**Cyber Programme**:
- Strategic Uplift (Data Security Fabric)
- DLP channel Protection
- AI, Cloud, SaaS & API Data Security Uplift
- DataSecOps Uplift
- Data Threat Detection & Response
- Data Access & Entitlement Management

**Data Programme**:
- Governance Workstream
- Snowflake Uplift workstream
- Data Products Workstream

**EIM (Enterprise Information Management)**:
- Document Management Workstream
- Imaging Workstream

### Key Initiatives:

**Current Investment**:
- DLP Channels strengthening (zScaler & Purview)
- M365 Tenancy Control Uplift
- Email Threat Detection & Response Modernisation
- Purview IASPM & IRM uplift
- Application & Infrastructure Protection Modernisation (ASPM & ATDR)
- Security and governance by design in data pipelines (shift left)
- Classification, lineage and reconciliation uplift
- Hollow out and decommission of legacy assets

**Future Investment**:
- Strategic Data Protection Uplift: Option analysis & experiment
- Strategic Enterprise Data Protection Tool Uplift - Execution
- Wiz AISPM & DSPM uplift
- Cloud Security Modernisation
- API Edge Security
- Attack & Defence Posture Optimisation
- Identity Fabric Foundations (Zero Trust Data Access Enablement)

---

## Slide 26: Platforms @ BNZ

### BNZ Platform Architecture:
A key theme of BNZ's Technology Strategy is to adopt a platform mindset that will help transform the bank with the Intentional Modernisation approach.

### Platform Categories:

**Experience Platforms**:
- Channels: Customer Digital, Colleague Digital, Conversational Banking, Physical Experiences
- Enablers: Customer Identity & Access Management, Colleague Identity & Access Management, Open & Proprietary Banking APIs

**Customer Serving Platforms**:
- Customer Management: Customer and Party Lifecycle Management, Customer and Party Master, Customer Financial Analysis, Customer Engagement, Marketing & Campaign Management
- Product Origination & Maintenance: Everyday Banking Product Origination, Lending Origination, Credit Modelling, Pricing & Decisioning
- Account Management & Servicing: Collateral Management, Core Banking Ledger, Product Master, Investment & Private Wealth, Loyalty Offers & Rewards, Card Issuing & Management, Money Market, Merchant Acquiring
- Payments: Transaction Switch, Domestic Payments, International Payments

**Business Enablement Platforms**:
- Enabling Services: Collections & Hardship, Complaints & Disputes, Financial Crime & Fraud
- Enterprise Services: Group Credit Risk, Treasury Risk, Governance, Operational Risk & Compliance, Regulatory Reporting, Enterprise Information Management, People & Culture, Finance, Procurement Management

**Core Technology Platforms**:
- Enterprise Security: **Data & Information Protection** (highlighted in purple), Cyber Threat Intelligence Detection & Response, IT Asset Assurance & Service Management, Application & Infrastructure Protection
- Enabling Technologies: Enterprise Interfaces API Events & Integration, Engineering & Automation Software, Workplace Technology, Workflow Automation & Robotics, Infrastructure Foundations, Delivery Platform, Operational Observability, Core Network Management

### Platform Dependencies:
- **Platform in scope**: Highlighted in purple (Data & Information Protection)
- **Up-stream dependencies**: Highlighted in lime
- **Down-stream dependencies**: Highlighted in orange

---

## Slide 27: NAB Alignment

### NAB Approach Comparison:
NAB haven't adopted Data & Information Protection as a platform, however the approach is similar. NAB includes the higher level BIAN capabilities for Data & Information Protection into other platforms while BNZ aggregates lower level capabilities into Data & Information Protection. BNZ & NAB are targeting similar outcomes across contributing platforms e.g. secure-by-design, proactive risk and threat informed protection.

### NAB Platform Integration:
NAB have instead built the (higher level) BIAN capabilities that cover Data & Information Protection into other platforms, such as:
- Storage & Data Protection, Data Archiving & Records Management
- Governance, Compliance & Risk (breach reporting)
- Workflow Process Automation
- Security Services

### Key Considerations:
- It could be useful to map the lower level capabilities in BNZ Data & Information Protection to the higher level BIAN capabilities and draw out the similarities and differences further
- The Data & Information Protection at BNZ does not neatly align to NAB's definition of platform – while it has a well defined capability boundary it is an aggregation, the proposal is an aggregate of technologies that sit in other platforms
- The responsibility for technology within the platform is therefore challenging, because on it's own Data & Information Protection won't have any technologies
- NAB's Data Protection Team are still taking the cyber centric approach for the next 12-18 months. Overall, we align on capabilities and outcomes

### Open Question:
Why is Data & Information a platform at BNZ, but not for NAB?

**Consulted**:
- John Roome @ NAB
- Sam Siggins Lead Domain Architect – Data Security
- Karan Narad – Head Of Data Security

---

## Slide 28: Strategic Alignment

### BNZ Strategic Ambition Alignment:
This target state is architected in alignment with BNZ Strategic Ambition through Technology Themes and Intentions.

### Five Strategic Themes:

**Modernise and Simplify**:
- **Objective**: Intentional simplification and modernisation
- **Approach**: Getting the Basics Right (significantly reduced tool landscape, functional overlap and complexity), Laying the Right Foundations (modernise and build missing capabilities), Fit for purpose capabilities (enable capabilities guided by TSA and reference blueprint)

**Agile and Adaptable**:
- **Leveraging Engineering & DataSecOps**: Ensure the bank is positioned to build and deploy controls with minimal manual steps by automating and orchestrating security using context to invoke the right testing and remediation
- **Key Focus**: Shift from reactive to proactive Data & Information Protection, Embed and automate detection & response, Data & Information Protection as an enabler - Guardrails not gates

**Platform Mindset**:
- **Approach**: Deliver a composable, well-architected, engineered, and automated platform
- **Strategy**: Simplify by aggregating data & information protection capabilities across existing platforms, rather than a platform on its own, Extend capability coverage to have breadth, depth and reach across all BNZ distributed environments

**Resilient, Secure and Safe**:
- **Capabilities**: Shifting from reactive to proactive Data & Information Protection, Adaptive Posture Refinement, Close to real-time security observability, Compliance and Secure by design

**Deeply Digital**:
- **Focus**: Manual touch points will be limited with flow through automation favoured, Just in time access to data delivering exceptional colleague experiences, Use of automation and orchestrations consistently across the DIP ecosystem

---

## Slide 29: Section 5 - Risk Overview of Current State

This slide introduces Section 5, which provides an analysis of the current state risks and how the Data & Information Protection platform addresses them.

---

## Slide 30: Current State – Business Risk Overview

### GRACE Risk Impact Analysis:
The following GRACE risks are impacted by the Data & Information Protection Platform:

**RSK-171: Cyber Compromise Risk**:
- **Risk Description**: Risk that information systems containing customer, employee or business data lose their confidentiality, integrity, or availability due to inappropriate access, malware attacks, compromised credentials, insecure coding practices, etc.
- **TSA Impact**: This TSA is responsible for building and delivering key foundational capabilities and controls for enabling mitigation of this risk and managing the need for proactive detection, response and containment of cyber compromises
- **Current State**: Current capabilities are rudimentary and require significant uplift to transition to a fit-for-purpose target state
- **Impact Level**: **Direct Risk Buydown**

**RSK-166 Data Loss**:
- **Risk Description**: Focuses on unauthorised access to BNZ data in electronic or physical format (customer, employee and intellectual property) resulting in loss or disclosure of BNZ confidential information
- **TSA Impact**: Capabilities and controls delivered through the target state directly impacts ability to proactively detect, respond and contain any risks, threats, and breaches associated with data breaches
- **Current State**: Current capabilities are rudimentary and require significant uplift to transition to a fit-for-purpose target state
- **Impact Level**: **Directly Impacts Risk Mitigation**

**RSK-158 IT System Failure**:
- **Risk Description**: Failure to properly manage BNZ Information Technology (IT) assets and effectively respond to IT incidents resulting in service outages and disruptions
- **TSA Impact**: Cyber incidents such as Denial of Services and Ransomware attacks usually result in system failure when they occur. The TSA contributes to minimisation by delivering autonomic cyber defence capabilities. Modernisation will also result in simplification and optimisation of tools
- **Impact Level**: **Directly Impacts Risk Mitigation**

---

## Slide 31: Current State – Business Risk (Continued)

**RSK-1300 Data Management Risk**:
- **Risk Description**: Data management risk is the risk that data/information/records is incorrect (incomplete, inaccurate, inaccurately transformed), or is incorrectly used (inappropriate use, unethical use, use breaching confidentiality or privacy, outputs not fit for purpose, incorrectly disposed)
- **TSA Impact**: The TSA positively impacts Data Risk 4 - Inappropriate or unethical use of data (incorrect use of data). Reducing overcollection, through appropriate classification and enabling appropriate retention and disposal. Through reduced opportunity for unauthorised manipulation and alteration of data and in applying appropriate protection for sensitive data. The observability in the target state allows identification and resolution, where overcollection occurs and where sensitive data is found to be unprotected
- **Impact Level**: **Direct Risk Buydown**

**RSK-1288 Issuing and Acquiring Compliance Risk**:
- **Risk Description**: Risk of failure to comply with Payment Card Industry Data Security (PCI DSS) requirements, Card Scheme requirements (issuing & acquiring), Payments NZ Industry rules, and manage appropriately merchant acquiring customer and exposure risk
- **TSA Impact**: Capabilities and controls delivered through the target state directly impacts ability to proactively deliver the control efficacy required to meet PCI DSS data security requirements and to reduce the residual risk of non-compliance. Capabilities delivered will also enhance abilities to protect customer and card payments data
- **Impact Level**: **Directly Impacts Risk Mitigation**

---

## Slide 32: Section 6 - Focus Areas

This slide introduces Section 6, which outlines the key technical and strategic focus areas for the Data & Information Protection modernisation initiative.

---

## Slide 33: Technical Focus Areas

### Six Key Technical Focus Areas:

**Zero-Trust Architecture**:
- **Objective**: Shift to identity & trust based architecture – dynamic and risk based access
- **Key Principles**: Verify every access (no user or device trusted by default), Enforce least privilege (minimum access needed), Continuously validate trust (monitor and re-authenticate dynamically), Secure across boundaries (consistent controls across cloud, on-prem and hybrid)

**Event-driven and Decoupled Systems Security**:
- **Objective**: Enhancing resilience by securing service interactions, protecting data, detecting anomalies and maintaining accuracy
- **Benefits**: Limit breach impact (decoupled systems isolate vulnerabilities), Enable real-time alerts (instant threat detection), Enforces Zero-Trust (each service manages its own access controls), Boosts Resilience (systems recover independently and securely)

**Synthetic Data & Data Simulation**:
- **Question**: Agentic AI to generate synthetic data for testing & training?
- **Benefits**: Protect privacy (realistic data without exposing sensitive info), Enable safe testing (secure testing without prod data), Speed up development (remove data access barriers), Improve security validation (simulate edge cases to test protection controls)

**Data Detection & Response Uplift**:
- **Objective**: Proactive detection & response to threats and breaches
- **Benefits**: Proactively identify threats (advanced analytics/AI to detect suspicious activity), Accelerate incident response (rapid containment and remediation), Improved visibility (enhanced monitoring across data flows), Support continuous protection (integrate with security ops for real-time threat management)

**Data Security Posture & Configuration**:
- **Objective**: Automation of capabilities responsible for identifying exposures and misconfiguration across data assets and their mitigations
- **Benefits**: Automate exposure detection (continuously scan for misconfiguration & vulnerabilities), Prioritise risk mitigation (flag high risk issues and recommend actions), Improve visibility (centralised insight into data security posture), Policy enforcement (align config with security policy & compliance standards)

**Channel Loss Prevention**:
- **Objective**: Strengthening breadth and coverage across channels
- **Benefits**: Expand Coverage (strengthen monitoring across all communication channels), Detect Data Leakage (identify unauthorised data exfiltration in real time), Apply consistent controls (enforce data protection policies across email, web, cloud and endpoint), Reduce insider risk (monitor user behaviour to prevent data loss)

---

## Slide 34: Future Focus Areas

### Six Future-Focused Areas:

**AI Readiness**:
- **Objective**: Prepare to safely and effectively adopt and scale AI technologies
- **Key Actions**: Establish data governance (ensure integrity, privacy and security in AI systems), Enable risk monitoring (continuously audit AI deployments), Promote ethical AI use (train stakeholders on responsible AI practices), Build scalable infrastructure (distributed, fault tolerant systems)

**AI Opportunities**:
- **Objective**: Understand how AI can enhance Data & Information Protection
- **Applications**: Detect threats early (identify anomalies and suspicious behaviour), Classify sensitive data (automate tagging and access control), Protect privacy (enable techniques like synthetic data and differential privacy), Predict risks (anticipate vulnerabilities through behavioural analysis)

**Privacy-enhancing Technologies**:
- **Objective**: Trusted execution environments to protect sensitive data and code during processing
- **Capabilities**: Secure data in use (protect sensitive data during processing), Isolate execution (run code in secure, tamper-resistant environments), Prevent unauthorised access (block external threats from accessing protected workloads), Support compliance (enable secure processing aligned with privacy regulations)

**Post Quantum Cryptography**:
- **Objective**: As quantum computing advances, traditional encryption methods may become vulnerable
- **Preparation**: Prepare for Quantum threats (anticipate future risks to current encryption), Secure Long-term Data (protect sensitive data that must remain confidential for decades), Enable cryptographic transition (support migration to quantum-resistant algorithms), Maintain compliance (align with emerging standards for post-quantum security)

**Data Sovereignty & Cross Border Compliance**:
- **Objective**: Architect to account for data residency, support geo-fencing and enable jurisdiction aware data handling
- **Capabilities**: Data residency (ensure data is stored and processed within approved jurisdictions), Enable geo fencing (restrict data access and movement based on geographic boundaries), Implement jurisdiction awareness (adapt data handling to comply with local laws), Mitigate legal risk (reduce exposure to cross-border data transfer violations)

**Resilience Against Ransomware & Data Tampering**:
- **Objective**: Confidential computing, immutable storage, air-gapped backups and recovery architecture. Blockchain for tamper-evident logs
- **Capabilities**: Prevent alteration (through confidential computing, immutable storage), Ensure recovery (maintain attested backups and resilient recovery architecture), Detect tampering (leverage blockchain for tamper-evident logging and audit trails), Browser as the last mile (bolstering browser protection to mitigate against browser driven data and AI threats)

*Note: AI Readiness will be covered in AI TSA

---

## Slide 35: Next Steps

### Four Key Next Steps:

**Data & Information Protection as a Platform?**:
- Consider whether D&IP as a sub-platform of Security is appropriate? Or if Data & Information Protection as a platform is appropriate at all?
- The target state demonstrates how DIP is delivered outside of a specific platform
- Does BNZ have the scale and investment to support dropping the platform in alignment with NAB?
- The apps within the current DIP platform can be collapsed into existing platforms – may drive slight changes to naming & boundaries of existing platforms

**Operating Model**:
- A more holistic and strategic focus, requires significant operating model change
- RACI to clarify roles, boundaries and responsibilities
- Building the capacity to enable an engineering centric operating model, right sized to deliver DataSecOps
- Who owns the blueprint for delivering the uplift and the ongoing currency?

**Exec Buy-in**:
- Commitment & investment is required from BNZ leaders
- Cross-functional leadership – CIO, DD&A, legal, risk and business. Governance is integrated into enterprise risk and strategic planning
- Overarching accountability for the existing Excessive data risks e.g.: RSK-166, 171, RSK 1288, etc.
- Approach for driving investments to deliver the target state uplift and outcomes

**Principles, Practices & Patterns**:
- The foundations and scaffolding for Data & Information Protection uplift
- Defining the structure for core enabling tools
- Establishment of patterns and guardrails for enabling coherence
- Codification and standardisation of guardrails, standards and policies
- Automation and Orchestration of controls and workflows

---

## Slide 36: Appendices Section

This slide introduces the Appendices section, which contains supporting documentation, detailed definitions, and supplementary information for the Data & Information Protection TSA.

---

## Slide 37: Value Chain & Capability Definitions

### Data Discovery & Classification:
Processes and tools that help identify, catalog, and classify data based on its sensitivity, criticality, and business value. This enables appropriate protection and governance measures to be applied.

**Classification**: Categorising data and information assets based on sensitivity and criticality to apply appropriate protection measures

**Data Business Rules Management & Refinement**: Managing and refining business logic applied to data and information assets, for example data transformation or metadata used for data protection

**Data Catalog**: Centralized inventory of data and information assets to support discovery, governance, and access control

**Data Lineage**: Tracking the origin, movement, and transformation of data and information assets across systems

### Protection Controls:
Technical and procedural safeguards that prevent unauthorised access, disclosure, alteration, or destruction of data. These include encryption, access controls, and secure configurations.

**Access & Entitlement Management**: Controlling who can access data and what actions they can perform

**Backup**: Creating periodic copies of data to recover in case of loss or corruption

**Data Channel & Loss Protection**: Preventing unauthorized and unintentional data transmission and leakage

**Data Encryption**: Securing data by converting it into unreadable format without proper keys

**Engineering Automation & Orchestration**: Automating and embedding security, responses and workflows

**Masking & Tokenisation**: Obscuring sensitive data to reduce exposure risk during processing or testing

**Ransomware Protection**: Defending against malicious software that encrypts data for ransom

**Secure Posture & Configuration**: Ensuring systems are securely configured to prevent vulnerabilities

### Governance & Assurance:
Policies, roles, oversight mechanisms, and continuous improvement practices that ensure data protection is embedded in organisational culture and aligned with regulatory and business requirements.

**Awareness Training**: Educating staff on data protection policies and practices

**Consent Management**: Ensuring that individuals have control over how their personal data is collected, used, shared, and retained

**Continuous Improvement**: Iteratively enhancing data protection capabilities

**Data Patterns, Principles & Guardrails**: Defining consistent rules and standards for data usage and protection

**Metrics, Reporting & Analytics**: Measuring and analysing data protection performance

**Policy Management**: Defining and enforcing rules for data security and privacy

**Privacy & AI Trust Oversight**: Ensuring responsible use of personal data and AI systems

**Process & Workflow Optimisation**: Framework for ensuring the ongoing improvement of data protection processes and workflows for efficiencies and completeness

**Risk & Compliance Management**: Monitoring and managing risks to meet regulatory requirements

---

## Slide 38: Value Chain & Capability Definitions (Continued)

### Transfer, Storage & Destruction:
Controls and practices that govern how data is securely stored, moved, retained, and ultimately disposed of, ensuring lifecycle integrity and compliance with legal and operational standards.

**Archiving & Retention**: Preserving data for legal, regulatory, or operational needs

**Data Transformation**: Modifying data formats securely during processing

**Destruction & Disposal**: Securely eliminating data that is no longer needed

**Movement & Exchange**: Securing data as it moves (in motion) or as it is exchanged between different parties with varying risk or trust levels

**Storage**: Securely maintaining data in physical or cloud environments

**Versioning & Batching**: Managing data changes and grouping for efficient processing

### Detection, Response & Recovery:
Capabilities that enable the organization to detect threats, respond to incidents, and recover from data breaches or system failures, minimizing impact and restoring normal operations.

**Behavioural & Activity Monitoring**: Observing user and system behaviour to detect anomalies

**Data Breach Analysis & Response**: Investigating and mitigating data breaches

**Data Incident Playbooks**: Predefined procedures for responding to data security incidents

**Data Quality**: Observing that information is accurate, complete, and consistent—making it easier to detect anomalies, prevent breaches, and enforce access controls effectively

**Data Recovery & Restoration**: Restoring data after loss or compromise

**Data Threat Monitoring & Orchestration**: Identifying and coordinating responses to threats

**Data Vulnerability & Exposure Management**: Identifying and mitigating weaknesses in data systems

**Forensics Analysis & Investigation**: Examining incidents to understand root causes and impacts

**Performance Monitoring**: Tracking system performance to detect potential security issues

---

## Slide 39: Stakeholder Engagement

### Comprehensive Stakeholder Consultation Process:
The document development involved extensive engagement across multiple areas of the organisation from August to September 2025.

### Key Engagements:

**Architecture & Strategy Leadership**:
- Rodger Donaldson, Paul Dudding (Data platform architects)
- Shirley McIntyre, Tanya Boelema, Ann Tiatia (GM Tech Strategy & Architecture, HoA)
- Kim Arnold (HoA engagement)

**Digital, Data & Analytics Teams**:
- Dan Williams, Grace Shin, Dan Dove, Rebecca Mursell, Alan Fowler (Key DD&A people in data engineering, data risk, data governance)
- Anna Tarasoff, Roberta Prentice, Alex Dickson (DD&A GMs & data risk)
- Lee Challoner-Miles (GM Data, Digital & AI)
- Sandra Towgood, Alex Wardle (DD&A leaders)
- Damion Riordan, Deb Gill, Jane Eagle, Haseeb Quazi, Dave Dyer (DAP LT)

**Cybersecurity & Risk**:
- Richard Boxall, Brett Williams, Mrinal Mukherjee (CISO, HO and Product Manager)
- Mrinal Mukherjee, Diego McCormic, Karl Lellman, Red Hanlon (Cyber Data Protection Team & Security Architects)

**Engineering & Infrastructure**:
- Nic Olivier (GM briefing)
- Hayden Smith, Oliver Jennings, Bianca Collor, Francois Herbert (Engineering HO and Product Managers)

**Executive Leadership**:
- Kate Skinner (Exec briefing)

**Cross-Domain Collaboration**:
- Cross Domain (Strategy & Architecture, DD&A, Cyber and Core) GMs Workshop with key cross functional GMs to discuss and clarify Operating Model, Boundaries and Approach

---

## Slide 40: User Perspective

### Data Flow and User Interactions:
This diagram illustrates how different user types interact with data across BNZ's ecosystem.

### User Types and Perspectives:

**Colleague**:
- "I want it to 'just work'"
- "I want it to be easy to do the right thing"
- "I want to know the data is secure"
- "I have an obligation to treat data securely"

**Customer**:
- "I want it to 'just work'"
- "I want to trust my bank"
- "I need guidance in how to keep my data safe"
- "I want to know that the data I produce, provide and access is secure"

**Party** (Prospects, Partners, Regulatory bodies, vendors):
- "I want to have agreement with BNZ as to how data is accessed and used"
- "I want easy and secure ways to access data"
- "I want easy & secure ways to acquire and provide data"

**Vendor**:
- "I want to treat data according to BNZ regs & standards"

### Data Operations:
**Data Capture**:
- **Produce**: Create data & information
- **Consume**: Use data for business value

**Data Distribution**:
- **Provide**: Supply data or information that has already been created
- **Acquire**: Acquire data that is already created

### Central Data Hub @ BNZ:
- Access, Movement, Storage, Curate
- Data Quality, Metadata Management, Discover, Lineage

---

## Slide 41: Governance Perspective

### Comprehensive Governance Framework:
This diagram shows the regulatory and policy environment that governs Data & Information Protection at BNZ.

### Regulatory Framework:

**Global Standards**:
- **PCI DSS** (Payment Card Industry Data Security Standard)

**New Zealand Regulatory Bodies**:
- **RBNZ** (Reserve Bank of New Zealand)
  - CPS234, CPS230, CPG235
- **FMA** (Financial Markets Authority)
- **MBIE** (Ministry of Business, Innovation and Employment)
- **Privacy Act**
- **Open Banking/CDR** (Consumer Data Right)

**International Regulations**:
- **EU GDPR** (General Data Protection Regulation)

**Banking Compliance**:
- **AML/CFT** (Anti-Money Laundering/Countering Financing of Terrorism)

### Data Protection Controls:
The diagram shows how various controls flow through the data ecosystem:
- **Consent Management**
- **Identity Validation**
- **User Access Controls**
- **Data Management Risk training**
- **Third party data management**
- **Data Retention & Disposal**
- **Data Reconciliation**
- **Critical Data Elements**
- **Data Issue Capture**
- **Sensitive data usage**
- **Data deidentification monitoring**
- **Backup & Recovery tests**
- **Encryption applied**
- **Data Validation**
- **Metadata Management**
- **Data Quality**
- **Info Classification**

### User Interaction Flow:
**Acquire** → **Provide** → **Consume** → **Produce** through various channels (APPS, Cloud, Vendor) with comprehensive governance oversight.

---

## Slide 42: Data & Information Protection Blueprint

### Unified Enterprise Data Protection Blueprint:
A unified enterprise data protection blueprint streamlines, and modernises operations through coherent guiding practices, use cases, infrastructure, and tools.

### Benefits:
- Streamlines target state delivery by eliminating duplication
- Enables a flexible, modular ecosystem that enhances colleague experience
- Boosts productivity, ensures full data visibility, and strengthens threat defences

### Blueprint Architecture:
The diagram depicts how different components of the ecosystem must mould together to deliver the desired ecosystem, showing integrated protection across:
- **Visibility**, **Intelligence**, **Access**, **Protection**, **Recovery**
- **Information flow or API integration**
- **Agentless Built In Capabilities** (Email, Messaging, AI, Event Streams, APIs & Microservices, Cloud)
- **Integrated Data Protection** connecting to various management and protection services
- **Agent Integrations** (Endpoint, Network, Web)
- **Governance & Data Management** including automated discovery, classification, metadata management, AI/ML capability, and privacy management
- **Policy Lifecycle Management**
- **Event, Alert Triaging & Enrichment**
- **Automated Risk & Compliance Management**
- **Auto Remediation**
- **ZTA Driven Identity, Access, Entitlement & Secrets Management**
- **Cross Functional Capabilities** including Data Analytics & Strategy, Engineering Automation, Cloud & Platforms, FinCrime, Enterprise Information Management, Digital, Data & AI, Customer, Internet Banking & Customer XP, Operational Observability, Enterprise Interfaces, Workplace
- **Cyber Threat Intelligence, Detection & Response**

The blueprint shows comprehensive integration across data stores, movement & exchange, disposal & destruction, and encryption/transmission/masking & PII protection.

---

## Summary

This Target State Architecture document presents a comprehensive transformation roadmap for BNZ's Data & Information Protection capabilities. The document outlines a journey from reactive, cybersecurity-led approaches to a unified enterprise trust and resilience model that embeds governance, security, and technology across all platforms and teams.

Key themes include the shift from siloed operations to orchestrated governance, the implementation of zero-trust architectures, and the establishment of a Centre of Enablement to coordinate enterprise-wide protection efforts. The target state emphasizes automation, proactive threat detection, and the integration of data protection into the design and deployment lifecycle rather than as an afterthought.

The document demonstrates BNZ's commitment to enabling the organisation to "move faster, operate safer and lead with confidence in a digital first, regulated world" through a technology-enabled approach that bridges current capabilities with future enterprise trust and resilience objectives.