# Enterprise Information Management (EIM) – Target State Architecture Summary

## Document Overview
**Document:** Enterprise Information Management TSA - V3.pdf
**Author:** Hugh Walcott
**Date:** March 2025 v1.0
**Responsible Head of Architecture:** Tanya Bolema (Colleague Enablement and Data)
**Primary Platform Stakeholder:** Kate Skinner, Executive Data & Analytics

---

## Slide 1: Title Page
**Enterprise Information Management (EIM) – Target state Modernisation roadmap**

This document outlines BNZ's comprehensive strategy for modernizing enterprise information management capabilities, authored by Hugh Walcott in March 2025. The initiative is led by key stakeholders including Kate Skinner (Executive Data & Analytics), Michelle Maxwell (GM Colleague Enablement), and Roberta Prentice (Head of Data Risk), along with 9 GMs for platform dependencies.

## Slide 2: Table of Contents
**Document Structure Overview**

The TSA is organized into 8 main sections:
1. Executive Summary - Platform scope, definition and business purpose
2. Target State Summary - Scope, definition and value stream view
3. Risk Overview - Current state challenges, GRACE risks, and business impacts
4. Target Architectures/Platform - NAB alignment and invest/divest recommendations
5. Enterprise Context - Data flows, enterprise integration & strategic alignment
6. Simplification & Modernisation Roadmap - Roadmaps and tipping points
7. Platform Horizons - Technology transition from now to FY27
8. Appendices - Supporting documentation

## Slide 3: Executive Summary Section Header
**Strategic Context Introduction**

This section establishes the foundational understanding of EIM's role in BNZ's mission to be the best bank for all New Zealanders, emphasizing that information management is central to business growth and strategic implementation.

## Slide 4: EIM Platform Objectives and Roadmap
**Strategic Vision and Implementation Timeline**

**Key Technology Objectives:**
- Less manual document management with machine learning for classification and categorization
- Enterprise information services publishing Kafka business events for real-time insights
- Document migration from expensive collaborative storage to cheaper commodity storage
- Context-aware information services with basic, advanced, and intelligent search APIs
- Reuse of existing BNZ data product infrastructure for intelligent reporting
- Expert-crafted knowledge articles accessible to the right people at the right time
- Plug-and-play enterprise grade API for frontline and core banking systems
- Decommissioning of legacy document generation, distribution, and management infrastructure

**Proposed Journey (February 2025):**
1. **Strategy Development** - Target and EIM roadmap, GenAI auto-cataloguing experiments
2. **Enterprise Document Uplift** - DocMan uplift & enterpriseDocument API (Q4 FY25)
3. **Modernize Imaging and Scanning** - Replace Kofax with Abbyy Vantage (FY25 Q4)
4. **Intelligent Knowledge Transfer** - GenAI experiments over Te Kete (FY25 Q3+Q4)

**Target State Focus Areas:**
- **Scope & Context:** BIAN capability areas including Document Services, Archive Services, Information Reporting, Knowledge Management
- **Modernisation Approach:** Building on SmartComm and DocMan API foundations with intelligent categorization
- **NAB Alignment:** Strategic alignment on document services with divergence in operating models
- **Current State BMI View:** High number of legacy systems requiring modernization

## Slide 5: EIM Platform Target State Architecture Overview
**Technical Architecture and Implementation Strategy**

**Target State Overview:**
The architecture aims to build enterprise services for Document Generation with additional capabilities for Document Storage, Retrieval, Distribution and Lifecycle Management. Key components include:

1. **Consistent Experience:** Shared information services backbone for Customer, Colleague and Third Party platforms
2. **Capability Specific Services:** Generic information services tailored using domain-specific microservices
3. **Enterprise Services/APIs:** DocMan information services published as REST APIs on Kong gateway
4. **Intelligent Auto-cataloguing:** 100% auto-populated metadata using GenAI and Machine Learning
5. **Kafka Business Events:** Real-time business event publishing for document lifecycle events
6. **EIM Data Products:** Native integration between Kafka and BDH SnowFlake for analytics
7. **Plug-in-play Backend Services:** Integrated best-in-class third party services (Abbyy, SmartComm)

**Technical Focus Areas:**
- **Uplift Document Processing Practice:** Standards development, SmartComm cloud uplift, DocMan high availability
- **Align with Tech Stack Simplification:** Archive process support, bulk ingestion capabilities
- **Decommissioning Legacy EDM Systems:** Priority retirement of HotDocs, BI Publisher, MCF migration
- **Leverage ML and AI:** GenAI auto-categorization, CoPilot Studio experiments
- **Scaling and Growing Capability:** AWS EKS migration, 2+ billion row document database

**Challenges and Issues:**
- **Strategic Oversight:** Historical lack of enterprise-level management
- **Inconsistent Customer Experience:** Outdated and clunky experiences across all touchpoints
- **Non-Compliant:** Difficulty evidencing regulatory compliance and information disposal
- **Escalating Maintenance Costs:** Fragmented technologies with poor visibility and support

## Slide 6: Target State Summary Section Header
**Detailed Target State Vision**

This section provides comprehensive details on the target state architecture, capabilities, and implementation approach for the EIM platform transformation.

## Slide 7: EIM Definition & Scope
**Platform Scope and Capability Framework**

**Definition:** Coordinated activities and technologies for the management and operational use of enterprise information assets.

**Platform Users:** Colleagues, bankers, and customers through core banking and experience systems

**Capability Areas (shown in blue):**
- **Enterprise Digital Asset Management:** Database backup storage, digital document storage, physical document storage
- **Enterprise Document Service:** Document clustering, security and threat detection, predictive analytics, document distribution, document library, document generation, document storage and lifecycle management, e-signatures, imaging and scanning
- **Enterprise Records and Archive Management:** Records archiving, records reporting, records classification
- **Enterprise Knowledge & IP Service:** Enterprise architecture, knowledge exchange, intellectual property portfolio, management manual

The platform provides comprehensive capabilities for digital asset management, document services, records and archive management, and intellectual property and knowledge management.

## Slide 8: Platforms@BNZ Context
**Enterprise Platform Integration**

The EIM platform operates as one of the Business Enablement Platforms within BNZ's platform architecture, supporting:

**Upstream Dependencies (generates for):**
- Customer serving platforms (Customer Management, Product Origination, Account Management, Payments)
- Experience platforms (Customer Digital, Colleague Digital, Conversational Banking)

**Downstream Dependencies (consumes from):**
- Core technology platforms (Enterprise Security, Infrastructure Foundations, Enterprise Interfaces)
- Enabling technologies (Data & Information Protection, Engineering & Automation, Workplace Technology)

