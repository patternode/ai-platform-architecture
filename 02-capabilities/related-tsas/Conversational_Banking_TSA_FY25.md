# Conversational Banking - Target State Modernisation Roadmap (FY25)

## Slide 1: Title Page
**Conversational Banking - Target state Modernisation roadmap (FY25)**

Document details:
- Author: Dan Barratt, Technology Strategy & Architecture
- Date Produced & Version: July 2025 v1.0
- Responsible Head of Architecture: Angus Cotton
- Enterprise Owners: Steve Brunskill, COO Partnership Banking

## Slide 2: Version Control (For TSA Template Only)
Version control for the TSA template with the following entries:
- V 1.0 (07/04/2025): Ann Tiatia - Addition of a version control slide
- V 1.1 (07/04/2025): Ann Tiatia - Addition of versioning guidelines
- V 1.2 (08/04/2025): Ann Tiatia - Platform Modernisation Journey finalised and added (slide 26)

## Slide 3: Version Control
Document version control with versioning guidelines:
- V 0.1 (1-July-2025): Dan Barratt - Initial version using latest template (FY25)

**Versioning Guidelines:**
- Draft (0.): V 0.1, V 0.2, etc.
- Post HOA review (1.): V 1.0, V 1.1, etc
- Post Shirley review (2.): V 2.0, V 2.1, etc
- Post Paul Norman / SAA review (3.): V 3.0, V 3.1, etc
- Final approved version (4.): V 4.0
- Periodic/annual updates (5.): V 5.0

## Slide 4: Table of Contents
The document is structured in 9 main sections:
1. Executive Summary - Platform Scope, definition and business purpose
2. Target State Summary, Platform Vision - summary and value stream view
3. Simplification & Modernisation Roadmap
4. Target State Architecture
5. Enterprise Context - Data, Integration & Platform themes (dependencies and interactions)
6. Platform horizons - Technology transition from now to FY28
7. Risk overview - Current State landscape, Key Pain Points and Opportunities
8. Focus Areas
9. Appendices: Target State Architecture

## Slide 5: Stakeholder Engagement and Accountability
Key stakeholders across different areas with review schedules:

**Partnership Banking:**
- Anna Flower (Exec), Steven Brunskill (COO), Phil Simpson (Head of Operations)
- Adam Ward (Customer Hubs GM), Megan Scholey (Head of Strategic Transformation)
- Damien Allen (Head of Performance)

**Digital Data & Analytics:**
- Bronwyn Jones (GM, Digital Channels)
- Lee Challoner-Miles (GM – Data, Digital & Analytics)

**Technology (Architecture):**
- Shirley McIntyre (GM, Tech Strategy & Architecture)
- Angus Cotton (Head of Architecture)
- Dermot O'Brien (Enterprise Architect for AI)

**Technology (Delivery):**
- Michelle Maxwell (GM – Colleague & Enterprise Platforms)
- Andy Hamilton - Head of Technology (Colleague Digital)
- Nataleigh Elston– Platform Manager (Conversational Banking)

The first iteration was originally endorsed at TAF on 18th Sept 2024, with subsequent iterations requiring stakeholder input to ensure alignment between business needs and technology solutions.

## Slide 6: Section 1 – Executive Summary
Section divider slide introducing the Executive Summary section.

## Slide 7: Conversational Banking Platform - Current State Summary
**Purpose:** The Conversational Banking platform combines traditional contact centre telephony with advanced contact automation. Currently supports ~40 agent teams to handle contacts from customers and colleagues.

**Vision:** To empower customers and agents with an AI-powered platform that delivers brilliant, personalized sales and service.

**Key User Groups:**
- Customers: BNZ Customers, Internal Colleagues
- Agents: Customer facing agents, Colleague facing agents
- Platform Operations: Central Platform Operations Team, Distributed Agent Team Leaders

**Technology Fit Assessment:**
- Platform has completed its simplification and modernisation phase
- Majority of applications introduced since 2020
- Modernisation Tipping point was passed in FY25
- Platform BMI Score (v1) is 1,330

**Business Fit Assessment:**
- Low level of contact automation across voice and messaging
- Poor agent experience drives low efficiency and productivity
- Lack of data to support monitoring, reporting and analytics
- Lack of system integration, requiring manual data handling

## Slide 8: Section 2 – Target State Summary, Platform Vision
Section divider slide introducing the Target State Summary and Platform Vision section.

## Slide 9: Platform Overview and Purpose
The Conversational Banking platform combines traditional contact centre telephony with advanced contact automation, currently supporting ~40 agent teams for customer and colleague contacts.

When supporting BNZ customers, the platform connects both digital self-service and banker-assisted channels, delivering on the "Digital First, Human when it matters" approach.

**Channel Categories:**
- **Digital Channels:** Self-service banking through digital devices/apps (Mobile, Web, Open Banking APIs)
- **Conversational Channels:** Conversation based engagement through digital devices/apps with NLP and AI tools (Voice, Messaging)
- **Assisted Channels:** Direct engagement with a banker, either face-to-face or remotely (Virtual Meetings, Email, Branch Visit, Face to Face)

## Slide 10: Platforms @ BNZ
Shows BNZ's platform architecture with the Conversational Banking platform highlighted in aubergine as the platform in scope. The diagram illustrates:

