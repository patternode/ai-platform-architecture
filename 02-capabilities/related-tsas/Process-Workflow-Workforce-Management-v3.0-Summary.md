# Process, Workflow & Workforce Management - Target State & Modernisation Roadmap v3.0

**Author:** Michael Lomas
**Date:** September 2025 v3.0
**Responsible Head of Architecture:** Tanya Boelema

## Executive Summary

### Document Overview
This document outlines the target state architecture and modernisation roadmap for BNZ's Process, Workflow & Workforce Management Platform. The document presents a transformational vision driven by advances in Artificial Intelligence, anticipating a revolutionary change in how work is performed across the organisation.

### Key Stakeholders
- **Executive Sponsor:** Simon Kwan (Exec, Operational Excellence)
- **GM Approver:** Alina Barota (Colleague & Customer Support Ops)
- **Other Key Stakeholders:** Claire Hale, Anna Flower, Steve Brunskill, Sam Perkins, Paul Hay, Shirley McIntyre, Michelle Maxwell, Lee Challoner-Miles

---

## Table of Contents

The document is structured into 9 main sections:
1. **Executive Summary** - Platform scope, definition and business purpose
2. **Target State Summary** - Summary and value stream view
3. **Simplification & Modernisation Roadmap**
4. **Target Architecture**
5. **Enterprise Context** - Data, Integration & Platform themes
6. **Platform Horizons** - Technology transition from now to FY30+
7. **Risk Overview**
8. **Focus Areas**
9. **Appendices**

---

## Section 1: Executive Summary

### Platform Vision
This platform represents a story of transformational/revolutionary change in how work is performed in service of Customers, Colleagues and Corporate Entity. The approach focuses on making transitional decisions that align with future transformation while minimising technical debt.

### Current State & Challenges
- **BMI Impact:** K2 legacy workflow platform is the biggest contributor to poor BMI (~1400 in June 2025, expected reduction to ~200 by ~2030)
- **Transformation Approach:** Primarily renovation with BNZ hosted to SaaS migration and selective replacement
- **Future Vision:** Expected transformational change in 2-5 years via AI-driven consolidation

### Roadmap Overview
1. **Strategy Development (FY25 Q4):** Revisit Business Vision considering AI-driven consolidation
2. **Workflow Management & Low Code (FY24-FY27):** SaaS uplift, renovation and Microsoft Power Platform deprecation
3. **Workforce Management (FY25-FY27):** Renovations and replacement for Aspect
4. **Workforce Automation (FY26-FY27):** Renovate or Replace to align with consolidation targets
5. **K2 Decommissioning (FY28+):** Complete legacy platform retirement

---

## Section 2: Target State Summary & Platform Vision

### Platform Vision Statement
The Platform focuses on work performed in service of Customers, Colleagues and Corporate Entity. Through understanding this work and performance, it directly supports BNZ's Mātāpono and enables:
- **Perfecting the basics**
- **Building strong foundations**
- **Delivering market-leading experiences**

### Work Understanding Framework
The platform provides understanding through how work is:
- **Discovered** - Identifying and cataloguing work processes
- **Defined** - Documenting and modelling work requirements
- **Orchestrated** - Coordinating work execution across actors
- **Executed** - Performing work through various actors (Machine, Robot, AI Agent, Human)
- **Measured** - Monitoring performance and outcomes
- **Optimised** - Improving efficiency and effectiveness
- **Managed** - Overseeing work execution and resources
- **Compliant** - Ensuring regulatory adherence
- **Reported** - Providing visibility and insights

### Target State Summary
The target state envisions a consolidated ecosystem that will replace existing assets through AI-driven transformation. Key elements include:

- **Artificial Intelligence Impact:** Generative/Agentic AI enabling vendor expansion of core competencies
- **Consolidation Belief:** Single vendor providing complete value stream technology (watching Pega, Microsoft, Camunda, Salesforce, UIPath)
- **Timeline:** 2-5 years before satisfactory consolidation solution emerges
- **Risk Consideration:** Vendor concentration/coupling risk requiring mitigation strategies

---

## Section 3: Simplification & Modernisation Roadmap

### Modernisation Journey Overview
The roadmap shows architectural view of initiatives to modernise the platform and reduce BMI score across four sub-platforms:

#### Process Management
- **Signavio Replacement:** Driven by NAB Process Mining RFP
- **Pega GenAI Blueprint:** Production and extension capabilities
- **Process Mining Capability:** New capability development

#### Workflow Management & Low Code
- **Pega SaaS Migration:** Move from BNZ hosted to cloud
- **Citizen Development Enablement:** Governance and capabilities
- **Power Platform Migration:** Consolidation from Microsoft tools
- **Renovations:** Multiple modernisation activities

#### Workforce Automation
- **Transitional Discovery:** Evaluate Power Automate vs Pega RPA options
- **Commercial Fitness:** Address Blue Prism limitations