The platform serves as a critical enabler for information management across all customer touchpoints and internal operations, while depending on core infrastructure and security platforms for foundational capabilities.

## Slide 9: EIM Value Chain & Data Lifecycle
**Information Management Process Flow**

**Information Management Value Chain encompasses five key stages:**

1. **Capture:** Information assets manually crafted, automatically generated by systems, or obtained externally via document scanning and ingestion
2. **Distribution:** Information assets sent externally either physically (mail house) or electronically (electronic notification)
3. **Retention:** Information assets stored for collaboration (hot storage), reference (cold storage), or archived (very cold storage)
4. **Processing:** Information assets searched and retrieved with appropriate access controls and permissions
5. **Disposal:** Information assets lifecycle managed ensuring timely and defensible disposal

**Supporting Capabilities:**
- Archive Services (Database Backup Storage and Archival, Digital Document Storage and Archival, Physical Document Storage and Archival)
- Reporting, Analytics and Optimisation (Document Clustering, Security and Threat Detection, Predictive Analytics)
- Document Services (Document Distribution, Document Library, Document Generation, Document Storage and Lifecycle Management, E-Signatures, Imaging and Scanning)
- Records Management (Records Archiving, Records Reporting, Records Classification)
- Intellectual Property and Knowledge (Enterprise Architecture, Knowledge Exchange, Intellectual Property Portfolio, Management Manual)

## Slide 10: EIM Capability Model
**Comprehensive Capability Framework**

The EIM platform enables end-to-end value chain management through four enterprise platforms:

**Enterprise Document Service:** Document generation, storage, e-signing, imaging and distribution with reporting and analytics

**Enterprise Knowledge and IP Service:** Knowledge creation, maintenance and exchange capabilities with IP portfolio management

**Enterprise Records and Archive Management:** Records identification, classification, and management with archiving and disposal systems

**Digital Asset Management:** Management of digital 'documents' including images, brand assets, and design artifacts

**Supporting Capabilities span the entire information lifecycle:**
- Document Services: Generation, distribution, library, storage and lifecycle management
- Reporting, Analytics and Optimisation: Clustering, security detection, predictive analytics
- Records Management: Archiving, classification, reporting
- Intellectual Property and Knowledge: Architecture, exchange, portfolio management
- Archive Services: Database backup, digital and physical document storage

## Slide 11: EIM Capability Model with BMI Scores
**Business Modernization Index Assessment**

The capability model shows BMI scores across all EIM capabilities, indicating modernization priorities:

**BMI Score Legend:**
- 0 (best) to 200+ (highest modernization need)
- Color coding: Blue (low BMI) to Dark Blue/Black (high BMI requiring urgent modernization)

**Key Observations:**
- Many capabilities show high BMI scores (dark blue/black), indicating significant modernization needs
- Document Services platform shows mixed BMI scores with several high-priority modernization areas
- Knowledge Management capabilities generally show better BMI scores
- Records and Archive Management shows areas requiring urgent attention
- Archive Services shows critical modernization needs

The BMI visualization helps prioritize modernization efforts based on business criticality, architectural lifecycle, and modernization complexity.

## Slide 12: EIM Target State Summary
**Strategic Objectives and Key Benefits**

**Core Mission:** Information is central to developing and implementing strategies and processes, fundamental to business growth and being the best bank for all New Zealanders.

**Key Target State Components:**

**Headless Information Service:** 'Plug-and-play' enterprise grade API enabling frontline and core banking systems to easily store, retrieve, and manage information assets

**Event Based Architecture:** Enterprise information services publishing Kafka business events on all state changes for real-time insights and consumer support

**Enterprise Document Storage:** Migrate documents from expensive collaborative storage to cheaper commodity storage or long-term archive without breaking hyperlinks

**Enterprise Document Search:** Context-aware information services using basic, advanced, and intelligent search APIs for colleagues to access needed information

**Document Data Product:** Reuse existing BNZ data product infrastructure for intelligent reporting to continuously improve operating cost, performance, and EIM outcomes

**Multi-channel Knowledge:** Expertly crafted knowledge articles accessible by the right people, at the right time, in whatever channel they work for informed decision-making

**Auto-classify, Auto-categorise:** Less manual document management with machine learning to confidently classify and categorize documents, increasing productivity and embedding record compliance by design

**Modern and Simple Technology Stack:** Decommission legacy and unsupported document generation, distribution, and management infrastructure to reduce critical business risk and operating costs

## Slide 13: Risk Overview Section Header
**Current State Risk Assessment**

This section examines the current state challenges, business risks, and compliance issues that drive the need for EIM platform modernization.

## Slide 14: Current State Challenges and Issues
**Systemic Information Management Problems**

**Strategic Oversight Gap:** Information Management has been managed at requirements/project level without enterprise strategy, resulting in fragmented applications and approaches

**Inconsistent Customer Experience:** Outdated and clunky experiences for customers, colleagues and third parties across all document lifecycle stages, customer segments, banking products, and internal processes

**Compliance Challenges:** Difficulty evidencing regulatory compliance due to information access and disposal problems, with over-retention increasing personal information breach impact

**Escalating Maintenance Costs:** Poor visibility across fragmented technologies impacts business-critical process support and maintenance, with piecemeal improvements leading to duplication, inefficiencies and information bloat

These foundational issues demonstrate the urgent need for enterprise-level information management strategy and modernized technology platforms.

## Slide 15: Current State Architecture
**Complex Legacy Technology Landscape**

**System Inventory:**
- 53 EIM capabilities across platform layers
- 70+ IT Assets with IM capabilities or dependencies:
  - Document Generation (17 systems)
  - Document Management (16 systems)
  - Document Scanning (5 systems)
  - Document Library (11 systems)
  - Knowledge Transfer (16 systems)

**Storage Infrastructure:**
- 6 enterprise grade document storage repositories totaling over 200TB:
  - SharePoint2013 (37 TB)
  - SharePoint2019 (34 TB)
  - SharePoint Online (33 TB)
  - VRetrieve (~60 TB)
  - Network Drives (~40TB)
  - Cloud Storage (<1 TB) - target state

The architecture diagram shows the complexity of current state with applications and IT components arranged in platform layers, highlighting the need for significant simplification and modernization.

## Slide 16: Current State Architecture - Conceptual
**Storage Cost and Volume Analysis**

