# Enterprise Information Management (EIM) - Target State Architecture

**Modernisation Roadmap**

| Attribute | Value |
|-----------|-------|
| Author | Hugh Walcott |
| Date Produced & Version | March 2025 v1.0 |
| Responsible Head of Architecture | Tanya Bolema (Colleague Enablement and Data) |
| Primary Platform Stakeholder | Kate Skinner, Executive Data & Analytics |
| Other Stakeholders | Michelle Maxwell (GM Colleague Enablement), Roberta Prentice (Head of Data Risk), and 9 GMs for platform dependencies |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Target State Summary](#2-target-state-summary)
3. [Risk Overview](#3-risk-overview)
4. [Target Architectures / Platform](#4-target-architectures--platform)
5. [Enterprise Context](#5-enterprise-context)
6. [Simplification & Modernisation Roadmap](#6-simplification--modernisation-roadmap)
7. [Platform Horizons](#7-platform-horizons)
8. [Appendices](#8-appendices)

---

## 1. Executive Summary

### Enterprise Information Management (EIM) Platform

Our information is what informs how we develop and implement our overall strategies and related processes. It is at the **heart of business growth and improvement**, and central to our mission to be the best bank for all New Zealanders.

### EIM Platform Objectives

| Objective | Description |
|-----------|-------------|
| **Less manual document management** | More machine learning to confidently classify and categorise documents, increasing productivity and embed record compliance by design |
| **Kafka business events** | Enterprise information services that publish Kafka business events on all state changes, so we can gain insights and help producers or consumers in near real-time |
| **Cheaper storage** | Migrate documents from expensive collaborative storage to cheaper commodity storage or long-term archive, without breaking hyperlinks |
| **Context-aware search** | Build context aware information services from anywhere using basic, advanced, and intelligent search APIs, so colleagues and customers can get the information they need, where and when they need it |
| **Intelligent reporting** | Reuse existing BNZ data product infrastructure to build intelligent reporting so we can continuously improve operating cost, performance, and EIM outcomes |
| **Knowledge articles** | Knowledge articles to be expertly crafted, and accessible by the right people, at the right time, in whatever channel they work so they can make informed decisions |
| **Plug-and-play API** | Enterprise grade API enabling frontline and core banking systems to more easily store, retrieve, and appropriately manage their information assets |
| **Decommission legacy** | Decommission legacy and unsupported document generation, distribution, and management infrastructure, to reduce critical business risk and operating costs |

### Scope & Context

EIM Platform coordinates the resources and people needed for the information value chain supported by the following BIAN capability areas:
- Document Services
- Archive Services
- Information Reporting, Optimisation and Analytics
- Knowledge Management and Intellectual Property

### Modernisation Approach

The approach is to build on the foundations laid by SmartComm and the DocMan API pattern, adding intelligent categorisation and GIRP compliance, so attracting document producers and consumers to our enterprise service.

- **FY25**: Focus on the basic - Document Generation, Storage, and Distribution
- **FY26**: Adds the intelligence and Lifecycle Management
- **FY27**: Scales this across the bank absorbing legacy workflows

### NAB Alignment

In general, BNZ and NAB align on document services strategy, including building MiniApps and Microservices over third party apps, and publishing EDM Data Products as reusable data assets.

**Key areas of divergence:**
- Operating model (BNZ intends to automate more using GenAI)
- Use of Kafka for business events and Snowflake for EIM data products

### Current State BMI View

Parts of the Information Management ecosystem are in pretty good shape (knowledge management), but others are a risk to critical business systems and customer value chains. The BNZ Modernisation Index reflects the high number of legacy (Contain & Exit) assets with low architectural & functional fitness. Achieving target state drastically reduces BMI of these high-risk areas.

### Proposed Roadmap Journey (February 2025)

1. **Strategy**: Develop target and EIM roadmap, experiment with GenAI auto-cataloguing capabilities (Business case FY25 Q3-Q4)
2. **Enterprise Document Uplift**: Support inflight change for generate, store, search, retrieve and distribute - DocMan uplift & enterpriseDocument API Q4 FY25
3. **Modernize Imaging and Scanning**: Replace Kofax system to address automation gap in load disbursements - Abbyy Vantage release FY25 Q4
4. **Intelligent Knowledge Transfer**: Experiment with GenAI over Te Kete for context-aware 'best fit' knowledge services (Experiments in FY25 Q3 + Q4)
5. **Scale delivery** of headless enterprise information services for colleagues, customer and third parties

---

## EIM Platform - Target State Architecture Overview

This target state aims to build on existing enterprise services available for Document Generation, and added additional capability for **Document Storage, Retrieval, Distribution and Lifecycle Management** this financial year, then the following year add additional capabilities for **Artificial Intelligence for Metadata Management, Information Data Products for IM quality control and governance**.

### Key Points

1. **Consistent experience**: Customer, Colleague and Third Party experience platforms backed by a shared information services backbone
2. **Capability specific...only where needed**: Generic information services are tailored into customer workflows using domain specific microservices
3. **Enterprise services / APIs**: DocMan's information services documented and published as REST APIs on our internal Kong gateway
4. **Intelligent auto-cataloguing / classifications**: No manual completion of annoying metadata fields; aiming for 100% auto-populated using GenAI and Machine Learning
5. **Kafka business events**: Real-time business event published for clients of any state change document, scanning, e-signing, distribution and lifecycle events
6. **EIM data products**: Native integration between Kafka and BDH SnowFlake for EIM system analytics and performance metrics
7. **Plug-in-play backend information services**: Integrated best-in-class third party document services such as Abby for scanning and imaging, and SmartComm for document generation

### Challenges and Issues

| Challenge | Description |
|-----------|-------------|
| **Strategic Oversight** | Historically, Information Management has not been managed at an enterprise or strategic level but at a requirements or project level, without an end-to-end business strategy to guide investment, resulting in a plethora of applications and approaches |
| **Inconsistent Customer Experience** | CX is inconsistent, outdated and clunky for customers, colleagues and third parties across all stages of the document lifecycle and across all customer segments, banking products, and internal processes such as staff hiring |
| **Non-Compliant** | Challenging to evidence compliance with our regulatory obligations, due to difficulty in accessing and disposing of information. Over-retention of information increasing potential impact of personal information breaches |
| **Escalating Maintenance Costs** | Visibility across the fragmented and disconnected technologies used is opaque and poorly understood, impacting support and maintenance of business-critical processes. Improvements to date have been piecemeal through point solutions by customer segment or banking product, leading to duplication, inefficiencies and information bloat |

### Technical Focus Areas

| Focus Area | Activities |
|------------|------------|
| **Uplift document processing practice** | Develop standards to establish and uplift Information management practices across the data lifecycle; Uplift SmartComm to pure cloud to support batch processing; Uplift DocMan to high availability multi-cloud infrastructure |
| **Align with Tech Stack Simplification** | Support the new archive process for the data on our legacy applications, enabling them to be decommissioned faster; Uplift DocMan for the bulk ingestion of millions of system archival documents |
| **Decommissioning legacy EDM systems** | Prioritise the decommission of legacy Document Generation systems such as HotDocs and BI Publisher; Prepare for the migration of MCF to EDM; Move information assets from expensive on-prem and SPO storage to the cloud |
| **Leverage ML and AI where it counts** | Experiment with GenAI for Auto-Categorisation; Experiment with CoPilot Studio and open-source orchestrators for improved Te Kete knowledge transfer |
| **Scaling and growing capability** | Migration of core EDM infrastructure to scalable AWS EKS; Provision of 2+ billion row document database; Release v1 of the EnterpriseDocuments API |

---

## 2. Target State Summary

### EIM - Definition & Scope

**Definition**: Coordinated activities and technologies for the management and operational use of enterprise information assets.

**Who uses the EIM Platform?**
- Colleagues, bankers, and customers
- Core banking and experience systems

**What capabilities does it provide for?**
Capabilities for digital asset management, document services, records and archive management, intellectual property and knowledge.

### EIM Platform Capabilities

| Platform | Capabilities |
|----------|--------------|
| **Enterprise Information Management** | Enterprise Digital Asset Management, Enterprise Document Service, Enterprise Records and Archive Management, Enterprise Knowledge & IP Service |

#### Detailed Capability Breakdown

| Capability Area | Sub-capabilities |
|-----------------|------------------|
| **Archive Services** | Database Backup Storage and Archival, Digital Document Storage and Archival, Physical Document Storage and Archival |
| **Reporting, Analytics and Optimisation** | Document Clustering By Subject and Dimension, Security and Threat Detection, Predictive Analytics and Insights |
| **Document Services** | Document Distribution, Document Library, Document Generation, Document Storage and Lifecycle Management, E-Signatures, Imaging and Scanning |
| **Records Management** | Records Archiving, Records Reporting, Records Classification |
| **Intellectual Property And Knowledge** | Enterprise Architecture, Knowledge Exchange, Intellectual Property Portfolio, Management Manual |

### Platforms@BNZ

The enterprise **Information Management** (EIM) platform is one of the Business Enablement Platforms. EIM supports customer serving, business enablement, and experience platforms, and depends on core platforms for security, storage, reporting, analytics and more.

### EIM - Value Chain & Data Lifecycle

Information Management platform enables the following end-to-end value chain (also known as the Data Lifecycle) for information assets within BNZ:

| Stage | Description |
|-------|-------------|
| **Capture** | Information assets are manually crafted, or automatically generated by systems, or they can be obtained externally via document scanning and ingestion process |
| **Distribution** | Information assets are sent externally either physically (via a mail house) or electronically (via electronic notification) |
| **Retention** | Information assets may be stored for collaboration (hot storage), reference (cold storage), or archived (very cold storage) |
| **Processing** | Information assets can be searched and retrieved with all appropriate access controls and permissions applied |
| **Disposal** | Information assets stored by the platform are lifecycle managed, ensuring timely and defensible disposal |

### EIM - Capability Model

Information Management enables the end-to-end value chain for all information assets, from creation to disposal. The capabilities necessary to support the value chain will be provided by the following enterprise platforms:

| Platform | Description |
|----------|-------------|
| **Enterprise Document Service** | Supporting the generation, storage, e-signing, imaging and distribution of documents as a service. Also included in this platform are the relevant reporting and analytics |
| **Enterprise Knowledge and IP Service** | Supporting capabilities for creation, maintenance and exchange of knowledge, along with the maintenance of a common Intellectual Property (IP) portfolio |
| **Enterprise Records and Archive Management** | Supporting capabilities for identifying, classification, and management of records, as well as systems for archiving and disposal |
| **Digital Asset Management** | Supporting the management activities for digital 'documents': images, brand assets, design artifacts etc. |

### EIM - Target State Summary

Our information is what informs how we develop and implement our overall strategies and related processes. It is at the heart of business growth and improvement, and central to our mission to be the best bank for all New Zealanders.

| Target State Element | Description |
|---------------------|-------------|
| **Headless Information Service** | A 'plug-and-play' enterprise grade API enabling frontline and core banking systems to more easily store, retrieve, and appropriately manage their information assets |
| **Event Based Architecture** | Enterprise information service to publish Kafka business events on all state changes, so we can gain insights and help producers or consumers in near real-time |
| **Enterprise Document Storage** | Move documents from expensive collaborative storage to cheaper commodity storage or long-term archive, without breaking hyperlinks |
| **Enterprise Document Search** | Build context aware information from anywhere using basic, advanced, and intelligent document search APIs |
| **Document Data Product** | Reuse existing BNZ data product infrastructure to build intelligent reporting |
| **Multi-channel Knowledge** | Knowledge articles to be expertly crafted, and accessible by the right people, at the right time, in whatever channel they work |
| **Auto-classify, Auto-categorise** | Less manual document management, and more machine learning to confidently classify and categorise documents |
| **Modern and Simple Technology Stack** | Decommission legacy and unsupported document generation, distribution, and management infrastructure |

---

## 3. Risk Overview

### Current State - Challenges and Issues

| Challenge | Description |
|-----------|-------------|
| **Strategic Oversight** | Historically, Information Management has not been managed at an enterprise or strategic level but at a requirements or project level, without an end-to-end business strategy to guide investment, resulting in a plethora of applications and approaches |
| **Inconsistent Customer Experience** | Customer experience is inconsistent, outdated and clunky for customers, colleagues and third parties across all stages of the document lifecycle and across all customer segments, banking products, and internal processes such as staff hiring |
| **Compliance Challenges** | Challenging to evidence compliance with our regulatory obligations, due to difficulty in accessing and disposing of information. Over-retention of information increasing potential impact of personal information breaches |
| **Escalating Maintenance Costs** | Visibility across the fragmented and disconnected technologies used is opaque and poorly understood, impacting support and maintenance of business-critical processes. Improvements to date have been piecemeal through point solutions |

### Current State Architecture

This map shows all 53 EIM capabilities and their related applications and IT components arranged into platform layers.

**70+ IT Assets with IM capabilities or dependencies:**
- Document Generation (17)
- Document Management (16)
- Document Scanning (5)
- Document Library (11)
- Knowledge Transfer (16)

**6 enterprise grade documents storage repositories:**
- SharePoint 2013 (37 TB)
- SharePoint 2019 (34 TB)
- SharePoint Online (33 TB)
- VRetrieve (~60 TB)
- Network Drives (~40TB)
- Cloud Storage (<1 TB) - target state

### Current State Architecture - Conceptual

**Key points:**
- Over 100 TB of expensive SharePoint Online storage. Used for both operational and archive datasets
- Over 780 million files stored in third party archive (V-Retrieve), not covered by GIRP
- Over 180 million files stored in old network drives
- GIRP retention rules not consistently applied. Estimate 50% of information could be deleted
- Cost / volume is the wrong way around

### Current State - Business Risk

EIM is at the heart of business growth and improvement, and central to our mission to be the best bank for all New Zealanders. **Without the functional management of our information, this mission will be impossible.**

EIM impacts many of our enterprise risks, with significant impact on:
- **RSK-1300** Data Management
- **RSK-166** Data Loss
- **RSK-171** Cyber Compromise Risk

All three of these risks are currently rated not effective. Uplift of EIM will support the uplift of these risks, in particular by enforcing records disposal, reducing the volume of information potentially available in data breach events.

### Current State - Business Risk (BMI Analysis)

**The BNZ Modernisation Index (BMI)** represents our commitment to technology risk reduction and simplification. It is calculated using business criticality, architectural lifecycle and modernisation complexity for each asset in our tech landscape. The higher the BMI, the higher the need to modernise.

**Key points:**
- Disproportionally large number of Exit status systems in the Business Critical or Mission Critical category
- Over 60% of system with a BMI of greater than 120, considered technically material

### Current State - Application Landscape

| Observation | Details |
|-------------|---------|
| Document Services | 16 document service applications in an Exit/Divest state, all with a BMI score over 100 |
| Knowledge Management | Relatively good BMI, few systems in a poor state of health |
| Records Management | 0 applications in an encourage or healthy state |

### Current State - IT Component Landscape

- Document services platform has 6 foundational IT components in an Exit/Divest state, including SharePoint and our File Cluster

---

## 4. Target Architectures / Platform

### Target State Architecture - Conceptual

We aim to shift the primary storage location for unstructured information away from hot (fast and expensive), more to cold and very cold tiers (cheaper and slow).

**Our goals:**
1. More cloud and SaaS, less SharePoint Online
2. Shrink on-prem network storage by applying RecordPoint retention rules
3. Phase out of V-Retrieve as a long-term archive
4. Shrink SharePoint to just SPO and only for docs in their collaborative lifecycle phase
5. Introduce a new Zero carbon cloud storage tier (for verified archives)

### NAB Current State

**Convergent Points:**
- NAB have two document service stacks, one for generating documents, the other for document management
- Both stacks are served by a NabOne Miniapp over a SpringBoot microservice supporting API integrations to third party service providers
- This TSA aligns with this pattern, combined as a single enterprise API for all BNZ document services
- This TSA aligns to the intent to build multi-context MiniApp, as opposed to using 'out of the box' user interfaces

**Divergent Points:**
- Where NAB have Alfresco for the underlying document management capability, this TSA proposes building management logic into the document microservice layer, avoiding vendor lock-in of records and their metadata
- NAB use Databricks for their Data Products and business event integration. BNZ proposed Kafka for business events and BDH (snowflake) for our data products and BI analytics for our reporting

### Target State Architecture - Logical

We will achieve our document management goals by investing in a **headless document management** microservice. This will provide the foundational IM capabilities, extendable by a capability specific apps and other microservices to improve customer and colleague experiences.

**Supporting the microservice will be the full suite of capability aligned services:**
- Document generation
- Ingestion (storage and lifecycle management)
- Digital signatures
- Imaging and scanning
- Document distribution (post and authenticated channels)
- Search (basic, advanced and intelligent levels)
- Knowledge base

---

### Enterprise Document Service Platform

#### Document Generation

We will invest in, and scale, SmartComm document generation, uplifting it to a secure AWS pure cloud environment, extending the functionality to support high volume batch (for CLR), and provide an API for generating document, integrated with the Kafka event bus. We will also allow for the upload of new customer information assets, automatically scanned and managed from ingestion, from all customer document uploads.

**Divest:**
1. HotDocs
2. BI Publisher
3. iText (eCredit, Apex and LOPi docs)
4. CustomerJoining/DocGenerateAPI
5. InterAct
6. IBIS Hardship Communications
7. vRetrieve (for doc generation)

#### Document Management

We will invest in an intelligent headless document management system, serving customer and colleague experience systems (SaaS and internal applications, agnostic to any vendor storage or management technology, and replacing existing legacy document libraries.

**Divest:**
1. MyCustomerFiles
2. DORIS (LendingDirect and LSD)
3. MyPeopleDocs
4. SharePoint 2013 and 2019
5. vRetrieve (for doc archive)
6. Correspondence WPS (IBM)
7. Legal Document Management
8. myMarketing

#### Document Distribution

We will reuse existing authenticated channels where we can, and invest in a new mail-house and channel agnostic Distribute API. This will act as an anti-corruption layer between frontline systems and our distribution providers. The microservice will require the address and method of distribution, physical or digital, and will publish distribute state changes (queued, sent, received) on the business event bus.

**Divest:**
- VRetreive (in its current legacy state), migrating to the vRetrive target state (modern integration)
- Email, as a way to distribute confidential document
- DocuSign, as a means to distribute documents to third parties and prospects

#### Digital Signatures

We will invest in more automation of our DocuSign SaaS tooling, phasing out manual uploads of documents, and phasing in both tightly coupled and loosely coupled connectors. The default workflow pattern will be the loosely coupled connector, accessed by the DocMan microservice, and reduces the complexity and cost of integration, while maintaining an anti-corruption layer between envelope originating systems and our third party vendor. The tightly coupled connector (like nCino-DocuSign), offers capability specific integrations via a SaaS to SaaS connector.

**Divest:**
- Business processes that manually upload documents to DocuSign
- Business processes that require wet signatures

#### Imaging and Scanning

We will invest in Abbyy Vantage SaaS as our target state document scanner. This advanced machine learning tool can receive documents by manual upload, SPO connector, or MS Graph to BNZ O365 (email). Processed document can be retrieved via a exposing a BNZ API (1), or by polling the Abby transaction API (4). For more simple scanning tasks, robotic automated can be achieved using the Blue Prism and Adobe stack. For physical scanning, we will promote the use of our Smart Printers, modified to leverage Abbyy ML skills before pushing the result to SPO.

**Divest:**
- Kofax
- Lending Services Doc Prep (Pega)

#### EDM User Interface

Follow NAB's lead and build a superior integrated customer and colleague experience for document services.

- All documents generated or uploaded will be accessible via the BnzGO DocMan MiniApp
- Supports both generic and domain specific services (such as Lending Origination)

**Divest opportunities:**
- MyCustomerFiles
- Hot Docs (first off the rank)
- SharePoint 2013/2019

---

### Enterprise Knowledge & IP Service Platform

#### Knowledge & IP Management

There are eleven improvements identified to the current fragmented knowledge landscape, including the development of a knowledge platform, curating and sharing content, a GenAI chatbot channel, improved knowledge notifications, proactive knowledge creation, better reporting of usage and trends, and improved analytics to turn insights into productivity gains across the whole bank.

**Divest:**
- Atlassian Confluence (as a knowledge base)
- SharePoint Online (as a knowledge base)
- Te Kete (as an analytical and management tool)

---

### Enterprise Records and Archive Management Platform

#### Records Management

We will invest in automation of records management, leveraging the intelligent classification and categorisation of unstructured data across all document libraries: on-prem, third-party, private cloud or SaaS.

Where SaaS or cloud services are unable to implement GIRP or privacy act policies we will leverage internal GenAI and the BNZ Docs to classify and categorise documents in place and manage their lifecycle.

**Contain:**
- RecordPoint (to SPO and network drives)
- SharePoint Online (as a metadata enforcement point)

#### Archive Management

We will invest in a headless enterprise archive solution, capable of storing structured or unstructured information from retired or soon-to-deprecated systems.

The archive service will provide a tiered storage model for documents, and integrating lifecycle management for all data assets designed for optimal storage speed and cost.

**Divest:**
- Tech-stack Simplification systems (23 identified for archive)
- SharePoint Online as an archive repository
- vRetrieve as an operational archive repository
- CMOD – Content Management On Demand archive repository
- Imprint (cheque image archive)
- Pega UW archives
- Assist forms (archives)

---

### Enterprise Digital Asset Management Platform

#### Digital Asset Management

We will invest in a headless content management system, offering centralised Digital Asset Management (DAM) for the public website and BNZ business applications (internal or SaaS). This enables a scalable, consistent workflow capability for the publication of images, letters, legal text, signatures, banners, page blocks, CSS and more, across multiple channels, devices and languages.

**Contain:**
- SilverStripe (as a CMS, at least until MarTech have completed the market analysis / RFP)

---

## 5. Enterprise Context

### FY25 Initiatives and their Objectives

#### Technology Strategy Objectives
- Modernise and Simplify
- Agile and Adaptable
- Platform Mindset
- Deeply Digital
- Resilient, Secure, Safe

#### Corporate Strategy Objectives
- Modernise our Technology and Data Infrastructure
- Accelerate Digital Customer Experiences
- Radically Simplify products, policies and processes
- Perfect the Banking Basics

#### EIM Program FY25 Initiatives
- Enterprise Document Management (Initiative #71318)
- Enterprise Document Storage and Lifecycle Management (Initiative Idea)
- Enterprise Imaging and Scanning (Initiative Idea)
- Information Management (Initiative #74070)

#### FY25 Contributors
- Core Ledger Replacement Phase 1 (Programme #46426)
- Enterprise Data Products (Initiative #71831)
- 1.0 Zero Trust Acceleration & Network Fundamentals (Initiative #72291)
- Reimagine Consumer Lending (RCL) (Initiative #71396)
- LeanIX Integration (Initiative #72345)
- Generative AI (Initiative #74067)
- TSS - State Enabled Asset Decommissioning & Archiving (Initiative #74553)

#### FY25 Consumers
- Digital Programme (Initiative #71822)
- Customer360 Decision Hub (Initiative #71707)
- Pega Customer Decision Hub (Initiative #72306)
- Workflow Automation (Initiative #71763)

### Platform Data Flows and Integration

EIM Document Services platform exposes two APIs (one active, one in an innovate state), and published 5 business event topics (Kafka events).

Documents are generated upstream, then ingested for downstream consumers.

Data products (not shown) will be generated from each Kafka topic shown, i.e. the DocGen topic will be used to seed a reusable DocumentGenerated data product in BDH.

### Technology Strategy Alignment

| Theme | Description |
|-------|-------------|
| **Modernise and Simplify** | The EIM TSA offers a blueprint for replacing the current landscape of fragmented, broken, unsupported, and not-fit-for-purpose applications (BI Publisher, HotDocs, iText, Kofax, MCF, vRetrieve, etc.) with a new enterprise grade EIM service: Springboot microservices offering the full suite of IM value chain operations; Enables migration of information storage from expensive vendor-lock-in to multi-tiered commodity cloud storage; Intelligent and automated (GenAI) document classification and categorisation |
| **Agile and Adaptable** | This target state comprises of loosely coupled microservices, built by small agile teams, using Miniapps (for Lending Docs, doc admin, MCF target state) and SpringBoot microservice (DocMan). Patterns: Event-Driven Architecture using Kafka; Kong Enterprise Services; Kafka to BDH data products |
| **Platform Mindset** | This TSA encourages investments in a suite of enterprise platforms, each offering dedicated support and operating model aimed at enabling an uplift of capability maturity and the federated onboarding of IM workflows: Enterprise Document Services, Enterprise Knowledge and IP Services, Enterprise Records and Archive Management, Enterprise Digital Asset Management |
| **Resilient, Secure and Safe** | Developed in conjunction with data protection and information security domain workstreams: Move to SmartComm pure cloud for more resilient document generation; Core information protection capabilities baked into DocMan microservice; Automatic classification of documents at creation/ingestion for full lifecycle governance |
| **Deeply Digital** | Drives more digital experiences for document generation, e-signing, distribution and management: New shared DocuSign API connector (aim for 90% automatic envelope generation vs current 90% manual); GenAI to classify and categorise documents automatically; Growing SmartComm document template capability |

---

## 6. Simplification & Modernisation Roadmap

### Roadmap - Information Services

| Area | FY24 Q4 | FY25 | FY26 | Future (<FY29) |
|------|---------|------|------|----------------|
| **Strategy** | EIM Program Delivery Plan | IM Market Scan, DocMan Detail Designs | IM UX, UI, and GenAI Roadmaps | |
| **Knowledge Management** | Te Kete OpenAI Chatbot | Data Product (Knowledge) | Knowledge Platform, Knowledge API | |
| **Records Management** | SPO + Drives (RecordPoint), IM LLM Experiment | GenAI Auto-Classification Microservice | MyCustomerFiles / vRetrieve | SaaS / Cloud |
| **Analytics and Reporting** | BDH Foundations | Data Product (Generate), Data Product (Distribute) | Data Product (Lifecycle), Data Product (E-Signature) | |
| **Archive Services** | Document Archive Process | Tiered Archive Storage | Archive Retrieval Miniapp | |

### Roadmap - EIM Document Services

| Area | FY24 Q4 | FY25 | FY26 | Future (<FY29) |
|------|---------|------|------|----------------|
| **Generation** | SmartComm Purecloud Uplift | Batch * 20%, Secure Upload POC | Scale to 1M/month, Secure Upload Portal | Scale to 4M+/month |
| **Store and Retrieve** | DocMan Ingest and Retrieve | Metadata Index (no SQL), Basic Search, Lending DocMan Miniapp | Advanced Search, DocMan Miniapp | Intelligent Search |
| **Lifecycle Management** | DocMan MicroService | GenAI Auto-Classification Microservice | BNZ Docs (Target State) | |
| **Distribute** | | Distribute via Post (Datam) | Distribute via Auth Channels | |
| **Imaging** | Abbyy POC | EIM Imaging Service | Data Product (Imaging), Automate Imaging Workflows | |
| **Digital Signatures** | | EIM DocuSign Connector | Automate Signature Workflows | |

### Roadmap - By Platform

| Platform | FY24 Q4 | FY25 | FY26 | Future (<FY29) |
|----------|---------|------|------|----------------|
| **EIM Platform Strategy** | EIM Program Delivery Plan | IM Market Scan, DocMan Detail Designs, Business Analysis: UX, UI, and GenAI | EIM FY26 Business Case / Program Delivery Plan, MyCustomerFiles / vRetrieve Exit | |
| **Enterprise Knowledge Management** | Te Kete OpenAI Chatbot | Data Product (Knowledge) | Knowledge Platform | Knowledge API |
| **Enterprise Records & Archives Management** | Document Archive Process, IM LLM Experiment | GenAI Auto-Classification Microservice, Tiered Archive Storage | Archive Retrieval Miniapp, BNZ Docs (Target State) | |
| **Enterprise Document Services** | DocMan MicroService, Basic Search, Batch Generate, Abbyy POC | Metadata Index (no SQL), Data Product (Generate), EIM Imaging Service | DocMan Miniapp, Advanced Search, Data Product (Distribute), Data Product (Imaging) | |
| **Enterprise Digital Asset Management** | | MarTech DAM RFP | DAM / CMS Implementation | |

### Roadmap Modernisation Tipping Point

Document services tipping point, defined as the point where we have more assets in 'Encourage' state than in 'Exit'.

**Key observations:**
- Document services platform starts FY25 with 32 applications, 15 in exit state, and 7 in encourage
- Assets that start in innovate state are delivered into an encourage via the EIM and other supporting change programs
- Within 5 years we will have simplified the EIM platform, supporting half the number of IT assets
- **Tipping point expected around 2026**

---

## 7. Platform Horizons

### Roadmap - EIM Platform Horizons

| Horizon | Timeframe | Focus |
|---------|-----------|-------|
| **Horizon 1** | FY25 | CLR + C360 Delivery Plan (Basic doc services) - Specific CLR and C360 funded EIM services, limited generic EIM capability delivery |
| **Horizon 2** | FY26-FY27 | EIM Program Delivery (Phase 2) (Advanced doc services) - Generic EIM services, advanced search, MCF+DORIS migration, 3rd party portal |
| **Horizon 3** | FY28+ | EIM Program (Phase 3) (Intelligent doc services, including knowledge) - Scaled EIM services, intelligent search, V-Retrieve migrated, legacy IM systems removed |

**Business Case Timeline:**
- EIM Business Case: FY25
- EIM Business Case (refresh): FY27

---

## 8. Appendices

### APRA Checklist

#### Target State Architecture Roadmaps

**APRA Feedback:**
While initial roadmaps have been drafted for certain platforms, these are fragmented and do not provide visibility of the total body of work to be completed. Currently, there is no enterprise technology roadmap that includes key milestones and timeframes or evidence that sequencing and dependencies have been considered in the planning process.

In addition, the reporting and governance mechanism for the technology transformation initiatives has yet to be established. APRA acknowledges that the BNZ Modernisation Index (BMI) is being rolled out, however the effectiveness of BMI in incentivising and driving progress is yet to be proven as it is being introduced in scorecards in FY25, and we understand it is not an effective measure of progress.

**Deliverable (Due 30 June):**
Develop technology modernisation roadmaps at the enterprise and divisional level. The roadmaps should provide visibility of the totality of work to be undertaken and include target state, accountabilities, feasible timelines, interdependencies and sequencing. There should be a funding model to support the execution of the program of work each year and a governance and reporting mechanism to monitor progress against the roadmaps and the impact on technology risk profiles.

**What this means for us:**
1. Deliver approved target state architectures for all 52 Platforms (45 remaining)
   - Review target state architecture contents to ensure APRA satisfaction and NAB alignment
   - Prioritise Platforms based on BMI of assets, also reprioritise or reallocate lower priority work
   - Enlist internal and external resource assistance to complete
2. Establish Strategic Architecture Authority to govern and monitor progress against TSAs

### TSA Content Checklist

1. Platform Scope & Definition
2. Platform Vision - Target state summary
3. Context:
   - Value chain-stream
   - Capability map
   - Interdependencies with other Platforms, Domains, areas
   - Stakeholder map
4. Current state:
   - Current state architecture
   - Landscape (Lean IX) + BMI
   - Challenges, Issues & GRACE risks
5. Target state:
   - Target state overview - what will great look like? how will it address challenges, and risk profile?
   - Alignment of Target state with Strategic ambition, Tech strategy themes, NAB TSA and direction
   - Modernisation journey with horizons/Tipping point/Initiatives funded, planned and underway
   - Simplification & Modernisation roadmap, potential timeframes, dependencies, foundational work required

---

*Document Classification: PRIVATE*