**Experience Platforms:** Customer Digital, Colleague Digital, Conversational Banking, Physical Experiences
**Customer Serving Platforms:** Various banking services including payments, lending, and customer management
**Business Enablement Platforms:** Enterprise services, data & analytics, risk management
**Core Technology Platforms:** Security, infrastructure, and enabling technologies

The Conversational Banking platform sits within the Experience Platforms layer and integrates with both upstream and downstream dependencies.

## Slide 11: Platform Vision
**Vision Statement:** To empower customers and agents with an AI-powered conversation platform that delivers brilliant, personalized customer service.

**Customer Experience Vision:** Deliver a customer experience that is efficient, convenient, deeply personal, empathetic, and tailored to each person's financial journey. Provide instant access and self-service options for simple needs, while ensuring complex, sensitive, and high-value interactions are handled with world class human expertise.

**Agent Experience Vision:** Transform agents from problem-solvers to trusted financial advisors and empathetic partners, empowered by technology to deliver personalized, proactive, and truly human-centric experiences.

**Platform Operations Vision:** Be the continuous improvement engine that powers a world-class customer experience. Measure every facet of service delivery, relentlessly pursue operational excellence and unparalleled customer satisfaction through data and technology.

## Slide 12: Customer Contact Automation
**Current State:**
BNZ uses two tools for contact automation:
- Voice automation (IVR) via Convai Oration (Concierge) - handles customer identity & verification, call steering, and phone banking
- In-App Messaging automation via Amazon Lex - provides customer intent recognition and basic deflection to Digital Channels

Neither automation tool provides optimized monitoring, design and delivery workflow for fast customer experience improvements.

**Future Direction:**
BNZ has an opportunity to invest in modern Conversational AI tools for both voice and messaging channels to increase customer service and reduce low value servicing enquiries to human agents.

**Candidate Tools:**
1. Amazon Q in Connect
2. InGenous.ai (NAB Target State)
3. Cognigy

**Key Priority:** Identify a modern Conversational AI tool to support a step-change in messaging and voice automation capability, with immediate priority on enabling customer self-service for servicing enquiries in messaging.

## Slide 13: Agent Efficiency
BNZ currently supports 3 user interfaces for various colleague teams:

**BNZ Banker Desktop** (current use: in voice, outbound dialler)
- High engineering cost for additional agent-assist features
- Low UX integration with sales, servicing and enquiry screens
- No additional vendor license cost

**Salesforce Customer360** (current use: inbound messaging)
- Requires additional Salesforce licenses
- Increased business impact for technology outage risk
- Supports wide range of banker groups
- Evergreen access to Salesforce agent-assist features

**Amazon Connect Agent Workspace** (current use: IT Helpdesk)
- No additional vendor license cost
- Evergreen access to Amazon Connect agent-assist features
- Does not support banker groups outside of Customer Hubs
- Unknown cost to provide customer data and servicing

**Outstanding Task:** Select target state user interfaces aligned to agent personas to help support workflows and introduce AI-based agent-assist features.

## Slide 14: Platform Operations
**Current State Tools:**
- Amazon Connect Portal
- Aspect (Alvaria) Workforce Management (WFM)
- Hadoop reporting platform
- Convai Oration (Concierge) for voice IVR intent recognition

**Future Direction:**
Centralized platform operations team needs deeper, comprehensive access to monitoring and configuration capabilities. Distributed team leaders need access to subset of features.

BNZ prefers to simplify IT estate by adopting native Amazon Connect features over additional 3rd party applications, including:
- Amazon Connect Forecasting, Capacity Planning, and Scheduling
- Amazon Connect Contact Lens (Banker Performance Evaluation)

**Platform Configuration Areas:**
- Inbound call flow configuration and Agent/Queue Assignment
- Workforce Management with inbound demand monitoring/forecasting and agent capacity planning
- Banker Performance Evaluation with call analytics & playback and automated conversation evaluation
- Platform Reporting with realtime reporting/trends and enterprise/historical reporting
- Conversation Design and Configuration including customer utterance monitoring, customer intent design & delivery, comprehensive knowledgebase, and digital channel feedback

## Slide 15: Customer Experience - Digital Channel Integration
**Current State:**
BNZ's Online Banking apps provide simple contact mechanisms:
- Visibility of dialable 0800 numbers for Phone Banking and banker colleagues
- In-App messaging feature providing access to Āwhina chat bot and banker colleagues

Currently minimal data re-use between Digital and Conversational channels, requiring customers to explain their journey and issue when engaging with a banker.

**Future Direction:**
Seamless integration between Digital and Conversational channels enabling customers to advance their journey in their channel of choice, with seamless hand-off between self-service forms, bot automation and colleagues.

**Integration Components:**
- In-App Messaging and In-App Calling
- Social Media Channels and WWW Messaging
- Virtual Assistant with digital journey context and personalized responses
- Colleague Hand-off with digital & bot journey context and skill based routing
- Comprehensive knowledgebase and customer data integration

**Recommendation:** Further investigation needed to understand potential benefits of delivering messaging into social media channels and WWW to support prospective customers.

## Slide 16: Automation Maturity (vs Industry)
Contact centre platforms are increasing levels of automation to support customers and colleagues, with AI evolution from text-to-speech and speech-to-text through to modern GenAI and Agentic AI tools.

