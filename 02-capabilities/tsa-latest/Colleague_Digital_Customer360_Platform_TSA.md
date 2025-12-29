# Colleague Digital inc Customer360 Platform - TSA - Draft3

## Document Information

**Authors:** Shawn Cawood, Dan Barratt
**Date Produced & Version:** July 2025 v2.0
**Responsible Head of Architecture:** Angus Cotton
**Executive Sponsor:** Karna Luke (Exec Customer Product & Services)
**Primary Platform Stakeholder:** Anna Flower (Exec, Personal & Business Banking)
**Other Stakeholders:**
- GM Approver: Elisa Ashby (GM, Customer 360)
- GM Approver: Steve Brunskill (COO, Partnership Banking)

---

## Slide 1: Cover Page

**Title:** Colleague Digital - Target state Modernisation roadmap

This document outlines BNZ's strategic approach to modernizing the Colleague Digital platform, including Customer360, to enable bankers to serve customers brilliantly through a unified and intentional set of applications.

---

## Slide 2: Version Control

**Document Versioning:**
- **V 0.1** (14/04/2025): Establishing the baseline pack
- **V 2.0** (02/07/2025): Reviewed by GM Architecture & Architecture HO's
- **V 2.1** (05/09/2025): Updated Stakeholder GM C360

**Versioning Guidelines:**
- Draft (0.): V 0.1, V 0.2, etc.
- Post HOA review (1.): V 1.0, V 1.1, etc
- Post Shirley review (2.): V 2.0, V 2.1, etc
- Post Paul Norman / SAA review (3.): V 3.0, V 3.1, etc
- Final approved version (4.): V 4.0
- Periodic/annual updates (5.): V 5.0

---

## Slide 3: Table of Contents

The document is structured into eight main sections:

1. **Executive Summary** - Platform scope, definition and business purpose
2. **Target State Summary** - Summary and value stream view
3. **Simplification & Modernisation Roadmap**
4. **Target Architecture**
5. **Enterprise Context** - Data, Integration & Platform themes (dependencies and interactions)
6. **Platform Horizons** - Technology transition from now to FY27
7. **Risk Overview**
8. **Appendices: Target Architecture**

---

## Slide 4: Section 1 – Executive Summary

This section introduces the comprehensive target state for the Colleague Digital platform, focusing on enabling bankers to serve customers brilliantly through modernized, integrated applications and workflows.

---

## Slide 5: Colleague Digital Platform Overview

**Platform Purpose:** Provide a set of business capabilities to enable bankers to serve customers brilliantly.

**Three Sub-Platforms:**
1. **Customer Relationship Management and Sales** - Enables bankers to manage customer relationships including sales and goals
2. **Customer Fulfilment** - Complete customer enquiries or requests in the moment
3. **Customer Servicing** - Capture, tracking and assignment of long running customer service requests

**Key Strategic Elements:**
- **Unified Banker Experience** for various banker cohorts preserving customer context
- **Anchor Home** for each banker cohort enabling majority of customer-related tasks
- **Deep Link Navigation** between anchor applications
- **Enterprise APIs & Business Events** with API-first approach and open standards
- **Seamless handover to Assisted Channels**
- **Next Best Conversation** capabilities
- **Integrated 3rd Party Ecosystem**

**Roadmap Highlights:**
- Customer360 commenced deployment of Salesforce Lightning and FSC (FY22)
- Retire Salesforce Classic & Retire Assist Forms (FY26)
- Exit NAB Client Centre & transition to EIM document storage (FY27)
- InterAct and Tellers retirement (FY27+)
- All Customer360 technical debt items remediated, Deep Link entrenchment across Anchor Home's (FY27+)

**Current State BMI:** 3540 in July 2024, rising to 4400 in February 2025, with expected reduction to 520 as target state is realized.

**NAB Alignment:** Heavy influence by NAB on BNZ's Colleague Digital Platform with group aligned Salesforce license agreement and common micro-front architecture for developing custom banking screens.

---

## Slide 6: Target State Overview

**Key Points:**
- **Unified Banker Experience UX model** provides framework to deliver optimized experience for each banker cohort
- Platform will grow to support colleague experience as legacy customer serving applications are modernized
- Applications can be deployed for increased banker mobility, both inside and outside BNZ locations
- Data integrations are uplifted to provide better customer context to bankers and share CRM data with BNZ

**Customer Relationship Management & Sales:**
- Customer360 provides CRM and Sales capabilities to all BNZ bankers

**Customer Servicing:**
- Customer360 and Pega Workflow will provide better tracking of customer servicing requests, eliminating re-keying

**Customer Fulfilment:**
- Mini-apps provide standard UI development pattern, allowing bankers to interact with customer accounts, payments and complete other customer transactions 'in the moment'

**Challenges and Issues:**
- **Exec/Stakeholder Support:** Currently no single key stakeholder to provide aligned business strategy or support IC initiatives
- **Siloed Business and Design Teams:** Current teams across Customer360 and BNZ Go operate independently
- **Data/Integration:** Ability to provide all relevant customer data to bankers is hampered by lack of enterprise interfaces

**Technical Focus Areas:**
- **Colleague Experience UX Model**
- **End to End Sales Orchestration**
- **End to End Customer Servicing**
- **Visibility of Customer Data and Activity**

---

## Slide 7: Platform Context

**Platform Definition:** Provides business functionality for bankers to brilliantly serve customers, excluding specialized platforms such as Lending Origination and Collections & Hardship.

**Banker Definition:** Any colleague who provides personalized sales, service or support activities to customers, across the customer lifecycle in any front/middle/back-office role.

**Three Core Capabilities:**

1. **Customer Relationship Management (CRM) and Sales**
   - Enterprise capability enabling bankers to manage customer relationships, including goal and sales tracking

2. **Customer Fulfilment**
   - Optimized user interface to customer serving platforms, allowing bankers to complete customer enquiry or request 'in the moment'

3. **Customer Servicing**
   - Enterprise capability to capture, track and assign long running customer servicing requests

**Service Categories:**
- **Informational:** Product and service descriptions for knowledge and sales discussions
- **Origination & Onboarding:** Support for customer onboarding and product origination
- **Product Servicing:** Customer and product servicing activities (immediate or assigned)
- **Transactional:** Customer transactions, remotely or in-person, including physical branch services
- **Value Add Services:** Customer service request capture and tracking across teams

---

## Slide 8: Platforms@BNZ Context

The Colleague Digital platform operates within BNZ's broader technology ecosystem, aligned with the bank's Technology Strategy to adopt a platform mindset for Intentional Modernisation.

**Platform Position:**
- **In Scope:** Highlighted in aubergine within the platform architecture
- **Up-stream Dependencies:** Highlighted in wasabi
- **Down-stream Dependencies:** Highlighted in orange

**Platform Categories:**
- **Experience Platforms:** Channels, Customer Digital, Colleague Digital, Conversational Banking, Physical Experiences
- **Customer Serving Platforms:** Customer Management, Product Origination & Maintenance, Account Management & Servicing, Payments
- **Business Enablement Platforms:** Enterprise Services, Enterprise Data & Analytics
- **Core Technology Platforms:** Enterprise Security, Enabling Technologies

