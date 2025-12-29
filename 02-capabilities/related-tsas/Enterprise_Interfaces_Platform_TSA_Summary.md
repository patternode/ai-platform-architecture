# Enterprise Interfaces Platform TSA - Summary

## Slide 1: Title Page
**Enterprise Interfaces (APIs, Events and Integration) – Target State Modernisation Roadmap**

- **Author:** Glenn Bellam
- **Date:** June 2025 v1.0
- **Responsible Head of Architecture:** Angus Cotton
- **Executive Sponsor:** Paul Norman (CIO)
- **GM Approver:** Nic Olivier (GM Core Infrastructure - Acting)
- **Key Stakeholders:** Shirley McIntyre (GM Architecture & Technology Strategy), Anna Tarasoff (GM Data - DD&A Central)

## Slide 2: Version Control
Document version tracking and approval process:
- V 0.9 dated 18/5/2025
- Versioning guidelines from Draft (0.x) to Final approved version (4.0)
- Structured review process through HOA, Shirley, and Paul Norman/SAA reviews

## Slide 3: Table of Contents
Document structure covering nine main sections:
1. Executive Summary - Platform scope and business purpose
2. Target State Summary and Platform Vision
3. Simplification & Modernisation Roadmap
4. Target State Architecture
5. Enterprise Context - Data, Integration & Platform dependencies
6. Platform Horizons - Technology transition timeline
7. Risk Overview - Current state challenges and opportunities
8. Focus Areas
9. Appendices

## Slide 4: Section 1 – Executive Summary
Introduction to the executive summary section covering platform scope, definition, and business purpose.

## Slide 5: Executive Summary Content
**Target State Overview:** Enable resilient, flexible integration architecture for best customer, colleague and 3rd party experience with future feature growth capability.

**Key Points:**
- Enterprise Interfaces are primary mechanism for application integration
- Built once, used many times, discoverable, self-service onboarding
- Consist of Enterprise REST APIs, Enterprise Business Events, and Data Streams
- Establish API & Integration Enablement Team
- Build right Enterprise Interfaces through bounded context modeling
- Migrate from legacy integrations to Enterprise Interfaces

**Technical Focus Areas:**
- Accelerate Enterprise API Adoption
- Use Engineering Platform patterns (Recipes)
- Focus on Bounded Contexts providing Enterprise Interfaces
- Legacy Integration Migration
- New API & Integration Enablement Team

**Challenges and Issues:**
- Lack of focus on refactoring/retiring legacy integrations
- Accidental complexity from slow target state adoption
- Change programs focus on program outcomes vs. enterprise-first approach
- No API Designers for integration practice uplift
- Key technology platforms still need implementation

## Slide 6: Platform Roadmap Overview
**Transformation Approach:** Built on three pillars - technology change, process improvement, and people enablement.

**Six-Phase Roadmap:**
1. Legacy interface discovery & remediation (FY 25-28)
2. Implement target state tools and processes (FY 26-28)
3. Priority 1 Bounded Context Enterprise Interfaces (FY 27-30)
4. Priority 2 Bounded Context Enterprise Interfaces (FY 30+)
5. Containment - Block new use of non-priority integrations (FY 30+)
6. Complete decommissioning of legacy tools (FY 30+)

**Key Benefits:** Re-use, risk reduction, cost transparency, agility, standardisation

**NAB Alignment:** Shared desire to reduce complexity and focus on core technologies

## Slide 7: Section 1a – What is Application Integration?
Introduction to application integration concepts and scope.

## Slide 8: Enterprise Interfaces Vision
**Vision:** Modernising BNZ integration landscape by transforming from tightly coupled, point-to-point and legacy host-based integrations towards future-ready, API and event-driven enterprise.

**Key Drivers:**
- Enterprise-first approach prioritising shared capability and sustainability
- Pragmatic management of legacy integration debt
- Shift in mindset beyond technology upgrade
- Programs contribute to long-term enterprise health and flexibility

**Scope:** All communications between applications

## Slide 9: What is Integration and Why is Important?
**Definition:** Integration describes connection between different systems, applications and data sources to enhance user experience.

**Two Main Categories:**
1. **Application & Process Integration:** Connect software applications for real-time data/service exchange
2. **Data Pipelines:** Consolidate and curate data for reporting, analytics and operational use cases

**Purpose:** Deliver safe, stable, efficient and cost-effective service to BNZ stakeholders

## Slide 10: Why Enterprise Interfaces?
**Current State Challenges:**
- BNZ Integrations make it hard to change/exit applications
- Typically increase tight coupling and use many technologies
- Duplication of integrations performing same/similar functions
- Little enterprise-level formal governance
- No API Designers and little integration visibility