**Maturity Levels:**
- **Level 0:** No Contact Automation
- **Level 1:** Menu Based Navigation (touch-tone, IVR, known intent recognition)
- **Level 2:** Pre-defined Dialog Automation (bots follow predefined scripts, omnichannel across voice & chat)
- **Level 3:** System Generated Conversations (semantic intent recognition, generative responses within strict workflows)
- **Level 4:** Agentic Experience Generation (AI reasoning engine, AI can follow described process and policy)
- **Level 5:** Universal Agentic Orchestration (agent-to-agent orchestration, agent empathy, self-optimizing agents)

**BNZ Current Position:**
- Customer Hubs: Level 1 (Menu Based Navigation)
- IT Helpdesk & Other BUs: Level 0-1

**Industry Tools Available:**
- Genesys Cloud, Amazon Q in Connect, Salesforce AgentForce
- Amazon Bedrock AgentCore, Convai Oration

## Slide 17: Value Chain - Stream
Comprehensive view of the conversational banking value chain across four main areas:

**Customer Experience:**
- In-App Experience (In-App Calling, In-App Messaging)
- Telephony (Inbound Voice, Outbound Voice)

**Contact Automation:**
- Call Flows, Customer Authentication, Customer Intent Recognition
- Voicemail, Callback
- Advanced Automation (Knowledge Articles, Customer Servicing, Customer Fulfilment, Channel Deflection, Outbound Dialler)

**Agent Experience:**
- Agent Desktop, Customer Authentication, Customer Details & CRM
- Knowledge Articles, Sentiment Analysis
- Agent Automation (Customer Sales Tracking, Customer Servicing Tracking, Customer Fulfilment, Call Summary/Resolution)

**Supervisor Experience:**
- Call Flow Configuration, Agent Queue Configuration, Contact History
- Call Recording and Analysis, Quality Assurance/Coaching
- Realtime Reporting & Insights, Historical Reporting & Insights, Realtime Alerting, Skill based Routing

**AI Opportunities** and **Partnership Banking requested capability uplift** are marked throughout the value chain.

## Slide 18: Platform Metrics
Framework showing what platform improvements can be made to increase operational metrics across four categories:

**Strategic Metrics:**
- Reduce enquiry costs (Service)
- Increase Market Share (Sales)

**Customer Experience Metrics:**
- Provide 24/7 Instant Support for customers (target 80%)
- Reduce manual ID&V rate by agents (target 10%)
- Increase First-Contact Resolution rate (FCR) (target 75%)
- Decrease call/chat Average Speed to Answer (ASA) (chat from 12.5h to 2h)
- Reduce customer transfers (banker to banker)

**Agent Metrics:**
- Decrease Average Handling Time (AHT) (current 18mins)
- Reduce variance across bankers (delivery of consistent customer experience)
- Decrease After-call Work (ACW) time

**Platform Metrics:**
- Increase QA rate (target 95+)
- Increase call QA sampling rate (target 100%)

Each metric is paired with potential technology treatments including automated QA, conversational AI tools, improved UX, and enhanced integration capabilities.

## Slide 19: Section 3 – Simplification & Modernisation Roadmap
Section divider slide introducing the Simplification & Modernisation Roadmap section.

## Slide 20: Platform Vision
**Top 5 Modernisation Objectives:**

**Platform Vision Statement:** To brilliantly serve customers through a seamless, integrated communication platform, that drives banker efficiency, ongoing operational excellence and 24/7 self-service automation.

**1. Tech Simplification & Modernisation:**
- Migrate WFM from Alvaria to Amazon Connect

**2. Customer Experience:**
- Modernise existing messaging and voice automation to increase 24/7 self-service rate
- Introduce open conversation flow using conversational AI tools
- (Deeper Digital integration, enabling context sharing into messaging and improved deflection mechanisms)

**3. Agent Efficiency:**
- Deliver fit for purpose agent desktop to provide proactive support, customer data and agent assistance
- Enable proactive surfacing of enterprise knowledge and process guides
- Automated call transcription and summarisation

**4. Platform Operations:**
- Deliver self-service tools for platform configuration and monitoring
- Automated QA of calls using Amazon Connect Contact Lens and Evaluations
- Integrated contact analytics across applications using data products
- Enable reporting insights into current call purposes

## Slide 21: Simplification & Modernisation Roadmap
Detailed roadmap showing the transition from FY25 through Future timeframes across four key areas:

**Timeline:** Focus on Simplification and Modernisation → Look to the Art of the Possible → Future

**Customer Channel Integration:**
- FY25: Click to Call / Mobile In-App channel (overlap with Digital Channels platform)
- FY27: Online Banking integration uplift
- Future: Social Media Channel Discovery, WWW / Prospect Channel Discovery

**Customer Contact Automation:**
- FY25: Messaging GenAI quick wins, Conversational AI tool Discovery
- FY26: Messaging automation re-platform, Data integrations to support BAU delivery of customer intents
- FY27: Voice automation re-platform, Customer ID&V Uplift / Digital Identity Integration

**Contact Platform / Supervisor Experience:**
- FY25: Verint Decommissioning, Contact Lens Call Summarisation, Automated QA Evaluation
- FY26: Enhancement of Admin Portal for additional platform controls
- FY27: Aspect WFM to Amazon Connect WFM, Hadoop to Snowflake Reporting Migration

**Agent Efficiency:**
- FY25: Agent Desktop – Discovery, (TSX) Zoom Virtual Meeting
- FY26: Agent Desktop - Delivery, Real-time agent assist
- FY27: Real-time agent alerts, Real-time supervisor alerts, Next Best Conversation Integration (overlap with Customer Engagement platform)

