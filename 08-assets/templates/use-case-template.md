# [Full Name of Use Case]

## Document Control

| Property | Value |
|----------|-------|
| **Use Case ID** | `UC-XXX` (e.g., UC-025) |
| **Version** | `0.1` |
| **Status** | `Preliminary` |
| **Created Date** | `YYYY-MM-DD` |
| **Last Modified** | `YYYY-MM-DD` |
| **Owner** | [Business Unit / Department] |
| **Author(s)** | GenAI, [Name and Contact] |
| **Product Owner** | [Name and Contact] |
| **Executive Sponsor** | [Name and Title] |

## 1. Executive Summary

### 1.1 Use Case Overview

**One-Line Summary**: 
[Single sentence describing what this use case does]

**Business Problem**:
[Describe the current business problem or opportunity in 2-3 sentences]

**AI Solution**:
[Describe how AI addresses this problem in 7-8 sentences]

**Expected Outcomes**:

[Specify only qualitative outcomes, not quantitative outcomes]

- [Outcome 1: e.g., reduction in processing time]
- [Outcome 2: e.g., annual cost savings]
- [Outcome 3: e.g., improved customer satisfaction by 25%]

### 1.2 Strategic Alignment

**Business Category**: 
[Select one as primary from: Customer & Relationship Management, Risk Management, Lending & Credit Operations, Finance & Accounting, Data & Analytics, Customer Service & Support, Marketing & Personalization, Compliance & Financial Crime, Fraud Detection & Prevention, IT Operations & Service Management, Cybersecurity & Threat Detection, Software Development & Engineering, Procurement & Supply Chain, Quality Assurance & Compliance]

**Strategic Themes** (select all that apply):

- [ ] Customer Experience Excellence
- [ ] Operational Efficiency & Automation
- [ ] Risk & Compliance Excellence
- [ ] Data-Driven Decision Making
- [ ] Innovation & Competitive Differentiation

**Alignment Statement**:
[Explain how this use case supports BNZ's strategic objectives]

## 2. Business Case

### 2.1 Business Value

**Value Type** (select all that apply):

- [ ] Revenue Growth
- [ ] Cost Reduction
- [ ] Risk Reduction
- [ ] Customer Experience Improvement
- [ ] Regulatory Compliance
- [ ] Competitive Advantage

**Qualitative Benefits**:

| Benefit Type | Description | AI Accelerant | Evidence / Indicator |
|--------------|----------|--------|--------|
| [e.g., Time savings] | [Description of the benefit] | [Describe how AI will assist] | [e.g., Task completion time, process cycle time] |
| [e.g., Ease of use] | [Description of the benefit] | [Describe how AI will assist] | [e.g., User satisfaction scores, reduced training time] |
| [e.g., Customer Conversion] | [Description of the benefit] | [Describe how AI will assist] | [e.g., % increase] |

## 3. Target State Solution

### 3.1 Solution Overview

**AI/ML Approach**:
[Describe the AI/ML techniques that will be used: GenAI, ML prediction, NLP, Computer Vision, etc.]

![](UC-XXX-[UseCase]-Blueprint-v1.0.0.png)

**Solution Components**:

1. **[Component 1]**: [Description, e.g., GenAI-powered document extraction]
2. **[Component 2]**: [Description, e.g., ML risk scoring model]
3. **[Component 3]**: [Description, e.g., Automated workflow orchestration]

### 3.2 Data Architecture

**Data Inputs**:

| Dataset | Description | Source | Volume | Frequency | Format | Interface Status |
|-----------|--------|-----------|--------|--------------|--------------|--------------|
| [e.g., Customer profile] | [e.g., Customer details] | [e.g., CRM System] | [e.g., Large] | [e.g., Real-time] | [e.g., JSON via API] | Requires Work |
| [e.g., PDFs, scanned docs] | [e.g., Scanned documents] | [e.g., Documents] | [e.g., Very Large] | [e.g., Batch daily] | [e.g., PDF] | Requires Work    |

**Data Transformations**:
1. **[Transformation 1]**: [Description, e.g., OCR extraction from documents]
2. **[Transformation 2]**: [Description, e.g., Feature engineering for ML model]
3. **[Transformation 3]**: [Description, e.g., Data enrichment from external sources]

**Data Outputs**:

| Dataset | Description | Destination | Volume | Frequency | Format | Interface Status |  |
|-------------|-------------|-------------|--------|-----------|-----------|-----------|-----------|
| [e.g., Risk Score] | [e.g., Credit risk probability] | [e.g., Lending system] | [e.g., Large] | [e.g., Real-time] | [e.g., JSON via API] | Requires Work |  |
| [e.g., Summary Report] | [e.g., AI-generated narrative] | [e.g., Dashboard] | [e.g., Very Large] | [e.g., Real-time] | [e.g., HTML/PDF] | Requires Work |      |
| [e.g., Alerts] | [e.g., Fraud detection alerts] | [e.g., Case management] | [e.g., Large] | [e.g., Real-time] | [e.g., Event/Message] | Requires Work |  |

**Data Quality Requirements**:

- **Accuracy**: [e.g., 99%+ for financial data]
- **Completeness**: [e.g., No missing critical fields]
- **Timeliness**: [e.g., Real-time for fraud, batch daily for reports]
- **Consistency**: [e.g., Standardized formats across sources]

**Data Governance**:
- **Classification**: [Public / Internal / Confidential / Restricted]
- **Retention**: [Period and policy]
- **Privacy**: [PII handling, anonymization requirements]
- **Lineage**: [How data lineage will be tracked]

### 3.3 Architecture Patterns

**Primary Patterns Used**:

| Pattern ID | Pattern Name | Usage in Use Case |
|-----------|-------------|-------------------|
| PT-XXX | [e.g., Retrieval Augmented Generation] | [e.g., Knowledge base Q&A] |
| PT-XXX | [e.g., Real-Time Scoring] | [e.g., Fraud detection] |
| PT-XXX | [e.g., Intelligent Document Processing] | [e.g., Loan application extraction] |

**Architecture Building Blocks (ABBs)**:

| ABB ID | ABB Name | Purpose in Use Case | Criticality |
|--------|----------|-------------------|-------------|
| AB-XXX | [ABB Name] | [Role in use case] | Critical / High / Medium |
| AB-XXX | [ABB Name] | [Role in use case] | Critical / High / Medium |

## 4. Prioritization Scoring

TBD - Prioritization scoring to be completed during portfolio planning.

## 5. Risk Management

TBD - Risk assessment to be completed during detailed planning phase.

## 6. Success Metrics & KPIs

Track business and technical KPIs (details TBD).

