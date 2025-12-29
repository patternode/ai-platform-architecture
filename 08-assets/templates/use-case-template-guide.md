# Use Case Template - Quick Start Guide

## Overview

The **USE-CASE-TEMPLATE.md** provides a comprehensive framework for documenting AI use cases at BNZ. This guide helps you get started with using the template effectively.

---

## When to Use This Template

Use this template when:
- ✅ Proposing a new AI use case
- ✅ Documenting an existing use case for prioritization
- ✅ Preparing a business case for executive approval
- ✅ Planning implementation of an approved use case
- ✅ Creating use case documentation for the AI Programme

---

## Template Structure

The template has **14 main sections** organized by use case maturity level:

### Phase 1: Initial Proposal (For Prioritization)
**Sections 1-6** - Minimum required for prioritization workshops

| Section | Purpose | Estimated Time |
|---------|---------|----------------|
| 1. Executive Summary | High-level overview and strategic alignment | 30 minutes |
| 2. Business Case | Benefits, costs, ROI, industry benchmarks | 1-2 hours |
| 3. Current State | Pain points, stakeholders, current process | 1 hour |
| 4. Target State | Solution approach, data, technology | 2-3 hours |
| 5. Implementation Plan | Timeline, dependencies, resources | 1 hour |
| 6. Prioritization Scoring | WSJF, DVF, multi-dimensional scores | 30 minutes |

**Total Time**: 6-8 hours (can be done over 1-2 weeks)

### Phase 2: Detailed Planning (Post-Prioritization)
**Sections 7-11** - Required before implementation begins

| Section | Purpose | Estimated Time |
|---------|---------|----------------|
| 7. Risk Management | Risks, mitigations, model risk, compliance | 2 hours |
| 8. Success Metrics & KPIs | Business and technical KPIs, monitoring | 1 hour |
| 9. Governance & Compliance | Governance model, audit requirements | 1 hour |
| 10. Change Management | Training, rollout, stakeholder engagement | 2 hours |
| 11. Post-Implementation | Hypercare, continuous improvement | 1 hour |

**Total Time**: 7 hours

### Phase 3: Documentation & Approvals
**Sections 12-14** - Final documentation

| Section | Purpose | Estimated Time |
|---------|---------|----------------|
| 12. References & Appendices | Links, glossary, related documents | 30 minutes |
| 13. Approvals | Sign-offs from key stakeholders | N/A (review process) |
| 14. Notes for Authors | Guidance for completing template | N/A (reference only) |

---

## Quick Start: 3 Pathways

### Pathway 1: New Use Case for Prioritization (6-8 hours)

**Goal**: Get a new use case ready for DVF and WSJF workshops

**Steps**:
1. **Copy the template**: 
   - Save as `UC-0XX-[YourUseCaseName]-v1.0.0.md`
   - Update Document Control section with your details

2. **Complete Sections 1-6**:
   - Section 1: Write the executive summary (30 min)
   - Section 2: Quantify business benefits and costs (1-2 hours)
   - Section 3: Document current pain points (1 hour)
   - Section 4: Describe the AI solution approach (2-3 hours)
   - Section 5: Estimate timeline and dependencies (1 hour)
   - Section 6: Score using WSJF and DVF (30 min - can be done in workshop)

3. **Review**: 
   - Check the Quality Checklist in Section 14
   - Share with Enterprise Architect for feedback

4. **Submit**: 
   - Add to prioritization spreadsheet
   - Bring to DVF workshop

**Deliverable**: Use case ready for prioritization workshop

---

### Pathway 2: Approved Use Case - Implementation Planning (7 hours)

**Goal**: Take a prioritized use case and prepare for implementation

**Prerequisites**: 
- Use case has passed DVF and WSJF scoring
- Use case assigned to Wave 1 or Wave 2
- Budget and resources approved in principle

**Steps**:
1. **Start with existing Sections 1-6** from prioritization phase