**Target State Benefits:**
- Integrations built once and used many times
- Described via contracts allowing change tracking
- Human and machine readable contracts
- API Portal enables discovery and onboarding
- Embedded security by design
- Loosely coupled interfaces

## Slide 11: Interfaces are Key to BNZ's Future
Enterprise Interfaces enable developers to build applications based on BNZ services and easily consume partner SaaS/COTs applications.

**Key Interface Types:**
- **Enterprise Interfaces:** Built once, published in API Developer Portal for discovery
- **Private Interfaces:** Point-to-point integrations (generally anti-pattern)
- **Industry Interfaces:** NZ Payments Standard APIs (Open Banking)

**Consumer Contexts:**
- BNZ Colleagues
- BNZ Customers
- 3rd Party consumers
- Developers

## Slide 12: API and Integration Enablement
**New Team Structure:** API & Integration Enablement Team to design, measure and track all application integrations.

**Key Capabilities:**
- Tooling and Practice uplift
- External Developer Onboarding
- Knowledge base
- Integration reporting
- Oversight of legacy integration migration
- Guardrails for compliance
- Embedded Security

## Slide 13: Application Integration Visibility
**Current Challenges:**
- Little visibility with GCS/MQ and webservice messages (no message level authorization)
- No central register of file transfer and ETL jobs
- Lack of visibility makes cost of change estimation difficult

**Target State:**
- Enterprise REST APIs, Events and Data streams discoverable and self-service onboardable
- Enterprise Events publish business outcomes with updated state
- Enterprise Data Streams publish data where BNZ don't have corresponding command

## Slide 14: Bounded Context Modelling
**Approach:** Group like business functions based on communication patterns through event storming.

**Benefits:**
- Change programs focus on transforming bounded contexts rather than individual applications
- Track integrations, bounded contexts and relationships in Leanix
- Report on Enterprise Interface progress by requiring each bounded context to provide at least 1 Enterprise REST API and 1 Business Event

## Slide 15: From Projects to Platforms: Reusable Interfaces
**Strategic Approach:**
- Expose Value Across BNZ through Enterprise REST APIs and Events
- Modernise by Domain targeting Bounded Contexts
- Address Upstream Gaps recognising dependencies outside program scope

**Challenge:** Bounded Contexts with no initiatives have no funding for enterprise interfaces despite being upstream dependencies

## Slide 16: How to Get Visibility of Legacy
**File Transfer:** TSS exiting existing solution for AWS Transfer Family with data contract standards

**Host Communications:**
- Currently no understanding of client consumption due to lack of message level authorisation
- Two approaches: Host Gateway and Z/OS Connect REST APIs
- Testing client-to-legacy message-level authorisation via host gateway

## Slide 17: Bounded Context Reporting in Leanix
Prototype custom report showing Customer and Party Master platform integrations with other platforms through bounded context relationships, displaying status of Enterprise Interfaces and legacy integrations.

## Slide 18: BNZ Application Interactions
**Comprehensive Integration Architecture:**
- Bounded Context interactions between different application types
- Data interactions with products and streams
- SaaS/COTs application interactions through anti-corruption layers
- Integration with Data Catalogue and security controls

## Slide 19: Interface Contracts and Shifting Left
**Three Contract Types:**
1. **REST API Contracts:** OpenAPI specification via Kong Gateway
2. **Event API Contracts:** AsyncAPI specification via Confluent Kafka
3. **Data Contracts:** DataContract specification for streams and file transfer

**Benefits:** Build once, use many times approach with pre-cleansed, curated data objects

## Slide 20: Contract Specifications Comparison
Detailed comparison of REST API, Event, and Data Streams specifications covering:
- Purpose and triggering mechanisms
- Data exposure patterns
- Correlation to business logic
- Contract specification focus
- Metadata emphasis
- Shared data model integration

## Slide 21: API Contract Management and Developer Portal
**Architecture:** Single place for discovery and onboarding to all Enterprise Interfaces with contract definitions stored in source control and automated deployment to Kong/Kafka platforms.

## Slide 22: Section 2 – Target State Summary, Platform Vision
Introduction to target state summary and platform vision section.

## Slide 23: Platform Context
**Six Integration Categories:**
1. **REST APIs:** HTTP standard methods, Enterprise APIs with multi-context authorization
2. **Business Events and Data Streams:** Real-time signals and data flows
3. **Batch File Transfer:** Bulk data mechanisms across platforms
4. **Host Integration:** 7+ host integration patterns (most marked for exit)
5. **Point to Point Integrations:** To be avoided except for specific ACL cases
6. **ETL:** Shift towards Enterprise Interfaces (data streams)