**Key Issues:**
- Over 100 TB of expensive SharePoint Online storage used for both operational and archive datasets
- Over 780 million files in third party archive (V-Retrieve) not covered by GIRP
- Over 180 million files in old network drives
- GIRP retention rules not consistently applied - estimated 50% of information could be deleted
- Cost/volume ratio is inverted (expensive storage holds more data than cost-effective options)

**Storage Tiers by Cost and Volume:**
- **SharePoint (High Cost, High Volume):** Frontline Experience, Lending Origination, C360, Workplace
- **V-Retrieve (Medium Cost, High Volume):** Core Transactional Systems
- **Network Drives (Low Cost, Medium Volume):** Branch Services, Core Data Systems
- **SaaS (Very Low Cost, Low Volume):** Customer serving and colleague enablement apps
- **Cloud (Target State, Very Low Cost, Low Volume):** Future state optimization

## Slide 17: Current State Business Risk
**Enterprise Risk Impact Assessment**

**Central Business Impact:** EIM is fundamental to business growth, improvement, and BNZ's mission. Without functional information management, the mission becomes impossible.

**Significant Enterprise Risk Impact:**
- **RSK-1300 Data Management:** Currently rated not effective
- **RSK-166 Data Loss:** Currently rated not effective
- **RSK-171 Cyber Compromise Risk:** Currently rated not effective

**Risk Mitigation Benefits:** EIM platform uplift will support risk improvement by enforcing records disposal, reducing information volume potentially available in data breach events.

**Capability Risk Mapping:** The platform architecture shows risk connections across Enterprise Document Service, Enterprise Knowledge & IP Service, and Enterprise Records and Archive Management, with specific risks mapped to capabilities including data loss, data management, and cyber compromise risks.

## Slide 18: Current State Business Risk - BMI Analysis
**BNZ Modernisation Index Assessment**

**BMI Framework:** Calculated using business criticality, architectural lifecycle and modernisation complexity - higher BMI indicates higher modernization need.

**Critical Findings:**
- Disproportionally large number of Exit status systems in Business Critical or Mission Critical categories
- Over 60% of systems have BMI greater than 120, considered technically material
- Document Services matrix shows most systems in Exit/Divest state with high BMI scores

**Risk Categories by BMI Score:**
- **>200 (Dark Blue):** Immediate modernization required
- **>160 (Navy Blue):** High priority modernization
- **>120 (Medium Blue):** Moderate priority modernization
- **>80 (Light Blue):** Lower priority modernization

**Systems Status Distribution:**
- **Exit (Red):** Multiple business-critical and mission-critical systems requiring immediate replacement
- **Contain (Yellow):** Systems requiring maintenance and eventual replacement
- **Encourage (Green):** Modern systems to be enhanced
- **Innovate (Teal):** New systems under development

## Slide 19: Current State Application Landscape
**Application Portfolio Assessment**

**Key Observations:**
- **Document Services:** 16 applications in Exit/Divest state, all with BMI scores over 100
- **Knowledge Management:** Relatively good BMI scores with few systems in poor state
- **Records Management:** 0 applications in encourage or healthy state

**Platform Status Overview:**
- **Enterprise Digital Asset Management:** Limited current capability, mostly placeholder systems
- **Enterprise Document Service:** Mix of systems across lifecycle states, many requiring modernization
- **Enterprise Knowledge & IP Service:** Better positioned with several systems in good health
- **Enterprise Records and Archive Management:** Significant modernization needs across all systems

**BMI Distribution:** Applications color-coded by lifecycle state and BMI score, showing clear modernization priorities and retirement candidates for platform simplification.

## Slide 20: Current State IT Component Landscape
**Infrastructure Component Analysis**

**Critical Infrastructure Issues:**
- Document services platform has 6 foundational IT components in Exit/Divest state
- Key infrastructure including SharePoint and File Cluster marked for retirement
- Color coding represents lifecycle state across all platform components

**Component Categories:**
- **Exit (Red):** Infrastructure requiring immediate replacement
- **Contain (Yellow):** Infrastructure requiring maintenance and planning for replacement
- **Encourage (Green):** Modern infrastructure to be enhanced
- **Innovate (Blue):** New infrastructure under development

**Platform Infrastructure Status:**
- **Enterprise Digital Asset Management:** Limited current infrastructure
- **Enterprise Document Service:** Mixed infrastructure health with critical components requiring modernization
- **Enterprise Knowledge & IP Service:** Stable infrastructure foundation
- **Enterprise Records and Archive Management:** Significant infrastructure modernization needs

## Slide 21: Target State Architectures Section Header
**Future State Design and Implementation**

This section details the comprehensive target state architecture designs for each EIM platform component and their integration patterns.

## Slide 22: Target State Architecture - Conceptual
**Storage Strategy Transformation**

**Primary Goals:**
1. More cloud and SaaS, less SharePoint Online
2. Shrink on-premise network storage by applying RecordPoint retention rules
3. Phase out V-Retrieve as long-term archive
4. Shrink SharePoint to SPO only for collaborative lifecycle phase documents
5. Introduce Zero carbon cloud storage tier for verified archives

**Storage Tier Strategy:**
- **Cloud (Large Volume, Low Cost):** 90% of all unstructured data storage
- **SaaS (Medium Volume, Low Cost):** Core Data Systems
- **Network Drives (Small Volume, Medium Cost):** Significantly reduced footprint
- **SharePoint (Small Volume, High Cost):** Workplace collaboration only
- **V-Retrieve (Phased Out):** Replaced by modern cloud archive solutions

**Cost Optimization:** Shift from expensive hot storage to cost-effective cold and very cold storage tiers while maintaining access and compliance requirements.

## Slide 23: NAB Current State Comparison
**Strategic Alignment Analysis**

**Convergent Points:**
- NAB operates two document service stacks (generation and management) served by NabOne MiniApp over SpringBoot microservice
- Both use API integrations to third party service providers
- BNZ TSA aligns with single enterprise API pattern for all document services
- Both support multi-context MiniApp approach rather than out-of-box user interfaces

**Divergent Points:**
- **Document Management:** NAB uses Alfresco; BNZ proposes building management logic into microservice layer to avoid vendor lock-in
- **Data Integration:** NAB uses Databricks; BNZ proposes Kafka for business events and BDH (Snowflake) for data products and BI analytics

**Architecture Patterns:**
- Document Management MiniApp with mobile customers, customer/banker interfaces, and prospects
- Document Generate MiniApp for bankers with form completion capabilities
- Shared microservice layer (DocMngt and DocGen) supporting multiple interfaces
- Integration with third-party services (BlueStart, DocuSign, Alfresco, Kofax, SmartComm)