The platform integrates with multiple other platforms including Customer Identity & Access Management, Open & Proprietary Banking APIs, Marketing & Campaign Management, and various core banking and operational systems.

---

## Slide 9: Section 2 – Target State Summary, Platform Vision

This section outlines the comprehensive vision for the Colleague Digital platform, focusing on providing bankers with intuitive and intentional applications to serve customers brilliantly.

---

## Slide 10: Platform Vision

**Core Vision:** Ensure bankers have an intuitive and intentional set of applications to brilliantly serve customers.

**Five Categories of Activities:**

1. **Informational**
   - Bankers have access to Product and Service descriptions to support initial knowledge and sales discussions

2. **Origination & Onboarding**
   - Bankers are able to support customer onboarding and product origination

3. **Product Servicing**
   - Bankers support customers with customer and product servicing activities (completed in the moment or captured, tracked and assigned)

4. **Transactional**
   - Bankers complete customer transactions, remotely or in-person, with BNZ's branch network facilitating physical transactions

5. **Value Add Services**
   - Bankers provide value-add services to improve customer satisfaction and contribute to BNZ's revenue streams

**Unified Banker Experience Framework:**
Every banker colleague will have an 'Anchor Home Interface' providing an intuitive and intentional set of applications. The 'home anchor' depends on the banker cohort/persona, with deep link integration of capabilities between anchor home bases, achieving a unified banker experience and "single interface" or "single pane of glass" for all tasks.

---

## Slide 11: Banker Cohorts

**Target User Base:** Over 3,600* bankers providing value to customers across various outcomes and physical locations.

**Banker Categories:**

1. **Service & Transactional Bankers**
   - Task driven, helping customers complete sales or servicing tasks
   - Tasks originate from customers, task queues, or internal systems
   - Includes: Frontline Bankers (Service Focus), Operational Excellence Processing Teams, Credit Teams

2. **Value Chain Bankers**
   - Support long running value chains, typically towards business onboarding or product origination
   - Includes: Frontline Bankers (Sales Focus), Responsible Business Customer Assist Team

3. **Relationship & Growth Bankers**
   - Maintain long-term relationships with customers, providing trusted guidance towards short and long-term needs
   - Includes: Partnership Banking Relationship Bankers, Corporate & Institutional Bankers

**Physical Work Locations:**
- **Customer Site:** Bankers travel offsite for face-to-face customer engagement
- **BNZ Branch Network:** Desk-based and mobile bankers around branch and Partners Centre network
- **BNZ and Partner Offices:** Office-based support and customer communication
- **Working from Home:** Remote access using laptops with BNZ network access

*Based on number of Salesforce FSC licenses (March 2024)

---

## Slide 12: Unified Banker Experience

**Framework Goals:**
1. Each banker has a defined 'anchor' application where they can perform 80% of customer related tasks
2. High quality UX design principles to improve efficiency and reduce manual errors
3. Navigation between anchor applications, preserving customer context

**Anchor Applications:**

- **Customer360:** CRM+Sales, Lending Origination for Frontline Bankers (Sales Focus), Operational Excellence teams, and Credit Teams
- **BNZ Go:** Customer/Product Maintenance for Frontline Bankers (Service Focus)
- **Pega Workflow:** Customer Service Workflow/Cases for Operational Excellence teams
- **Specialist Tools:** Collections, Trade Finance, Markets for Specialist Teams

**Navigation Types:**
- **Deep Link:** Hyperlink between anchor applications, preserving customer context
- **Standard Link:** Hyperlink to supporting applications, improving banker flow

**Supporting Applications:** OmniMax, DealPoint, Valocity, Figured, Equifax integrate through deep linking to maintain context and workflow efficiency.

---

## Slide 13: Colleague Digital Vision

**Top 5 Modernisation Objectives:**

1. **Complete CRM goals of Customer360 program**
   - Fully retire Salesforce Classic
   - Migrate C&IB bankers from NAB Client Centre to C360
   - Trial and adoption of further FSC features to increase platform value

2. **Modernise Customer Fulfilment Apps**
   - Hollowing-out of monolithic applications (InterAct, Tellers) into modern miniapp architecture
   - Reassessment and redesign of existing features based on current banker needs

3. **Unified Banker Experience**
   - Identify UX best practices to increase banker flow and eliminate cognitive load and human error
   - Identify UX patterns to enable navigation and data re-use across BNZ and vendor applications
   - Enable mobility across devices and locations

4. **Uplift of Sales/Servicing Task Tracking**
   - Retire Assist and other apps promoting re-keying
   - Integration of front-office CRM and back-office workflow platforms
   - Enable customer visibility of service requests
   - All sales tasks tracked and prioritized in C360

5. **Enterprise Data/Interfaces**
   - Build Enterprise Data Interfaces in/out of FSC
   - Data can be used in other operational systems
   - Ability to deliver activity feed of relevant historical customer events
   - Egress of activity feed of bankers

**Vision Statement:** Provide an intentional and intuitive toolset to bankers, enabling them to provide a world class experience to customers.

---

## Slide 14: Modernisation Overview

**Three-Phase Modernisation Approach:**

**Phase 1: Simplify & Modernise (In Scope FY26)**
- **Now: Standardise on Customer360 and BNZ Go**
  - Customer360 as BNZ's single consolidated CRM tool for all bankers
  - BNZ Go provides banker interface into core banking and other product platforms, replacing legacy customer fulfilment apps
  - Clarify design principles and UX integration patterns for ongoing platform capability development

**Phase 2: Automate & Integrate (Target State not defined)**
- **Next: Automation & Integration**
  - End-to-End Customer Servicing: Design and deploy wholistic solution for capturing, tracking and fulfilling customer service requests
  - End-to-End Leads Orchestration: Automate manual tasks of capturing, assigning and tracking sales leads across Marketing, Digital Channels, Analytics and Customer360
  - Customer Data/Events: Replace 'Diary Notes' with fit-for-purpose solution for bankers to understand historical customer journey context
  - Enterprise APIs (to be refined)
  - Business Events (to be defined)

**Phase 3: Innovate**
- **Then: Grow Capabilities**
  - Identify opportunities to introduce agentic and generative AI tools to enhance colleague experience
  - Dependent on Enterprise AI foundations and guardrails

---

## Slide 15: Colleague Digital Dependant Platforms

The Colleague Digital platform provides user experience over most Customer Serving platforms while providing bank capabilities in its own right. Complex platform inter-dependencies may require investigation and capability re-alignment.

**Platform Relationships:**

**Customer Platforms:**
- Customer Engagement ↔ Customer Relationship Management and Sales
- Customer Master ↔ Customer Relationship Management and Sales
- Customer Onboarding ↔ Customer Fulfilment
- Customer Lifecycle ↔ Customer Fulfilment

**Lending Origination Platform:**
- Lending Origination ↔ Customer Relationship Management and Sales
- Product Hierarchy ↔ Customer Relationship Management and Sales