## Slide 24: Platform Vision
**Five Key Areas:**
1. **Enterprise Interface Ownership:** Teams accountable for applications and interfaces they expose
2. **Enterprise-First Delivery Mindset:** Programs deliver reusable enterprise assets
3. **Discoverability & Developer Experience:** Centralized developer portal
4. **Quality and Visibility:** Consistent standards across all integrations
5. **Planned Migration:** Systematic migration from legacy patterns

## Slide 25: Target State Summary
**Five Core Focus Areas:**
1. **Interface Ownership & Reuse:** Teams own applications and enterprise interfaces
2. **Developer Enablement & Tooling:** API & Integration Enablement team with self-service tools
3. **Event & Data Stream Architecture:** Events from business commands, data streams capability
4. **Legacy Integration Transition:** Migrate to AWS Transfer Family, exit ESB tooling
5. **Integration Visibility & Governance:** All integrations mapped to Bounded Context relationships

## Slide 26: Value Chain – Enterprise Interfaces
**Five-Stage Value Chain:**
1. **Discover:** Integration discovery and bounded context identification
2. **Build Tooling:** API contracts and governance automation
3. **API Contract Based Governance:** Standards and tracking
4. **Build Enterprise Interfaces:** Various application patterns and integration types
5. **Modernise Legacy:** Migration and decommissioning processes

## Slide 27: Stakeholder Engagement and Accountability
**Key Stakeholders:** Engineering Product teams, Engineering Practices, Strategy and Architecture teams

**Executive Stakeholders:** Paul Norman (CIO), Nic Olivier (GM Core Systems), Shirley McIntyre (GM Strategy and Architecture), TBD Chief Engineer

**Note:** Many stakeholders not yet engaged, indicating need for broader consultation

## Slide 28: Section 3 – Simplification & Modernisation Roadmap
Introduction to simplification and modernisation roadmap section.

## Slide 29: Identifying Priority Bounded Contexts
**Approach:** Model relationships in Leanix to identify:
1. Bounded contexts with most relationships to other bounded contexts
2. Applications providing most legacy integrations
3. Initiatives impacting bounded contexts and integration complexity

**Visual Tools:** Prototype reports showing integration complexity and relationships

## Slide 30: Simplification & Modernisation Roadmap
**Detailed Timeline (FY 25-26 to FY 30+):**
- Discovery, planning and remediation of legacy systems
- Target state tooling implementation
- Priority bounded context transformation
- Legacy integration migration and decommissioning

## Slide 31: Modernisation Tipping Point and Horizons
**Three Horizons:**
1. **Horizon 1 (2026-2028):** Engineering platform practices and tooling, priority 1 bounded contexts
2. **Tipping Point (2028):** Domain teams can build enterprise interfaces using target state tooling
3. **Horizon 2 (2030-2032+):** All host communications private, discoverable self-service interfaces

## Slide 32: Section 4 – Target State Architecture
Introduction to target state architecture section.

## Slide 33: Target Architecture
**Key Components:**
- **Client Applications:** Interact with Enterprise APIs, Sagas, or Backend for Frontends
- **Sagas:** Orchestration for workflows and value streams
- **Enterprise Services:** Built in Java using Spring Boot Recipe
- **Anti-corruption Layers:** For SaaS/COTs integration
- **Kafka:** Event streaming platform for publishing events

## Slide 34: BNZ's Standard Software Architecture Patterns
**Six Standard Patterns:**
1. **Mini-Apps:** Staff and customer facing web applications
2. **Saga:** Value stream orchestration pattern
3. **Anti-Corruption Layer (ACL):** SaaS integration abstraction
4. **Strangler:** Gradual legacy system replacement
5. **Microservices:** Standard BNZ backend applications
6. **Backend for Frontend (BFF):** Private interface for specific clients

## Slide 35: Microservice, ACL and Strangler Interactions
**Three Interaction Patterns:**
1. **BNZ Applications:** Provide enterprise Rest APIs across all user types with business logic and events
2. **Anti-Corruption Layers:** Ensure SaaS/COTs standardised integration through enterprise interfaces
3. **Strangler Pattern:** Front host functions with enterprise interfaces for gradual migration

## Slide 36: Backend for Frontend Interactions
**Two BFF Options:**
1. **Spring Boot Application:** Simple, full control but more code and slower updates
2. **GraphQL Server:** Flexible, fast to change but more complex with stronger governance needs

**Constraints:** BFFs limited to specific user interface, part of bounded context, cannot replace Enterprise Interfaces