#### Workforce Management
- **Aspect Renovations:** Integration improvements
- **ControliQ Renovations:** Enhanced functionality
- **Amazon Connect Migration:** Future queue management solution

### Modernisation Tipping Point
By EOFY28, platform assets will be more "modern" than legacy, with:
- **Reduced Asset Count:** Simplification through consolidation
- **BMI Score Reduction:** Significant improvement despite renovation bumps
- **Living Document:** Annual updates reflecting changing landscape

---

## Section 4: Target State Architecture

### Architecture Overview
The target state architecture centers on a consolidated ecosystem replacing existing capabilities, except Queue Theory WFM which will integrate with Amazon Connect.

### Key Architecture Principles
- **Consolidated Technology:** Single vendor providing complete value stream coverage
- **AI-Driven Transformation:** Generative and Agentic AI at the core
- **Actor Agnostic:** Supporting Machine, Robot, AI Agent, and Human actors
- **Enterprise Integration:** Critical mass around enterprise data products and interfaces

### Platform Dependencies
The architecture shows how the Process, Workflow & Workforce Management Platform enables:
- **Experience Platforms:** 2 Level 2 Platforms, 7 Level 3 Platforms
- **Business Enablement Platforms:** 4 Level 2 Platforms, 19 Level 3 Platforms
- **Customer Serving Platforms:** 3 Level 2 Platforms, 14 Level 3 Platforms

---

## Section 5: Enterprise Context - Data Integration & Interactions

### Platform Context Overview
The platform offers enterprise enabling capabilities covering work discovery, understanding, performance, and optimisation within the bank's holistic value stream.

### Four Sub-Platforms
1. **Process Management:** Discover, model, analyse, optimise and manage processes
2. **Workflow Management & Low Code:** Systematic work execution with proper sequencing and tracking
3. **Workforce Management:** Adequate supply of human/agentic resources with appropriate skills and capacity
4. **Workforce Automation:** Automation of repeatable tasks and legacy system integration

### Data & Integration Patterns
The platform operates within three key interaction patterns:
1. **Enabled Platforms:** Bounded contexts requiring non-deterministic workflow fulfillment
2. **Deterministic Participants:** Platforms participating in non-deterministic workflows
3. **Local Orchestration:** Platforms fulfilling their own work while accessing workforce management

---

## Section 6: Platform Horizons - Technology Transition

### Major Technology Transitions

#### Pega SaaS & Modernisation (FY24-FY27)
- Migration from BNZ hosted to SaaS
- Target state patterns and modernised usages
- Citizen development enablement
- Process Fabric Hub implementation
- Microsoft Power Platform closure

#### Workforce Management Renovations (FY25-FY26)
- Aspect integrations with Workday
- ControliQ integrations with Pega
- Value release despite Contain status

#### Process Management Evolution (FY25-FY27)
- Response to NAB RFP outcomes
- Pega GenAI Blueprint implementation
- Potential Signavio replacement

#### Workforce Automation Transition (FY26-FY27)
- Discovery on Power Automate vs Pega RPA
- Commercial fitness improvement
- Consolidation alignment

#### Consolidation Horizon (FY27-FY30+)
- Transformative change across entire platform
- Massive BMI impact followed by reduction
- Vendor selection from watch list

---

## Section 7: Risk Overview of Current State

### Current Architecture Challenges
The platform directly enables a large number of other platforms but faces several modernisation concerns:

#### Key Risk Areas
- **K2 Legacy Platform:** Major BMI contributor awaiting decommissioning since ~2020
- **Commercial Fitness:** Process Management & Workforce Automation contain commercially unfit assets
- **Infrastructure Dependencies:** Delays due to AWS Private Link and Identity space challenges
- **Multiple WFM Solutions:** Recurring question about justification for multiple workforce management tools

### BMI (Bank Modernisation Index) Analysis
- **Current BMI:** ~1400 (June 2025)
- **Target BMI:** ~200 (by ~2030)
- **Major Contributors:** K2 platform, commercially unfit assets
- **Impact of Changes:** Renovations temporarily increase BMI before improvements

### Risk Categories from GRACE
- **27 Risks rated:** 18x Very High, 6x High, 3x Medium
- **89% Attribution:** Risks that this platform can reasonably mitigate through proper value stream performance
- **Regulatory Compliance:** CPS230, CoFI, Deposit Takers Act obligations

---

## Section 8: Focus Areas

### Technical Focus Areas

#### 1. Artificial Intelligence
- **Impact Scope:** Profound impact across short, medium and long term
- **Hype Cycle Position:** Early stage technology with concentration risks
- **Vendor Consolidation:** AI enabling vendors to expand core competencies
- **Risk Mitigation:** Maintaining control of IP and avoiding vendor lock-in

#### 2. Consolidation & Target State
- **Market Observation:** Author and Gartner observations showing consolidation trends
- **Strategic Direction:** Key long-term steering principle
- **Vendor Watch List:** Pega, Microsoft, Camunda, Salesforce, UIPath
- **Timeline:** 2-5 years for viable solutions