## Slide 24: Target State Architecture - Logical
**Comprehensive Technical Architecture**

**Core Strategy:** Headless document management microservice providing foundational IM capabilities, extendable by capability-specific apps and microservices.

**Architecture Layers:**
- **Colleague UX:** Core Banking (CLR), C360/nCino, BNZGo, Product Onboarding, Customer Onboarding
- **Customer UX:** Digital Channels
- **Third Party UX:** Secure Document Exchange
- **Capability Specific Services/BFF Layer:** Core Ledger Correspondence, BNZ Home Loan Advisor, DocMan MiniApp, Customer Joining Generate Documents API, Documents MA
- **Microservice Layer:** DocMan Microservice with GenAI Auto-Cataloguing capability

**Enterprise Services:**
- **Authentication:** Microsoft Active Directory 2022, OAuth2, Kong Gateway
- **Infrastructure:** EKS on AWS with access controls
- **Information Services:** Storage (AWS S3), Metadata (NoSQL), Configuration (SQL), Generation (DocGen/SmartCOMM), E-Signing (DocuSign), Imaging (Document Scanning Target State), Distribution (vRetrieve Target State), Collaboration (Microsoft SharePoint Online), Knowledge (Semantic Knowledge Index)
- **Integration:** Confluent Kafka for events, BNZ Data Hub (BDH) for IM Data Products

## Slide 25: Enterprise Document Service Platform Section Header
**Document Services Target Architecture**

This section details the comprehensive target state architecture for the Enterprise Document Service Platform, covering all aspects of document lifecycle management.

## Slide 26: Document Generation Architecture
**SmartComm-Based Generation Platform**

**Investment Strategy:** Scale SmartComm document generation with secure AWS pure cloud environment, high volume batch processing for CLR, and API integration with Kafka event bus.

**Key Capabilities:**
- **Customer Information Asset Upload:** Automatically scanned and managed from ingestion
- **High Volume Processing:** Support for CLR batch requirements
- **Event Integration:** Kafka business events for generation activities
- **Secure Cloud Infrastructure:** Pure AWS cloud deployment

**Systems to Divest:**
1. HotDocs
2. BI Publisher
3. iText (eCredit, Apex and LOPi docs)
4. CustomerJoining/DocGenerateAPI
5. InterAct
6. IBIS Hardship Communications
7. vRetrieve (for doc generation)

**Architecture Components:**
- **Client Gateway:** C360/nCino, Customer Onboarding, Core Banking (CLR), Prospects and Third Parties, Customer Digital Channels
- **Capability Specific Services:** BNZ Lending Origination Document Orchestrator Service, Customer Joining Generate Documents API, Core Ledger Correspondence Management
- **Enterprise Services:** Kong Gateway integration
- **Microservice Layer:** DocMan Microservice, BNZ Docs Target State
- **Storage:** Document S3 Store, AWS Private Link, Templates storage
- **Event Integration:** Generation Topic, Kafka, Business Domain Events, BNZ Data Hub (BDH), Power BI Service

## Slide 27: Document Management Architecture
**Intelligent Headless Document Management**

**Core Strategy:** Intelligent headless document management system serving customer and colleague experience systems, agnostic to vendor storage/management technology.

**Key Features:**
- **Vendor Agnostic:** No dependency on specific storage or management technology
- **Legacy Replacement:** Replaces existing legacy document libraries
- **Multi-Channel Support:** Serves SaaS and internal applications
- **Intelligent Classification:** GenAI Auto-Classification Microservice for automated categorization

**Systems to Divest:**
1. MyCustomerFiles
2. DORIS (LendingDirect and LSD)
3. MyPeopleDocs
4. SharePoint 2013 and 2019
5. vRetrieve (for doc archive)
6. Correspondence WPS (IBM)
7. Legal Document Management
8. myMarketing

**Architecture Components:**
- **Channel Applications:** Product Onboarding (Lending), Core Banking/CLR, Customer Onboarding, Online Channels, Customer Document Master, BNZGo
- **Capability Specific Services:** BNZ Lending Origination Document Orchestrator Service, Core Ledger Correspondence Management (Placeholder), MyCustomerFiles Target State, Customer Correspondence Microservice, DocMan MiniApp
- **Enterprise Services:** Kong Gateway, WS-in Cloud Native Application Protection (CloudFlare platform)
- **Microservice Layer:** DocMan Microservice, BNZ Docs Target State, GenAI Auto-Classification Microservice
- **Storage Tiers:** Hot Storage (SharePoint Online), Cold Storage (vRetrieve Target State), Very Cold Storage (Zero-Carbon Storage)
- **Integration:** DocMngt Topic, Kafka, Business Domain Events, BNZ Data Hub (BDH), Power BI Service

## Slide 28: Document Distribution Architecture
**Multi-Channel Distribution Platform**

**Strategy:** Reuse existing authenticated channels with new mail-house and channel agnostic Distribute API as anticorruption layer between frontline systems and distribution providers.

**Key Capabilities:**
- **Physical and Digital Distribution:** Support for both distribution methods
- **State Change Publishing:** Business event bus integration for distribution lifecycle events
- **Channel Agnostic:** Works across multiple distribution channels
- **Address Management:** Handles distribution addressing and method selection

**Systems to Divest:**
- VRetrieve (current legacy state) - migrate to vRetrieve target state with modern integration
- Email for confidential document distribution
- DocuSign for third party and prospect document distribution

**Architecture Components:**
- **Source Systems:** C360, Core Banking/CLR, BNZGo
- **Request Processing:** Correspondence Request Command (Kafka), Customer Options
- **Service Layer:** BNZ Lending Origination Document Orchestrator Service, Core Ledger Correspondence Management, Customer Statement Preferences Service, DocMan MiniApp
- **Enterprise Services:** Kong Gateway with Distribute Authorization
- **Distribution Channels:**
  - Physical: DocMan Microservice → BNZ Docs Target State
  - Digital: B2B Gateway → Print & Post, Customer Portal (Authenticated Channel), Other Authenticated Channels
- **Integration:** Distribution Topic, Kafka, Business Domain Events, BNZ Data Hub (BDH), Power BI Service

## Slide 29: Digital Signatures Architecture
**Automated DocuSign Integration**

**Investment Strategy:** Automate DocuSign SaaS tooling, phase out manual uploads, implement tightly and loosely coupled connectors.

**Default Workflow:** Loosely coupled connector accessed by DocMan microservice, reducing integration complexity while maintaining anticorruption layer.