**Color Coding:**
- Current platform investment (funded)
- Future platform investment (unfunded)
- In progress, but unfunded

## Slide 22: Roadmap - Applications
BNZ's Conversational Banking platform has achieved its modernisation tipping point by retiring all legacy on-premise applications in favor of AWS cloud hosted and SaaS applications during FY19-FY23 platform investment.

**Further Simplification Achieved:**
- Verint Call Recording & Analysis (retired Aug 2025)
- eMite realtime reporting (retired Nov 2023)

The application timeline shows the evolution from 2024 through 2028, with various applications in different phases:
- Plan (grey)
- Phase In (dark grey)
- Active (blue)
- Phase Out (yellow)
- Retired (red)

Key applications include Virtual Meetings, NAB/AWS Softphone, Aspect WFM, Amazon Connect, Customer Access Service, and various contact center components.

The platform BMI score is tracked showing improvement over time, with the modernisation tipping point clearly marked.

## Slide 23: Section 4 – Target State Architecture
Section divider slide introducing the Target State Architecture section.

## Slide 24: Target State Architecture
Comprehensive architecture diagram showing the future state of the Conversational Banking Platform with three main user groups:

**Digitally-Enabled Customers:** Access through Internet Banking Customer Experience and Mobile Native Customer Experience

**Prospects / General Public:** Access through One NZ Tollfree Calling

**Supervisors:** Oversight of the entire Conversational Banking Platform

**Core Platform Components:**
- **Channel Integration:** AWS Connect Async Messaging Service, BNZ AWS Click to Call Service, One NZ 0800 Platform
- **Contact Automation:** AWS Connect Contact Centre Voicemail, Outbound Dialler, AWS Connect Bot Service, Concierge Smart IVR
- **Contact Platform:** Amazon Connect, AWS Connect Contact Centre Event Bus, Contact Centre Admin Miniapp, Cyara Automated CX Assurance, AWS Connect Configuration API, Transcribe Miniapp
- **Agent Experience:** Agent Desktop Target State Placeholder, Contact Centre Banker Desktop Miniapp, Contact Centre Call Manager, Contact Centre Authentication Miniapp

**Integration:** Platform integrates with customer serving platforms including Customer Relationship Management & Sales, Customer and Party Master, Core Ledger, Card Issuing, Customer Engagement, Loyalty Offers & Rewards, Investment & Private Wealth, and Payments.

**Notes:** Contact Automation target state and Agent Experience target state are pending the outcome of current research work.

## Slide 25: Strategic Alignment
The platform aligns with BNZ's technology strategy across five key themes:

**Modernise and Simplify:**
- Current platform designed circa 2020 as combination of AWS services and 3rd party vendor products
- Platform can benefit from further simplification to 3rd party vendor products with new Amazon Connect features
- Provides opportunities for customization using AWS developer experience

**Agile and Adaptable:**
- Amazon Connect provides good opportunities for customisation and configuration of additional value-add features
- Further investment should be considered for self-service configuration by business teams

**Platform Mindset:**
- Conversational Banking acts as a platform to deliver defined set of business capabilities to various customer and colleague groups
- Single platform used to deliver contact automation and configurable many-to-many engagement model

**Resilient, Secure and Safe:**
- Amazon Connect platform designed and delivered to AWS and cloud-native best practices
- Alignment to cloud native architecture and secure development practices
- Precludes alignment to current industrialised patterns (Engineering Five Flavours)

**Deeply Digital:**
- Delivers both customer and colleague experience
- Provides relevant navigation opportunities and application data integrations eliminating re-keying errors
- Further investment could increase self-service customer fulfilment and automation/streamlining of agent workflows

## Slide 26: Section 5 – Enterprise Context
Section divider slide introducing the Enterprise Context section.

## Slide 27: Contextual Impacts
The Conversational Banking platform requires data integration for two main purposes:

**1. Customer and colleague channel integration, including authentication**
**2. Automation of customer contacts, for read and write operations to core banking systems**

**Downstream Dependencies (Conversational Banking provides to):**
- Data & Analytics: Data warehouse hydration
- Colleague Digital: Embedded Colleague Softphone
- Domestic Payments: Create Funds Transfer, Amend Bill Payment, Amend Automatic Payments
- Customer Digital: Voice Calling, Messaging

**Upstream Dependencies (Conversational Banking consumes from):**
- Colleague Identity & Access Mgmt: Colleague SSO, Get Customer Data
- Customer and Party Master: Customer Authentication, IVR Channel Verification
- Customer Identity & Access Management: Get Customer Accounts, Get Transactions
- Core Banking Ledger: Get Bill Payments, Get Automatic Payments
- Domestic Payments: Create Video Meeting
- Colleague Digital: Outbound Dialler
- Hardship & Collections: Get/Maintain Cards (activate, block, unblock, order)
- Card Issuing

**Integration Types:**
- Existing enterprise grade (green)
- Existing integration, but requires uplift/modernisation (orange)
- Tech Debt, needs replacing (red)
- Events (gear icon)
- API (circle)
- Managed Connectors (rectangle)
- ETL / Files (database icon)

## Slide 28: Section 6 – Platform Horizons
Section divider slide introducing the Platform Horizons section.

## Slide 29: Modernisation Overview
**Three-phase approach to platform evolution:**