**Customer Digital Platform:**
- WWW, Online Banking ↔ Customer Fulfilment

**Conversational Banking Platform:**
- Colleague Softphone, Messaging/Voice/Video Channels ↔ Customer Relationship Management and Sales

**Core Banking Platforms:**
- Customer Arrangements, Collateral Management ↔ Customer Servicing
- Domestic Payments, International Payments ↔ Customer Servicing

**Process, Workflow & Workforce Management:**
- Workflows ↔ Customer Servicing

**Key Integration Points:**
- Sales Leads/Goals, Appointments, Service Cases, Interaction Summaries
- Service Forms, Customer Open/Maintain, Product Open/Maintain
- Payments, Physical Transactions

⚠️ Denotes complex platform inter-dependency, potentially requiring remediation

---

## Slide 16: Value Chain – Colleague Digital Platform

The platform delivers two value streams:
1. **Experience/Channel Value Chain** - Effectively being the Colleague Channel
2. **Customer Relationship & Sales/Service Value Chain** - CRM sub-platform capabilities

**Experience/Channel Value Chain:**
- **Presentation:** Responsive Experience, Colleague Experience, Personalisation, Context Aware, Mobility
- **Consolidation:** Interaction History, Information Architecture, Screen Flows
- **Orchestration:** One way-Same way, Context Preservation

**Customer Relationship & Sales/Service Value Chain:**
- **Identify:** Household Model, Account relationships, Contact relationships, Person Accounts
- **Understand:** Financial Goals, Business Milestones, Life Events, Matrix Tables, Expression Sets, Product Catalogue
- **Assist:** Account Enquiries, Product Catalogue, Product Matching, Product Origination, Sales Lead Management
- **Service:** Account Maintenance, Payments, Physical Transactions, Service Catalog, Service Management

**Platform Dependencies:**
- **Input:** Experience, Customer Serving and Core Technology Platforms
- **Output:** Business Enablement Platforms

---

## Slide 17: Stakeholder Engagement and Accountability

**Comprehensive Stakeholder Engagement Process:**

**Key Stakeholders Consulted:**

**CP&S (Customer Product & Services):**
- Karna Luke (Exec), Angela Payne (GM - Customer360), Alisa Ashby (GM - Customer360), Michelle Taylor (Head of Design & Enablement)

**Partnership Banking:**
- Anna Flower (Exec), Steven Brunskill (COO), Megan Scholey (Head of Strategic Transformation), Michelle Trubshoe (Head of Management Assurance)

**Corporate & Institutional Banking:**
- Peny Ford (Exec), Morag McCaw-Pretty (Head of Strategic Initiatives & Conduct)

**Operational Excellence:**
- Deanne Nicholas (GM - Service & Payment Operations), Alina Barota (GM - Colleague & Customer Support Ops)

**Technology (Architecture & Build&Run):**
- Shirley McIntyre, Angus Cotton, Michelle Maxwell, Adam McLoughlin, Andy Hamilton, Matt Davin, Ben Hamid, Thomas Marshall

**Engagement Process:**
1. **Initial Context Discussion:** Basic slides to describe context, set the scene, and gather current problems, business direction, and wish-list items
2. **Draft Pack Review:** Follow-up sessions to explain proposed target state and roadmap, gathering feedback for pack refinement

---

## Slide 18: Stakeholder Input Summary

**Key Feedback Themes:**

**Karna Luke (Exec, CP&S):** "Our ambition is for a single interface" - desires Customer360 to be an intuitive, unified experience enabling colleagues to meet customer needs accurately, efficiently and seamlessly.

**Steven Brunskill (Partnership Banking):** Emphasized boundaries between platforms aren't clear cut in practice, "One-way, Same-way – what is the right platform," and handling same customer requests through multiple channels.

**Angela Payne (GM, C360):** Important to have unified experience and shared business language across Customer360 and BNZ Go. Suggested Customer360 as a combined platform.

**Paul Norman (Exec, Tech):** Need to manage risk profile of using SaaS platforms, avoiding regrettable vendor lock-in.

**Megan Scholey (PB):** Bankers want more proactive outreach options beyond email and phone, ways to optimize operating model and customer workflow, mobile app and Outlook integration requests.

**Michelle Taylor:** Lack of single exec owner for platform, need for common language across apps to avoid banker confusion during system navigation.

**Deanne Nicholas (GM, OpEx):** Wants work for teams tracked in one place, categorized and assigned to next available colleague.

**Morag McCaw-Pretty (C&IB):** Tools needed already exist in BNZ, just need enabling for C&IB bankers and customers.

**Relationship Managers:** Need quick access to customer details and task/note recording on mobile devices while on the move.

---

## Slide 19: Section 3 – Simplification & Modernisation Roadmap

This section details the comprehensive roadmap for transforming the Colleague Digital platform from current state legacy systems to a modern, integrated target state architecture.

---

## Slide 20: Simplification & Modernisation Roadmap Overview

**Strategic Focus Areas:**

**FY25-FY26: Focus on Simplification and Modernisation**

**Customer Relationship Management:**
- Salesforce Classic Retirement → Salesforce FSC
- NAB Client Centre Exit → Customer360
- Microsoft Bookings → Salesforce Scheduler transition
- Business Events implementation (Appointment Booking first, full suite to follow)
- API Modernisation (Case & Leads, Salesforce/AWS, Graph API Outlook Sync)

**Customer Fulfilment:**
- InterAct retirement → BNZ Go Miniapps
- Tellers Ecosystem Discovery/Design → re-build into miniapps
- Core Banking Platform overlap integration (Deposits Open/Maintain, Loans Maintain)

**Customer Service Workflow:**
- Assist Forms Replacement → Pega Workflow/C360 integration
- Workflow, Automation & Robotics Platform overlap management

**FY27 and Beyond: Look to the Art of the Possible**

**Advanced Capabilities:**
- C&IB Growth Uplift & Features
- Enterprise API Future Adoption
- Salesforce Mobile App consideration
- MS Outlook Integration
- Digital Integration (TBC)

**Infrastructure Modernisation:**
- Document Generation Rebuild → HotDocs Retirement
- Document Management Rebuild → MCF Retirement
- Information Management Platform overlap resolution

**Patterns/Guardrails:** Unified Banker Experience Design (Persona Discovery, Anchor app alignment, Common Language)

**Legend:**
- 🟦 Current platform investment (funded)
- 🟨 Future platform investment (unfunded)
- 🟧 In progress, but unfunded

*This is a draft view of a proposed transition roadmap. Further refinement required to understand prioritization and resourcing for delivery, based on agreed funding envelope.*

---

## Slide 21: Roadmap - Applications

**Application Modernization Timeline:**

**Customer Relationship Management & Sales:**
- **Phase Out (2025-2026):** Salesforce "Classic" CRM, NAB Client Centre, Microsoft Bookings
- **Phase In (Ongoing):** Salesforce Financial Services Cloud, BNZ C360 integrations, Customer360 FSC Managed Groups Sync
- **Target State:** Salesforce FSC Mobile, Appointment Booking Service, Interaction Summary Service

