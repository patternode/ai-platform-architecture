# Data & Analytics, Enterprise Reporting TSA - V3 Summary

**Author:** Tracey Davis
**Date:** February 2025
**Status:** Draft 0.4

---

## Executive Summary

This document outlines BNZ's Target State Modernisation Roadmap for Data & Analytics and Enterprise Reporting platforms. The strategy focuses on transforming from legacy monolithic systems to a modern, consolidated data ecosystem centered around the BDH (Business Data Hub) platform using Snowflake technology.

---

## 1. Title Slide - Data & Analytics, Enterprise Reporting

**Target State Modernisation Roadmap**

- Document prepared by Tracey Davis in February 2025
- Current status: Draft 0.4
- Focus on modernizing BNZ's data and analytics capabilities

---

## 2. Overview and Strategic Context

**Key Platform Definition:**
- Data & Analytics platform serves as foundational technology for secure, reliable data delivery
- Key enabler for AI and generative AI capabilities
- Comprises four main value streams: Data Acquisition, Data Curation, Data Consumption, Data ROI

**Strategic Pillars:**
- **Self-Service:** Move from centralized to self-service model with GenAI interface
- **Data Quality & Governance:** Embedded automated governance and stewardship
- **Advanced Analytics & AI:** ML model deployment and monitoring, AI/GenAI foundations
- **Security & Compliance:** Robust security by design with embedded regulatory compliance
- **Performance & Reliability:** Always-available, high-performing technology meeting SLAs
- **Visualization & Insight:** Easy-to-understand and actionable data presentation

**Transformation Approach:**
- Build foundations and rationalize over 3-5 years
- Hollow out existing systems, remove duplication, simplify data pipelines
- Move to composable architecture
- Generally aligned with NAB strategy with minor scale differences

**Current State BMI (Business Modernization Index):**
- High BMI reflects numerous legacy assets with low architectural and functional fitness
- Target state dramatically reduces BMI through modernization

---

## 3. Target State Overview and Technical Focus

**Published Target State Goals:**
- Intuitive data ecosystem enabling self-service and discovery
- Shift from legacy monolithic systems to consolidated automated technologies
- Trusted, compliant data ecosystem with embedded controls
- Elimination of data silos through improved collaboration
- Consistent data reuse through focused, curated Data Products
- Reduced technical debt via workload transformation
- Advanced Analytics uplift through Data Science and ML Ops maturity
- Operating Model maturity for guidance and data reuse support

**Key Implementation Points:**
1. **Standardize on BDH:** Core capabilities standardized and rationalized in cloud
2. **Augment & Integrate:** Self-service data ingestion, data products, governance tooling, ML workbench
3. **Exit Legacy:** Discover and hollow out monolithic systems
4. **Grow Capabilities:** Build expertise in domains for data product ownership

**Technical Focus Areas:**
- **Operating Model & Practices:** Fit-for-purpose model with clear accountability
- **Stack Simplification:** Focus on technology rationalization, hollow out Hadoop and GDW
- **Data Engineering:** Standardize practices, workflow simplification, optimize capabilities
- **Scaling Capability:** SageMaker foundations for AI/GenAI

**Challenges:**
- **DataOps Maturity:** Low level leading to inconsistencies in tools and practices
- **Blind Spots:** Complex pipelines without shared context and intelligence
- **Resources & Skills:** Need for training and specialist partnerships

---

## 4. Platform Overview

This section serves as a transition slide introducing the platform architecture details that follow.

---

## 5. Target State Summary

**Nine Key Transformation Areas:**

1. **Intuitive Data Ecosystem:** Enables self-service and discovery
2. **Trusted and Compliant:** Secure by design with embedded regulatory controls
3. **Consistent Data Use:** Focused, curated, ready-to-use Data Products
4. **Operating Model Maturity:** Guidance and support for data use and reuse
5. **Uplift Data Products:** Capability enhancement in enterprise domains
6. **Technology Shift:** From legacy monolithic to consolidated automated systems
7. **Technical Debt Reduction:** Transform workloads rather than 1-for-1 replacement
8. **Data Silo Elimination:** Improved collaboration and discoverability
9. **Advanced Analytics:** Maturity in Data Science and ML Ops with modern workbench

---

## 6. Scope, Vision & Purpose

**Platform Purpose:**
- Provide trusted copy of enterprise data
- Enable scaled data sharing and improved analytics use
- Snowflake adopted as target state technology
- Facilitate shift toward freely available, accessible data with appropriate controls

**Vision Statement:**
Transform data into actionable insights driving business value across strategic pillars:
- **Self-Service:** Enable independent data access, analysis, and visualization
- **Data Quality and Governance:** Automated quality/validation, clear ownership, embedded compliance
- **Advanced Analytics:** Wide range of capabilities, ML model deployment, advanced analysis tools
- **Security & Compliance:** Robust security by design, embedded regulatory compliance
- **Performance & Reliability:** Always available, high-performing, SLA-meeting critical pipelines
- **Visualization & Insight:** Understandable, actionable data through effective presentation