#### 3. Digital-first and Human When It Matters
- **Service Boundary:** Deterministic (digital-first) vs non-deterministic (human when it matters)
- **AI Bridge:** Agentic AI reducing friction at the boundary
- **Actor Framework:** Machine, Robot, AI Agent, Human coordination
- **Customer Experience:** Balancing automation with human touch

#### 4. Microsoft Power Platform Strategy
- **Current State:** Ungoverned usage since ~2017, finding FND-6990 audit item
- **Recommendation:** Consolidate to single platform (Pega)
- **Governance Model:** Centre for Enablement approach vs ungoverned citizen development
- **Migration Path:** Discovery required for Power Platform deprecation

#### 5. Workforce Management Rationalisation
- **Current Challenge:** Multiple WFM solutions (ControliQ, Aspect, Workday elements)
- **Production Theory:** Expected to collapse into consolidated technology
- **Queue Theory:** Recommend migration to Amazon Connect ecosystem
- **Synergy Analysis:** Four options evaluated for optimal approach

#### 6. K2 Legacy Workflow Management
- **Current Status:** ~13 workflows remaining, exit state since 2020
- **TSS Assessment:** Full decommissioning not near-term viable
- **Managed Retreat:** Efficient infrastructure and licensing right-sizing
- **BMI Impact:** Material positive impact upon complete decommissioning

#### 7. Robotic Process Automation Evolution
- **Value Realisation:** ~130k hours saved, $3.4 value per $1 spent since 2017
- **Commercial Challenge:** Blue Prism Contain status requiring replacement
- **Transition Options:** Microsoft Power Automate, Pega RPA, or UIPath RPA
- **Strategic Timing:** Align with consolidation timeline vs immediate migration

#### 8. Renovation Activities
- **Workflow Management & Low Code:** Four key migration activities to modernise usages
- **Dependency Driven:** Enterprise Document Management, Data Movement, AWS PrivateLink
- **Pattern Migration:** Universal Workflow to Modular/Low Code, Cosmos to Constellation UI
- **Automation Opportunity:** Pega GenAI Blueprint for migration efficiency

---

## Section 9: Appendices

### A. Platforms@BNZ Context
The Process, Workflow & Workforce Management Platform sits within BNZ's broader platform architecture as an Enabling Technology platform, supporting multiple upstream and downstream dependencies across the four platform layers:
- Experience Platforms
- Customer Serving Platforms
- Business Enablement Platforms
- Core Technology Platforms

### B. Workforce Management Work Types
The platform distinguishes between two fundamental work management approaches:

#### Queue Theory WFM
- **Demand Driver:** Traffic arrival (phone calls, social media, chat, face-to-face)
- **Distribution:** Based on agent/servicer availability
- **Applications:** Contact centers, bank branch operations, retail stores
- **Characteristics:** Predictable queue lengths and waiting times based on arrival patterns

#### Production Theory WFM
- **Demand Driver:** Work requirement to fulfill (case work, fraud investigations, disputes)
- **Distribution:** Based on age and priority of work items
- **Applications:** Back-office operations, financial services processing
- **Characteristics:** Output-focused with targeted service levels and productivity measures

### C. Strategic Alignment Framework
The target state architecture aligns with BNZ's Strategic Ambition through five Technology Themes:

1. **Modernise and Simplify:** Explicit modernisation planned with vendor consolidation
2. **Agile and Adaptable:** Governed citizen development and AI-enabled agility
3. **Platform Mindset:** Enabling technology platform supporting enterprise value streams
4. **Resilient, Secure and Safe:** Risk reduction through governance and modern platforms
5. **Deeply Digital:** Transitional automation enabling digital-first with human when it matters

---

## Key Recommendations

### Immediate Actions (FY25-FY26)
1. **Complete Pega SaaS Migration** - Modernise core workflow platform
2. **Implement Governance Framework** - Establish Pega Centre for Enablement
3. **Power Platform Consolidation** - Begin migration from Microsoft Power Platform to Pega
4. **WFM Renovations** - Integrate Aspect with Workday, enhance ControliQ capabilities

### Medium Term Strategy (FY26-FY28)
1. **Workforce Automation Transition** - Select and migrate from Blue Prism
2. **K2 Managed Retreat** - Right-size infrastructure while awaiting usage migration
3. **Amazon Connect Preparation** - Prepare for queue theory WFM migration
4. **AI Capability Development** - Expand Pega GenAI Blueprint usage

### Long Term Vision (FY28-FY30+)
1. **Consolidation Readiness** - Monitor vendor consolidation developments
2. **K2 Decommissioning** - Complete legacy platform retirement
3. **Target State Implementation** - Execute consolidation strategy when viable
4. **BMI Optimisation** - Achieve target BMI reduction through modernisation

---

*This document represents a living roadmap that will be updated annually or as triggered by material changes in the technology landscape, regulatory environment, or business strategy.*