**Customer Servicing:**
- **Phase Out (2024-2026):** Assist, Assist Forms API
- **Phase In (Ongoing):** MyRequests Miniapp, Find Form Miniapp, Forms Miniapp
- **Continuing:** Assist Forms on Pega Low Code

**Customer Fulfilment:**
- **Phase Out (2024-2027):** InterAct, Tellers Customer System, CustomerInformationReportService, MUP Replacement, RudderStack
- **Phase In (Ongoing):** BNZ Go, Multiple miniapps including Customer Notes, Customer Profile, Transaction Feed, Accounts, Homeloans
- **Target State:** Comprehensive miniapp ecosystem replacing legacy monolithic applications

**Key Notes:**
1. Approximately 30 current and planned BNZ Go Miniapps are excluded for brevity
2. Up-to-date visualizations of the roadmap for platform assets are available in LeanIX

**Application Lifecycle States:**
- 🔵 Active (continuing development/operation)
- 🟡 Phase Out (planned retirement)
- 🔴 Retired (decommissioned)
- ⚪ Plan (future implementation)

---

## Slide 22: Modernisation Tipping Point

**Platform Modernization Progress:**

**Customer Relationship Management & Sales:**
- **Current Status:** Modernization started with Salesforce Customer360 introduction (FY24/25)
- **Tipping Point:** EOFY26 after decommissioning Salesforce Classic and exiting Client Centre applications
- **Progress:** Steady transition from legacy assets to modern platforms

**Customer Servicing:**
- **Current Status:** Small number of applications (6) in sub-platform
- **Tipping Point:** EOFY26 when Assist has been fully retired
- **Note:** Small application count precludes accurate tipping point calculation

**Customer Fulfilment:**
- **Current Status:** Modernization started FY22/23 with BNZ Go introduction to replace InterAct, Tellers and other colleague-facing applications
- **Tipping Point:** EOFY27 when InterAct and Tellers applications are fully retired
- **Scope:** Approximately 30 current and planned miniapps excluded from this view

**Metrics Tracked:**
- **Invest Assets:** Modern, actively developed platforms (increasing trend)
- **Divest Assets:** Legacy platforms scheduled for retirement (decreasing trend)
- **Total Assets:** Overall platform portfolio size
- **Platform BMI:** Business Maintainability Index improvement over time

**Visual Indicators:**
⭐ Marks the modernization tipping point for each sub-platform where modern assets outnumber legacy systems

---

## Slide 23: Section 4 – Target State Architecture

This section provides detailed architectural views of the target state for the Colleague Digital platform, including technology components, integration patterns, and platform relationships.

---

## Slide 24: Target State Architecture Overview

**Platform Architecture Components:**

**Customer Relationship Management & Sales:**
- **Core Applications:** Salesforce Customer360, Salesforce Mobile App
- **Supporting Services:** Salesforce Scheduler, Salesforce Financial Services Cloud, BNZ C360 - nCino
- **Integration Components:** Multiple integration and IT components for seamless data flow

**Customer Servicing:**
- **Core Applications:** Salesforce Customer360, Customer Requests Miniapp, MyRequests Miniapp
- **Workflow Management:** Salesforce Financial Services Cloud, Salesforce Service Cloud, Forms Miniapp, Find Form Miniapp
- **Process Integration:** Process, Workflow and Workforce Management connections

**Customer Fulfilment:**
- **Core Platform:** BNZ Go with comprehensive miniapp ecosystem
- **Miniapp Portfolio:** What's New, Registry Services, Banker Activity Microservice, Customer Notes, Overview, Relationships, Customer Profile, Customer Search, Channel Access, Authorities Overview, Customer Authentication
- **Banking Services:** Customer and Party Master, Transaction Feed, Accounts, Homeloans, Rewards, Cards MiniApp, Loyalty Offers & Rewards, Card Issuing & Mgt, Enterprise Information Management, Funds Transfer, Domestic Payments, Interest Rate Calculator, Information Reports, Repayment Calculator, Affordability
- **Core Banking Integration:** Core Banking Ledger, Branch Maintenance, Cash Drawer Balancing, Cash Drawer Transactions, YouWealth, Branch experience, Investment & Private Wealth

**Technology Stack:**
- **Backend Systems:** Everyday Banking Product Origination, Lending Origination (KiwiSaver, Transactional, Term Deposits)
- **Supporting Platforms:** Data & Analytics, Conversational Banking, Collections and Hardship, Customer and Party Lifecycle Management, Customer Engagement

**Legend:**
- 🟦 Placeholder
- 🟢 Innovate (Invest)
- 🟡 Encourage (Invest)
- 🟠 Contain
- 🔴 Exit (Divest)
- 🟤 Retired

---

## Slide 25: Target State Architecture Overview - Sub-Platform Details

**Customer Relationship Management & Sales:**
- All BNZ bankers migrated to Salesforce Customer360 from legacy instances (Classic and NAB Client Centre)
- Enables true 'One way, same way' for sales and service across BNZ
- Salesforce mobile app enables Relationship and Growth bankers to access relevant customer data in various locations

**Customer Servicing:**
- Consolidation of customer servicing activity onto Salesforce Customer360 and Pega Workflow
- Simplifies IT landscape and reduces re-keying between systems
- Efficient use of task prioritization/routing and workforce management improves operating efficiency and speeds up time to resolution

**Customer Fulfilment:**
- BNZ Go and miniapps provide single experience and information architecture for majority of customer fulfilment tasks
- As legacy applications from other Customer Serving platforms are modernised, additional miniapps are created to provide colleague experience
- Miniapps are the primary engineering pattern for building custom user interfaces to colleagues

---

## Slide 26: NAB Alignment

**Extent of Alignment for Colleague Digital Platform:**

**Aligned Elements:**
- **Group-aligned Salesforce license arrangement**
- **Shared NAB-X libraries for building miniapps**
- **Aligned platform scope and purpose**
- **Shared micro-frontend architecture**
- **Common microservice/ACL pattern integrating Salesforce to the enterprise**

**BS11 Threshold Maintained:**
- **Separate Salesforce instances for BS11 purposes (as per target state)**
- **No group-shared miniapps**

**Alignment Levels:**
- **L1:** Strategy and Enterprise Architecture Alignment
- **L2:** Vendor and Contract Alignment
- **L3:** Common solution architecture
- **L4:** Shared codebase for individual instances
- **L5:** Codebase shared but separate pipelines and hosting environments
- **L6:** Codebase and pipeline shared (separate application instances)
- **L7:** Single (shared) application instance
- **L8:** Service (including business operation) provided by one party for Group

**BNZ Position:** Maintains separate applications and associated codebases while leveraging shared architecture patterns and vendor relationships. Alignment focuses on L1-L4 levels while maintaining operational independence above the BS11 threshold.

**Strategic Benefits:**
- Cost efficiencies through shared licensing
- Accelerated development through shared libraries
- Architectural consistency across NAB Group
- Maintained regulatory compliance and operational independence

---

## Slide 27: Technology Guardrails - Salesforce