2. **Complete Sections 7-11**:
   - Section 7: Detailed risk assessment and mitigations (2 hours)
   - Section 8: Define KPIs and monitoring (1 hour)
   - Section 9: Plan governance and compliance (1 hour)
   - Section 10: Develop change management plan (2 hours)
   - Section 11: Plan hypercare and continuous improvement (1 hour)

3. **Create Supporting Documents**:
   - Architecture diagram (drawio)
   - Sequence diagram (drawio)
   - Test plan
   - Training materials

4. **Obtain Approvals**:
   - Route through Section 13 approval process
   - Executive Sponsor, Enterprise Architect, Security, Risk & Compliance

**Deliverable**: Fully documented use case ready for implementation kickoff

---

### Pathway 3: Existing Use Case - Documentation (2-3 hours)

**Goal**: Document an existing/in-flight use case for the AI Programme

**Steps**:
1. **Gather Existing Materials**:
   - Business case, architecture docs, test plans
   - Performance data, metrics, user feedback

2. **Complete Template in Order**:
   - Focus on what exists (Current State, Target State, Implementation)
   - Document lessons learned in Post-Implementation section
   - Update metrics with actuals vs targets

3. **Fill Gaps**:
   - If prioritization scores missing, calculate retroactively
   - If KPIs not defined, establish going forward
   - If governance not formalized, document current approach

**Deliverable**: Documented use case for AI Programme portfolio

---

## Section-by-Section Guidance

### 1. Executive Summary (Required)

**Purpose**: Communicate the essence of the use case in 1 page

**Key Questions to Answer**:
- What business problem are we solving?
- How does AI help solve it?
- What are the expected outcomes?
- How does it align with BNZ strategy?

**Tips**:
- Write this LAST after completing other sections
- Make it executive-friendly (no jargon)
- Lead with business value, not technology

**Common Mistakes**:
- ❌ Too technical, too long
- ❌ Vague benefits ("improve efficiency")
- ❌ Missing strategic alignment

**Good Example**:
> *"Partnership Banking relationship managers spend 5-7 hours preparing for client meetings, manually gathering data from 15+ systems. This use case deploys GenAI to automate meeting preparation, generating personalized client briefings in <10 minutes. Expected outcomes: 40-60% efficiency gain, 2-3x increase in qualified leads, 5% boost in conversion rates. Aligns with Customer Experience Excellence and Revenue Growth strategic pillars."*

---

### 2. Business Case (Required)

**Purpose**: Justify the investment with quantified benefits and costs

**Key Questions to Answer**:
- What are the quantified benefits? (revenue, cost, risk, CX)
- What will it cost to build and run?
- What's the ROI and payback period?
- What evidence supports our assumptions? (benchmarks, examples)

**Tips**:
- **Be specific**: "$2-5M annual savings" not "significant savings"
- **Use ranges**: Accounts for uncertainty
- **Include industry benchmarks**: Builds credibility
- **Document assumptions**: Make them transparent

**Benefit Quantification Formula**:
```
Annual Benefit = (Current State Cost - Future State Cost) × Volume
OR
Annual Benefit = Revenue Uplift × Customer Base × Conversion Rate
```

**Common Mistakes**:
- ❌ Vague, unquantified benefits
- ❌ Overly optimistic estimates with no evidence
- ❌ Missing comparable examples/benchmarks
- ❌ Forgetting ongoing costs (just showing development costs)

**Good Example**:
```markdown
| Benefit Type | Baseline | Target | Impact | Annual Value |
|--------------|----------|--------|--------|--------------|
| Processing Time | 5-7 days | 24-48 hours | 70% reduction | $800K (reduced FTE costs) |
| Error Rate | 5% | 0.5% | 90% reduction | $400K (reduced rework) |
| Customer Conversion | 2% | 3.5% | 75% increase | $2M (revenue uplift) |

Total Annual Benefit: $3.2M
Total Development Cost: $850K
Annual Run Cost: $150K
ROI: 300% over 3 years, Payback: 10 months
```