**Strategic Alignment:**
Informed by Data Strategy, BNZ Strategy, and Technology Strategy

---

## 7. Data & Analytics Value Chain

**Comprehensive Data Lifecycle Coverage:**

**Data Acquisition:**
- Data Sourcing, Ingestion, Streaming, Batch Processing
- Data Extraction, API Integration, Database Replication
- Data Encryption, Metadata Capture, Data Versioning

**Data Curation:**
- Data Profiling, Standardization, Deduplication, Error Detection
- Missing Value Handling, Outlier Detection, Data Type Conversion
- Data Normalization, Integration, Transformation, Validation
- Data Masking, Aggregation, Parsing, Reconciliation, Cleansing
- Data Lineage Tracking, Enrichment, Preservation

**Data Consumption:**
- **Business Intelligence:** Operational reporting, Interactive dashboards, Ad-hoc querying, Standard KPI monitoring
- **Analytics:** Descriptive, Exploratory, Prescriptive, Statistical, Predictive
- Machine Learning, Data Mining, Time Series Analysis, Geospatial Analysis
- Regression Analysis, Hypothesis Testing, Sentiment Analysis
- **Operational Feedback:** Decision engine updates, Model deployment & scoring, Business rules refinement

**Data ROI:**
- Value Quantification, Cost Tracking, ROI Calculation, KPI Development
- Benefit Realization Tracking, Customer Value Analysis, Impact Analysis
- Efficiency Measurement, Regulatory Compliance Value, Time to Value Analysis

**Governance Throughout:**
- Metadata Management, Data Classification & Tagging, Data Governance
- Data Lineage, Cataloguing, Lifecycle Management, Data Quality Assessment

---

## 8. Platforms @ BNZ

**Platform Categories:**
- **Experience Platforms:** Customer Digital, Colleague Digital, Conversational Banking, Physical Experiences
- **Customer Serving Platforms:** Customer Management, Product Origination, Account Management, Payments
- **Business Enablement Platforms:** Enterprise Services (including Data & Analytics and Enterprise Reporting), Enterprise Data & Analytics, Artificial Intelligence
- **Core Technology Platforms:** Enterprise Security, Enabling Technologies, Infrastructure Foundations

**Data & Analytics Position:**
- Located within Business Enablement Platforms
- Key enabler for other platform categories
- Supports enterprise-wide data needs

---

## 9. High Level Platforms Context

**Platform Dependencies:**
- **Dependent on:** Core Technology platforms (foundational technology, observability)
- **Dependency for:** Business Enablement Platform components

**Data Flow Vision:**
- Acquire data from all BNZ platforms
- Publish Data Products as Data Assets for organization-wide consumption
- Support Credit Modeling, Metadata Management, Data Quality, Regulatory Reporting

**Platform Interactions:**
- Data Acquisition from operational and external sources
- Data Products delivery to various platforms
- Reporting & Insights provision across organization

---

## 10. Reference Architecture

**Architectural Framework:**
Comprehensive L2 capabilities covering the full data lifecycle from acquisition through consumption, with AI enablement capabilities.

**Key Architectural Components:**
- **Acquire Layer:** Databases, Files, Unstructured data, 3rd Party, Devices, Sensors, Cloud
- **Curate Layer:** Data curation, Enterprise data, Data provisioning, Real-time messaging
- **Consume Layer:** Data services, Data consumption, Self-service, Insights

**Data Supply Chain:**
- Raw data → Data curation → Enterprise data → Data provisioning → For purpose data
- Real-Time/Messaging/Pub-Sub capabilities throughout

**Governance & Management:**
- Data management, Data governance, Analytics management
- Data security & common services (Data Security & Privacy, FinOps, DataOps)

**Future AI Capabilities:**
- Vector store, Knowledge graph, Enterprise Search, Sandbox workbench
- Similarity search, Prompt engineering, Semantic layer
- Classic AI, Gen AI, Agentic AI capabilities

---

## 11. Lifecycle Status

**Technology Portfolio Assessment:**

**Invest Category:**
- AstroCloud, BNZ Cards & Payments hub (MDH)

**Encourage Category:**
- DataShield, Analytics Execution (BAE), BNZ Data Hub (BDH)
- Data Labs, AWS SageMaker, Alation, FiveTran

**Contain Category:**
- Astronomer, Financial Compliance Hub (FCH), Active Batch

**Exit Category:**
- BIW, Global Datawarehouse (GDW), ODM, Informatica Suite, SAS Suite
- Multiple legacy tools including Ataccama ONE, Cloudera Hadoop, Tableau Server

**BMI Impact:**
- High BMI score due to numerous legacy (Contain & Exit) assets
- Low architectural and functional fitness in current state
- Target state significantly improves BMI through modernization