**Modernisation & Simplification (Completed):**
- Completed cloud migration from Genesys to Amazon Connect core telephony platform
- Technology modernisation of voice automation (IVR) to Convai Oration (Concierge)
- Align messaging capability to Conversational Banking platform
- Simplification of application stack reducing vendor count, license and operating costs:
  - eMite Realtime reporting (Retired)
  - Verint call recording (Retired)
  - Aspect WFM (Planned retirement)

**AI Adoption to Improve Experience and Efficiency (In Scope of this pack - 3-5 year delivery):**
- **Customer Contact Automation:** Increased self-service ability on messaging channel using modern Conversational AI tools to reduce agent servicing workload
- **Agent Efficiency:** Identify and deliver suitable agent experience aligned to Partnership Banking future needs and Unified Banker Experience model within Colleague Digital platform
- **Platform Management:** Enable additional monitoring of the platform, self-service configuration and contact automation

**Future Initiatives (Target State not defined):**
- Re-imagination of Digital channel integration
- Re-assess Outbound Dialler target state
- Simplification of voice automation (IVR) tool, aligned to messaging

## Slide 30: Finance Modernisation Journey – Major Targets
Comprehensive view of the modernisation journey showing key investments and their replacements from FY19 through FY28+.

**Key Achievements:**
- Modernisation Tipping Point has already been achieved
- Platform migration from Genesys to Amazon Connect (inc 1st + 3rd party apps)
- Voice IVR modernisation to Convai Oration (Concierge) for risk remediation and business enablement

**Current Focus Areas:**
- **AI Adoption (FY26-FY28):** Amazon Connect AI features to improve supervisor, agent and customer experiences
- **Agent Efficiency:** NAB Softphone + Banker Desktop → Agent Experience Target State
- **Contact Automation:** Lex Bot → Conversational AI Target State
- **Supervisor Experience:** Manual QA → Contact Lens Performance Evaluations, Contact Lens Call Summarisation

**Future Platform Simplification:**
- Aspect WFM → Amazon Connect WFM
- TSA Outbound Dialler → Amazon Connect Outbound Dialler

**Digital Channel Integration (FY??):**
- Increase integration of customer channels towards an omnichannel vision
- In-App Messaging → Digital Integration Target State
- Banker actioned inbound NBC → Bot delivered Next Best Conversation

**Legend:**
- Unfunded - Future Plan
- Funded and Planned
- Exit / Modernisation Required
- Target to be determined
- No prior capability
- Modernisation Target
- Funding start year
- Target state achieved

## Slide 31: Section 7 – Risk Overview of Current State
Section divider slide introducing the Risk overview of current state section.

## Slide 32: Current State Architecture
Detailed current state architecture diagram showing the existing Conversational Banking Platform setup with identified opportunities for improvement:

**Key Opportunities Identified:**
- Voice and Messaging automation should align to a single automation tool, to eliminate duplication
- Conversational Banking has clear opportunities to adopt AI tools, to benefit both customers and agents
- Supervisor experience can be improved to allow self-service configuration of call flows and contact automation
- Agent experience requires modernisation, aligned to the Colleague Digital platform

**Current Platform Components:**
- **Channel Integration:** AWS Connect Async Messaging Service, BNZ AWS Click to Call Service, One NZ 0800 Platform, Conversational AI App Placeholder
- **Contact Automation:** AWS Connect Contact Centre Voicemail, Outbound Dialler (TSA Group), AWS Connect Bot Service, Concierge Smart IVR, Customer Access Service (Mute)
- **Contact Platform:** Amazon Connect, AWS Connect Configuration API, AWS Connect Contact Centre Event Bus, Contact Centre Admin Miniapp, Cyara Automated CX Assurance, Aspect (Alvaria) WFM, Queue Theory WFM ACL, Transcribe Miniapp
- **Agent Experience:** NAB/AWS Softphone, AWS Connect Messaging History Miniapp, Contact Centre Call Manager, Contact Centre Banker Desktop Miniapp, Agent Desktop Target State Placeholder, Contact Centre Authentication Miniapp

**User Groups:**
- Digitally-enabled Customers
- Any customer or prospect
- Contact Centre Operations
- Contact Centre Agent

The architecture integrates with customer serving platforms and shows both current implementations and planned improvements.

## Slide 33: Platform Scope and Context
Current State applications with Business Criticality and BMI Scores organized by platform component:

**Conversational Banking Platform:**

**Agent Experience:**
- Agent Desktop Target State Placeholder (★★★★ - Placeholder)
- Contact Centre Authentication Miniapp (★★★★ - 100)
- Contact Centre Banker Desktop Miniapp (★★★★ - 100)
- Contact Centre Call Manager (★★★★ - 100)
- AWS Connect Messaging Miniapp (★★★★ - 180)
- NAB/AWS Softphone (★★★★ - 180)

**Channel Integration:**
- BNZ AWS Click to Call Service (★★★★ - 0)
- AWS Connect Async Bot Service (★★★★ - 0)
- One NZ 0800 Platform (★★★★ - 0)

**Contact Automation:**
- Conversational AI App Placeholder (★★★ - 0)
- AWS Connect Contact Centre Voicemail (★★★★ - 0)
- Outbound Dialler (TSA Group) (★★ - 0)
- AWS Connect Bot Service (★★★★ - 100)
- Concierge Smart IVR (★★★★ - 100)
- Customer Access Service (Mute) (★★★★ - 180)

