# Data & Analytics, Enterprise Reporting Target State Architecture

**Version:** 3.0
**Status:** Draft 0.4
**Author:** Tracey Davis
**Date:** February 2025

---

## Executive Summary

This document defines the Target State Architecture (TSA) for BNZ's Data & Analytics and Enterprise Reporting capabilities. It establishes the strategic direction for transitioning from legacy data platforms to a modern, cloud-native data ecosystem built on Snowflake and supporting technologies.

### Target State Vision

> "Unlock a competitive advantage by transforming data into value which is connected to business decisions, actions and outcomes."

The vision is realized through four strategic pillars:

1. **Simplification & Standardisation** - Reduce complexity through platform consolidation
2. **Data Products** - Treat data as a product with clear ownership and quality standards
3. **Self-Service** - Enable business users to access and analyze data independently
4. **DataOps** - Implement modern data engineering practices for agility and reliability

---

## Platform Overview

### Data Value Chain

The platform supports the complete data value chain:

| Stage | Description | Key Technologies |
|-------|-------------|------------------|
| **Data Acquisition** | Ingest data from source systems | FiveTran, AstroCloud |
| **Data Curation** | Transform, cleanse, and model data | dbtCore, Snowflake |
| **Data Consumption** | Enable analytics and reporting | Power BI, Alation |
| **Data ROI** | Drive business outcomes | ML/AI capabilities |

### Scope

**In Scope:**
- Enterprise Data Warehouse (BNZ Data Hub)
- Data Integration and ETL/ELT
- Business Intelligence and Reporting
- Data Governance and Cataloguing
- Analytics and Data Science enablement

**Out of Scope:**
- Operational/transactional systems
- AI/ML Platform (covered separately)
- Real-time streaming (covered in separate TSA)

---

## Current State Architecture

### Existing Platforms

| Platform | Technology | Status | Issues |
|----------|------------|--------|--------|
| **GDW** | Oracle | Exit | Legacy, high cost, limited scalability |
| **BIW/ODM** | Microsoft SQL Server | Exit | Fragmented, technical debt |
| **Hadoop** | Cloudera | Exit | Underutilized, complex operations |
| **Informatica Suite** | PowerCenter, BDM, IDQ | Exit | High licensing costs, aging technology |
| **SAS** | SAS Enterprise | Exit | Expensive, limited integration |
| **Tableau** | Tableau Server | Exit | Consolidating to Power BI |

### Current State Issues

1. **Fragmentation** - Multiple data platforms with inconsistent data models
2. **Technical Debt** - Legacy systems requiring significant maintenance
3. **High Costs** - Expensive licensing and infrastructure
4. **Limited Agility** - Slow time-to-value for new analytics requirements
5. **Data Quality** - Inconsistent data quality across platforms
6. **Skills Gap** - Specialized skills required for legacy technologies

---

## Target State Architecture

### BNZ Data Hub (BDH)

The BNZ Data Hub built on **Snowflake** is the strategic enterprise data warehouse platform.

#### Architecture Principles

1. **Cloud-Native** - Leverage cloud scalability and elasticity
2. **Separation of Compute & Storage** - Independent scaling of resources
3. **Multi-Cluster Shared Data** - Single source of truth with workload isolation
4. **Zero-Copy Cloning** - Efficient development and testing environments
5. **Time Travel** - Data recovery and historical analysis

### Target Technology Stack

| Layer | Technology | Purpose | Lifecycle |
|-------|------------|---------|-----------|
| **Data Warehouse** | Snowflake | Enterprise data platform | Encourage |
| **Data Integration** | FiveTran | ELT data ingestion | Encourage |
| **Data Orchestration** | AstroCloud (Airflow) | Workflow orchestration | Encourage |
| **Data Transformation** | dbtCore (via Cosmos) | SQL-based transformation | Encourage |
| **Data Catalogue** | Alation | Data discovery & governance | Encourage |
| **Business Intelligence** | Power BI | Reporting & visualization | Encourage |
| **Data Science** | AWS SageMaker | ML model development | Encourage |

### Technology Lifecycle States

| State | Definition | Action |
|-------|------------|--------|
| **Innovate** | Emerging technologies for evaluation | Pilot, assess fit |
| **Encourage** | Strategic technologies for new work | Adopt for new projects |
| **Contain** | Current but transitioning technologies | No new development |
| **Exit** | Technologies being decommissioned | Migrate and retire |

---

## Technology Transition Roadmap

### Data & Analytics Roadmap