**Salesforce Platform Governance Framework:**

**Interoperability and Integration:**
- API-First with Open Standards and Business Events
- Data Portability Strategy
- Data as Enterprise Asset
- Integration Patterns and Anti-Corruption Layer
- Event-Driven Architecture (EDA)
- Customer Master Integration
- Document Management Integration

**Data Privacy and Security:**
- Data Residency requirements
- Vendor Security Audits
- Data Backups and Recovery
- Key Management
- SaaS Security Best Practices
- Banking-Specific Controls

**No Customisation only Configuration:**
- Configuration over Customisation approach
- Moderate Configuration limits
- Managed Packages utilization
- Code Reviews for any custom development
- Technical Debt Management
- Financial Services-Specific Components

**Vendor Management and Exit Strategy:**
- Contract Negotiation protocols
- Exit Strategy planning
- Alternate Solutions identification
- Business Continuity planning
- Service Level Agreements (SLAs)
- Performance Monitoring

**Monitoring and Performance:**
- Salesforce Optimizer utilization
- Capacity Planning
- Performance monitoring protocols

**Salesforce Lightning and FSC CRM Capabilities:**
- 360-degree customer views (sourced from Customer Master)
- Relationship mapping (Households, business relationships)
- Interactions and client engagement tracking
- Referrals and leads management
- Opportunity management for banking products
- Client onboarding workflows
- Branch and banker management tools
- Banking-specific engagement tracking
- Client meeting preparation and follow up
- Relationship-based banking insights

**Critical Integration Statements:**
- **Customer Master Integration:** Salesforce is NOT the customer master system. Proper integration maintained with bank's authoritative customer data systems.
- **Document Integration:** Salesforce is NOT the document management system. Integration maintained with Enterprise Information Management (EIM) system.

---

## Slide 28: Strategic Alignment (Themes)

**Alignment with BNZ Strategic Ambition through Technology Themes:**

**Modernise and Simplify:**
- Platform delivers goal of modern and simple platform
- Known roadmap to replace legacy applications with modern fit-for-purpose applications (Salesforce FSC, BNZ Go)
- Strong "no customisation" rule ensuring ongoing vendor updates
- Enterprise integration patterns enable contribution to overall technology and data ecosystems

**Agile and Adaptable:**
- Salesforce adoption with strong "no customisation" rule ensures ongoing vendor updates
- Enterprise integration patterns enable applications to contribute to overall technology and data ecosystems
- Technology platforms of Salesforce and BNZ Go reduce time to market for ongoing agile feature delivery

**Platform Mindset:**
- Salesforce provides evergreen platform supporting overall sales and servicing capabilities
- Can be customised to capture different service types, sales leads, customer interactions and customer knowledge
- BNZ Go and miniapps provide re-usable pattern and extensible platform for delivering colleague-facing interfaces

**Resilient, Secure and Safe:**
- Continue to maintain close vendor relationship for enhancing security profile of SaaS solution through BNZ standard due diligence process
- Supporting assets conform to engineering recipes and inherit security and resiliency that BNZ has industrialised in patterns

**Deeply Digital:**
- Platform target state aims to provide integrated solution to track sales leads and service enquiries
- Need for colleague forms and re-keying of information between colleague systems intends to be significantly reduced by building data integrations across strategic platforms
- Salesforce FSC and intended integrations will be key to delivering omnichannel sales and servicing capability to customers

---

## Slide 29: Section 5 – Enterprise Context, Data Integration and Interactions

This section outlines how the Colleague Digital platform integrates with the broader enterprise ecosystem, including data flows, integration patterns, and platform dependencies.

---

## Slide 30: Contextual Impacts

**Data Integration Requirements:**

The Colleague Digital platform requires data integration for two main purposes:

1. **Bi-directional interaction with most Customer Serving Platforms**
   - Data can be accessed in real-time or cached for performance and referential integrity purposes

2. **CRM data mastered in Salesforce**
   - Published into operational and analytical planes using API and Event interfaces

**Further hydration of customer data into Customer360** enables easier access by colleagues (and by Salesforce AI agents supporting colleagues)

**Integration Flows:**

**Downstream (Colleague Digital provides to):**
- Infrastructure Foundations: CM Platform Backup
- Customer Master: Legacy Managed Groups Sync
- Operational Observability: Logging Data
- Data & Analytics: Data warehouse hydration, Next Best Conversation
- Customer and Party Lifecycle Management: Onboarding Sync
- Process, Workflow and WFM: Servicing Case
- Domestic Payments: Funds Transfer
- Collections & Hardship: Customer Data
- Everyday Banking Product Origination: Create Account
- Lending Origination: Start Lending Process

**Upstream (Colleague Digital consumes from):**
- Customer and Party Master: Customer Data
- Colleague Identity & Access Management: Access Management, Organisation Hierarchy and Staff data
- Workplace Technologies: User Credentials, Data UI Components
- Customer Engagement: Next Best Conversation
- Data & Analytics: Reference Data
- Website, Sales & Acquisition: Sales Lead, Servicing Case, Appointment Booking
- Conversational Banking: Colleague Softphone
- Core Banking Ledger: Customer Accounts
- Card Issuing & Management: Card Details, Maintenance
- Investment & Wealth: KiwiSaver, Managed Funds
- Transaction Switch: Payment Details
- Loyalty Offers & Rewards: Loyalty Details
- Enterprise Information: Document Details, Generation

**Key Integration Patterns:**
- 🟢 Existing enterprise grade
- 🟡 Existing integration, but requires uplift/modernisation
- 🔴 Tech Debt, needs replacing
- ⚙️ Events
- 🔵 API
- 📊 Managed Connectors
- 📁 ETL / Files

---

## Slide 31: Colleague Digital Platform Boundaries and Guardrails

**Platform Definition:**
The purpose and scope of the colleague digital platform is to provide business functionality used for bankers to brilliantly serve customers. This excludes specialized platforms such as Lending Origination and Collections & Hardship (having their own functionality).

A banker is defined as any colleague who provides personalised sales, service or support activities to customers, across the customer lifecycle in any front/middle/back-office role.

**Boundaries (of sub-platforms):**
- **Salesforce** drives the experience for unified banker desktop
- **Colleague-focused functionality** available OOTB from SaaS assets
- **nCino:** lending origination, internal facing, integrated into Salesforce, not for Customer experience delivery apart from product hierarchy structure
- **EXUS:** collections and hardship
- **PEGA:** human centered workflow
- **BNZ Go:** miniapp pattern for solving feature gaps where banker experience requires features not solved in Salesforce, nCino, Fenergo, Exus as features relate to core banking back-end capability
- **Amazon Connect:** part of Colleague Digital Experience but in the platform called Conversational Banking
- **Relies on BNZ Customer Master** for customer hydration

**Guardrails:**
- **Manages all colleague digital interaction** for Sales and relationship management teams
- **Configuration not Customisation** of SaaS assets. Functionality unable to be configured is accessed via integration
- **Integration via enterprise interfaces:** APIs, Business and CDC events, defined enterprise data products
- **SaaS assets kept evergreen** by regularly upgrading to latest vendor supported version
- **PII controls heavily monitored,** no SaaS product will be Customer Master
- **3rd party risk controls** require Australia regional SaaS hosting