**Contact Platform:**
- Amazon Connect (★★★★ - 0)
- AWS Connect Configuration API (★★★★ - 0)
- AWS Connect Contact Centre Event Bus (★★★★ - 0)
- Contact Centre Admin Miniapp (★★★ - 0)
- Cyara Automated CX Assurance (★ - 0)
- Aspect (Alvaria) WFM (★★ - 50)
- Queue Theory WFM ACL (★★ - 50)
- Transcribe Miniapp (★ - 30)

**Virtual Meetings:**
- Virtual Meetings using Zoom (★★★ - 0)
- Virtual Meetings using Microsoft Teams (★★★ - 100)

**Legend:**
- Placeholder (light blue)
- Innovate (Invest) (blue)
- Encourage (Invest) (green)
- Contain (yellow)
- Exit (Divest) (red)

## Slide 34: Challenges and Issues
**Business Fit Challenges:**

**Contact Automation:**
- Limited use of call containment and deflection mechanisms to help increase customer self-service and reduce low value calls to bankers (messaging ~20-30%, voice ~10%)

**Historical Reporting:**
- Reporting of customer contacts across applications is incomplete, preventing an end-to-end view of incoming and outbound customer contacts
- The current reporting platform is end of life (Hadoop)

**Agent and Management Experience:**
- Poor tooling to allow business units to manage their own call flows (e.g. set welcome messages, operating hours, voicemail). Changes are often made via technology DevOps teams
- Current agent experience is not integrated with Customer360

**Technology Fit Challenges:**

**Workforce Management:**
- WFM is currently delivered using Alvaria Workforce Management ($388k p.a.)
- BNZ can simplify its IT landscape by moving WFM capability into Amazon Connect Optimisation

**Telephony Charges:**
- One.NZ Tollfree $1.76m and Amazon Connect Telephony $430k (pa)
- Promote In-App Messaging as an alternative to inbound voice channels for digital enabled customers
- Enable In-App Calling within mobile banking apps, reducing dialled number costs

**Application Integration:**
- Lack of investment in enterprise APIs impacts the ability to deliver contact automation
- Self-service mechanisms within messaging and voice channels cannot be delivered without suitable integration to core banking services

## Slide 35: Key Pain Points – and Opportunities
**Summary of Current Challenges:**

**Challenges & Issues:**
- Contact automation across voice and messaging has a low self-service rate. The current Intent automation tools do not enable a fast design and delivery cycle. Future self-service automation will require data integrations from other customer serving platforms.
- The current agent experience was designed using engineering patterns to deliver basic contact information and controls. Agents are still required to alt-tab into different applications to access different customer systems.

**Risks (from GRACE):**
- Fraud Management: RSK-167 External Fraud
- Financial Crime: RSK-1287 Financial Crime Risk
- Data Management: RSK-1300 Data Management Risk

**Current BMI:**
The Conversational Banking centres on Amazon Connect, which provides an ever-green SaaS application for handling voice and messaging. The majority of applications have been introduced after 2020, as part of the Contact Centre of the Future program. Since the completion of the program, further feature releases to Amazon Connect provide ongoing opportunities to simplify the number of applications.

The current platform BMI is 1,330.

## Slide 36: Page 36
Simple page marker showing page number 36.

## Slide 37: Technical Focus Areas
To support the move towards the proposed target state, three key focus areas have been identified:

**Business Enablement:**
Business teams desire the ability to configure their customer experience through self-service administration.
- Simple call centre controls, such as active hours and inbound welcome messages, should be made self-service
- Advanced controls such as call flows and customer intent automation, should be made available to power users

**Unified Contact Automation:**
- Voice automation is currently delivered using Concierge IVR, purchased as a SaaS solution
- Messaging automation is currently delivered using Lex bot, developed using PaaS tools
- In the 2-4 year horizon, BNZ should consider consolidating onto a single PaaS or SaaS automation tool

**Enterprise Integration / Data:**
- There is a strong desire to increase adoption of self-service mechanisms across voice and messaging channels
- There is a strong dependency on Technology domains to provide Enterprise APIs, to enable self-service automation

## Slide 38: Focus Area – Business Enablement
**Problem / Opportunity:**
Business teams desire the ability to configure their customer experience through self-service administration. This need extends across teams with both internal or external customers.

Simple call centre controls, such as active hours and inbound welcome messages, can be made self-service through an admin portal.

Advanced controls, such as IVR call flows, can be made available to power users and development teams, via configuration and customisation.

**Options Considered:**
1. Provide a basic 'Admin Portal', enabling business teams to configure basic call flow options (e.g. operational hours, welcome message)
2. Identify and develop re-usable call flow features, to enable customer self-service (e.g. knowledge base search, internal chatbot integration)
3. Evaluate tooling to allow business teams to design and deploy customised call flows

**Next Steps:**
- Discover what tooling NAB currently use to support business enablement (e.g. conversation design, call steering design, contact flow configuration)
- Research modern call design tools, which can integrate with the Amazon Connect platform
- Identify the propensity for self-service call automation by BNZ business teams

## Slide 39: Focus Area – Unified Contact Automation Tools
**Problem / Opportunity:**
Conversational Banking provides a customer experience across voice and messaging channels. This platform enables BNZ to deliver a differentiable customer service, providing an opportunity to deliver market leading experiences.

- Voice automation is currently delivered using Concierge Smart IVR, purchased as a SaaS solution
- Messaging automation is currently delivered using Lex bot, developed using PaaS tools
- In the 2-5 year horizon, BNZ should consider consolidating onto a single PaaS or SaaS automation tool across both voice and messaging