**Connector Types:**
- **Loosely Coupled:** Default pattern via DocMan microservice for most use cases
- **Tightly Coupled:** SaaS-to-SaaS connectors (like nCino-DocuSign) for specific integrations

**Systems to Divest:**
- Business processes requiring manual document uploads to DocuSign
- Business processes requiring wet signatures

**Architecture Components:**
- **Channel Applications:** C360, Workday (Channel Specific), Core Banking (CLR), Document Admin (MiniApps), Banker Workflows (Pega UW)
- **Integration Layer:** nCino-DocuSign Connector, Workday-DocuSign Connector (Proposed), Pega Platform, Capability Specific Services
- **Enterprise Services:** Service Gateway, Enterprise DocuSign Connector
- **Microservice:** DocMan Microservice → BNZ Docs Target State
- **Third Party Services:** B2B Gateway → DocuSign, DocGen (SmartCOMM)
- **Event Integration:** E-Signature Topic, Event Hub, Business Domain Events, E-Signature Event Listeners, BNZ Data Hub (BDH), Microsoft Power BI Service

## Slide 30: Imaging and Scanning Architecture
**Abbyy Vantage ML-Powered Scanning**

**Investment Strategy:** Abbyy Vantage SaaS as target state document scanner with advanced machine learning capabilities.

**Input Methods:**
- Manual upload
- SPO connector
- MS Graph to BNZ O365 (email)
- Smart Printers with Abbyy ML skills

**Processing Options:**
- **Advanced ML:** Abbyy Vantage for complex document processing
- **Simple Automation:** Blue Prism and Adobe stack for basic scanning tasks
- **Physical Scanning:** Smart Printers modified to leverage Abbyy ML before pushing to SPO

**Systems to Divest:**
- Kofax
- Lending Services Doc Prep (Pega)

**Architecture Components:**
- **Input Sources:** Trade Finance Inbox, Lending Services Documents (2k+/day), Legal Docs (paper and images uploaded to SPO folders), KiwiSaver Wet Signatures (Withdraw Process), Demand Payments
- **Processing Layer:** Smart Printer, Lending Originator Document Orchestrator, Pega Platform, Blue Prism
- **Enterprise Services:** API Gateway, ACLess REST API
- **Microservice:** DocMan Microservice → BNZ Docs Target State
- **Integration:** DocImage Topic, Event Hub, Business Domain Events, BNZ Data Hub (BDH), Power BI Service
- **Storage:** BNZ Office365, SharePoint Online, Document Scanning Target State

## Slide 31: EDM User Interface
**Integrated Customer and Colleague Experience**

**Strategy:** Follow NAB's approach with superior integrated experience for document services through BnzGO DocMan MiniApp.

**Capability Coverage:**
- **Customer Care:** Customer Case, Customer Case Management, Servicing Order
- **Loans and Deposits:** Consumer Loan, Merchandising Loan, Syndicated Loan, Term Deposit, Corporate Loan, Loan, Mortgage Loan
- **Cross Channel:** Customer Workflows
- **Document Services:** Document Distribution, Document Storage and Lifecycle Management, Document Library, E-Signatures, Document Generation

**Integration Flow:**
- **Enterprise Document Management:** DocMan MiniApp as central hub
- **Domain-Specific Services:** BNZ C360-nCino, BNZ Lending Origination Document Orchestrator Service, Lending DocGen BFF, Smart IQ
- **Document Services:** Multi-tiered Storage, vRetrieve Target State, DocuSign
- **Data Services:** MyLending, eLend, Colleague Data API (C3X) for document validation

**Systems to Divest:**
- MyCustomerFiles
- Hot Docs (priority)
- SharePoint 2013/2019

## Slide 32: Enterprise Knowledge & IP Service Platform Section Header
**Knowledge Management Target Architecture**

This section outlines the target state architecture for Enterprise Knowledge and IP Service Platform, focusing on knowledge creation, maintenance, exchange, and intellectual property management.

## Slide 33: Knowledge & IP Management Architecture
**Comprehensive Knowledge Platform Enhancement**

**Improvement Areas Identified:**
1. **Platform Development:** Knowledge platform development for better content curation and sharing
2. **GenAI Integration:** Chatbot channel for enhanced knowledge access
3. **Notification Enhancement:** Improved knowledge notifications and alerts
4. **Content Creation:** Proactive knowledge creation processes
5. **Analytics and Reporting:** Better usage tracking and trend analysis
6. **Productivity Analytics:** Turn insights into bank-wide productivity gains

**Systems to Divest:**
- Atlassian Confluence (as knowledge base)
- SharePoint Online (as knowledge base)
- Te Kete (as analytical and management tool)

**Architecture Components:**
- **User Channels:** Public, Customers, Colleagues, Technology, Partners
- **Gateway Layer:** Public Gateway, Client Gateway
- **Integration Services:** Salesforce CMS, Aprach Chat BOT, Mercury (SPO), Front line systems (BMGo MiniApps), Te Kete, SAP Cherwell HR, DIY Knowledge Portal, Portent Quality CAST (staging PROD)
- **Knowledge Platform:** Avalon, Semantic Knowledge Index with Knowledge Semantic Layer
- **Data Integration:** BNZ Data Hub (BDH), DocMan Microservice, BNZ Enterprise Search, DocMan API
- **Supporting Services:** Prompt Library, Create + Manage Process, Knowledge Data Identified, Power BI Service, KnowledgeMngr Topic, People Topic, Business Domain Events

**Themes for Enhancement:**
- Live chatbot for conversational interfaces in KM resources
- SLT Integration with banking systems
- BNZ Discovery for terms and definitions
- Creation process governance
- Central knowledge data
- Enhanced content and continuous improvement

## Slide 34: Enterprise Records and Archive Management Platform Section Header
**Records and Archive Management Target Architecture**

This section details the target state architecture for Enterprise Records and Archive Management Platform, covering records lifecycle management and archive services.

## Slide 35: Records Management Architecture
**Automated Records Classification and Lifecycle Management**

**Strategy:** Invest in automation of records management using intelligent classification and categorization across all document libraries (on-premise, third-party, private cloud, SaaS).

**Scope Coverage:**
- **33 Document Types (3M/month):** Across multiple business areas including MCF, MyPeopleDocs, DORIS, Mercury13, Mercury, Legal, KiwiSaver, Wealth, Informatics, RSA, IBIS, Termenos
- **Classification Approach:** Human classification for legacy systems, Records365 for network drives, GenAI Auto-Classification Microservice for modern systems

**Systems to Contain:**
- RecordPoint (for SPO and network drives)
- SharePoint Online (as metadata enforcement point)