**Build vs Buy Decision Matrix:**
The platform operates across the spectrum from System of Record to System of Differentiation, balancing Data Producer/Consumer roles, NPS impact levels, and frequency of change requirements.

**Vendor Ecosystem:**
- **Core SaaS Platforms:** Salesforce, nCino, PEGA, Amazon (AWS), EXUS, Fenergo
- **BNZ Custom Development:** BNZ Go miniapp framework

---

## Slide 32: Section 6 – Platform Horizons

This section outlines the technology transition timeline and modernisation horizons for the Colleague Digital platform from current state through FY27 and beyond.

---

## Slide 33: Modernisation Horizons

**The majority of the journey is to SIMPLIFY & MODERNISE** via standardising on Customer360 and BNZ Go, providing colleague banker cohorts with single consolidated customer relationship management tools and banker interface into core banking and other product platforms. **TECH STACK SIMPLIFICATION** modernises customer service workflow for operational excellence cohorts.

**Timeline Overview:**

**FY25-FY26: Simplify & Modernise**

**Customer Relationship Management:**
- Salesforce NAB Client Centre → Salesforce FSC
- Salesforce Classic CRM → Salesforce FSC
- Microsoft Bookings → Salesforce Scheduler
- Marketing Lead Integration
- Lead Scoring + Prioritisation
- Customer Journey Tracking

**Customer Service Workflow:**
- Assist Forms → Pega Workflow
- Tech Stack Simplification

**Customer Fulfilment:**
- EMAX Channel Maintenance → BNZ Go Miniapps
- IBIS – Lending Screens → BNZ Go Miniapps
- IBIS – Term Deposit Screens → BNZ Go Miniapps
- Payment Switch Modernisation → BNZ Go Miniapps

**FY27: Tech Stack Simplification**
- InterAct → BNZ Go Miniapps
- Tellers → BNZ Go Miniapps

**FY28+: Omnichannel Integration**
- Salesforce Mobile App
- Salesforce/Pega Workflow Integration
- Advanced integration capabilities

**Key Milestones:**
⭐ **Modernisation Tipping Point FY26:** Customer Relationship Management and Customer Service Workflow
⭐ **Modernisation Tipping Point FY27:** Customer Fulfilment

**Legend:**
- 🟦 Funded and Planned
- 🟨 Unfunded - Future Plan
- 🔲 Exit/Modernisation Required
- ⚙️ Modernisation Target

---

## Slide 34: Section 7 – Risk Overview of Current State

This section provides analysis of the current state architecture, identifying key risks, challenges, and pain points that the target state modernisation will address.

---

## Slide 35: Current State Architecture Overview (1/2)

**Current Architecture Challenges:**

**Customer Relationship Management & Sales:**
- **Legacy Systems:** Microsoft Bookings, Salesforce Customer360, Salesforce Classic CRM, Salesforce NAB Client Centre
- **Modern Systems:** Salesforce Financial Services Cloud, BNZ C360 - nCino integration
- **Integration Components:** Multiple integration and IT components with varying levels of modernisation

**Customer Servicing:**
- **Legacy Forms:** CRM Servicing (Colleague Forms), Assist, Customer Requests Miniapp, MyRequests Miniapp
- **Modern Workflow:** Salesforce Financial Services Cloud, Salesforce Service Cloud, Forms Miniapp, Find Form Miniapp

**Customer Fulfilment:**
- **Legacy Systems:** BNZ Go, What's New Miniapp, BNZ Go, RAPID (Legacy Integration Connector), InterAct, Tellers Customer System
- **Miniapp Ecosystem:** Customer Notes, Overview, Relationships, Customer Profile, Customer Search, Channel Access, Authorities Overview
- **Core Banking:** Transaction Feed, Accounts, Homeloans, Affordability, DocMan, Funds Transfer, KiwiSaver
- **Supporting Services:** Rewards, Cards MiniApp, Loyalty Offers & Rewards, Card Issuing & Mgt, Domestic Payments

**Platform Dependencies:**
- Colleague Identity & Access Management, Conversational Banking, Collections and Hardship, Customer and Party Lifecycle Management, Customer Engagement, Data & Analytics

**Key Risk Areas:**
- Multiple legacy systems requiring maintenance and integration
- Complex interdependencies between platforms
- Aging technology stacks with limited support
- Data consistency challenges across multiple systems

---

## Slide 36: Current State Architecture Overview (2/2)

**Sub-Platform Analysis:**

**Customer Relationship Management & Sales:**
- Customer360 program has achieved modernisation tipping point but has not completed planned exit/decommission of legacy applications
- **Remaining Legacy:** Salesforce Classic (and integrations), Salesforce NAB Client Centre, Microsoft Bookings
- Bankers continue using Salesforce Classic pending migration of 3 remaining use cases: Credit Workflow (nCino), CPE Case (nCino), FATCA case (Pega Low Code)
- Customer360 instance remains 'MVP' implementation, not yet achieving full banker adoption or unlocking full potential of purchased product

**Customer Servicing:**
- Customer service task capture and transfer is fragmented across various applications and office tools:
  - Assist Forms
  - Salesforce Service Cases
  - Pega Workflow (defined in separate platform)
  - K2 Workflow (defined in separate platform)
- Significant technology simplification achievable by considering these applications as single capability

**Customer Fulfilment:**
- Development of miniapps remains key modernisation activity to remediate legacy applications
- Current FY25 delivery focus supports Core Ledger Replacement program
- Lack of Enterprise APIs from dependent domains demands ongoing use of legacy integration patterns (Web Services)
- **High Risk:** InterAct and Tellers both have high risk of non-recoverable failure due to complex and unsupported technology underpinning

---

## Slide 37: Current State Landscape - Applications

**Application Portfolio Analysis by BMI (Business Maintainability Index):**

**Customer Fulfilment (High Risk Applications):**
- **CST InterAct (BMI: 200)** - High risk legacy system
- **CST Tellers Customer System (TCS) (BMI: 200)** - High risk legacy system
- **CustomerInformationReportService (BMI: 120)** - Moderate risk
- **InterAct (BMI: 220)** - Highest risk legacy system
- **Maintain User Profile (MUP) (BMI: 160)** - High risk
- **RAPID Legacy Integration Connector (BMI: 220)** - Highest risk
- **Tellers Customer System (BMI: 220)** - Highest risk

**Modernised Applications (Low BMI):**
- **Multiple BNZ Go Miniapps (BMI: 0)** - Banker Activity, Customer Notes, Overview, Relationships, Transaction Feed, etc.
- **Modern Integration Components (BMI: 0)** - New miniapp architecture

**Customer Relationship Management & Sales:**
- **BNZ C360 - FSC Managed Groups Sync (BMI: 180)** - Moderate risk
- **BNZServiceGateway (BMI: 240)** - High risk legacy integration
- **Salesforce "Classic" CRM (BMI: 240)** - High risk legacy system
- **Microsoft Bookings (BMI: 120)** - Scheduled for replacement