---

### 3. Current State Assessment (Required for Implementation)

**Purpose**: Document what's broken and who's impacted

**Key Questions to Answer**:
- What's the current process?
- What are the pain points?
- Who is affected and how?
- What systems are involved?

**Tips**:
- Interview actual users, not just managers
- Quantify pain points (time wasted, error rates)
- Identify all stakeholders, including those who might resist
- Map the current system landscape

**Common Mistakes**:
- ❌ Generic pain points without evidence
- ❌ Missing key stakeholders
- ❌ No baseline metrics (can't measure improvement)

---

### 4. Target State Solution (Required)

**Purpose**: Define the AI solution and technical approach

**Key Questions to Answer**:
- What AI/ML techniques will we use?
- What data is required and is it available?
- What technology stack will we use?
- What architecture patterns apply?

**Tips**:
- **Reference existing patterns**: Don't reinvent (see PT-001 to PT-018)
- **Assess data availability**: "Requires work" is honest
- **Reuse enterprise platforms**: List what you'll reuse from Wave 1
- **Calculate ABB count**: More ABBs = better architecture

**Data Inputs Template**:
```markdown
| Data Source | Data Type | Volume | Frequency | Availability |
|-------------|-----------|--------|-----------|--------------|
| CRM | Customer profile | 2M records | Real-time | ✅ Ready |
| Loan System | Application data | 50K/year | Batch daily | ⚠️ Needs ETL work |
```

**Common Mistakes**:
- ❌ Not referencing architecture patterns
- ❌ Unrealistic data availability ("all data is ready")
- ❌ Missing ABBs or not mapping to standard ABBs
- ❌ Proposing custom platforms instead of reusing

**Pattern Reference Example**:
```markdown
| Pattern ID | Pattern Name | Usage in Use Case |
|-----------|-------------|-------------------|
| PT-005 | Retrieval Augmented Generation | Knowledge base Q&A for customer queries |
| PT-011 | Intelligent Document Processing | Loan application data extraction |
| PT-001 | Enterprise AI Governance | Compliance and audit trail |
```

---

### 5. Implementation Plan (Required)

**Purpose**: Plan the delivery timeline and resources

**Key Questions to Answer**:
- How long will it take?
- What are the phases? (Discovery, Build, Pilot, Rollout)
- What dependencies exist?
- What resources are required?

**Tips**:
- Use realistic timelines (6-12 months typical)
- Include 20% contingency
- Identify blocking dependencies
- Don't forget change management resources (10-15% of budget)

**Timeline Estimation Guide**:
- **Simple use case** (low complexity, proven tech): 3-4 months
- **Medium use case** (moderate complexity, some integration): 6-8 months
- **Complex use case** (high complexity, extensive integration): 9-12 months
- **Transformational** (end-to-end process change): 12-18 months

**Common Mistakes**:
- ❌ Underestimating timeline (forgetting testing, training, rollout)
- ❌ Missing critical dependencies
- ❌ Not allocating change management resources
- ❌ No contingency buffer

---

### 6. Prioritization Scoring (Required)

**Purpose**: Objectively score the use case for prioritization

**Key Questions to Answer**:
- What's the WSJF score? (Cost of Delay ÷ Job Size)
- Does it pass DVF filter? (all dimensions ≥3)
- What's the multi-dimensional priority score?
- Which wave should it be in?

**Scoring Scales**:
- **WSJF Components**: Fibonacci (1, 2, 3, 5, 8, 13, 20)
- **DVF Components**: 1-5 scale (≥3 to pass)
- **Multi-dimensional**: 0-10 scale per dimension

**Tips**:
- Do this WITH the team, not alone
- Use Planning Poker for anonymous voting
- Document your rationale
- Review BNZ's existing WSJF scores for calibration

**WSJF Scoring Worksheet**:
```markdown
User/Business Value: 13 (High revenue impact: $3M+)
Time Criticality: 5 (Important but not urgent)
Risk Reduction/Opp Enable: 8 (Enables 3 other use cases)
Cost of Delay = 13 + 5 + 8 = 26

Job Size: 8 (6-8 months, moderate team)

WSJF = 26 ÷ 8 = 3.25
```

**Common Mistakes**:
- ❌ Using non-Fibonacci numbers (e.g., 7, 15)
- ❌ Scoring in isolation without team input
- ❌ Underscoring "Risk Reduction/Opportunity Enablement" for platform use cases
- ❌ Not documenting rationale

---

### 7. Risk Management (Required for Implementation)

**Purpose**: Identify and mitigate risks proactively

**Key Questions to Answer**:
- What could go wrong?
- How do we mitigate each risk?
- What's the model risk tier?
- What are the compliance requirements?

**Risk Categories**:
1. **Technical**: Model accuracy, integration complexity
2. **Regulatory**: Model risk, data privacy, compliance
3. **Operational**: User adoption, process change
4. **Reputational**: Customer impact, media exposure
5. **Financial**: Cost overruns, benefit realization

**Model Risk Tiers**:
- **Tier 1**: High impact (credit decisions, regulatory) → Full validation required
- **Tier 2**: Medium impact (operational automation) → Moderate validation
- **Tier 3**: Low impact (analytics, reporting) → Light validation
- **Tier 4**: Minimal impact (content generation) → Self-certification

**Common Mistakes**:
- ❌ Generic risks with no specific mitigations
- ❌ Underestimating regulatory risk
- ❌ Missing model risk tier classification
- ❌ No rollback plan

---

### 8. Success Metrics & KPIs (Required for Implementation)

**Purpose**: Define how success will be measured

**Key Questions to Answer**:
- What business KPIs will we track?
- What technical KPIs matter?
- How will we measure adoption?
- What are the alert thresholds?

**KPI Categories**:
1. **Business KPIs**: Revenue, cost, customer satisfaction, risk
2. **Technical KPIs**: Model performance, system performance, data quality
3. **Adoption KPIs**: User adoption rate, daily active users, feature usage
4. **Operational KPIs**: Support tickets, override rate, false positives

**Tips**:
- Set baseline AND target for each KPI
- Include threshold (minimum acceptable)
- Define measurement method and frequency
- Plan monitoring dashboard

**Common Mistakes**:
- ❌ Too many KPIs (focus on top 5-7)
- ❌ KPIs without baselines (can't measure improvement)
- ❌ No thresholds for alerting
- ❌ Vague KPIs ("improve efficiency" vs "reduce time by 40%")

---

### 9. Governance & Compliance (Required for Implementation)

**Purpose**: Define governance structure and compliance approach

**Key Questions to Answer**:
- Who makes which decisions?
- How will the model be governed?
- What compliance requirements apply?
- How will audits be handled?

**Decision Authority Matrix**:
| Decision | Authority |
|----------|-----------|
| Strategic direction | Executive Sponsor |
| Scope changes | Product Owner + Steering Committee |
| Technical architecture | Enterprise Architect |
| Model approval | Model Risk Committee |
| Go/No-Go Production | Steering Committee |

**Tips**:
- Engage Risk & Compliance early
- Plan for model documentation and validation
- Set up regular review cadence
- Prepare audit trail from day 1

---

### 10. Change Management (Required for Implementation)

**Purpose**: Plan for user adoption and organizational change

**Key Questions to Answer**:
- Who is impacted and how?
- What training is required?
- How will we roll out?
- How will we communicate?

**Change Impact Levels**:
- **High**: New workflows, new tools, job role changes
- **Medium**: Process modifications, new reporting
- **Low**: Minor changes, additional features

**Training Plan Elements**:
1. End user training (how to use)
2. Power user training (advanced features)
3. Support team training (troubleshooting)
4. Manager training (reporting, dashboards)

**Common Mistakes**:
- ❌ Underestimating change impact
- ❌ Insufficient training budget/time
- ❌ Big bang rollout without pilot
- ❌ Poor communication plan

---

### 11. Post-Implementation (Required for Implementation)

**Purpose**: Plan for go-live support and continuous improvement

**Key Questions to Answer**:
- What's the hypercare plan?
- How will we handle issues during early days?
- What enhancements are planned?
- How will we track benefits realization?

**Hypercare Period**: Typically 2-4 weeks post go-live
- Extended support hours (24/7 or extended hours)
- Daily war room check-ins
- Rapid issue escalation
- Daily status updates

**Tips**:
- Plan enhancements based on user feedback
- Track benefits monthly (vs waiting a year)
- Set up feedback loops
- Celebrate quick wins

---

## Tips for Different Roles

### For Product Owners
**Focus on**:
- Business Case (Section 2): This is your bread and butter
- Current State (Section 3): You know the pain points
- Change Management (Section 10): Critical for adoption
- Benefits Tracking (Section 11.3): Prove the ROI

**Delegate to**:
- Enterprise Architect: Target State, Patterns, ABBs
- Technical Lead: Implementation Plan, Risk Management
- Change Manager: Training plans, rollout strategy

---

### For Enterprise Architects
**Focus on**:
- Target State Solution (Section 4): Your expertise
- Architecture Patterns (Section 4.4): Reference existing patterns
- Implementation Plan (Section 5): Technical dependencies
- Risk Management (Section 7): Technical and regulatory risks

**Delegate to**:
- Product Owner: Business Case, Current State
- Technical Lead: Detailed technology stack
- Change Manager: Stakeholder engagement, training

---

### For Business Analysts
**Focus on**:
- Current State (Section 3): Process mapping, pain points
- Stakeholders (Section 3.2): Impact analysis
- Success Metrics (Section 8): KPI definition
- User Journeys (Section 4.5): UX design

**Delegate to**:
- Enterprise Architect: Solution architecture
- Product Owner: Business value quantification
- Technical Lead: Technology decisions

---

## Common Pitfalls to Avoid

### 1. Vague Benefits
❌ **Bad**: "Will improve efficiency and customer experience"  
✅ **Good**: "Will reduce processing time by 60% (5 days → 2 days), improving customer satisfaction by 25 NPS points and saving $800K annually"

### 2. Technology-First Thinking
❌ **Bad**: "We want to use GPT-4 for..."  
✅ **Good**: "We need to solve [business problem]. GenAI/LLMs are the appropriate technology because..."

### 3. Unrealistic Timelines
❌ **Bad**: "6 weeks from concept to production"  
✅ **Good**: "6 months: 4 weeks discovery, 10 weeks build, 4 weeks pilot, 6 weeks rollout"

### 4. Ignoring Change Management
❌ **Bad**: "Build it and they will come"  
✅ **Good**: "15% of budget allocated to change management: training, communication, champions program"

### 5. Missing Governance
❌ **Bad**: "We'll figure out governance later"  
✅ **Good**: "Model Risk Tier 1 requires independent validation, model documentation, ongoing monitoring per BNZ framework"

### 6. No Comparable Examples
❌ **Bad**: "We think this will work"  
✅ **Good**: "JPMorgan achieved 80-90% productivity increase with similar AI KYC implementation (source: [link])"

---

## Quality Checklist

Before submitting your use case document, verify:

### Document Control
- [ ] Use Case ID assigned (check with EA team for next available)
- [ ] Version number set (1.0.0 for first version)
- [ ] All owners and contacts listed
- [ ] Document status set correctly

### Business Case
- [ ] Benefits quantified (with $ values or % improvements)
- [ ] Costs estimated (development + ongoing)
- [ ] ROI and payback period calculated
- [ ] 2-3 comparable examples included with references
- [ ] Industry benchmarks cited

### Prioritization
- [ ] WSJF score calculated with rationale
- [ ] DVF scores provided (≥3 on all to pass)
- [ ] Multi-dimensional scores completed
- [ ] Wave assignment recommended

### Technical
- [ ] AI/ML approach clearly described
- [ ] Data inputs and outputs documented
- [ ] Architecture patterns referenced (PT-XXX)
- [ ] ABBs identified and counted
- [ ] Dependencies listed (prerequisites and enables)

### Risk & Governance
- [ ] Risk assessment completed
- [ ] Model risk tier assigned
- [ ] Compliance requirements identified
- [ ] Audit approach documented

### Success Metrics
- [ ] 5-7 key KPIs defined
- [ ] Baselines and targets set
- [ ] Monitoring approach planned
- [ ] Alert thresholds defined

### Change Management
- [ ] Stakeholder impact analysis done
- [ ] Training plan outlined
- [ ] Rollout approach defined
- [ ] Communication plan created

### Approvals
- [ ] All approvers identified
- [ ] Review process initiated

---

## Getting Help

### Questions About the Template
- **Enterprise Architecture**: Template structure, patterns, ABBs
- **AI Programme Office**: Prioritization process, WSJF scoring
- **Risk & Compliance**: Model risk, governance requirements

### Questions About Your Specific Use Case
- **Enterprise Architect (assigned)**: Listed in use case summary CSV
- **AI Platform Team**: Technical feasibility, platform capabilities
- **Product Community**: Best practices, lessons learned

### Resources
- **Prioritization Framework**: USE-CASE-PRIORITISATION-FRAMEWORK.md
- **Pattern Library**: patterns/ directory (PT-001 to PT-018)
- **Spreadsheet Guide**: SPREADSHEET-USER-GUIDE.md
- **Architecture Best Practices**: data/2025-BEST-PRACTICES-UPDATE.md

---

## Next Steps After Completing Template

### If Your Use Case is New (Not Yet Prioritized)
1. Complete Sections 1-6 of template
2. Add to prioritization spreadsheet (Sheet 1)
3. Participate in DVF workshop (get DVF scores)
4. Participate in WSJF workshop (get WSJF scores)
5. Wait for wave assignment
6. If approved for Wave 1 or 2, complete Sections 7-11

### If Your Use Case is Approved for Implementation
1. Ensure Sections 1-11 are complete
2. Create architecture diagram (use draw.io templates)
3. Create sequence diagram (use draw.io templates)
4. Obtain approvals (Section 13)
5. Submit to TAF (Technical Architecture Forum)
6. Commence delivery once approved

### If Your Use Case is Existing/In-Flight
1. Document current state using template
2. Update with lessons learned
3. Fill any gaps (KPIs, governance, etc.)
4. Add to AI Programme portfolio
5. Share with stakeholders

---

## Template Maintenance

**Template Owner**: BNZ Enterprise Architecture

**Version**: 1.0.0 (December 5, 2025)

**Feedback**: If you have suggestions for improving this template or guide, please contact the Enterprise Architecture team.

**Updates**: Template will be reviewed quarterly and updated based on:
- User feedback
- Lessons learned from use case implementations
- Changes to BNZ architecture standards
- Updates to prioritization framework

---

## Appendix: Example Use Cases

For reference examples of completed use cases, see:
- **UC-001**: FrontLine - Partnership Banking (High maturity, comprehensive)
- **UC-004**: Credit Risk (Complex, Tier 1 model risk)
- **UC-009**: Data Products (Platform/enabler use case)

These examples demonstrate best practices for:
- Quantifying benefits with evidence
- Referencing architecture patterns
- Documenting model risk and compliance
- Planning change management

---

**Ready to start?**

1. Make a copy of USE-CASE-TEMPLATE.md
2. Save as UC-0XX-[YourUseCaseName]-v1.0.0.md
3. Follow the pathway that matches your situation
4. Use the quality checklist before submitting
5. Reach out for help when needed

**Good luck with your use case!** 🚀

