# Analytical Semantic Modelling as a Function Within A&I

## Current State A&I Report Development

### Example
A business requirement has been received to create a new report showing customer contacts for each campaign. Estimated time for completion: **1 month**.

#### Current Process
1. **Investigation (1 Day)**  
   Insights Analyst investigates available tables, their locations, relationships, and suitability for the business need.

2. **Data Wrangling (2-3 Weeks)**  
   Analyst builds SQL tables in Hadoop, sets up scheduled refreshes, and creates a data model.

3. **Report Development (1 Week)**  
   Analyst collaborates with the requester to create visuals and set up security groups.

4. **Report Delivery (1 Day)**  
   Report is published to a shared workspace for secure access.

### Concerns with the Current Process
- **Fragmented Data**: Data is developed for specific requirements, limiting reuse.
- **Inefficiencies**: Repeated data shaping increases time-to-insight and reduces scalability.
- **Limited Support for New Use Cases**: Current setup lacks integration with tools like Copilot.
- **Future Security Needs**: Fragmented approach cannot reliably support governance.

---

## Problem Statement

The current process for developing analytics reports is fragmented and inefficient. Data is often shaped for specific requirements, leading to limited reusability and increased time-to-insight. Additionally, the lack of integration with modern tools like Copilot and the inability to reliably support governance pose significant challenges. These issues hinder scalability, consistency, and the ability to meet future security and business needs.

---

## Current Direction for Future State Analytics

### Plan
- **Goal**: Deliver trusted, secure, and centralized data analytics solutions.
- **How**: Build a modular architecture, provide strong governance, and ensure seamless platform integration.

### Key Issues
- Ineffective integration between Snowflake and Power BI.
- Performance, cost, and development challenges with Snowflake security.

---

## Proposed Approach

### Improvements
1. **Faster Report Delivery**: Centralized semantic models enable quicker content delivery.
2. **Consistent Metrics**: Centralized logic ensures uniformity across reports.
3. **Reduced Tech Debt**: Larger reusable models reduce the need for bespoke solutions.
4. **Enhanced Copilot Experience**: Centralized models improve natural language querying.
5. **Cost Efficiency**: Scheduled data retrieval reduces Snowflake compute costs.

### Considerations
- **Security Management**: Align access controls in Power BI with Snowflake.
- **Minimize Data Duplication**: Design semantic models for maximum reuse.
- **Monitor Data Traffic**: Implement tools to track data usage.
- **Near-Real-Time Data**: Address business cases requiring near-real-time reporting.

---

## Semantic Models and Layers

### Definition
A **semantic model** is a structured representation of business data that:
- Translates technical data into business-friendly formats.
- Centralizes business logic for consistency.

### Core Functions
- **Reusability**: Enables reuse across dashboards, reports, and tools.
- **Data Abstraction**: Simplifies complex data into understandable terms.
- **Governance**: Embeds security, compliance, and version control.

### Strategic Importance
- Supports CI/CD pipelines for automated testing and deployment.
- Enhances collaboration between data engineers and analysts.

---

## Analytics Engineering

### Definition
A specialized function bridging data engineering and analytics, focusing on:
- Building and maintaining semantic models.
- Defining key business metrics.
- Ensuring data quality and governance.

### Responsibilities
- Transforming enterprise data products into semantic models.
- Designing reusable and optimized semantic models.
- Documenting definitions, transformations, and lineage.

---

## Future State Workflow

### Example
Using the same business requirement as before, the new workflow reduces task completion time to **1 week**.

1. **Semantic Model Development (Immediate)**  
   Pre-built Customer Engagement Semantic Model is used.

2. **Investigation (0.5 Days)**  
   Analyst checks the semantic model for required data.

3. **Copilot Usage (Immediate)**  
   Copilot assists in querying the semantic model.

4. **Report Development (1 Week)**  
   Analyst collaborates with the requester to create visuals.

5. **Report Delivery (1 Day)**  
   Report is published to a secure shared space.

### Benefits
- **Efficiency Gains**: Faster analytics and report creation.
- **Reusability**: Standardized models improve accuracy and trust.
- **Reliable Development**: CI/CD pipelines ensure quality.
- **Stronger Governance**: Centralized security and compliance.
- **Improved Collaboration**: Aligns data engineers and analysts.
- **AI Enablement**: Centralized metadata enhances LLM accuracy.

---

## Supporting Tools

### Azure DevOps
- Enables version control, automation, and governance for data assets.

### GitHub Copilot
- Accelerates development of code-heavy BI components.

---

## Future State Platforms
- **Snowflake**: Centralized data storage and governance.
- **Power BI**: Reporting and visualization.
- **Azure DevOps & GitHub Copilot**: Supporting tools for development.

---

## Engagements
### Analytics & Insights Leadership
- Alex Dickson (General Manager, Endorsed)
- Yi-Jing Chung (Lead Data Designer, Reviewed)

### External Consultants
- Duncan Gillies (Accenture, Reviewed)
- Cherise Stevens (Reviewed)

### Heads of Analytics
- Lydia Bandzo, Danny Mwiinga, Vinay Badigar, Francis Loh, David H. Grant (Reviewed)