**Customer Servicing:**
- **Assist (BMI: 200)** - High risk, scheduled for retirement
- **Assist Forms API (BMI: 180)** - High risk legacy system
- **Forms Miniapp, MyRequests Miniapp (BMI: 0)** - Modern solutions

**Risk Assessment:** Applications with BMI scores above 100 represent significant technical debt and operational risk, while BMI 0 applications represent modern, maintainable solutions.

---

## Slide 38: Current State Landscape - IT Components

**IT Component Analysis:**

**Colleague Digital incl Customer 360:**

**Customer Relationship Management:**
- **AutoRABIT BNZ C360 - ARM 4.0 (BMI: 0)** - Modern deployment automation
- **AutoRABIT BNZ C360 - CodeScan (BMI: 0)** - Modern code quality management
- **Salesforce Hosting Platform (BMI: 0)** - Modern cloud platform

**Component Portfolio Status:**
The IT component landscape shows significantly better modernisation progress compared to applications, with most components already modernised to BMI 0 status. This indicates strong foundational technology infrastructure supporting the platform modernisation journey.

**Key Observations:**
- **Low Technical Debt:** Most IT components have achieved BMI 0 status
- **Modern Infrastructure:** Salesforce hosting platform provides stable, evergreen foundation
- **Automation Tools:** AutoRABIT deployment and code quality tools support modern DevOps practices
- **Platform Readiness:** IT component modernisation enables application layer transformation

---

## Slide 39: Key Pain Points – and Opportunities

**Summary of Current Challenges and Strategic Opportunities:**

**Challenges & Issues:**

**Exec/Stakeholder Support:**
- No single key stakeholder to provide aligned business strategy or support IC initiatives for combined platform
- Lack of funding support inhibits progress towards target state

**Siloed Business and Design Teams:**
- Current business and design teams across Customer360 and BNZ Go operate independently
- Potentially delivering disjointed experience to users

**Data/Integration:**
- Ability to provide all relevant customer data to bankers hampered by lack of enterprise interfaces from Customer Serving platforms
- Limited analytical capability (e.g., generating customer activity timeline)
- Data mastered in Colleague Digital platform not fully provided for enterprise consumption

**Risks (from GRACE):**
- RSK-1290 Unsuitable Sales or Lending Risk
- RSK-1242 Product Management Risk
- RSK-170 Internal Fraud
- RSK-1297 Third Party Risk

**Current BMI Issues:**

**Customer Relationship Management & Sales:**
- Customer360 program has hollowed out majority of Salesforce Classic app
- Further effort needed to migrate remaining use cases to target state before decommissioning

**Customer Fulfilment:**
- Legacy Tellers, InterAct and supporting applications are EOL
- Expected to be remediated per 2019 APRA commitment
- Funding and priority remain issues
- Tellers remains high risk due to aging state, lack of engineering resource, limited BCP options

**Customer Servicing:**
- Assist application has high BMI score due to complex architecture and aging technology set

**Opportunities:**

**Omnichannel Sales & Servicing:**
- Current Sales & Servicing processes fragmented across channels (Digital vs Assisted)
- Omnichannel approach across platforms can contribute to world class customer experience

**CRM Uplift:**
- Current Customer360 CRM implementation is modern and simple
- Hasn't yet uplifted BNZ's CRM capability to leverage purchased features

**Future Thinking:**
- Complaint & Disputes platform TSA to be finalised
- Includes specialised CRM capabilities (e.g., Distress) which may be revised into Colleague Digital or another platform

---

## Slide 40: Focus Areas

This section identifies four critical technical focus areas that require attention to achieve the target state vision for the Colleague Digital platform.

---

## Slide 41: Technical Focus Areas

To support the move towards the proposed target state, the following focus areas have been identified as relevant, either as foundational enabling aspects or unknown areas that would require further refinement:

**Colleague Experience UX Model:**
- The Customer360 program has promoted a 'single pane of glass' experience, expecting that bankers can operate within the Salesforce app
- A more achievable approach is to aim for a 'unified banker experience' model, ensuring ease of navigation between key applications

**End to End Sales Orchestration:**
- A number of early stage lead processes are tracked outside of a CRM platform, limiting visibility and prioritisation
- BNZ has no capability to track customer sales journeys, limiting our ability to optimise the sales funnel

**End to End Customer Servicing:**
- BNZ has a number of disparate systems, used to track customer service activities for different teams
- A wholistic solution must be considered, spanning platforms, to support customer and colleague needs

**Visibility of Customer Data and Activity:**
- The current 'Diary Notes' datasets in BIS are no longer fit for purpose, and need to be redesigned
- Bankers need good visibility of customer actions across all channels, as context to help support the customer journey
- C360 masters Household customer groups, a data product is required for consumer adoption

---

## Slide 42: Focus Area: Colleague Experience UX Model

**Problem/Opportunity:**
The current assumed UX model intends that Salesforce provides a single pane of glass for all banker needs. This model expects that the single navigation experience is composed from a number of UI components:
- 1st party apps (e.g., Financial Services Cloud, Scheduler)
- 3rd party apps (e.g., nCino, Fenergo Plugin)
- BNZ configured Salesforce screens
- BNZ customised NAB-X miniapps

**Issues that need to be addressed:**
- Bankers must 'swivel-chair' to applications not built into this Customer360 experience
- Using Salesforce as a 'single pane of glass' for the majority of BNZ employees, attracts a significant single vendor risk to key banking operations

**Mitigations:**
An alternate Unified Banker Experience model ensures that each banker is provided with an 'anchor' interface, suited to their role. Across all banker teams in BNZ, this is likely to be delivered by 3-5 distinct interfaces.

Anchor applications are configured or engineered to deliver optimised experiences, to their intended personas. Each application provides internal navigation, as well as contextual navigation to other key and supporting apps.

**Key Messages and Next Steps:**
BNZ should adopt a Unified Banker Experience approach to the Colleague Digital platform, which provides a fit for purpose experience to specific banker groups, while managing vendor and technology risks.

Architecture provides consistent guidance on the 'buy vs build' decision for colleague UI.

---

## Slide 43: Focus Area: Colleague Experience UX Model - Buy vs Build

**Key Decision Points:**

1. **For commodity business capabilities,** BNZ prefers to purchase and configure a vendor product. An out-of-the-box colleague experience eliminates the need for custom UI development

2. **A custom business process** will typically require a custom UI to operate the process

3. **Where a custom UI is required,** BNZ prefers to use a single engineering platform, aligned to in-market skillsets

4. **BNZ typically avoids heavy configuration** or customisation of vendor products, in order to retain an evergreen platform