---

## 12. Current State Architecture

Introduction to the current state technology landscape, showing the complexity and fragmentation that needs to be addressed.

---

## 13. Current State Detailed Architecture

**Complex Current Environment:**

**Data Movement:** Multiple ETL tools (Informatica PowerCenter, SAS, IBM InfoSphere)
**Data Storage:** Fragmented across Snowflake (BDH), Oracle (GDW), MSSQL (BIW, ODM), Cloudera Hadoop
**Data Transformation:** Multiple processing technologies with overlapping capabilities
**Reporting:** Diverse tools including Power BI, Tableau, Newton, various legacy systems
**Governance:** Multiple Informatica tools for different governance aspects

**Key Issues:**
- Technology overlap and duplication
- Complex integration patterns
- Multiple technologies serving similar functions
- Legacy systems with limited future viability

---

## 14. Current State - Business Risk

**GRACE Risk Alignment:**

**RSK-1300 Data Management Risk:** **IMPROVES RISK PROFILE**
- Enhanced discoverability, access, description, ownership
- Improved timeliness, trust, data protection, security

**RSK-6 Stat, Reg & Reporting Risk:** **IMPROVES RISK PROFILE**
- Same improvements as RSK-1300 apply to external reporting

**RSK-166 Data Loss:** **IMPROVES RISK PROFILE**
- Automatic data classification and protection
- Access limited to job requirements

**RSK-158 IT System Failure:** **IMPROVES RISK PROFILE**
- Reduced technology count and complexity
- Simplified management and maintenance

---

## 15. Current State - Issues & Challenges

**Technology Obsolescence:**
- Significant time/investment in exit/contain technologies
- Historic lack of priority for legacy exit
- Non-compliance and security risks
- Lack of visibility in legacy systems

**Complexity & Duplication:**
- Overlapping technologies and inappropriate usage
- Complex data ecosystem with duplication
- Inconsistent point-to-point solutions
- Difficult data discovery leading to duplication
- Inconsistent business rule application

**Cost Issues:**
- Waste from unrealized technology benefits
- High storage, compute, scalability costs
- Expensive concurrent legacy and modern systems
- Cost of duplicated data in legacy systems

**Resource & Skills:**
- Difficulty recruiting for legacy technologies
- Growing demand for skilled data professionals
- No enterprise domain expertise
- Unsustainable centralized model risk

**Uplift Challenges:**
- Slower than anticipated BDH progress
- Modern technology adoption challenges
- Lack of operating model and guidelines
- Poor observability capabilities
- Limited third-party data management

---

## 16. Target State Architecture

Introduction to the simplified, modern target state architecture that addresses current state challenges.

---

## 17. Target State Overview

**Strategic Approach:**
"Providing trusted, predictable and continuously available data across the enterprise."

**Three-Pillar Strategy:**

**1. Standardise on BDH:**
- Core data and analytics capabilities standardized in cloud
- Cloud native services for cost efficiency

**2. Augment and Integrate:**
- **Data Ingestion Framework:** Self-service with approval workflows
- **Data Products:** Well-defined domains with consistent tooling
- **Data Management & Governance:** Integrated automated capabilities
- **ML Uplift:** Cloud-based ML workbench for self-service experimentation

**3. Grow Capabilities:**
- Observability, Test Data Management, Data Quality
- Reference Data Management, Semantic Layer, Data Modeling
- AI/ML, Gen AI/LLM capabilities
- Skills and mindset development

**Parallel Activities:**
- Exit legacy technology
- Adopt innovative technology

---

## 18. Target State Architecture Detailed

**Simplified Technology Stack:**

**Data Movement:** FiveTran, Kafka, sFTP
**Data Storage:** Snowflake (BDH), S3
**Data Transformation:** dbtCore (AstroCloud), Spark
**Advanced Analytics:** AWS SageMaker, Data Labs
**Reporting:** Power BI Service, Regular Standard Advices, CMOD
**Governance:** Alation for catalog, classification, governance
**Operations:** AstroCloud Airflow, GitHub, AWS CloudFormation

**Key Improvements:**
- Dramatic reduction in technology complexity
- Standardized tooling across capabilities
- Cloud-native, scalable solutions
- Integrated governance and security

---

## 19. Target State Treatment Strategy

**Technology Migration Approach:**
Capabilities transitioned to target state technologies rather than one-for-one replacement.

**Migration Patterns:**
- **Data Storage:** GDW/ODM/BIW → Snowflake (BDH), Hadoop → BDH (Snowflake)
- **Data Movement:** Multiple ETL tools → FiveTran
- **Data Transformation:** Multiple tools → AstroCloud dbtCore
- **Reporting:** Multiple tools → Power BI Service
- **Data Science:** VM/Bespoke → AWS SageMaker
- **Governance:** Informatica Suite → Alation
- **Orchestration:** ActiveBatch/Astronomer → AstroCloud Airflow

