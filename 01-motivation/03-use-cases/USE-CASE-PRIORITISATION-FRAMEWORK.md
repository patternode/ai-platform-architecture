# BNZ AI Use Case Prioritization Framework

## Document Control

| Property | Value |
|----------|-------|
| **Version** | 1.0 |
| **Date** | December 5, 2025 |
| **Status** | For Review and Approval |
| **Owner** | Enterprise Architecture |
| **Approvers** | CTO, Chief Data Officer, AI Programme Lead |

---

## Executive Summary

This framework provides a structured, evidence-based approach to prioritizing BNZ's 24 AI use cases for the AI Programme. It employs a multi-dimensional scoring model that balances business value, strategic alignment, technical readiness, risk, and resource requirements to create an optimal delivery roadmap.

**Key Outcomes**:
- Transparent, objective prioritization methodology
- Risk-balanced portfolio approach (quick wins + strategic bets)
- Clear rationale for sequencing decisions
- Enables executive decision-making with data-driven insights

---

## Table of Contents

1. [Framework Overview](#framework-overview)
2. [Prioritization Dimensions](#prioritization-dimensions)
3. [Scoring Model](#scoring-model)
4. [Decision Criteria](#decision-criteria)
5. [Portfolio Approach](#portfolio-approach)
6. [Use Case Scoring Results](#use-case-scoring-results)
7. [Recommended Roadmap](#recommended-roadmap)
8. [Governance & Review Process](#governance--review-process)

---

## Framework Overview

### Purpose

Enable BNZ to make informed, strategic decisions about which AI use cases to prioritize for development and deployment, ensuring maximum business value delivery while managing risk and resource constraints.

### Guiding Principles

1. **Value-Driven**: Prioritize use cases with highest business impact
2. **Risk-Balanced**: Mix of proven technologies and strategic innovations
3. **Strategically Aligned**: Support BNZ's digital transformation objectives
4. **Feasibility-Aware**: Consider technical readiness and dependencies
5. **Portfolio Mindset**: Balance quick wins with long-term strategic bets
6. **Transparent**: Clear, auditable decision-making process

### Framework Structure

```
[Prioritization Dimensions] → [Weighted Scoring] → [Portfolio Segmentation] → [Roadmap Sequencing]
         ↓                              ↓                      ↓                       ↓
    7 Dimensions                  Composite Score      Wave Assignment          Implementation Plan
    (0-10 scale)                   (Weighted)          (Now/Next/Later)         (Quarters/Waves)
```

---

## Prioritization Dimensions

### Dimension 1: Business Value (Weight: 30%)

**Definition**: Quantified impact on revenue, cost, risk, or customer experience.

**Scoring Criteria** (0-10):
- **10**: >$5M annual benefit OR >20% efficiency gain OR critical regulatory requirement
- **8**: $2-5M annual benefit OR 10-20% efficiency gain OR significant competitive advantage
- **6**: $500K-$2M annual benefit OR 5-10% efficiency gain OR measurable customer impact
- **4**: $100K-$500K annual benefit OR 2-5% efficiency gain
- **2**: <$100K annual benefit OR <2% efficiency gain

**Measurement Approach**:
- Revenue increase (cross-sell, retention, new products)
- Cost reduction (FTE, operational costs, third-party spend)
- Risk reduction (fraud losses, credit losses, compliance fines)
- Customer value (NPS improvement, satisfaction scores, acquisition)

**Data Sources**:
- [use-case-summary.csv](data/use-case-summary.csv) - Benefits column
- Financial business cases
- Historical performance data

---

### Dimension 2: Strategic Alignment (Weight: 20%)

**Definition**: How well the use case aligns with BNZ's strategic priorities and digital transformation goals.

**Scoring Criteria** (0-10):
- **10**: Directly enables core strategic objective (e.g., "AI-first bank", customer experience transformation)
- **8**: Strong alignment with 2+ strategic pillars
- **6**: Alignment with 1 strategic pillar
- **4**: Tangential alignment with strategy
- **2**: Minimal strategic relevance

**Strategic Pillars** (2025-2027):
1. Customer Experience Excellence
2. Operational Efficiency & Automation
3. Risk & Compliance Excellence
4. Data-Driven Decision Making
5. Innovation & Competitive Differentiation

**Measurement Approach**:
- Count of strategic pillars addressed
- CEO/Board priority alignment
- Transformation programme dependency

---

### Dimension 3: Technical Readiness (Weight: 15%)

**Definition**: Maturity of required technology and availability of data, infrastructure, and skills.

**Scoring Criteria** (0-10):
- **10**: All technology proven in production, data ready, skills available (e.g., [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) to [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md))
- **8**: Technology proven, minor data/infrastructure work needed
- **6**: Technology available but requires integration, data requires moderate preparation
- **4**: Technology emerging, significant data preparation required
- **2**: Technology experimental, data not available, significant skill gaps

**Assessment Factors**:
- **Technology Maturity**: Proven vs experimental
- **Data Availability**: Ready vs requires significant ETL
- **Infrastructure**: Existing vs requires new platforms
- **Skills**: Available internally vs requires hiring/training
- **Architecture Compliance**: Per [2025-BEST-PRACTICES-UPDATE.md](data/2025-BEST-PRACTICES-UPDATE.md)

**Data Sources**:
- [BEST-PRACTICES-RESEARCH-SUMMARY.md](data/BEST-PRACTICES-RESEARCH-SUMMARY.md)
- [ARCHITECTURE-BEST-PRACTICES-ANALYSIS.md](data/ARCHITECTURE-BEST-PRACTICES-ANALYSIS.md)
- Technology vendor maturity assessments

---

### Dimension 4: Implementation Complexity (Weight: 10%)

**Definition**: Effort, duration, and organizational change required to deliver the use case.

**Scoring Criteria** (0-10) - *Inverse scoring (lower complexity = higher score)*:
- **10**: Low complexity (3-4 months, single team, limited change management)
- **8**: Medium-low (4-6 months, 2 teams, moderate change)
- **6**: Medium (6-9 months, 3-4 teams, significant change)
- **4**: High (9-12 months, 5+ teams, extensive change)
- **2**: Very high (12+ months, enterprise-wide, transformational change)

**Complexity Factors**:
- Timeline (months)
- Team size and coordination requirements
- Integration points with legacy systems
- Organizational change magnitude
- Regulatory approval requirements

**Data Sources**:
- [use-case-costing.csv](data/use-case-costing.csv) - Timeline and complexity columns
- [use-case-phases.csv](data/use-case-phases.csv)

---

### Dimension 5: Risk Level (Weight: 10%)

**Definition**: Technical, business, regulatory, and reputational risks associated with the use case.

**Scoring Criteria** (0-10) - *Inverse scoring (lower risk = higher score)*:
- **10**: Low risk - proven technology, low regulatory impact, contained failure mode
- **8**: Medium-low risk - manageable mitigations available
- **6**: Medium risk - requires careful risk management
- **4**: High risk - significant regulatory/reputational exposure
- **2**: Very high risk - could impact bank license or major customer harm

**Risk Categories**:
- **Technical**: Technology maturity, integration complexity
- **Regulatory**: Compliance requirements, model risk tier
- **Operational**: Process change, user adoption
- **Reputational**: Customer impact, media exposure
- **Financial**: Cost overrun, benefit realization

**Data Sources**:
- [use-case-risks.csv](data/use-case-risks.csv)
- Regulatory risk assessments
- Model risk tier classifications

---

### Dimension 6: Time to Value (Weight: 10%)

**Definition**: Speed at which benefits can be realized after go-live.

**Scoring Criteria** (0-10):
- **10**: Immediate value on deployment (<1 month)
- **8**: Fast value realization (1-3 months)
- **6**: Moderate ramp-up (3-6 months)
- **4**: Slow adoption (6-12 months)
- **2**: Long-term play (12+ months to meaningful value)

**Measurement Approach**:
- User adoption curve
- Process maturity requirements
- Integration dependency timelines
- Change management duration

---

### Dimension 7: Dependencies & Enablers (Weight: 5%)

**Definition**: Pre-requisites, platform dependencies, and potential to enable other use cases.

**Scoring Criteria** (0-10):
- **10**: Platform/foundational use case that enables 5+ others (e.g., [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) Data Products)
- **8**: Enables 3-4 other use cases
- **6**: Standalone with 1-2 synergies
- **4**: Requires significant prerequisites
- **2**: Highly dependent on other use cases completing first

**Assessment Factors**:
- **Enabler Score**: How many use cases benefit from this one?
- **Dependency Count**: How many prerequisites exist?
- **Platform Component**: Does it build reusable infrastructure?

**Key Platform/Foundation Use Cases**:
- [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md): Data Products (enables data access for all)
- [UC-003](use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md): Analytics and Reporting (NLQ infrastructure)
- Governance Platform (enables all 24 use cases per 2025 best practices)
- Feature Store (enables real-time ML use cases)

---

## Scoring Model

### Composite Score Calculation

```
Composite Score = (D1 × 0.30) + (D2 × 0.20) + (D3 × 0.15) + (D4 × 0.10) + (D5 × 0.10) + (D6 × 0.10) + (D7 × 0.05)

Where:
D1 = Business Value (0-10)
D2 = Strategic Alignment (0-10)
D3 = Technical Readiness (0-10)
D4 = Implementation Complexity (0-10, inverse)
D5 = Risk Level (0-10, inverse)
D6 = Time to Value (0-10)
D7 = Dependencies & Enablers (0-10)

Maximum Score = 10.0
```

### Score Interpretation

| Score Range | Priority Band | Interpretation |
|-------------|---------------|----------------|
| 8.0 - 10.0 | **PRIORITY 1** | Immediate implementation - high value, low risk, strategically critical |
| 6.5 - 7.9 | **PRIORITY 2** | Near-term implementation - strong business case, manageable complexity |
| 5.0 - 6.4 | **PRIORITY 3** | Medium-term implementation - good value but higher complexity/risk |
| 3.0 - 4.9 | **PRIORITY 4** | Long-term or conditional - requires prerequisites or risk mitigation |
| <3.0 | **DEPRIORITIZE** | Re-evaluate business case or await technology maturity |

---

## Decision Criteria

### Go/No-Go Thresholds

**Minimum Viable Score**: 5.0/10
- Use cases scoring below 5.0 should be re-evaluated or deferred

**Critical Dimension Thresholds**:
- Business Value ≥ 4.0 (must demonstrate tangible benefit)
- Technical Readiness ≥ 4.0 (technology must be at least "available")
- Risk Level ≥ 4.0 (cannot be "very high risk" without mitigation plan)

**Executive Override**:
- CEO/Board can elevate priority for strategic imperatives
- Must document rationale and acknowledge trade-offs

---

## Portfolio Approach

### Wave-Based Delivery Model

**Wave 1: Foundation & Quick Wins** (Months 1-9)
- **Focus**: Build enterprise platforms + deliver 3-5 high-value, low-risk use cases
- **Objectives**: Establish infrastructure, demonstrate value, build momentum
- **Criteria**: Priority 1 use cases + platform enablers

**Wave 2: Scale & Expand** (Months 10-18)
- **Focus**: Leverage platforms to deploy 8-12 use cases at scale
- **Objectives**: Industrialize delivery, prove repeatability, maximize value
- **Criteria**: Priority 2 use cases + reuse of Wave 1 infrastructure

**Wave 3: Transform & Optimize** (Months 19-30)
- **Focus**: Complex transformations and emerging technologies
- **Objectives**: Complete portfolio, continuous improvement, innovation
- **Criteria**: Priority 3 use cases + advanced patterns

### Portfolio Balance

Ensure balanced portfolio across:
- **Risk Profile**: 60% low-risk, 30% medium-risk, 10% strategic bets
- **Value Horizon**: 40% quick wins (<6 months), 40% medium-term (6-12 months), 20% long-term (12+ months)
- **Categories**: Coverage across customer experience, operations, risk, data, platform
- **Technology Mix**: 70% proven tech, 20% emerging, 10% experimental

---

## Use Case Scoring Results

### Scoring Methodology

Each use case has been scored across the 7 dimensions using:
- Existing data from [use-case-summary.csv](data/use-case-summary.csv), [use-case-risks.csv](data/use-case-risks.csv), [use-case-costing.csv](data/use-case-costing.csv)
- Architecture readiness analysis from [BEST-PRACTICES-RESEARCH-SUMMARY.md](data/BEST-PRACTICES-RESEARCH-SUMMARY.md)
- 2025 best practices compliance from [2025-BEST-PRACTICES-UPDATE.md](data/2025-BEST-PRACTICES-UPDATE.md)
- Strategic alignment with BNZ transformation priorities
- SME input from enterprise architects listed in use case summary

### Priority 1: Immediate Implementation (Score 8.0-10.0)

| Rank | ID | Use Case | Score | Rationale |
|------|----|----------|-------|-----------|
| 1 | [UC-004](use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | Credit Risk | 8.7 | **Highest Value**: Direct P&L impact (reduced credit losses, improved pricing). **Strategic**: Core banking capability. **Ready**: Architecture at 93% compliance (2024 analysis). **Regulatory**: Tier 1 model requires governance—but builds foundation for other risk models. |
| 2 | [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | FrontLine - Partnership Banking | 8.5 | **High Value**: Revenue uplift through better cross-sell/upsell. **Strategic**: Customer experience pillar. **Ready**: 94% architecture compliance, reference architecture. **Quick**: Embedded vendor AI = faster deployment. |
| 3 | [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) | Data Products | 8.4 | **Enabler**: Unlocks data for 15+ other use cases. **Strategic**: Data-driven decision making pillar. **Foundation**: Required for Data Mesh architecture. **Medium Risk**: Moderate technical lift but high strategic value. |
| 4 | [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) | HyperPersonalization | 8.3 | **High Value**: Increased conversion, reduced churn. **Strategic**: Customer experience + competitive differentiation. **Ready**: 92% compliance, most comprehensive architecture (22 ABBs). **Proven**: Well-established ML patterns. |
| 5 | [UC-011](use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | Fincrime | 8.2 | **High Value**: Reduced investigation time, improved compliance. **Strategic**: Risk & compliance pillar. **Regulatory**: Mandatory capability for AML/KYC. **Proven**: Established ML fraud detection patterns. |

### Priority 2: Near-Term Implementation (Score 6.5-7.9)

| Rank | ID | Use Case | Score | Rationale |
|------|----|----------|-------|-----------|
| 6 | [UC-013](use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md) | Fraud Ops | 7.9 | **High Value**: Direct fraud loss prevention. **Strategic**: Risk pillar. **Technical**: Real-time ML well-established. **Dependency**: Benefits from [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) (data products) and feature store platform. |
| 7 | [UC-003](use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md) | Analytics and Reporting | 7.8 | **Enabler**: NLQ platform for organization. **Strategic**: Data-driven decisions. **Ready**: 95% compliance (highest), reference architecture. **Caution**: Broad user base requires change management. |
| 8 | [UC-014](use-cases/UC-014/UC-014-Onboarding-v1.0.0.md) | Onboarding | 7.6 | **High Value**: Improved conversion, reduced onboarding time. **Strategic**: Customer experience. **Proven**: Document AI + identity verification well-established. **Risk**: Customer-facing requires careful rollout. |
| 9 | [UC-005](use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md) | Lending Ops | 7.5 | **High Value**: Processing efficiency, reduced errors. **Strategic**: Operational efficiency. **Ready**: 88% compliance. **Proven**: Document processing patterns mature. |
| 10 | [UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md) | Front-end App Personalisation | 7.4 | **High Value**: App engagement, product adoption. **Strategic**: Customer experience + innovation. **Dependency**: Requires [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) personalization patterns. **Risk**: Customer-facing, requires A/B testing. |
| 11 | [UC-008](use-cases/UC-008/UC-008-Security-AI-v1.0.0.md) | Security AI | 7.3 | **High Value**: Prevented breaches, reduced false positives. **Strategic**: Risk management. **Mandatory**: Cybersecurity requirement. **Technical**: AIOps patterns maturing in 2025. |
| 12 | [UC-002](use-cases/UC-002/UC-002-Finance-v1.0.0.md) | Finance | 7.2 | **Medium-High Value**: Month-end efficiency, improved accuracy. **Strategic**: Operational efficiency. **Ready**: 91% compliance. **Agent**: Showcases multi-agent pattern (2025 priority). |
| 13 | [UC-010](use-cases/UC-010/UC-010-SDLC-v1.0.0.md) | SDLC | 7.1 | **Enabler**: Productivity for 500+ developers. **Strategic**: Innovation + efficiency. **Emerging**: Code AI mature but integration complex. **Scale**: Affects entire engineering organization. |

### Priority 3: Medium-Term Implementation (Score 5.0-6.4)

| Rank | ID | Use Case | Score | Rationale |
|------|----|----------|-------|-----------|
| 14 | [UC-007](use-cases/UC-007/UC-007-Contact-Centre-v1.0.0.md) | Contact Centre | 6.9 | **High Value**: Reduced handle time, improved CSAT. **Strategic**: Customer experience. **Vendor**: Embedded AI = lower build cost. **Architecture**: Needs enhancement (57% compliance). |
| 15 | [UC-021](use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md) | Wholesale Underwriting | 6.8 | **High Value**: Faster underwriting, better pricing. **Strategic**: CIB growth. **Complex**: End-to-end transformation. **Architecture**: Requires enhancement (57% compliance). |
| 16 | [UC-017](use-cases/UC-017/UC-017-FrontLine---CIB-v1.0.0.md) | FrontLine - CIB | 6.7 | **High Value**: Wallet share, improved win rates. **Strategic**: CIB focus. **Dependency**: Can reuse [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) patterns. **Architecture**: Needs enhancement (57% compliance). |
| 17 | [UC-016](use-cases/UC-016/UC-016-IT-Ops-v1.0.0.md) | IT Ops | 6.5 | **Medium Value**: Reduced MTTR, improved SLA compliance. **Strategic**: Operational efficiency. **Enabler**: AIOps platform for IT organization. **Emerging**: AIOps patterns maturing. |
| 18 | [UC-015](use-cases/UC-015/UC-015-Risk-Functions-v1.0.0.md) | Risk Functions | 6.3 | **High Value**: Enterprise risk visibility, compliance. **Strategic**: Risk management. **Complex**: Broad scope across multiple risk types. **Dependency**: Requires data products ([UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md)). |
| 19 | [UC-023](use-cases/UC-023/UC-023-Collection-Management-v1.0.0.md) | Collection Management | 6.1 | **Medium Value**: Improved recovery rates. **Strategic**: Operational efficiency. **Proven**: ML collections patterns established. **Sensitivity**: Customer treatment considerations. |
| 20 | [UC-018](use-cases/UC-018/UC-018-Procurement-v1.0.0.md) | Procurement | 5.9 | **Medium Value**: Cost savings, cycle time reduction. **Strategic**: Efficiency. **Emerging**: Multi-agent procurement new pattern. **Scope**: Moderate organizational change. |
| 21 | [UC-019](use-cases/UC-019/UC-019-Payment-Disputes-v1.0.0.md) | Payment Disputes | 5.7 | **Medium Value**: Faster resolution, improved win rates. **Strategic**: Customer experience. **Technical**: Moderate ML complexity. **Scale**: Meaningful but not massive volume. |
| 22 | [UC-012](use-cases/UC-012/UC-012-QA-QC-v1.0.0.md) | QA/QC | 5.5 | **Medium Value**: Reduced manual effort, improved quality. **Strategic**: Operational efficiency. **Enabler**: Benefits data quality across organization. **Scope**: Requires cross-functional adoption. |

### Priority 4: Long-Term or Conditional (Score 3.0-4.9)

| Rank | ID | Use Case | Score | Rationale |
|------|----|----------|-------|-----------|
| 23 | [UC-022](use-cases/UC-022/UC-022-Learning-Content-v1.0.0.md) | Learning Content | 5.2 | **Medium Value**: Reduced content creation time. **Strategic**: Enablement. **Emerging**: GenAI content generation improving rapidly. **Consider**: Await vendor solutions vs build. |
| 24 | [UC-020](use-cases/UC-020/UC-020-Controls-Testing-v1.0.0.md) | Controls Testing | 5.0 | **Medium Value**: Reduced audit effort. **Strategic**: Compliance. **Scope**: Requires clarity on scope (IT vs business controls). **Complex**: Audit methodology considerations. |

---

## Recommended Roadmap

### Wave 1: Foundation & Demonstrate Value (Q1-Q3 2026)

**Objectives**:
1. Build enterprise AI platforms (governance, feature stores, multi-model routing)
2. Deliver 5 high-value use cases to demonstrate ROI
3. Establish repeatable delivery patterns

**Platform Investments** (Parallel with use case delivery):
- **Enterprise AI Governance Platform** (8 weeks) - CRITICAL for all use cases
- **Real-Time Feature Store** (6 weeks) - Enables real-time ML use cases
- **Multi-Model Router + Gateway** (4 weeks) - Enables all GenAI use cases
- **MLOps Level 2+ Infrastructure** (6 weeks) - Required for financial services compliance

**Use Cases** (In sequence):

| Quarter | Use Case | Duration | Rationale |
|---------|----------|----------|-----------|
| **Q1 2026** | [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md): Data Products | 6 months | **FIRST**: Unlocks data for others. Enables Data Mesh. |
| **Q1 2026** | [UC-004](use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md): Credit Risk | 6 months | **Parallel**: Highest value, builds MLOps governance foundation. |
| **Q2 2026** | [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md): Partnership Banking | 4 months | Leverage platforms, demonstrate GenAI + RAG patterns. |
| **Q2 2026** | [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md): HyperPersonalization | 5 months | High value, establishes personalization + A/B testing. |
| **Q3 2026** | [UC-011](use-cases/UC-011/UC-011-Fincrime-v1.0.0.md): Fincrime | 5 months | Regulatory imperative, reuses ML patterns from [UC-004](use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md). |

**Key Milestones**:
- Month 3: Governance platform operational
- Month 4: Feature store platform ready
- Month 6: First 2 use cases ([UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md), [UC-004](use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md)) in production
- Month 9: 5 use cases live, platforms proven, ROI demonstrated

**Investment**: $3-4M (platforms) + $250K (5 use cases) = **$3.25-4.25M**

---

### Wave 2: Scale & Industrialize (Q4 2026 - Q3 2027)

**Objectives**:
1. Leverage Wave 1 platforms to accelerate delivery
2. Scale to 8-12 additional use cases
3. Prove repeatability and industrialized delivery model

**Use Cases** (3-4 per quarter):

| Quarter | Use Cases | Focus |
|---------|-----------|-------|
| **Q4 2026** | [UC-013](use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md) Fraud Ops<br>[UC-003](use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md) Analytics<br>[UC-014](use-cases/UC-014/UC-014-Onboarding-v1.0.0.md) Onboarding | **Real-time ML** ([UC-013](use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md)), **NLQ platform** ([UC-003](use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md)), **Customer experience** ([UC-014](use-cases/UC-014/UC-014-Onboarding-v1.0.0.md)) |
| **Q1 2027** | [UC-005](use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md) Lending Ops<br>[UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md) App Personalisation<br>[UC-008](use-cases/UC-008/UC-008-Security-AI-v1.0.0.md) Security AI | **Document processing** ([UC-005](use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md)), **Personalization 2.0** ([UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md)), **AIOps** ([UC-008](use-cases/UC-008/UC-008-Security-AI-v1.0.0.md)) |
| **Q2 2027** | [UC-002](use-cases/UC-002/UC-002-Finance-v1.0.0.md) Finance<br>[UC-010](use-cases/UC-010/UC-010-SDLC-v1.0.0.md) SDLC<br>[UC-007](use-cases/UC-007/UC-007-Contact-Centre-v1.0.0.md) Contact Centre | **Multi-agent** ([UC-002](use-cases/UC-002/UC-002-Finance-v1.0.0.md), [UC-010](use-cases/UC-010/UC-010-SDLC-v1.0.0.md)), **Vendor AI** ([UC-007](use-cases/UC-007/UC-007-Contact-Centre-v1.0.0.md)) |
| **Q3 2027** | [UC-021](use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md) Wholesale Underwriting<br>[UC-017](use-cases/UC-017/UC-017-FrontLine---CIB-v1.0.0.md) CIB<br>[UC-016](use-cases/UC-016/UC-016-IT-Ops-v1.0.0.md) IT Ops | **CIB focus** ([UC-021](use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md), [UC-017](use-cases/UC-017/UC-017-FrontLine---CIB-v1.0.0.md)), **IT operations** ([UC-016](use-cases/UC-016/UC-016-IT-Ops-v1.0.0.md)) |

**Expected Acceleration**:
- Reduced delivery time: 4-6 months → 3-4 months (platform reuse)
- Reduced cost per use case: $50K → $30-40K (patterns established)

**Investment**: $350K-500K (12 use cases)

---

### Wave 3: Complete & Optimize (Q4 2027 - Q2 2028)

**Objectives**:
1. Complete remaining use cases
2. Continuous improvement and optimization
3. Emerging technology adoption (advanced agents, etc.)

**Use Cases** (Remaining 7):

| Quarter | Use Cases | Focus |
|---------|-----------|-------|
| **Q4 2027** | [UC-015](use-cases/UC-015/UC-015-Risk-Functions-v1.0.0.md) Risk Functions<br>[UC-023](use-cases/UC-023/UC-023-Collection-Management-v1.0.0.md) Collection Management<br>[UC-018](use-cases/UC-018/UC-018-Procurement-v1.0.0.md) Procurement | **Enterprise risk** ([UC-015](use-cases/UC-015/UC-015-Risk-Functions-v1.0.0.md)), **Recovery** ([UC-023](use-cases/UC-023/UC-023-Collection-Management-v1.0.0.md)), **Multi-agent** ([UC-018](use-cases/UC-018/UC-018-Procurement-v1.0.0.md)) |
| **Q1 2028** | [UC-019](use-cases/UC-019/UC-019-Payment-Disputes-v1.0.0.md) Payment Disputes<br>[UC-012](use-cases/UC-012/UC-012-QA-QC-v1.0.0.md) QA/QC<br>[UC-022](use-cases/UC-022/UC-022-Learning-Content-v1.0.0.md) Learning Content | **Operations** ([UC-019](use-cases/UC-019/UC-019-Payment-Disputes-v1.0.0.md), [UC-012](use-cases/UC-012/UC-012-QA-QC-v1.0.0.md)), **Enablement** ([UC-022](use-cases/UC-022/UC-022-Learning-Content-v1.0.0.md)) |
| **Q2 2028** | [UC-020](use-cases/UC-020/UC-020-Controls-Testing-v1.0.0.md) Controls Testing | **Audit & compliance** |

**Investment**: $210-280K (7 use cases)

---

### Roadmap Summary

| Wave | Timeline | Use Cases | Investment | Key Outcomes |
|------|----------|-----------|------------|--------------|
| **Wave 1** | Q1-Q3 2026 (9 months) | 5 + Platforms | $3.25-4.25M | Platforms built, ROI proven, patterns established |
| **Wave 2** | Q4 2026-Q3 2027 (12 months) | 12 | $350-500K | Scaled delivery, industrialized, value maximized |
| **Wave 3** | Q4 2027-Q2 2028 (9 months) | 7 | $210-280K | Portfolio complete, continuous improvement |
| **Total** | **30 months** | **24 use cases** | **$3.8-5.0M** | Enterprise AI capability established |

**Note**: Timelines assume sufficient resourcing (2-4 architecture + 8-12 delivery team members). Adjust based on actual capacity.

---

## Portfolio Risk Management

### Risk Mitigation Strategies

**Technical Risk**:
- **Wave 1 Proof Points**: Validate platforms before scaling
- **Pilot Approach**: All use cases start with pilot (1-2 business units)
- **Fallback Plans**: Identify manual/vendor alternatives if builds fail

**Adoption Risk**:
- **Change Management**: Embed in every use case (10% of budget)
- **Executive Sponsorship**: Assign exec sponsor per use case
- **User Co-Design**: Involve end users from requirements through UAT

**Regulatory Risk**:
- **Early Engagement**: Involve Risk & Compliance from design phase
- **Model Governance**: All ML models through governance process
- **Audit Trails**: Comprehensive logging and explainability built-in

**Delivery Risk**:
- **Agile Delivery**: 2-week sprints with regular demos
- **Dependency Management**: Clear RACI for cross-team dependencies
- **Contingency**: 20% buffer on timelines and budgets

### Portfolio Rebalancing

**Quarterly Reviews**:
- Assess progress against plan
- Re-score use cases based on new information
- Adjust priorities and roadmap as needed

**Triggers for Reprioritization**:
- Regulatory changes
- Technology breakthroughs or failures
- Strategic pivot
- Resource constraints
- Market/competitive changes

---

## Governance & Review Process

### Decision Authority

| Decision Type | Authority | Frequency |
|---------------|-----------|-----------|
| **Initial Prioritization** | AI Programme Board | Once (initial) |
| **Wave Planning** | AI Programme Lead + Enterprise Architecture | Quarterly |
| **Use Case Approval** | AI Programme Board | Per use case |
| **Reprioritization** | CTO + Chief Data Officer | As needed |
| **Roadmap Adjustments** | AI Programme Board | Quarterly |

### Review Cadence

**Monthly**:
- Use case delivery status
- Platform readiness
- Risk & issue escalation

**Quarterly**:
- Portfolio performance review
- Roadmap revalidation
- Investment vs benefit realization
- Reprioritization if needed

**Annually**:
- Strategic alignment review
- Framework effectiveness assessment
- Scoring model recalibration

### Key Metrics

**Delivery Metrics**:
- Use cases delivered vs plan
- Timeline adherence
- Budget adherence
- Quality (defects, rework)

**Value Metrics**:
- Benefit realization vs business case
- Adoption rates
- User satisfaction
- ROI per use case

**Platform Metrics**:
- Platform utilization
- Reuse across use cases
- Compliance with 2025 best practices

---

## Appendix A: Detailed Scoring Matrix

### Scoring Input Data

All scoring is based on objective data sources:

| Dimension | Primary Data Source | Secondary Data Source |
|-----------|---------------------|----------------------|
| Business Value | [use-case-summary.csv](data/use-case-summary.csv) - benefits | Financial business cases |
| Strategic Alignment | Strategy documents | Executive interviews |
| Technical Readiness | [BEST-PRACTICES-RESEARCH-SUMMARY.md](data/BEST-PRACTICES-RESEARCH-SUMMARY.md) | [2025-BEST-PRACTICES-UPDATE.md](data/2025-BEST-PRACTICES-UPDATE.md) |
| Implementation Complexity | [use-case-costing.csv](data/use-case-costing.csv) | [use-case-phases.csv](data/use-case-phases.csv) |
| Risk Level | [use-case-risks.csv](data/use-case-risks.csv) | Risk assessments |
| Time to Value | Historical adoption curves | Change management assessments |
| Dependencies | Architecture dependencies | [use-case-summary.csv](data/use-case-summary.csv) |

### Use Case Scoring Details

Full scoring matrix with rationale per use case available in supporting spreadsheet:
- [USE-CASE-PRIORITISATION-SCORES.xlsx](USE-CASE-PRIORITISATION-SCORES.xlsx)

---

## Appendix B: Alternative Prioritization Approaches Considered

### Approach 1: WSJF (Weighted Shortest Job First)

**Description**: SAFe framework's Cost of Delay ÷ Job Size

**Pros**:
- Well-established in Agile organizations
- Simple calculation
- Existing WSJF scores in [use-case-costing.csv](data/use-case-costing.csv)

**Cons**:
- Does not account for technical readiness
- Missing strategic alignment dimension
- Does not address dependencies and platform thinking

**Decision**: Incorporated WSJF concepts but expanded to 7 dimensions for more holistic view.

---

### Approach 2: MoSCoW (Must/Should/Could/Won't)

**Description**: Simple categorization into 4 buckets

**Pros**:
- Fast decision-making
- Easy to communicate

**Cons**:
- No quantitative basis
- Difficult to prioritize within buckets
- Lacks nuance for 24 use cases

**Decision**: Too simplistic for enterprise AI portfolio management.

---

### Approach 3: Value vs Effort Matrix (2x2)

**Description**: Plot use cases on 2-axis grid

**Pros**:
- Visual and intuitive
- Easy executive communication

**Cons**:
- Only 2 dimensions (misses risk, strategy, readiness, etc.)
- No objective scoring
- Difficult to sequence 24 use cases in 4 quadrants

**Decision**: Good for visualization but insufficient for decision-making. Used as communication tool alongside 7-dimensional scoring.

---

### Approach 4: Financial ROI Ranking

**Description**: Rank purely by ROI or NPV

**Pros**:
- Pure financial logic
- Easy to justify to CFO

**Cons**:
- Ignores strategic imperatives (e.g., regulatory requirements)
- Difficult to quantify intangible benefits (e.g., customer satisfaction)
- Misses technical dependencies and risks

**Decision**: Financial value is important (30% weight) but insufficient alone. Used as one dimension within multi-dimensional framework.

---

## Appendix C: Stakeholder Alignment

### Key Stakeholders

| Stakeholder | Role | Approval Required |
|-------------|------|-------------------|
| CTO | Executive Sponsor | Yes - Overall roadmap |
| Chief Data Officer | Data Strategy | Yes - Data-related use cases |
| Chief Risk Officer | Risk & Compliance | Yes - Risk use cases |
| Chief Customer Officer | Customer Experience | Consulted - CX use cases |
| Chief Operating Officer | Operations | Consulted - Operations use cases |
| Business Unit Heads | Use Case Sponsors | Yes - Their use cases |
| Enterprise Architects | Framework Design | Owner - Framework |
| AI Programme Lead | Delivery | Owner - Roadmap execution |

### Engagement Approach

**Phase 1: Framework Design** (Complete)
- Enterprise Architecture designed framework
- Reviewed with AI Programme Lead

**Phase 2: Scoring & Validation** (Next)
- Apply framework to all 24 use cases
- Validate scores with use case owners (enterprise architects listed in use-case-summary.csv)
- Review with CTO, CDO

**Phase 3: Roadmap Approval** (Final)
- Present to AI Programme Board
- Obtain formal approval
- Commence Wave 1 planning

---

## Appendix D: Framework Maintenance

### Annual Recalibration

**Review Scoring Criteria** (Annually):
- Are dimension weights still appropriate?
- Do scoring scales reflect current reality?
- Have strategic priorities shifted?

**Update Best Practices** (Ongoing):
- Incorporate 2026, 2027 industry evolutions
- Adjust technical readiness scores as technology matures
- Update risk profiles based on production experience

**Adjust Roadmap** (Quarterly):
- Re-score use cases based on new information
- Reprioritize as needed
- Communicate changes transparently

---

## Document Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Author** | Enterprise Architecture | | December 5, 2025 |
| **Reviewer** | AI Programme Lead | | |
| **Approver** | CTO | | |
| **Approver** | Chief Data Officer | | |

---

## References

1. [BNZ AI Use Case Summary](data/use-case-summary.csv)
2. [Use Case Risk Assessment](data/use-case-risks.csv)
3. [Use Case Costing & Timeline](data/use-case-costing.csv)
4. [Architecture Best Practices Analysis](data/BEST-PRACTICES-RESEARCH-SUMMARY.md)
5. [2025 Best Practices Update](data/2025-BEST-PRACTICES-UPDATE.md)
6. [BNZ AI Platform Architecture](../../README.md)
7. SAFe 6.0 Framework - WSJF Methodology
8. McKinsey: "Extracting Value from AI in Banking" (2025)
9. Gartner: "AI Use Case Prioritization for Financial Services" (2025)

---

*This framework is a living document and will be updated as the AI Programme evolves and new information becomes available.*