## Slide 37: Saga (Orchestration) Recipe Interactions
**Temporal-based Implementation:** Automate complex business workflows spanning multiple microservices with centralized workflow engine managing REST API calls and event listening for coordinated, reliable, loosely coupled processes.

## Slide 38: Target Data Streams and Bounded Context Interactions
**Integration Approach:** Using Data Streams and Data Contracts between BNZ Data and Enterprise Interfaces platforms to ensure equitable access across analytical and operational applications.

**Requirements:** Shared capabilities across platforms, contract design alignment, and consistent data object standards

## Slide 39: Target File Transfer and Data Streaming Interactions
**Three-Layer Architecture:**
1. **Contract Tooling:** Developer-designed data contracts with data catalogue integration
2. **File Transfer Gateway:** AWS Transfer Family for file processing
3. **Data Streaming:** Real-time alternatives to batch processing with conform layer for data streams

## Slide 40: From Batch File Transfer to Real Time Streams
**Migration Approach:** Transition from file-based batch processing to real-time Enterprise REST APIs and data streams, maintaining file interfaces at edge while implementing real-time flows internally.

## Slide 41: Platforms@BNZ Integration Guidelines
**Integration Approach by Platform Layer:**
- **Experience/Customer Serving Platforms:** Must use Enterprise Interfaces
- **Business Enablement Platforms:** Enterprise Interfaces for BNZ data/functions, industry APIs for specific use cases
- **Core Technology Platforms:** Standardised tooling/plugins preferred, no Enterprise Interfaces needed

## Slide 42: NAB Alignment
**Aligned Areas:**
- Business capabilities as services
- Avoiding vendor entanglement
- Integration flexibility through microservices
- Event Driven Architecture
- Common tooling (Kafka, Kong, Java Spring Boot)

**Key Differences:**
- BNZ: Enterprise API focus, bounded context modelling
- NAB: GraphQL hypergraph, client-led API design
- BNZ: SaaS-first approach, NAB: Build over buy preference

## Slide 43: Strategic Alignment
**Alignment with BNZ Strategic Themes:**
1. **Modernise and Simplify:** Replace fragmented legacy with enterprise-grade interfaces
2. **Agile and Adaptable:** Reduce system dependencies, accelerate delivery cycles
3. **Platform Mindset:** Self-service capabilities and contract-first patterns
4. **Resilient, Secure and Safe:** Contract-first approach with data catalogue integration
5. **Deeply Digital:** APIs, events, and data streams as digital fabric

## Slide 44: Section 5 – Enterprise Context, Data Integration and Interactions
Introduction to enterprise context and data integration interactions.

## Slide 45: Data Integration Reports
Target state provides data integration reports for other target states, including prototype custom report in Leanix showing platform consumption/provision relationships and Enterprise Interface status.

## Slide 46: Enterprise Interfaces Platform Boundaries and Guardrails
**Platform Scope:**
- All Business Application communications at BNZ
- Experience, Customer Servicing, and some Business Enablement platforms
- SaaS, COTs and BNZ built application communications
- Host integrations and file transfer between business applications

**Key Guardrails:**
- Contract alignment to BNZ data standards
- Enterprise REST APIs across all contexts
- Integration tracking and reporting
- Automated deployment with contract governance

## Slide 47: Section 6 – Platform Horizons
Introduction to platform horizons and technology transition timeline.

## Slide 48: Strategic Intent - Roadmap
**Four-Phase Approach:**
1. **Discover, Plan, & Remediate Legacy:** Upgrade vulnerable infrastructure, quantify integrations, determine bounded contexts
2. **Complete Tooling Target State:** Deliver data streaming, edge processing, file transfer, integration debt dashboards
3. **Deliver Integration Target State:** Build target enterprise integrations, migrate clients, deprecate legacy
4. **Decommission Legacy Tools:** Mule, WPS/WTX, Legacy File Transfer, Control-M, Apigee

**Key Success Factors:** Measurement and quantification of existing integrations, bounded context modelling, discovery and planning investment

## Slide 49: Section 7 – Risk Overview of Current State
Introduction to current state risk overview.

## Slide 50: Platform Scope and Context
**Current State Challenges:**
- 7 different host communication patterns (most marked for exit)
- 4 non-host patterns with only 3 target patterns
- Complex technology landscape requiring simplification
- Movement from ETL/batch to real-time Enterprise Interfaces

## Slide 51: Current State Tooling, Patterns and Practices
**Tooling Status:**
- Target: Confluent Platform, Kong Gateway
- Exit: BNZ BMC Control-M, Apache Kafka, GCP Apigee
- Missing: Edge Streaming, API Developer Portal, Non-Restful API Gateway, Job Scheduling