**Strategic Focus:**
Transform capabilities, not just replace technologies

---

## 20. Target State Challenges

**Five Key Challenge Areas:**

**1. Address Technology Obsolescence:**
- Prioritize, invest, commit to legacy exit
- Plan with cost profile considerations
- Conservative approach costs more long-term

**2. Reduce Complexity & Duplication:**
- Adopt future state technologies with operating model
- Build simple, reusable data pipelines (ETL to ELT)
- Create discoverable, trusted, protected data assets

**3. Minimize Cost:**
- Deliver business benefit within existing platform
- Prioritize technology selection based on maturity/commitment
- Monitor costs by team, product, feature against business value

**4. Resource & Skills:**
- Training and support for new technologies
- Partner for specialist skills advancement
- Technology adoption and exit support

**5. Uplift Requirements:**
- Plan for gaps: Data Quality, Semantic Layer, Modeling, Reference Data
- Continue BDH adoption and data product focus
- Adopt target state technologies enabling legacy exit
- Address DataOps practice maturity
- Handle operational system analytics consumption
- Build third-party data management capability

**BDH Critical Success Factor:**
BDH uplift drives shift from fragmented repositories to coordinated ecosystem enabling scaled data collaboration and improved analytics use.

---

## 21. Modernisation Tipping Point

**Concept:**
Point where platform renewal rate outpaces legacy asset decay rate.

**Requirements:**
- **Simplification:** Active removal and replacement of aging assets
- **Modernisation:** Large-scale transformation on major platforms offering cohesive experiences

**Benefits:**
Once tipping point reached, focus shifts to modern, supportable, resilient platforms enabling easier execution and more resilient services.

---

## 22. Tipping Point - Data & Analytics and Enterprise Reporting

**Timeline:**
- **2027:** Indicative tipping point for both Data & Analytics and Enterprise Reporting
- Based on lifecycle status and roadmap estimates

**Risk Factors:**
- Multi-year modernization investments may slip
- Slippage affects tipping point timing
- Continued modernization investments beyond FY28
- Focus shift from legacy to contemporary systems post-tipping point

**Measurement:**
Tracking methodology based on component counts over time showing invest vs. divest trajectories.

---

## 23. NAB Alignment

**Strategic Alignment:**
General alignment on data strategy including Data Products as reusable assets and future state operating model, with minor scale differences.

**Key Technology Differences:**

| Capability | NAB Choice | BNZ Choice | Rationale |
|------------|------------|------------|-----------|
| **Scope** | Data & Analytics + Enterprise Reporting + AI in single TSA | Separate AI TSA | Different organizational structure |
| **Data Catalog** | Collibra | Alation | Price point considerations, similar capabilities for less cost |
| **Data Storage** | Databricks ADA | Snowflake BDH | BNZ originally followed NAB NDH path, benefits of changing didn't justify cost |
| **Data Quality** | Collibra (future) | TBD | Alation doesn't include DQ out of box |
| **ML Platform** | Databricks | AWS SageMaker | Databricks includes workbench, Snowflake does not |

**Consistency Areas:**
- Data strategy and Data Products approach
- Future state operating model
- Publishing reusable data assets

---

## 24. The Data Uplift Journey

Introduction to the comprehensive transformation approach covering technology, process, and practice improvements.

---

## 25. Data Uplift Principles

**Nine Guiding Principles:**

**Core Principle - Business Value:**
Achieving business value outcomes underpins all target state capabilities and tooling requirements.

**Supporting Principles:**
1. **Enable Self-Service & Discovery:** Platform capabilities for data access, exploration, consumer understanding
2. **Enable Data Products:** Position as analytics modernization pillar, include data and decision products
3. **Establish Integrated Data Model:** Right architecture foundation, integrated common data model
4. **Create Trusted State:** Data catalog processes, business-level data quality, defined products/owners
5. **Create Accessible Data:** Policy-based access, quick establishment, sensitive data protection
6. **Enable Automation:** End-to-end pipeline automation, standardized governance/controls
7. **Utilize AI Enablement:** Automate classification/tagging, responsible AI/ML use
8. **Future Proofing:** Architecture enabling AI/ML, Generative AI for business requirements

---

## 26. Target State Uplift at BNZ

**Holistic Transformation Approach:**
"The journey is not just (or all) about Technology."

**Three-Dimensional Framework:**

**Process Dimension:**
- Hydrate BDH
- Establish frameworks
- Principles & Guidelines
- Communications & Change

**Technology Dimension:**
- Foundational Data Platform (central)

**Practice Dimension:**
- Data Products
- Data Domains (Subject Areas)
- Data Ops
- Data Governance Uplift
- Service Management

**Integration:**
All dimensions work together to enable simplified operations, cost efficiency, and improved governance.

---

## 27. BDH - The One Stop Shop for Trusted Data