**Decision Flow Process:**
- Start: Can a COTS product provide required functionality and a well-designed colleague experience?
  - **Yes:** Unified Experience - Integrated Service (Configured UI, Configured Processes, Data)
  - **No:** Can a COTS product provide required functionality?
    - **Yes:** Where functionality aligns, a miniapp may be designed for customer AND colleague facing use
      - Unified Experience - Engineered UI (Miniapp) (COTS Service, Configured Processes, Data)
      - Unified Experience - Engineered UI (Miniapp) (Microservice, Engineered Processes, Data)
    - **No:** Unified Experience - Heavy Configured UI (Microservice, Engineered Processes, Data) [Not Preferred]

**Application Examples:**
- **COTS Application:** Salesforce FSC, Fenergo provide industry standard solutions
- **Miniapp + COTS Service:** Core Ledger integrated through miniapp interface
- **Miniapp + Microservices:** Customer Master - BIS provides custom banking functionality
- **COTS Experience + Microservice:** Avoid heavy COTS UI configuration, prefer microservice integration

---

## Slide 44: Focus Area: End to End Sales Orchestration

**Problem/Opportunity:**
Lead orchestration is fundamental to delivering world class customer experiences, by automating and optimising the sales funnel. It will create personalised, connected experiences allowing customers to be served across different channels most suitable to them.

Data, decisioning and improved system integrations are at the core of enabling more valuable proactive engagements with our customers.

Currently with a lack of system integration, data availability and funnel visibility there are many missed opportunities to proactively engage customers, inefficient business processes to create, deploy and report on leads, and ultimately does not enable BNZ to serve our customers brilliantly. This lead orchestration strategy will help to improve lead quality and conversion, increase operational efficiencies and uplift the banker and customer experience.

**Multi-year Programme Spanning Three Horizons:**
- **Horizon 1** – Enabling strong foundations through automation and integrations
- **Horizon 2** – Uplifting the digital prospect experience
- **Horizon 3** – Creating frictionless experiences through the use of AI

**Key Messages and Next Steps:**
The Target State Experience (TSX) program has developed a strategy and direction for uplifting sales lead management in BNZ.

The following slide describes the identified delivery horizons intended to uplift this capability – which has been incorporated into this overall target state.

---

## Slide 45: Focus Area: End to End Sales Orchestration - Implementation Horizons

**Horizon 1 – Automation and Efficiency (Delivery in FY25 Q4 onwards)**

**Pega CDH / Salesforce Integration:**
- Pega CDH to create leads in C360, for outbound engagement channel
- Lead updates are integrated back into C360

**Lead Management Uplift in C360:**
- Lead scoring
- Omnichannel lead assignment
- Automated Lead-to-Opportunity conversation

**Marketing Lead Integration:**
- Automated lead integration of social media platforms into C360
- Uplift in tracking and reporting of marketing leads

**Customer Journey Tracking:**
- All customer touchpoints are instrumented to identify sales activity
- Reporting to visualise aggregate journey performance

**Key Benefit:** Improved lead quality, improved operational efficiency

**Horizon 2 – Digital Integration (Delivery in FY26 onwards)**

**Prospect Identity:**
- Prospects are able to register a digital identity, to support secure data capture (e.g., HMCIB calculator)

**Integrated Sales Tools:**
- Existing sales tools on WWW can authenticate customers, allowing integration into lead systems:
  - WWW Calculators & forms
  - Appointment Booking
  - Product origination flows*
  - Document upload/download*

**Key Benefit:** Frictionless experience for prospects in digital channels

**Horizon 3 – Automated Sales**

**Hyper-Personalisation:**
- AI Product recommendation engine, based on customer history and financial goals
- Support for inbound engagement: "What is the best credit card for my spending pattern?"

**Omnichannel Sales:**
- Frictionless CX across digital and physical channels
- Customer onboarding and lending origination are fully digitised, for financially literate customers
- Seamless human + digital collaboration

**Key Benefit:** Customers can choose a blend of self-service, AI and colleague driven sales

---

## Slide 46: Focus Area: End to End Customer Servicing

**Problem/Opportunity:**
The capture, tracking, efficient routing and fulfilment of customer service requests is key to delivering a world class customer experience. Service requests through customer channels can be processed using different methods:

1. **Customer self-service / straight-through processing**
2. **Identification and immediate fulfilment by colleague**
3. **Identification, capture and deferred fulfilment by colleague**

**Current Issues:**
- BNZ does not have a consistent approach to identifying and delivering customer servicing across channels
- Each channel typically handles a different set of servicing tasks, increasing customer frustration and reducing customers' choice of channel
- Customers have no visibility of long running service requests, requiring them to consume banker time to enquire on status updates
- BNZ lacks consistent reporting, assignment and management of servicing tasks, impacting servicing SLAs and overall customer satisfaction

**Current Application Roadmap:**

**FY25:** (TSS) Assist Forms Replacement
**FY26:** Pega Workflow / C360 integration (TBC)
**FY27:** Digital Integration (TBC)

*Overlap with Workflow, Automation & Robotics Platform*

**Key Messages and Next Steps:**
The current application roadmap provides a path to simplification and modernisation of existing applications.

A further roadmap should be developed, to increase business capability and improve customer outcomes.

---

## Slide 47: Focus Area: Visibility of Customer Data / Activity

**Problem/Opportunity:**
Bankers still rely on multiple applications to gain a full picture of the current state of a customer (e.g., Customer360, InterAct, BNZ Go, BIS, Valocity). Bankers have little visibility of customer online activity or automated communications, to understand the customer journey.

**Customer data and activity history can include:**
- Customer activity in self-service channels (Online Banking, ATM, WWW)
- Tracking and visibility of customer service workflows
- Internally-triggered processes (e.g., Fraud detection, OCDD, Account Planning)
- Banker contact with customers

**The lack of available customer data impacts BNZ:**
1. The ability for bankers to know and support the customer journey
2. Provide relevant customer knowledge to generate next best conversations
3. Provide relevant customer knowledge for future AI use cases

**Mitigations:**
As BDH comes online, we have an opportunity to design appropriate data products, to enable banker, customer and automation outcomes.

Current investment in Google Analytics uplift, will provide visibility of customer and prospect WWW activity to Next Best Action decisioning.

**Key Messages and Next Steps:**
Legacy solutions, such as 'Diary Notes' are no longer fit for purpose.

Analysis is required to understand the data needs for bankers to support customers, across inbound/outbound channels; sales and servicing activities.

---

## Slide 48: Additional Content

**Note:** Not for endorsement/approval

This section contains supplementary materials and detailed architectural diagrams that provide additional context and technical detail for the Colleague Digital platform target state architecture.

---

## Conclusion

This Target State Architecture document provides a comprehensive roadmap for modernizing BNZ's Colleague Digital platform, including the Customer360 initiative. The transformation focuses on enabling bankers to serve customers brilliantly through:

- **Unified Banker Experience** across three core sub-platforms
- **Technology simplification** through legacy system retirement and modern platform adoption
- **Strategic alignment** with BNZ's Technology Strategy themes
- **Risk mitigation** through vendor guardrails and enterprise integration patterns
- **Phased modernisation approach** from FY25 through FY27 and beyond

The target state will significantly reduce technical debt (BMI reduction from 4400 to 520), improve operational efficiency, and enable enhanced customer experiences through integrated sales and servicing capabilities.