| Technology | 2025 | 2026 | 2027 | 2028 | 2029 |
|------------|------|------|------|------|------|
| **Snowflake (BDH)** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **FiveTran** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **AstroCloud** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **dbtCore/Cosmos** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **Alation** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **GDW (Oracle)** | Contain | Contain | Exit | Exit | - |
| **BIW/ODM** | Contain | Contain | Exit | Exit | - |
| **Hadoop** | Exit | Exit | - | - | - |
| **Informatica PC** | Contain | Exit | Exit | - | - |
| **Informatica BDM** | Contain | Exit | Exit | - | - |
| **Informatica IDQ** | Contain | Contain | Exit | Exit | - |
| **SAS** | Contain | Contain | Exit | Exit | - |

**Tipping Point:** 2027

### Enterprise Reporting Roadmap

| Technology | 2025 | 2026 | 2027 | 2028 | 2029 |
|------------|------|------|------|------|------|
| **Power BI** | Encourage | Encourage | Encourage | Encourage | Encourage |
| **Tableau** | Contain | Contain | Exit | Exit | - |
| **SSRS** | Contain | Contain | Exit | - | - |
| **SAS VA** | Contain | Exit | - | - | - |

**Tipping Point:** 2027

---

## NAB Alignment

### Aligned Elements

| Area | BNZ Approach | NAB Alignment |
|------|--------------|---------------|
| **Data Warehouse** | Snowflake | ✅ Aligned |
| **Data Integration** | FiveTran | ✅ Aligned |
| **Orchestration** | AstroCloud | ✅ Aligned |
| **Transformation** | dbtCore | ✅ Aligned |
| **Data Catalogue** | Alation | ✅ Aligned |
| **BI Platform** | Power BI | ✅ Aligned |

### BNZ-Specific Considerations

- **Regulatory Requirements** - RBNZ-specific compliance needs
- **Local Integration** - NZ-specific data sources and systems
- **Scale Differences** - Right-sized implementation for BNZ

---

## Focus Area Treatment Plans

### 1. Data Warehouse Consolidation

**Objective:** Migrate from GDW/BIW/ODM to Snowflake BDH

**Approach:**
- Domain-by-domain migration strategy
- Parallel running during transition
- Data validation and reconciliation
- Decommission legacy platforms post-migration

**Timeline:** 2025-2027

### 2. Data Integration Modernisation

**Objective:** Replace Informatica suite with FiveTran and AstroCloud

**Approach:**
- New integrations built on FiveTran
- Gradual migration of existing ETL jobs
- Leverage dbtCore for transformation logic
- Retire Informatica components progressively

**Timeline:** 2025-2028

### 3. BI Platform Consolidation

**Objective:** Standardise on Power BI for enterprise reporting

**Approach:**
- New reports built in Power BI
- Priority migration of Tableau dashboards
- Decommission legacy reporting tools
- Establish Power BI governance and standards

**Timeline:** 2025-2027

### 4. Data Governance Enhancement

**Objective:** Implement enterprise data catalogue and governance

**Approach:**
- Deploy Alation as data catalogue
- Establish data ownership model
- Implement data quality monitoring
- Enable self-service data discovery

**Timeline:** 2025-2026

### 5. Analytics Capability Uplift

**Objective:** Enable advanced analytics and data science

**Approach:**
- AWS SageMaker for ML workloads
- Integration with Snowflake data
- Self-service analytics enablement
- DataOps practices implementation

**Timeline:** 2025-2027

---

## BNZ Modernisation Index (BMI)

The BMI tracks progress of platform modernisation:

| Component | Current | Target | Notes |
|-----------|---------|--------|-------|
| **Data Warehouse** | 40% | 90% | GDW migration to BDH |
| **Data Integration** | 30% | 85% | Informatica to FiveTran |
| **Reporting** | 50% | 90% | Consolidation to Power BI |
| **Data Governance** | 35% | 80% | Alation implementation |

---

## Key Stakeholders

| Role | Responsibility |
|------|----------------|
| **Chief Data Officer** | Strategic direction and governance |
| **Head of Data Engineering** | Platform delivery and operations |
| **Head of Analytics** | Analytics capability and enablement |
| **Enterprise Architects** | Architecture standards and alignment |
| **Domain Data Owners** | Data quality and stewardship |

---

## Related Documents

- [AI Platform Architecture](../README.md)
- [Capability Model](../capabilities.csv)
- [Enterprise Information Management TSA](./Enterprise-Information-Management-TSA-V3.md)

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | Nov 2024 | Tracey Davis | Initial draft |
| 0.2 | Dec 2024 | Tracey Davis | Added roadmaps |
| 0.3 | Jan 2025 | Tracey Davis | NAB alignment updates |
| 0.4 | Feb 2025 | Tracey Davis | Final review draft |