**BDH Platform Vision:**
Shift from fragmented, duplicative data repositories to coordinated ecosystem making trusted data available across all BNZ business areas.

**Platform Capabilities:**
- **Data and Analytics:** Centralized repository with data enrichment
- **Enterprise Reporting:** Report creation and distribution management
- **Data Governance and Privacy:** Built-in management, measures, controls
- **Enterprise ML Services:** Machine learning capabilities

**Future Scaling:**
Expected to scale for Artificial Intelligence and Generative AI capabilities.

**Implementation Status:**
- Snowflake target state technology implemented and developing
- Multi-year effort required for legacy data warehouse consolidation

---

## 28. Data Products

**Definition:**
"Data Products are data & analytics assets that are produced & offered as a packaged, reusable, self-contained product to service a data consumer's needs"

**Seven Guiding Principles:**
1. **Valuable:** Relevant and aligns to strategic business goals
2. **Discoverable:** Easy to find and accessible
3. **Addressable:** Simple to consume
4. **Trustworthy:** Reliable, accurate, complete, consistent, up-to-date
5. **Self-explainable:** Easily understandable
6. **Interoperable:** Easy to combine
7. **Secure:** Adheres to security standards

**Producer/Consumer Framework:**
- **Data Producers:** Adopt product thinking, improve ownership of reusable products
- **Data Consumers:** Focus on value, set up portfolio, align on ownership/accountability, provide feedback, deliver reusable products

**Implementation Support:**
- Collaborate on portfolio setup
- Align ownership and accountability
- Manage consumer feedback for continuous improvement
- Accelerate delivery of reusable products

---

## 29. Data Domains (Subject Areas)

**Purpose:**
Logical organization of data into domains informing BDH data organization, ensuring simplified responsibility/ownership for Data Products, and guiding Service Management.

**Two-Level Structure:**

**Subject Areas:**
- Conceptual boundaries separating data product delivery and management
- Align to business value streams
- Same as current BDH tenancy
- Known as "data domains" outside BNZ

**Data Product Groups:**
- Lower granularity than Subject Areas
- Contain multiple schemas supporting related data products
- Enable focused product development and management

**Benefits:**
- Clear ownership boundaries
- Simplified responsibility model
- Effective service management (monitoring and alerting)
- Business alignment through value stream organization

---

## 30. Data Ops

**Definition:**
"The shift from DevOps to DataOps builds in automation, security and privacy by design, CI/CD and Service management."

**Core Components:**
- **Agile Development:** Agile ways of working and DevOps CI/CD processes
- **Automated Data Quality:** Built-in quality assurance
- **Automated Metadata Management:** Lineage, Data Definitions, Data Usage
- **Data Privacy and Compliance by Design:** RBAC, Masking Policies
- **Collaboration and Self-Service:** User empowerment with consistent governance

**Value Delivery:**
- **Data Engineering:** Analytics, data science, business intelligence
- **Data Governance:** Process control
- **Quality Assurance:** Consistent standards

**Empowerment Focus:**
Enable users to collaborate and consume data while ensuring governance and controls are enforced consistently.

---

## 31. Data Governance Uplift

**Framework Overview:**
Addresses gaps identified in Data Product Governance Framework developed with Accenture.

**Governance Structure:**

**Enablers (Capabilities):**
- Data Product Strategy, Operating Model, Regulatory compliance
- Data Governance automation, Change management, Executive Sponsorship

**Community Roles:**
- **Data Consumers:** Data Analyst, Data Scientist, Insights Analyst, Service/App Owner
- **Data Producers:** Solution Architect, Delivery Team, DP Business/Technical Owner
- **Data Governors:** DG Analyst, CDE Owner, Subject Area Owner, Data Steward

**Policies and Standards:**
- Data Management Standards, Policies, GIRP, SoP

**Lifecycle Processes:**
- DG Forum, DP Council, various management processes

**Governance Artefacts:**
- DP Registry, DP Contract, DP Usage Agreement, Audit and monitoring, Data marketplace

**Technology Enablers:**
- **Current:** Alation for catalog/workflow, GRACE for compliance
- **Gaps:** Data Quality, Reference Data Management capabilities

---

## 32. TSA Strategic Alignment

Introduction to how the Data & Analytics TSA aligns with BNZ's broader strategic technology themes.

---

## 33. Technology Strategy Alignment

**Five Strategic Technology Themes:**

**1. Modernise and Simplify:**
- Significantly reduced technology landscape
- Reduced functional overlap
- Move from expensive BNZ-hosted to SaaS
- Monolithic to modern, decoupled technologies
- Reusable data products, simplified pipelines
- Easy-to-work-with, integrate, secure technologies

**2. Agile and Adaptable:**
- Move to SaaS for easier management
- Modern, specialist technologies
- Delivering and adopting Data as a Product