**Architecture Components:**
- **Document Sources:** SharePoint (2013, 2019 Azure, SPO Cloud), Network Drives, V-Retrieve, Cloud/SaaS systems
- **Classification Services:** Human classification, Records365, GenAI Auto-Classification Microservice → BNZ Docs Target State
- **Metadata Management:** NoSQL Metadata storage
- **Integration:** Real-time classification and lifecycle management across all repositories

**Geographic and Compliance Coverage:** 33 document types across different retention schedules and compliance requirements, with automated classification enabling full lifecycle governance.

## Slide 36: Archive Management Architecture
**Headless Enterprise Archive Solution**

**Investment Strategy:** Headless enterprise archive solution for structured/unstructured information from retired or soon-to-be-deprecated systems.

**Key Features:**
- **Tiered Storage Model:** Optimal storage speed and cost for different access patterns
- **Lifecycle Integration:** Automated lifecycle management for all data assets
- **System Archive Support:** Handles both current operational and legacy system archives

**Systems to Divest:**
- Tech-stack Simplification systems (23 identified for archive)
- SharePoint Online as archive repository
- vRetrieve as operational archive repository
- CMOD (Content Management On Demand) archive repository
- Imprint (cheque image archive)
- Pega UW archives
- Assist forms (archives)

**Architecture Components:**
- **Input Sources:** Unstructured Documents, Database, Data Movement Ecosystem (DaMe)
- **Processing:** Document Archive Ecosystem (DaVE), DocMan MiniApp
- **Enterprise Services:** Kong Gateway
- **Microservice:** DocMan Microservice with Archive Business Event publishing
- **Storage Tiers:**
  - **Warm Storage:** AWS S3 Storage
  - **Cold Storage:** AWS S3 Storage
  - **Very Cold Storage:** Zero-Carbon Storage
- **Integration:** DocMngt Topic, Kafka, Business Domain Events, BNZ Data Hub (BDH), Power BI Service
- **User Interface:** Search Archives, Mongo Compass for archived data reports and graphQL query capabilities

## Slide 37: Enterprise Digital Asset Management Platform Section Header
**Digital Asset Management Target Architecture**

This section outlines the target state architecture for Enterprise Digital Asset Management Platform, focusing on centralized management of digital assets across all channels.

## Slide 38: Digital Asset Management Architecture
**Headless Content Management System**

**Investment Strategy:** Headless content management system offering centralized Digital Asset Management (DAM) for public website and BNZ business applications (internal or SaaS).

**Key Capabilities:**
- **Multi-Channel Publishing:** Scalable, consistent workflow for images, letters, legal text, signatures, banners, page blocks, CSS across multiple channels, devices and languages
- **Centralized Management:** Single source of truth for all digital assets
- **API-Driven:** Headless architecture enabling flexible content delivery

**Systems to Contain:**
- SilverStripe (as CMS) - at least until MarTech completes market analysis/RFP

**Architecture Components:**
- **Consumer Applications:** WWW (public website), BNZ SaaS Applications, BNZ Internal Applications
- **API Layer:** Internal Gateway, CMS API
- **Content Management:** SilverStripe CMS, Headless content management
- **Asset Management:** Content Producers → Digital Asset Management
- **Integration:** Seamless connection between traditional CMS and modern headless content management

The architecture enables content creators to manage digital assets centrally while supporting diverse consumption patterns across web, mobile, and application interfaces.

## Slide 39: Enterprise Context Section Header
**Strategic Integration and Alignment**

This section examines how the EIM platform integrates within BNZ's broader enterprise context, including strategic alignment, data flows, and cross-platform dependencies.

## Slide 40: FY25 Initiatives and Objectives
**Strategic Initiative Mapping**

**Technology Strategy Objectives:**
- Modernise and Simplify
- Agile and Adaptable
- Platform Mindset
- Identify Digital
- Resilient, Secure and Safe

**Corporate Strategy Objectives:**
- Modernise our Technology and Operating Model
- Accelerate Digital Customer Experience
- Radically Simplify products, policies, processes and systems
- Perfect the Banking Basics

**FY25 Contributors (Programs):**
- EIM Program FY25
- Core Ledger Replacement & Management (Phase 3)
- Document Production & Provisioning Platform
- 1.0 Zero Trust Network Architecture Programme
- Reimagine Consumer Lending
- Identity Integration Programme
- Generative AI Platform
- TSS - Sales Conversation Hub & Compensation Platform

**FY25 Consumers (Programs):**
- Digital Programme (Customer)
- Customer360
- People Decision Hub, Employee Decision Hub (Workforce)
- Marketplace Response Programme
- Support for Delivery of Customer Decision Hub, Workforce Decision Hub

**Capability Areas:**
- Document Services: Document Generation, Imaging and Scanning, Document Storage and Lifecycle Management, E-Signatures, Document Distribution, Document Library
- Reporting, Analytics and Optimisation: Document Clustering by Subject and Dimension, Security and Threat Detection, Predictive Analytics and Insights
- Archive Services: Database Backup Storage and Archival, Digital Document Storage and Archival, Physical Document Storage and Archival
- Records Management: Records Archiving, Records Classification, Records Reporting
- Intellectual Property and Knowledge: Enterprise Architecture, Knowledge Exchange, Intellectual Property Portfolio, Management Manual

## Slide 41: Platform Data Flows and Integration
**Enterprise Integration Architecture**

**EIM Platform Integration:** Exposes two APIs (one active, one in innovate state) and publishes 5 business event topics (Kafka events).

**Data Flow Pattern:** Documents generated upstream, then ingested for downstream consumers.

**Upstream Systems (Generate):**
- Lending Origination incl Customer 360: Generate, Search and Retrieve
- Core Banking Ledger: Generate Statements, TDs etc.
- Artificial Intelligence: Intelligent Auto-cataloguing, People Records
- People & Culture: People Records
- Colleague Digital incl Customer 360: Knowledge

**EIM Platform Components:**
- **Enterprise Information Management**
- **Enterprise Document Service:** Document Generation Business Events, Document Lifecycle Management
- **Enterprise Records and Archive Management:** Query archive, Knowledge Catalogue
- **Enterprise Knowledge & IP Service:** Knowledge
- **Enterprise Digital Asset Management:** Upload assets

**Downstream Systems (Consume):**
- Lending Origination incl Customer 360: Search, retrieve, load documents
- Customer Onboarding: Search, retrieve customer documents
- Customer Digital incl Website: View my documents
- Customer Master: Document references
- Card Issuing & Mgt: Card applications
- Customer Engagement: View customer documents
- Digital Experience Integration Layer: Cross-channel document access
- Enterprise Data & Information Protection: Compliance and security