**Options Considered:**
1. Consolidate onto a single SaaS application (ie. Concierge)
2. Consolidate onto a single PaaS application (ie. AWS Lex)
3. Continue to operate separate voice/messaging automation applications
   ➢ Duplicate costs to maintain applications and develop automations (e.g. fetch customer account balances)

**Next Steps:**
- Since migrating IVR capability to Concierge, BNZ is re-establishing its capability for designing and delivering contact automation
- BNZ should evaluate current voice/messaging automation tools, against technology and business delivery lenses
- Technology teams can monitor current demand and cost of automation in existing voice/messaging channels, to identify areas of alignment
- Across messaging and voice channels, determine if consolidating contact automation tools supports business objectives with a simpler tech stack

## Slide 40: Focus Area – Enterprise APIs
**Problem / Opportunity:**
There is a strong desire to increase adoption of automated agents across customer voice and messaging channels.

Automated triage and response to customer queries reduces call volumes to frontline bankers, allowing for re-deployment to high value activities.

There is a dependency on technology domains to provide Enterprise APIs, to surface relevant data to messaging/IVR automation tools.

Funding and priority of enterprise APIs sits below right-of-way programs, inhibiting progress.

**Options Considered:**
1. Wait for significant modernisation programs to deliver relevant Enterprise APIs, as part of their outcomes
   • Programs become an upstream dependency to deliver contact automation
   • Programs may remove Enterprise APIs from scope, to control cost/timelines

2. Re-use existing legacy integration patterns
   • Increases use of legacy integration platforms, which increases the need for regrettable remediation
   • Increased operational risk, as legacy integration patterns typically lack modern security controls

**Next Steps:**
- There is a need for Technology to capture cross-domain demand for re-usable service interfaces
- Currently no mechanism exists to collate API demand, which could help prioritise sequencing or delivery
- Once demand can be captured across domains, platform roadmaps can be adapted to help plan delivery

## Slide 41: Page 41
Simple page marker showing page number 41.

## Slide 42: Contact Automation - Conceptual Architecture and Delivery Process
**Cross-functional Product Team:** Technology + Integration, Data Analytics, Conversation Design

**Architecture Components:**

**Messaging Channels:**
- In-App Messaging, WWW Messaging, Social Media

**Voice Channels:**
- 0800 Direct Dial, In-App Calling (Using Awhina voice)

**Conversational AI Tool** (central component) connects to:
- **Public Data Sources:** Unstructured Knowledge Articles, Structured Datasets (e.g. Branch/ATM Locations)
- **Customer Platforms:** Customer Details, Account Details, Servicing Enquiries, Sales Journeys
- **Workflow Platforms:** Payments, Next Best Conversation
- **Contact Recording and Analytics:** Contact Transcripts, Analytics, Resolution Details, Customer Utterances

**Delivery Process (Iterative):**
1. **Measure and Analyse:** Instrument all aspects of customer utterances and contact history. Use language and data analytics to understand customer problems and intent.

2. **Ideate + Design:** Ideate a bot feature to response to an unmanaged intent. Initial solution design including desired outcome, technical build and dependencies.

3. **Prioritise:** Prioritise feature delivery based on predicted ROI (Banker time saving, Cost of technical build, Delivery dependencies, Conversation complexity).

4. **Design + Deliver:** Design conversation flow, Build data integrations, QA improvements.

## Slide 43: GenAI Opportunities
"Banking contact center managers face the dual challenge of enhancing operational efficiency and improving customer service. The strategic application of AI, particularly through Large Language Models, presents a transformative opportunity to address these challenges. By streamlining processes such as customer authentication and call logging, and providing real-time support and sentiment analysis, AI can significantly reduce inefficiencies and improve the customer experience"

**Customer Targeted GenAI:**
- **Now:** Triage & Intent Recognition, End-to-end Voice Assurance, End-to-end Messaging Assurance
- **Next:** Realtime Sentiment Analysis, Data & Insight Development, Call QA Evaluation, Call Summary, Fraud Detection
- **Later:** Customer Chatbot

**Colleague Targeted GenAI:**
- **Now:** (none specified)
- **Next:** Realtime KB Article Suggestion, Call flow Optimisation
- **Later:** Agent Chatbot

Source: https://thefinancialbrand.com/news/data-analytics-banking/artificial-intelligence-banking/how-genai-can-fulfill-contact-centers-potential-178995/

## Slide 44: Proposed Adoption of Colleague-Assist AI
**Architecture Overview:**
The choice of banker 'anchor' application is linked to the integration of colleague-assist AI features. BNZ would prefer to adopt an out-of-the-box vendor experience, augmented with BNZ specific plugins, ensuring low-engineered evergreen feature availability.

**User Interface Layer:**
- **Authenticated Customer:** In-App Messaging, Inbound Phone
- **Colleague (Enquiry & Service):** Amazon Connect Agent Workspace
- **Colleague (Relationship & Sales):** Customer360
- **Colleague (Branch Enquiry):** BNZ Go

**Multi-agent Supervisor Layer:**
- **Amazon Q in Connect** (for voice/phone interactions)
- **Salesforce AgentForce** (for Customer360 interactions)

**Utility Agent Layer:**
Specialist agents trained to be experts in single business capabilities:
- Customer Master Agent
- Payments Agent
- Knowledge Agent
- Core Banking Agent
- Payments Agent
- Sales Agent
- Servicing Agent