**3. Platform Mindset:**
- Challenges in mapping capabilities (BIAN limitations)
- NAB alignment exploration needed
- Questions about Data & Analytics vs AI platform overlap

**4. Resilient, Secure and Safe:**
- Security, compliance, resilience embedded in design
- Automation and pattern reuse
- Appropriate procurement and due diligence processes

**5. Deeply Digital:**
- Simplified data pipelines
- Reduced data and processing duplication

---

## 34. Data & Analytics Initiatives & Objectives

**Current Funded Initiatives:**

**Data Programme (Programme #71859):**
Nine child initiatives including:
- Customer Master (Initiative #71929)
- Data Products - Customer360, ESG, Foundations, Loan Level Data
- Data Simplification, Enterprise Data Products
- Generative AI, Information Management

**Four Supporting Objectives:**
- Modernise Technology and Data Infrastructure
- Radically Simplify products, policies and processes
- Technology advancement
- Modernise and Simplify operations

**Integration:**
All initiatives work together to support the journey to target state across technology, process, and organizational capabilities.

---

## 35. Roadmap

Introduction to the detailed implementation roadmap and sequencing approach.

---

## 36. Data & Analytics Technology Roadmap - Approach

**Incremental Transformation Strategy:**
Taking incremental approach to target state while uplifting data ecosystem maturity for business value along the way.

**Key Focus Areas:**
- **Hydrating Snowflake (BDH):** Trusted copy of data from source
- **Shift from ETL to ELT:** Simplify pipelines, load once for reuse multiple times
- **Publishing Data Products:** Trusted, timely data for organization-wide use
- **Automated Classification/Protection:** Simplify and standardize sensitive data handling
- **Easy Data Access:** Make data easy to find, access, and use

**Maturity Building:**
Allows data process and practice maturity to build alongside technology adoption and exit.

**Trade-offs:**
- Enables de-duplication of effort over time
- Allows for priority fluctuation and investment flexibility
- Impacts speed of exit and cost of legacy technology

---

## 37. Data & Analytics Technology Roadmap - Approach (Continued)

**High Level Approach Sequence:**

1. **Build Foundations**
2. **Focus on exiting legacy Data Warehouses**
3. **Build data pipelines to hydrate BDH on target state foundations**
4. **Incremental exit of ETL technologies**
5. **Build Data Products**
6. **Enhance Data Governance**
7. **Repoint and/or redevelop reporting and insights**
8. **Build Models on target state**
9. **Exit legacy technology**

**Alternative Approach Rejection:**
"Lift and shift" approaches rejected as they:
- Don't deliver business value along the way
- Carry forward current state issues and challenges
- Result in higher costs for complex, duplicated processes in cloud

---

## 38. Roadmap - Technology Adoption & Exit High Level

**Technology Adoption Timeline (2025-2029):**

**2025:**
- AWS SageMaker Adoption (Q2-Q4)
- FiveTran Adoption (Q2-Q3)
- Alation Adoption (Q3-Q4)

**2026:**
- AstroCloud adoption for Airflow, dbtCore and Cosmos (Q2-Q3)
- Data Quality Target State (Q3-Q4)

**Technology Exit Timeline:**

**2025:**
- Erwin Data Modelling exit (Q2)
- Tableau exit (Q4)
- Precisely 360 exit (Q4)

**2026:**
- Axon EDC exit (Q2)
- Finance PowerBI exit (Q3)
- Newton exit (Q4)
- Report Wrapper exit (Q4)

**2027-2029:**
- SASOP exit (2027)
- Major legacy system exits: BIW/ODM, GDW, Hadoop (2027-2028)
- Final ETL tool exits: Wherescape Red, Informatica BDM/PC, ActiveBatch, Astronomer (2028-2029)

---

## 39. Roadmap - Data Foundations & Data Storage

**Integrated Foundation Building:**

**Data Platform Foundations:**
- BDH Foundations (Q1-Q2 2025)
- Data Products uplift (Q1-Q2 2025)
- FiveTran Adoption (Q2-Q3 2025)
- Alation Adoption (Q3 2025-Q2 2026)
- Data Governance Uplift (Q2-Q3 2026)
- AWS SageMaker Adoption (Q3-Q4 2025)
- Data Quality Target State (Q3-Q4 2026)
- AstroCloud transition (Q3 2026-Q4 2026)

**Legacy System Exit Sequence:**
Each legacy system follows pattern: Discovery → Develop Pipelines → Create Data Products → Reports to PBI/BDH → System Exit

**SASOP Exit:** Q3 2025 - 2027
**BIW/ODM Exit:** Q4 2025 - 2027
**GDW Exit:** Q1 2026 - 2027
**Hadoop Exit:** Q2 2026 - 2028

**Dependencies:**
Clear dependency mapping showing prerequisite completions for each phase.

---

## 40. Roadmap Continued

**Remaining Technology Migrations (2025-2029):**

**ETL and Transformation:**
- Wherescape Red exit (2027)
- Informatica BDM exit (2028)
- Informatica PC exit (2028)

**Scheduling & Orchestration:**
- ActiveBatch discovery and migration (2026-2027)
- Astronomer migration to AstroCloud (2026-2028)

**Reporting Tools:**
- Finance PowerBI migration (Q3 2026)
- Tableau migrations (2025-2026)
- Newton and Report Wrapper migrations (Q4 2026)
- Precisely 360 exit (Q1 2026)

**Pattern:**
Each migration follows discovery → pipeline development → workload migration → system exit sequence.

**Note:**
Establishing target state pipelines and data products during major system exits (SASOP/BIW/ODM/GDW/Hadoop) will reduce remaining migration scope.

---

## 41. Roadmap - Exit Blueprint

**Workload Migration Approach:**

**Process Milestones:**
1. **Workload Discovery**
2. **Data Pipelines:** Migrate Data Movement to FiveTran, Data Transformation to dbtCore, Develop Orchestration in Airflow
3. **BDH Uplift:** Land data from source in BDH
4. **Data Discovery & Protection:** Catalog, Classify & Protect (Alation, DataShield SecureDPS)
5. **Data Products:** Develop and Publish Data Products
6. **Reporting Update:** Redevelop Reporting & Insights, Update to use BDH
7. **Technology Exit**

**Key Dependencies:**
- FiveTran implementation
- BDH Uplift completion
- Alation deployment
- Data Products Uplift
- Power BI Future State

**Achievements:**
- BDH Hydration
- Simplification
- Target State implementation
- Governance Uplift
- Reusable Data Assets
- Enterprise Reporting future state

---

## 42. Focus Areas

Introduction to detailed focus area implementations across different technology domains.

---

## 43. Data Storage Target State Treatment Plan

**Consolidation Strategy:**
- Exit monolithic, duplicative data warehouses (GDW/Oracle, ODM/MSSQL, BIW/MSSQL)
- Consolidate to single data warehouse (Snowflake in BDH)
- Support data products journey

**BDH Uplift Requirements:**
- **Account splitting:** Enable GIRP compliance in Snowflake
- **Architecture refactor:** Enable load once, reuse multiple times
- **Improved RBAC:** Better access control implementation
- **Operating Model:** Improve alongside technology to realize benefits

**Data Lake Transition:**
- Cloudera Hadoop → BDH (Snowflake)
- Leverage S3 for cloud-native storage

**Benefits:**
- Simplified data storage landscape
- Improved performance and scalability
- Better governance and compliance
- Reduced maintenance overhead

---

## 44. Data Movement Target State

**Simplification Principles:**
- Shift from Extract, Transform, Load (ETL) to Extract, Load, Transform (ELT)
- Fewer data pipelines that load once and transform many times
- Cannot exit ETL technologies until last workloads migrated

**Ingestion Prioritization:**
"Streaming over CDC, CDC over Batch, Batch over File Transfer"

**Technology Consolidation:**
- Multiple ETL tools (SAS, Informatica PowerCenter, Informatica BDM, IBM InfoSphere) → FiveTran
- Streaming: Kafka (retained)
- File Transfer: sFTP (retained)

**Interim State:**
- Adopt CDC with IBM InfoSphere for Mainframe zOS to BDH hydration
- Bridge legacy and modern capabilities during transition

**Benefits:**
- Reduced pipeline complexity
- Improved data freshness
- Lower maintenance overhead
- Better scalability

---

## 45. Data Transformation, Scheduling & Orchestration Target State

**Transformation Modernization:**
- Shift from ETL to ELT pattern
- Standardized data engineering practices
- Multiple legacy tools → dbtCore (AstroCloud)

**Technology Consolidation:**
- **Current:** SAS (SASOP/SASGRID), Informatica PowerCenter/BDM, Wherescape Red
- **Target:** dbtCore (AstroCloud)

**Orchestration Simplification:**
- **Current:** Astronomer Airflow, ActiveBatch
- **Target:** AstroCloud Airflow

**Implementation Approach:**
- AstroCloud adoption for Airflow, dbtCore and Cosmos as future state
- Transitional option: DD&A dbtCore and Airflow consolidation to Astronomer
- Cannot exit until last workloads migrated to future state

**Benefits:**
- Standardized practices
- Improved operating model
- Reduced tool complexity
- Better automation capabilities

---

## 46. Access Layer Target State Treatment Plan

**Semantic Layer Gap:**
- Current: Power BI (limited to Microsoft technologies)
- Target: TBD - Priority for 2025 to Lean Canvas problems/opportunities
- Issue: PowerBI limits semantic layer use and requires downstream data protection

**Code Development Standardization:**
- **Current:** PyCharm (limited users)
- **Target:** Visual Studio Code (standard for all new users)
- Simplifies access and user experience for data engineers

**Data Marketplace Establishment:**
- **Implementation:** Alation
- **Capability:** Search, discover, maintain, access, consume data products
- Critical for enterprise-wide data use and reuse

**Data Science Workbench:**
- Covered in separate Data Science & ML section
- Integrated with overall access strategy

---

## 47. Data Science & Machine Learning Treatment Plan

**Data Science Workbench:**
- **Current:** VM/Bespoke Pipeline, Data Labs, BAE (Analytics Execution)
- **Target:** AWS SageMaker
- **Benefits:** Simplified productionization, operationalization, model serving, feature-complete environment

**Machine Learning Operations:**
- **New Capability:** ML model deployment in AWS SageMaker
- **Current Users:** FinCrime (sole users of Data Labs and BAE)
- **Future Users:** Customer master and CCD use cases

**Platform Rationalization:**
- Review need for BAE and Data Labs alongside SageMaker
- Retain Data Labs as purpose-built analytics platform for real customer data access
- Simplification driver for technology selection

**Access Layer:**
- **Current:** PyCharm (single user), majority use VSCode
- **Target:** AWS SageMaker Studio, AWS Code Editor (VSS)
- **Standard:** VSCode for consistency

---

## 48. Data Governance & Management Treatment Plan

**Technology Exit Strategy:**
- Actively exiting all Informatica technologies
- **Current:** Informatica Axon EDC, Informatica BDQ, Erwin, Ataccama
- **Target:** Alation (foundational), TBD for other capabilities

**Implementation Status:**
- **Alation Data Catalogue:** Foundational, adoption in progress, expected mid-2025
- **Data Quality:** Work required in FY25 to confirm future state
- **Reference Data:** Aspirational (Ataccama was previous target but not adopted)
- **Data Modeling:** Erwin in "Good to Leave" process, few users, low business value

**Maturity Requirements:**
- BNZ maturity level requires uplift before adopting Enterprise Data Modeling technology
- Focus on foundational capabilities first
- Build governance practices alongside technology adoption

---

## 49. Reporting & Analytics Treatment Plan

**Consolidation Strategy:**
"Power BI is the single data visualization tool for the enterprise in future state."

**Migration and Exit Plan:**
- **Assess:** Determine redundant reports for retirement on legacy systems
- **Tableau:** Server and Cloud exit in progress, expected Q4 2025
- **Finance PowerBI:** Consolidate to Power BI service, address unsupported processes
- **Report Wrapper:** Consolidate to Power BI, discussions underway
- **Newton:** Discovery required to confirm Power BI meets business needs
- **Precisely 360 Analyse:** Retire once SAP to Workday complete

**Special Considerations:**
- **CDM:** In Reference Reporting TSA, future state TBD, specialist requirements unlikely met by PowerBI
- **Business Critical Reports:** May have characteristics not met by Enterprise Reporting platform, requires assessment

**Implementation Challenges:**
- Finance reliance on unsupported processes (data download to desktop)
- Alternative approaches needed to meet specific business requirements

---

## 50. Key Stakeholders

**Stakeholder Engagement:**
- Key stakeholders engaged through collaborative review sessions
- Gaps require continued stakeholder collaboration for target state alignment
- Core Tech collaboration needed to align data programme work and reduce duplication

**Key Stakeholder Categories:**

**Data Platform Team:**
- Architects: Rodger Donaldson, Paul Dudding
- PMs & PLs: Deborah Gill, Jane Eagle

**Leadership:**
- GM Core Systems: Nic Olivier
- Head of Tech – Data & Analytics Platforms: Damion Riordan
- GM Data: Anna Tarasof
- GM Analytics & Insights: Alex Dickson
- Head of Data Risk: Roberta Prentice

**Architecture & Strategy:**
- GM Technology Strategy & Architecture: Shirley McIntyre
- Heads of Architecture: Tanya Boelema, Angus Cotton, Kim Arnold
- Enterprise Architects across EIM, FinCrime, Platforms, Integration, Finance, Cyber

**DD&A Implementation:**
- Leads: Daniel Williams, Grace Shin, Amy di Benedetto, Anne Irwin

**Executive Oversight:**
- Exec Data & Analytics: Kate Skinner
- Exec CIO: Paul Norman

**Governance:**
- TAF: 2/4/25
- SAA: 28/3/25

---

## 51. Questions?

This concludes the comprehensive Target State Architecture document for Data & Analytics and Enterprise Reporting, outlining BNZ's strategic approach to modernizing their data ecosystem through the implementation of modern, cloud-native technologies centered around the BDH platform.

---

**Document Summary:**
This TSA represents a comprehensive 3-5 year transformation from a complex, fragmented legacy data landscape to a modern, integrated data ecosystem. The approach emphasizes business value delivery throughout the journey, with a focus on data products, self-service capabilities, and automated governance. The target state significantly reduces technical complexity while improving data accessibility, quality, and governance across the enterprise.