**Data Products:** Generated from each Kafka topic (e.g., DocGen topic seeds DocumentGenerated data product in BDH).

## Slide 42: Technology Strategy Alignment
**Five Pillar Strategic Alignment**

**Modernise and Simplify:**
- Replace fragmented, broken, unsupported applications (BI Publisher, HotDocs, iText, Kofax, MCF, vRetrieve) with enterprise grade EIM service
- SpringBoot microservices for full IM value chain operations
- Migration from expensive vendor lock-in to multi-tiered commodity cloud storage
- Intelligent automated (GenAI) document classification and categorization

**Agile and Adaptable:**
- Loosely coupled microservices built by small agile teams using industrialized recipes
- MiniApps for Lending Docs, doc admin, MCF target state
- SpringBoot microservice (DocMan)
- Event-Driven Architecture using Kafka
- Kong Enterprise Services for REST API endpoints

**Platform Mindset:**
- Suite of enterprise platforms with dedicated support and operating model
- Enterprise Document Services (Kevin Dittmer), Enterprise Knowledge and IP Services (Kate Alison-Tomlin), Enterprise Records and Archive Management (Kevin Dittmer), Enterprise Digital Asset Management (new platform)
- Federated onboarding of IM workflows
- Capability maturity uplift focus

**Resilient, Secure and Safe:**
- SmartComm pure cloud for more resilient document generation
- Core information protection capabilities (virus scanning, malware detection, PCI controls) baked into DocMan microservice
- Automatic document classification enabling full lifecycle governance
- Move to more secure and reliable infrastructure

**Deeply Digital:**
- New shared DocuSign API connector (target: 90% automatic vs current 90% manual)
- GenAI for automatic document classification and categorization
- Growing SmartComm template capability for system-generated customer communications
- Enhanced digital experiences across document lifecycle

## Slide 43: Simplification & Modernisation Roadmap Section Header
**Implementation Timeline and Delivery Strategy**

This section outlines the comprehensive roadmap for EIM platform modernization, including timelines, dependencies, and delivery milestones.

## Slide 44: Roadmap - Information Services
**Strategic Workstream Timeline**

**FY24 Q4 Foundations:**
- EIM Program Delivery Plan
- IM Market Scan
- DocMan Detail Designs

**FY25 Core Delivery:**
- **Strategy:** IM UX, UI, and GenAI Roadmaps
- **Knowledge Management:** Te Kete OpenAI Chatbot, Data Product (Knowledge)
- **Records Management:** SPO + Drives (RecordPoint), IM LLM Experiment, GenAI Auto-Classification Microservice
- **Analytics and Reporting:** BDH Foundations, Data Product (Generate), Data Product (Distribute), Data Product (Lifecycle), Data Product (E-Signature)
- **Archive Services:** Document Archive Process, Tiered Archive Storage

**FY26 Advanced Capabilities:**
- **Knowledge Management:** Knowledge Platform, Knowledge API
- **Records Management:** MyCustomerFiles/vRetrieve exit, SaaS/Cloud migration
- **Archive Services:** Archive Retrieval MiniApp

**Future State (>FY29):**
- Scaled enterprise information services
- Complete legacy system retirement
- Intelligent information management capabilities

**Program Classifications:**
- EIM Program/Strategy WS (Blue)
- EIM FY26 (Dark Blue)
- Enterprise Data Products (Orange)
- TechStack Simplification (Green)
- CLR/EIM workstream (Red)
- Data Program/GenAI (Yellow)
- Not Funded? (Gray)

## Slide 45: Roadmap - EIM Document Services
**Document Services Implementation Timeline**

**FY24 Q4:**
- SmartComm Purecloud Uplift
- Abbyy POC

**FY25 Core Implementation:**
- **Generation:** Batch capability (20% improvement), Secure Upload POC, Scale to 1M/month
- **Store and Retrieve:** DocMan Ingest and Retrieve, Basic Search, Metadata Index (NoSQL), Lending DocMan MiniApp
- **Lifecycle Management:** DocMan MicroService
- **Distribute:** Distribute via Post (Datam)
- **Imaging:** EIM Imaging Service
- **Digital Signatures:** EIM DocuSign Connector

**FY26 Advanced Features:**
- **Generation:** Secure Upload Portal, Scale to 4M+/month
- **Store and Retrieve:** Advanced Search, DocMan MiniApp
- **Lifecycle Management:** BNZ Docs (Target State), GenAI Auto-Classification Microservice
- **Distribute:** Distribute via Auth Channels
- **Imaging:** Automate Imaging Workflows, Data Product (Imaging)
- **Digital Signatures:** Automate Signature Workflows

**Future State (>FY29):**
- **Store and Retrieve:** Intelligent Search
- Full platform scaling and optimization

**Supporting Programs:**
- EIM Program/DocMan WS (Blue)
- EIM Program/Imaging WS (Teal)
- EIM FY26 (Dark Blue)
- Reimagine Consumer Lending (Yellow)
- CLR Program (Green)
- C360 Program (Orange)
- Data Protection (Purple)
- Data Program/GenAI (Orange)
- Not Funded? (Gray)

## Slide 46: Roadmap - By Platform
**Platform-Specific Implementation Timeline**

**EIM Platform Strategy:**
- **FY24 Q4:** EIM Program Delivery Plan, IM Market Scan, DocMan Detail Designs
- **FY25:** Business Analysis: UX, UI, and GenAI, EIM FY26 Business Case/Program Delivery Plan
- **FY26:** MyCustomerFiles/vRetrieve Exit

**Enterprise Knowledge Management:**
- **FY25:** Te Kete OpenAI Chatbot, Data Product (Knowledge)
- **FY26:** Knowledge Platform, Knowledge API

**Enterprise Records & Archives Management:**
- **FY25:** Document Archive Process, IM LLM Experiment, GenAI Auto-Classification Microservice, Tiered Archive Storage
- **FY26:** Archive Retrieval MiniApp, BNZ Docs (Target State)

**Enterprise Document Services:**
- **FY25:** DocMan MicroService, Basic Search, Batch Generate, Abbyy POC, Metadata Index (NoSQL), Data Product (Generate), EIM Imaging Service
- **FY26:** DocMan MiniApp, Advanced Search, Data Product (Distribute), Data Product (Imaging)

**Enterprise Digital Asset Management:**
- **FY25:** MarTech DAM RFP
- **FY26:** DAM/CMS Implementation