**System Design:**
- Each UX is designed for a specific target audience, providing access to a relevant supervisor agent (customer vs colleague)
- Understands the customer context, natural language input
- Applies content guardrails, delegates execution tasks to utility agents, generates response to the user
- Specialist agents provide context to supervisor agents to advertise purpose

## Slide 45: Business Vision - Partnership Banking
**Product Principles:**

**Focus on building customer relationships over completing transactions:**
"We make decisions that will benefit our customers. We are a their trusted financial partner. We build relationships through building an understanding, considering their experience, empathising and working with them for a path forward that helps them in the long-term."

**Listen, understand and act:**
"We use data, based on what our customers and colleagues tell us and numbers we can track, to make decisions. Leveraging data to form a better understanding of our customers and colleagues, to provide a personalised experience to each individual based upon their context, behaviours and options."

**Security is 'job one':**
"As a trusted advisor, it's everyone's job to ensure that the security of the customer, their data, and the platforms we build and use are safe and secure."

**Innovate & simplify at pace:**
"We are not afraid of innovation. We experiment – test and learn – to inform what we do and how we use new technology to create an experience that delights our customers and colleagues."

**Only Build the Necessary:**
"Seek an 'off the shelf' where possible approach, reducing technical debt for engineering and increasing features to market for product and banking teams."

**Measuring Success:**
- 20% Reduction in calls to the Contact Centre
- Continue to remain #1 NPS (Compared to big 4)
- Remain in Top Quartile for Banker NPS
- 83% IVR Containment Rates
- 95+ for Quality Assurance
- "We can innovate iteratively which continues to underpin the vision of digital first human when it matters."

## Slide 46: Technology Intentions Alignment
The Conversational Banking platform aims to focus on a subset of Cloud Platforms and Engineering flavours, centred on Amazon Connect, supporting AWS Services and specialised SaaS platforms.

**Strategic Alignment:**

**Cloud First:** All systems hosted are in AWS or SaaS

**Customer Centered:** The platform is a key enabler for the TSX initiative, enabling a world-class customer experience

**Security and compliance Embedded:** Alignment to cloud native architecture and secure development practices

**SaaS with No Customisation:** Evergreen Amazon Connect platform

**Industrialised for resilience and speed:** Delivery team focus on Miniapps, Serverless, PaaS, SaaS

**Experiment-led informing our choices:** Technical and business experiments to quickly discovery value

**Note:** Partial deviation from industrialised patterns, is due to historical 'Build once, deploy twice' group alignment

**Technology Intentions Framework shown at bottom includes:**
- Customer centered, differentiation through human-centered design
- Experiment-led informing our choices, minimal functional overlap
- Industrialise for resilience and speed, cloud-first
- Open banking on the inside, integration is a first class citizen
- Data as a product, event-based
- SaaS with no customisation, security and compliance embedded

## Slide 47: Target State Summary
**Vision & Purpose:**
BNZ's Conversational Banking extends the traditional Contact Centre platform, to provide voice, digital messaging and video channels to customers. Customers can be served by either automated or human agents, for sales and servicing purposes.

**Current State:**
Amazon Connect provides an extensible evergreen technology platform which allows for future modernisation of customer and agent experiences.

**Adoption / Usage:**
The platform supports ~40 agent teams, across most business units, serving internal and external customers:
- CCH / SME Hubs (external)
- Customer Assist (external)
- IT Helpdesk (internal)
- Procurement (internal + external)

**Challenges and Issues:**
- Agent experience across contact types is not well integrated into Customer360 environment
- Call flow configuration is not currently delivered as a business unit self-service task; instead, requiring technical operation

**Opportunities:**
Now that the base contact platform has been delivered, future investment can focus on user experiences:
- Customer experience (ie. self-service automation, video)
- Agent experience (ie. Customer360 integration)
- Business administrator experience (ie. Admin Portal)

**Target State:**
The Conversational Banking platform aims to provide BNZ business units with easily accessible capabilities and the flexibility to rapidly adapt and integrate services. We enable these teams to create new customer value and improve overall operational efficiency.

## Slide 48: Platform Vision
**Vision Statement:** To brilliantly serve customers through a seamless, integrated communication platform, that drives banker efficiency and operational excellence.

**Platform Capabilities Comparison:**

**Workplace Technology (Communication) Platform:**
- **Basic Communication Channels:** Voice (In/Out), Group Calling
- **Meets general purpose single user and small team telephony needs**

**Conversational Banking Platform:**
- **Basic Communication Channels:** Voice (In/Out), Messaging, Video
- **Configurable Commodity Features:** Call Queues, Agent Groups, Voicemail, Welcome Message, Callback
- **Custom/Value-Add features:** Āwhina Messaging Bot, Smart IVR, Campaign Dialling (Out), Customer360 Integration, Call Recording & Analysis
- **Meets additional regulatory and large team needs**
- **Delivers optimised agent and customer experience**

**Key Differentiators:**
Conversational Banking extends beyond simple telephony platforms, by providing additional commodity capabilities and value-add customisations.

All business teams using the Conversational Banking platform have access to configurable commodity features, such as call recording and basic call handling.

To deliver a world class customer experience, the Conversational Banking platform can deliver custom-engineered value-add features, in conjunction with customer-facing business teams.

**Scope Definition:**
- **Not in scope:** Basic workplace communication
- **In scope:** Advanced contact center capabilities with AI and automation features