**Current Patterns:**
- 175 Rest APIs (158 Enterprise, 17 Private)
- 42 Events (17 Enterprise, 22 Private)
- 359 GCS Messages, 93-130 Webservices, 275 ETL, 1700+ File Transfer

## Slide 52: Current Architecture
**Complexity Issues:**
- Dynatrace snapshot shows complex spider web of point-to-point connections
- Almost all integrations are synchronous (failure propagation)
- Change impact difficult to understand
- Business logic duplicated across layers
- Integration delivered with narrow vs. enterprise outcomes

## Slide 53: Current State Challenges
**Eight Key Challenge Areas:**
1. **Clarity:** Lack of understanding of application communications
2. **Historical Growth:** 25+ years of increasing complexity
3. **Legacy Patterns:** 7 Host Integration Patterns with duplicate functions
4. **Transition Time:** WPS to Mule migration took 2+ years
5. **Domain Dependencies:** Teams prioritise speed over Enterprise Interfaces
6. **SaaS Challenges:** Rising complexity due to diverse integration patterns
7. **Migration Difficulty:** Consumers difficult to identify
8. **Business Case Long Term:** Multi-year investment with delayed ROI

## Slide 54: Key Pain Points and Opportunities
**Current Issues:**
1. No formal platform ownership at BNZ
2. Limited practices/people for rollout support
3. Unclear data streaming between applications and data products
4. Difficult to identify legacy integration clients
5. Stretched engineering teams
6. Disestablished API Designer role

**GRACE Risks Addressed:** IT System Failure Risk, Data Loss Risk, Cyber Compromise Risk (all Very High)

## Slide 55: Focus Areas
Introduction to key focus areas section.

## Slide 56: Bounded Context Interactions
**Interaction Types:**
- **Private Integrations:** Within bounded contexts between individual applications
- **Enterprise Integrations:** Between bounded contexts, designed for reuse

**Requirements:** Each bounded context must provide at least 1 Enterprise Rest API and 1 Enterprise Event to ensure data and functions accessible to all applications.

## Slide 57: Current Data Interactions
**Current State Issues:**
- BNZ gets data directly into RAW then cleanses for data products
- Risk of different data views between Enterprise Interfaces and data analytics
- No standard mechanism for sharing data products with applications

**Components:** Data Product Management, Machine Learning/Gen AI Applications, Data Product Market Place

## Slide 58: Current File Transfer and Batch Interactions
**Current Complexity:**
- Multiple technologies and source/destinations
- Individual scripted file transfer jobs
- No visibility of existing jobs and system communications
- Limited Control-M rollout for scheduling

**Two Flow Types:**
1. **Customer Context Flow:** User authorisation required
2. **System Context Flow:** All data covered

## Slide 59: Path to Simplification in Integration Landscape
**Transformation Approach:**
- Move from complex Dynatrace spider web to Enterprise Services with APIs/Events
- Focus on building Enterprise Services that unlock biggest value
- Modify consumers to use Enterprise APIs vs. point-to-point connections
- Deprecate legacy integrations to reduce complexity and support costs

## Slide 60: Application vs Enterprise Data
**Two Distinct Focuses:**

**Application Integration (This TSA):**
- Interconnecting software applications using secure enterprise interfaces
- Streamline workflows for consistent customer/colleague experience
- Connect bounded contexts and platforms for all user contexts

**Data Pipeline (Data & Analytics TSA):**
- Consolidating data from different sources for downstream use
- Create and curate trusted copy data for analytics and reporting
- Ingest, consolidate and curate data from BNZ and external sources

## Slide 61: Appendices
Introduction to appendices section.

## Slide 62: Platforms@BNZ
**Complete Platform Architecture Overview:**
- **Experience Platforms:** Customer Digital, Colleague Digital, Conversational Banking
- **Customer Serving Platforms:** Customer Management, Product Origination, Account Management, Payments
- **Business Enablement Platforms:** Enabling Services, Enterprise Services, Enterprise Data & Analytics
- **Core Technology Platforms:** Enterprise Security, Enabling Technologies

**Platform Dependencies:** Enterprise Interfaces highlighted in aubergine with upstream (wasabi) and downstream (orange) dependencies clearly marked.

---

*This document provides a comprehensive summary of the Enterprise Interfaces Platform Target State Architecture, covering the transformation from legacy point-to-point integrations to a modern, API and event-driven enterprise architecture that enables faster change, real-time responsiveness, and scalable digital operations.*