**Program Coordination:**
- EIM Program/Strategy WS (Blue)
- EIM Program/DocMan Dev (Teal)
- EIM Program/Imaging (Dark Teal)
- EIM FY26 (Dark Blue)
- Enterprise Data Products (Orange)
- TechStack Simplification (Green)
- CLR/EIM workstream (Red)
- Data Program/GenAI (Yellow)
- Not Funded? (Gray)

## Slide 47: Roadmap - Document Management Applications
**Application Lifecycle Roadmap**

**Visual Roadmap:** Up-to-date visualizations available in LeanIX showing transition timeline for each application component.

**Banker Experience & Platforms:**
- BI Publisher, Broker (Loan) Portal, DocumentPreparation Microservice, DORIS, HotDocs, InterAct, Lending Direct, Lending Document Management Microservice, Lending Services Doc prep (PEGA UW), Salesforce "Classic" CRM, Salesforce Financial Services Cloud, Statementing, Stockletters

**Transactions & Investments:**
- Boardvantage, DocGen (SmartCOMM), Document Scanning Target State, DocuSign, Kofax, Legal Document Management, vRetrieve Target State, DGen (RPA), IBIS Hardship Communication, MyCustomerFiles, MyCustomerFiles Target State, Sharepoint BNZ Docs

**Workplace:**
- [Applications in workplace category]

**Corporate Services:**
- myMarketing, MyPeopleDocuments, MyPeopleDocuments (Manage Access), SharePoint (on Azure) - MyPeopleDocuments, Customer Information Collection Target State, Customer Joining Generate Documents API, Document Generation API, Internet Banking Documents Service

**Customer, Onboarding & Identity, Digital Channels:**
- [Applications in this category]

**Digital Asset and Archive Management platforms** shown separately with their own transition timeline.

**Legend:**
- Plan (Gray)
- Phase In (Blue)
- Active (Green)
- Phase Out (Yellow)
- Retired (Red)

## Slide 48: Roadmap Modernisation Tipping Point
**Platform Transformation Metrics**

**Document Services Tipping Point:** Defined as the point where more assets are in 'Encourage' state than in 'Exit' state.

**Current State (FY25):**
- 32 applications total
- 15 applications in Exit state
- 7 applications in Encourage state

**Transformation Timeline:**
- **2025:** Starting point with high Exit applications (15), low Encourage applications (7)
- **2026:** Tipping point achieved - Exit and Encourage applications intersect at approximately 8 applications each
- **2027-2029:** Continued improvement with Encourage applications growing to 12, Exit applications reducing to 3

**Asset Lifecycle Trends:**
- **Exit (Blue Line):** Decreasing from 15 to 3 applications over 5 years
- **Contain (Orange Line):** Relatively stable at 7-8 applications
- **Encourage (Green Line):** Growing from 7 to 12 applications
- **Innovate (Light Blue Line):** Stable at 3-4 applications
- **Total Assets (Dotted Line):** Decreasing from 32 to approximately 15 applications

**Simplification Impact:** Within 5 years, EIM platform will support half the number of IT assets while providing enhanced capabilities and reduced risk.

## Slide 49: Platform Horizons Section Header
**Multi-Year Platform Evolution Strategy**

This section outlines the platform evolution strategy across multiple financial years, showing the progression from basic capabilities to advanced intelligent services.

## Slide 50: Roadmap - EIM Platform Horizons
**Three-Horizon Implementation Strategy**

**Horizon 1 (FY25-FY26): Basic Document Services**
- **CLR + C360 Delivery Plan** (Basic doc services)
- **EIM Business Case** development
- Specific CLR and C360 funded EIM services
- Limited generic EIM capability delivery

**Horizon 2 (FY26-FY27): Advanced Document Services**
- **EIM Program Delivery (Phase 2)** (Advanced doc services)
- **EIM Business Case (refresh)**
- Generic EIM services
- Advanced search capabilities
- MCF+DORIS migration
- 3rd party portal implementation

**Horizon 3 (FY27-FY29+): Intelligent Document Services**
- **EIM Program (Phase 3)** (Intelligent doc services, including knowledge)
- Scaled EIM services
- Intelligent search capabilities
- V-Retrieve migration completed
- Legacy IM systems removal

**Strategic Milestones:**
- **FY25:** Foundation building with basic services
- **FY26:** Capability expansion and advanced features
- **FY27:** Intelligence and automation integration
- **FY28+:** Full platform maturity and optimization

Each horizon builds upon the previous, ensuring progressive capability enhancement while maintaining operational continuity and stakeholder value delivery.

## Slide 51: Appendices Section Header
**Supporting Documentation and References**

This section contains additional supporting materials, technical details, and reference information for the EIM Target State Architecture.

## Slide 52: APRA Checklist
**Regulatory Compliance Framework**

**Target State Architecture Requirements:**

**APRA Feedback Considerations:**
- Initial roadmaps have been drafted for certain platforms but are fragmented without complete visibility
- No enterprise technology roadmap includes key milestones and timeframes with sequencing and dependencies in planning process
- Reporting and governance mechanism for technology transformation initiatives needs establishment
- BNZ Modernisation Index (BMI) effectiveness in incentivizing and driving progress requires validation

**Deliverable Requirements:**
- Develop technology modernisation roadmaps at enterprise and divisional level
- Provide visibility of total work to be undertaken with target state, accountabilities, feasible timelines, interdependencies and sequencing
- Establish funding model to support program execution and governance/reporting mechanism to monitor progress

**Implementation Actions:**
1. **Deliver approved target state architectures for all 52 Platforms (45 remaining)**
   - Review target state architecture contents for APRA satisfaction and NAB alignment
   - Prioritise Platforms based on BMI of assets, reprioritise or reallocate lower priority work
   - Enlist internal and external resource assistance to complete

2. **Establish Strategic Architecture Authority to govern and monitor progress against TSAs**
   - Due: 30 June (as specified in deliverable requirements)

**Compliance Framework Coverage:**
1. Platform Scope & Definition ✓
2. Platform Vision - Target state summary ✓
3. Context: Value chain-stream, Capability map, Interdependencies, Stakeholder map ✓
4. Current state: Architecture, Landscape (LeanIX) + BMI, Challenges and GRACE risks ✓
5. Target state: Overview, Strategic alignment, Modernisation journey, Simplification roadmap ✓

---

*This document provides a comprehensive summary of BNZ's Enterprise Information Management Target State Architecture, covering strategic objectives, current state challenges, target state vision, and detailed implementation roadmaps across all EIM platform components.*