# Practical Use Case Prioritization Guide
## From Spreadsheet to Top 5 Executive Presentation

## Document Control

| Property | Value |
|----------|-------|
| **Version** | 1.0 |
| **Date** | December 5, 2025 |
| **Status** | Implementation Guide |
| **Purpose** | Step-by-step instructions for prioritizing AI use cases |
| **Target Audience** | Programme managers, enterprise architects, product owners |

---

## Executive Summary

This guide provides **practical, step-by-step instructions** for taking a spreadsheet with basic use case information (ID, Name, Summary) and systematically prioritizing them to produce:
1. A defensible **Top 10 list** for programme planning
2. A refined **Top 5 list** for executive presentation
3. Supporting data and visualizations for decision-making

**Time Required**: 4-6 weeks (depends on stakeholder availability)
**Team Required**: 5-8 people (cross-functional)
**Deliverables**: Prioritized spreadsheet, visualizations, executive presentation

---

## Table of Contents

1. [Recommended Framework](#recommended-framework)
2. [Required Spreadsheet Columns](#required-spreadsheet-columns)
3. [Step-by-Step Process](#step-by-step-process)
4. [Creating the Top 10 List](#creating-the-top-10-list)
5. [Refining to Top 5](#refining-to-top-5)
6. [Executive Presentation Template](#executive-presentation-template)
7. [Templates and Tools](#templates-and-tools)

---

## Recommended Framework

### Why WSJF (Weighted Shortest Job First)

Based on consolidated research, **WSJF is the recommended framework** for BNZ because:

1. ✅ **SAFe-Aligned**: BNZ preference for SAFe-aligned frameworks
2. ✅ **Economic Rigor**: Mathematically proven to optimize value flow
3. ✅ **Strategic Flexibility**: RR/OE component justifies foundational work (governance platforms, feature stores)
4. ✅ **Enterprise Proven**: Used by thousands of large organizations globally
5. ✅ **Scales Well**: Works across portfolio, programme, and team levels

### DVF as Pre-Filter

**Before applying WSJF**, use DVF (Desirability, Viability, Feasibility) to filter:
- Reduces 24 use cases → ~15-18 viable candidates
- Eliminates clearly infeasible ideas early
- Saves time on detailed scoring

### The Complete Model

```
Step 1: DVF Filtering (Week 1-2)
   ↓
Step 2: WSJF Scoring (Week 3-4)
   ↓
Step 3: Dependency Adjustment (Week 5)
   ↓
Step 4: Portfolio Balancing (Week 6)
   ↓
Output: Top 10 → Top 5 → Executive Deck
```

---

## Required Spreadsheet Columns

### Starting Inputs (You Already Have)

| Column | Type | Description |
|--------|------|-------------|
| **ID** | Text | Use case identifier (e.g., [UC-001](../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md)) |
| **Name** | Text | Use case name (e.g., "Credit Risk Assessment") |
| **Summary** | Text | 1-2 sentence description |

### Columns to Add (Detailed Instructions Below)

#### Phase 1: DVF Filtering Columns

| Column | Type | Scale | Purpose |
|--------|------|-------|---------|
| **Desirability Score** | Number | 1-5 | Is it wanted by users/stakeholders? |
| **Viability Score** | Number | 1-5 | Is it financially viable? |
| **Feasibility Score** | Number | 1-5 | Can we build it with current capabilities? |
| **DVF Total** | Formula | 0-15 | Sum of above three |
| **DVF Status** | Text | Pass/Fail | Pass if all dimensions ≥3 |

#### Phase 2: WSJF Scoring Columns

| Column | Type | Scale | Purpose |
|--------|------|-------|---------|
| **User/Business Value** | Number | 1, 2, 3, 5, 8, 13, 20 | Revenue, cost savings, customer impact |
| **Time Criticality** | Number | 1, 2, 3, 5, 8, 13, 20 | Urgency (regulatory, competitive, contractual) |
| **Risk Reduction/Opportunity Enablement** | Number | 1, 2, 3, 5, 8, 13, 20 | Reduces risk OR enables future use cases |
| **Cost of Delay** | Formula | Sum | Sum of above three |
| **Job Size** | Number | 1, 2, 3, 5, 8, 13, 20 | Effort/duration estimate |
| **WSJF Score** | Formula | Decimal | Cost of Delay ÷ Job Size |
| **WSJF Rank** | Number | 1-n | Ranking by WSJF Score (1 = highest) |

#### Phase 3: Context & Dependency Columns

| Column | Type | Purpose |
|--------|------|---------|
| **Category** | Text | E.g., Risk Management, Customer Experience, Operations |
| **Strategic Theme** | Text | E.g., Cybersecurity, AI Foundation, Customer-First |
| **Prerequisites** | Text | List of dependent use cases (IDs) |
| **Enables** | Text | List of use cases this enables (IDs) |
| **Earliest Start** | Text | Q1 2026, Q2 2026, etc. (based on dependencies) |

#### Phase 4: Portfolio View Columns

| Column | Type | Purpose |
|--------|------|---------|
| **Value Tier** | Text | High/Medium/Low (based on Cost of Delay) |
| **Effort Tier** | Text | High/Medium/Low (based on Job Size) |
| **Quadrant** | Text | Quick Win, Strategic Bet, Fill-in, Avoid |
| **Recommended Wave** | Text | Wave 1, Wave 2, Wave 3 |
| **Top 10 Status** | Boolean | TRUE/FALSE |
| **Top 5 Status** | Boolean | TRUE/FALSE |
| **Executive Notes** | Text | Key points for exec presentation |

---

## Step-by-Step Process

### WEEK 1-2: DVF Filtering Workshop

#### Objective
Filter 24 use cases down to 15-18 viable candidates

#### Participants Required
- 1 Product Owner/Business Owner per major category (4-5 people)
- 1-2 Enterprise Architects
- 1 Finance/Business Case representative
- 1 Technical Lead/CTO representative
- 1 Risk & Compliance representative

#### Materials Needed
- Spreadsheet with ID, Name, Summary
- Projector for group scoring
- DVF scoring guidelines (see below)

#### Process (3-hour workshop)

**Hour 1: DVF Training & Calibration**

1. **Explain DVF Framework** (15 min):
   - **Desirability**: Do customers/users want this? Does it solve a real problem?
   - **Viability**: Is it financially viable? Does it align with business model and strategy?
   - **Feasibility**: Can we build it? Do we have technology, data, and skills?

2. **Introduce Scoring Scale** (10 min):
   ```
   5 = Excellent    (strong evidence of success)
   4 = Good         (clear pathway to success)
   3 = Acceptable   (meets minimum bar)
   2 = Poor         (significant concerns)
   1 = Very Poor    (major blockers exist)
   ```

3. **Calibrate with 2 Example Use Cases** (35 min):
   - Score together as group
   - Discuss differences
   - Establish shared understanding

**Hour 2: Score All Use Cases**

4. **Silent Individual Scoring** (30 min):
   - Each participant scores all 24 use cases independently
   - Capture in shared spreadsheet

5. **Discuss Outliers** (30 min):
   - For each use case, calculate average score per dimension
   - If individual scores differ by >2 points, discuss
   - Reach consensus score

**Hour 3: Filter & Document**

6. **Apply Filter Rule**:
   - **Pass**: All three dimensions score ≥3
   - **Fail**: Any dimension scores <3

7. **Review Failures**:
   - For failed use cases, document specific concerns
   - Identify if concerns are temporary (e.g., "not feasible now but will be in 6 months")
   - Decide: Eliminate permanently or defer for future review

8. **Confirm Viable List**:
   - Expected outcome: 15-18 use cases pass DVF filter
   - If too many pass (>20), raise threshold to 3.5
   - If too few pass (<12), review scoring criteria

#### Deliverable
**Updated Spreadsheet** with:
- DVF scores (D, V, F) for each use case
- DVF Total and Status
- List of "Viable Candidates" (passed DVF)
- List of "Deferred/Eliminated" with reasons

---

### WEEK 3-4: WSJF Scoring Workshop

#### Objective
Prioritize viable candidates using WSJF economic model

#### Participants Required
- Same cross-functional team from DVF workshop
- Add: 2-3 subject matter experts for specific domains (e.g., Risk SME for fincrime use cases)
- Target: 5-11 people total (SAFe best practice)

#### Materials Needed
- Filtered list of 15-18 viable use cases
- Modified Fibonacci reference card (1, 2, 3, 5, 8, 13, 20)
- Planning Poker cards (optional but recommended)
- Spreadsheet for live scoring

#### Process (Two 3-hour workshops)

**Workshop 1: Score Cost of Delay Components**

**Hour 1: WSJF Training & Calibration**

1. **Explain WSJF Formula** (15 min):
   ```
   WSJF = Cost of Delay ÷ Job Size

   Cost of Delay = User/Business Value
                 + Time Criticality
                 + Risk Reduction/Opportunity Enablement
   ```

2. **Define Each Component** (20 min):

   **User/Business Value** - Economic and customer impact:
   - Revenue increase (new revenue, retention, cross-sell)
   - Cost reduction (FTE savings, operational efficiency)
   - Customer experience improvement (NPS, CSAT, retention)

   **Scoring Guidelines**:
   ```
   20 = >$5M annual benefit OR >20% efficiency gain OR critical customer experience
   13 = $2-5M benefit OR 10-20% efficiency OR major experience improvement
   8  = $500K-2M benefit OR 5-10% efficiency OR significant experience improvement
   5  = $100K-500K benefit OR 2-5% efficiency OR moderate improvement
   3  = $50K-100K benefit OR 1-2% efficiency OR minor improvement
   2  = <$50K benefit OR <1% efficiency OR marginal improvement
   1  = Negligible quantified benefit
   ```

   **Time Criticality** - Urgency and time-sensitivity:
   - Regulatory deadline (hard date, penalties for missing)
   - Competitive window (first-mover advantage)
   - Contractual obligation (SLA, commitment)
   - Market timing (seasonal, event-driven)

   **Scoring Guidelines**:
   ```
   20 = Fixed regulatory deadline within 6 months OR major competitive threat
   13 = Fixed deadline within 12 months OR significant competitive pressure
   8  = Preferred timing within 12 months OR moderate competitive benefit
   5  = Beneficial timing within 18 months OR some competitive benefit
   3  = Loose timing preference within 24 months OR minor competitive factor
   2  = No specific timing driver
   1  = Can be done anytime
   ```

   **Risk Reduction / Opportunity Enablement** - Strategic value:
   - **RR**: Reduces operational risk, cybersecurity risk, technical debt, compliance risk
   - **OE**: Enables future use cases, builds platform capabilities, creates reusable assets

   **Scoring Guidelines**:
   ```
   20 = Eliminates critical risk (e.g., major security vulnerability) OR enables 5+ use cases
   13 = Significantly reduces high risk OR enables 3-4 use cases
   8  = Reduces moderate risk OR enables 2 use cases
   5  = Reduces minor risk OR enables 1 use case
   3  = Small risk reduction OR creates reusable component
   2  = Minimal risk impact OR small reusability
   1  = No risk reduction or enabling capability
   ```

3. **Calibrate with 2 Examples** (25 min):
   - Score together as group
   - Practice relative estimation (comparing two use cases)
   - Build shared understanding

**Hour 2-3: Score Viable Use Cases**

4. **Silent Individual Scoring** (45 min):
   - Each participant scores all viable use cases on three CoD dimensions
   - Use Modified Fibonacci only: 1, 2, 3, 5, 8, 13, 20

5. **Consensus Discussion** (75 min):
   - For each use case, reveal scores (Planning Poker style)
   - If spread >1 Fibonacci number (e.g., some 5s, some 13s), discuss
   - Highest and lowest scores explain reasoning
   - Group agrees on consensus score
   - Facilitator enters in spreadsheet live

**Workshop 2: Score Job Size & Calculate WSJF**

**Hour 1: Job Size Estimation**

1. **Explain Job Size** (10 min):
   - Definition: Effort or duration to deliver use case to production
   - Can be measured in: person-months, team-months, or simply relative size
   - Includes: analysis, design, development, testing, deployment, training

2. **Define Estimation Approach** (10 min):
   - **Relative, not absolute**: Compare use cases to each other
   - **T-shirt sizing first**: XS, S, M, L, XL, XXL
   - **Then map to Fibonacci**:
     ```
     XS = 1-2
     S  = 3
     M  = 5
     L  = 8
     XL = 13
     XXL = 20
     ```

3. **Anchor with Reference Use Cases** (10 min):
   - Select 1 "medium" use case as anchor (assign Fibonacci 5)
   - Compare all others relative to anchor
   - Example: "[UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) is our Fibonacci 5 (M). [UC-001](../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) is half that size (3). [UC-021](../../use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md) is twice that size (10 → round to 8 or 13)."

4. **Score Job Sizes** (30 min):
   - Silent individual estimation
   - Planning Poker reveal
   - Discuss outliers
   - Consensus

**Hour 2: Calculate WSJF & Initial Ranking**

5. **Calculate in Spreadsheet** (15 min):
   ```
   Cost of Delay = User/Business Value + Time Criticality + RR/OE
   WSJF Score = Cost of Delay ÷ Job Size
   ```

6. **Sort by WSJF Descending** (5 min):
   - Rank 1 = Highest WSJF
   - Rank 15-18 = Lowest WSJF

7. **Sanity Check** (25 min):
   - Do high WSJF scores make intuitive sense?
   - Are there any surprising results?
   - Common surprises:
     - Small, valuable use cases rank higher than expected (good!)
     - Large, strategically important use cases rank lower than expected (investigate Job Size)
     - Platform/enabler use cases rank surprisingly high (good - RR/OE is working!)

8. **Document Assumptions** (15 min):
   - For top 10 WSJF scores, document key assumptions:
     - Business value: What specific benefits drive the score?
     - Time criticality: What specific deadline/driver?
     - RR/OE: What specific risk or enablement?
     - Job size: What's included in scope?

**Hour 3: Dependency Review**

9. **Identify Prerequisites** (30 min):
   - For each use case, ask: "What must be done before this?"
   - Types of dependencies:
     - **Technical**: Needs platform, API, data source
     - **Process**: Needs process change, policy approval
     - **Resource**: Needs specific skill/team
     - **External**: Needs vendor, partner, regulatory approval

10. **Map Enablement** (20 min):
    - For each use case, ask: "What does this enable?"
    - Platform/infrastructure use cases often enable many others
    - Example: [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) Data Products enables [UC-003](../../use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md), [UC-004](../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md), [UC-006](../../use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md), [UC-013](../../use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md), etc.

11. **Flag Dependency Conflicts** (10 min):
    - High WSJF use case that requires low WSJF prerequisite = conflict
    - Example: [UC-013](../../use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md) Fraud Ops (high WSJF) requires [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) Data Products (moderate WSJF)
    - Solution: Boost [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) priority or defer [UC-013](../../use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md)

#### Deliverable
**Updated Spreadsheet** with:
- WSJF component scores (User/Business Value, Time Criticality, RR/OE, Job Size)
- Cost of Delay calculation
- WSJF Score calculation
- WSJF Rank (1 = highest priority)
- Dependencies documented
- Assumptions documented

---

### WEEK 5: Dependency-Adjusted Scheduling

#### Objective
Create realistic implementation sequence accounting for dependencies

#### Participants Required
- Enterprise Architects (2-3)
- Technical Leads (2-3)
- Programme Manager
- Product Owners (2-3)

#### Materials Needed
- WSJF-ranked spreadsheet
- Dependency map (Visio, Miro, or whiteboard)
- Wave planning template

#### Process (2-hour workshop)

**Hour 1: Visualize Dependencies**

1. **Create Dependency Graph** (30 min):
   - Use tool (Miro, Visio, draw.io) or whiteboard
   - Nodes = use cases
   - Arrows = dependencies ("A → B" means "B depends on A")
   - Color code by WSJF rank:
     - Green = Top 5 WSJF
     - Yellow = Rank 6-10
     - Blue = Rank 11-15
     - Gray = Rank 16+

2. **Identify Critical Path** (20 min):
   - Which use cases enable the most others?
   - Which use cases have longest dependency chains?
   - Example critical paths:
     ```
     UC-009 (Data Products) → UC-004 (Credit Risk) → UC-013 (Fraud Ops)
     UC-009 (Data Products) → UC-003 (Analytics) → UC-015 (Risk Functions)
     Governance Platform → All 24 use cases (2025 best practice)
     ```

3. **Flag "Bottleneck" Use Cases** (10 min):
   - Use cases that many others depend on = bottlenecks
   - Must be prioritized even if WSJF is moderate
   - Example: [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) Data Products enables 15 others → must be Wave 1

**Hour 2: Adjust Sequence & Assign Waves**

4. **Apply Sequencing Rules** (20 min):

   **Rule 1: No Orphans**
   - Don't schedule use case if prerequisite isn't scheduled
   - If [UC-013](../../use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md) (WSJF Rank 6) needs [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) (WSJF Rank 9), schedule [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) first

   **Rule 2: Boost Enablers**
   - If use case enables 3+ others, consider boosting to earlier wave
   - Override WSJF if enablement value is high

   **Rule 3: Respect Capacity**
   - Don't overload single team/resource
   - Spread use cases across teams for parallel execution

   **Rule 4: Balance Portfolio**
   - Mix quick wins (low Job Size) with strategic bets (high Job Size)
   - Ensure each wave has visible value delivery

5. **Assign to Waves** (30 min):

   **Wave 1 (Q1-Q3 2026, Months 1-9)**: Foundation + Quick Wins
   - **Criteria**:
     - Platform/enabler use cases (even if moderate WSJF)
     - Top WSJF use cases with no dependencies
     - Quick wins (high WSJF, low Job Size)
   - **Target**: 4-6 use cases + enterprise platforms
   - **Example**:
     ```
     - Governance Platform (prerequisite for all)
     - UC-009 Data Products (enables 15 others)
     - UC-004 Credit Risk (highest WSJF, depends on UC-009)
     - UC-001 Partnership Banking (high WSJF, low dependency)
     - UC-006 HyperPersonalization (high WSJF, some dependency)
     ```

   **Wave 2 (Q4 2026-Q3 2027, Months 10-21)**: Scale + Leverage
   - **Criteria**:
     - Medium-high WSJF use cases leveraging Wave 1 platforms
     - Use cases dependent on Wave 1 completions
     - Parallel streams across different teams
   - **Target**: 8-12 use cases
   - **Example**:
     ```
     - UC-013 Fraud Ops (depends on UC-009 Data Products)
     - UC-003 Analytics (depends on UC-009)
     - UC-014 Onboarding (independent stream)
     - UC-005 Lending Ops (document AI stream)
     - UC-008 Security AI (independent stream)
     - UC-024 App Personalisation (depends on UC-006)
     - UC-002 Finance (agent framework stream)
     - UC-010 SDLC (independent dev productivity stream)
     ```

   **Wave 3 (Q4 2027-Q2 2028, Months 22-30)**: Complete + Optimize
   - **Criteria**:
     - Lower WSJF use cases
     - Complex transformations requiring mature capabilities
     - "Nice to have" rather than "must have"
   - **Target**: Remaining 6-8 use cases
   - **Example**:
     ```
     - UC-015 Risk Functions (complex, cross-cutting)
     - UC-017 FrontLine CIB (reuse UC-001 patterns)
     - UC-021 Wholesale Underwriting (complex transformation)
     - UC-016 IT Ops (AIOps maturity needed)
     - UC-018, UC-019, UC-020, UC-022, UC-023 (lower strategic priority)
     ```

6. **Document Rationale** (10 min):
   - For each wave, write 2-3 sentences explaining:
     - Why these use cases grouped together
     - How dependencies are satisfied
     - What value wave delivers

#### Deliverable
**Updated Spreadsheet** with:
- "Recommended Wave" column populated
- "Earliest Start" column populated (based on dependencies)
- Dependency graph visual (attached to spreadsheet or separate document)
- Wave rationale documented

---

### WEEK 6: Portfolio Balancing & Top 10 Selection

#### Objective
Create balanced portfolio and select Top 10 for detailed planning

#### Participants Required
- AI Programme Lead
- Enterprise Architecture Lead
- Finance/Business Case Owner
- Key Product Owners (3-4)

#### Materials Needed
- WSJF-ranked, wave-assigned spreadsheet
- 2×2 matrix template (Value vs. Effort)
- Portfolio balance checklist

#### Process (2-hour workshop)

**Hour 1: Create Value-Effort Matrix**

1. **Calculate Value and Effort Tiers** (10 min):

   **Value Tier** (based on Cost of Delay):
   ```
   High   = CoD ≥ 30
   Medium = CoD 15-29
   Low    = CoD < 15
   ```

   **Effort Tier** (based on Job Size):
   ```
   Low    = Job Size ≤ 3
   Medium = Job Size 5-8
   High   = Job Size ≥ 13
   ```

2. **Plot on 2×2 Matrix** (15 min):
   - X-axis = Effort (Low → High)
   - Y-axis = Value (Low → High)
   - Place each use case on matrix
   - Label with use case ID

3. **Identify Quadrants** (5 min):
   ```
   High Value, Low Effort     │  High Value, High Effort
   "Quick Wins"               │  "Strategic Bets"
   (Do First - Wave 1)        │  (Plan Carefully - Wave 2-3)
   ───────────────────────────┼───────────────────────────
   Low Value, Low Effort      │  Low Value, High Effort
   "Fill-ins"                 │  "Avoid"
   (Do if Time - Wave 3)      │  (Deprioritize/Eliminate)
   ```

4. **Check Portfolio Balance** (10 min):
   - **Target Distribution**:
     - 40% Quick Wins
     - 40% Strategic Bets
     - 20% Fill-ins or Enablers
     - 0% Avoid (should be eliminated in DVF filter)

   - If unbalanced, flag for discussion

**Hour 2: Select Top 10**

5. **Apply Top 10 Selection Criteria** (20 min):

   **Primary Criterion**: WSJF Rank (top 10 by WSJF score)

   **Adjustments for**:
   - **Enablers**: Boost if enables 3+ other use cases
   - **Dependencies**: Include if required by high-WSJF use case
   - **Portfolio Balance**: Ensure mix of categories, themes, quick wins vs. strategic bets
   - **Resource Feasibility**: Avoid overloading single team

   **Example Decision**:
   ```
   WSJF Rank 1-8: Automatic inclusion in Top 10
   WSJF Rank 9: UC-009 Data Products - include because enables Ranks 2, 4, 6, 7
   WSJF Rank 10: UC-011 Fincrime - include (regulatory)
   WSJF Rank 11: UC-002 Finance - DEFER to Wave 2 (no urgent dependencies)
   WSJF Rank 12: UC-010 SDLC - DEFER to Wave 2 (independent stream)
   ```

6. **Validate Against Wave Assignments** (10 min):
   - Top 10 should mostly be Wave 1 (with maybe 1-2 Wave 2 items)
   - If Top 10 includes Wave 3 items, investigate:
     - Is WSJF score correct?
     - Are there hidden dependencies pushing it later?

7. **Check Category Diversity** (10 min):
   - **Target**: Top 10 should span multiple categories
     - 2-3 Risk Management use cases
     - 2-3 Customer Experience use cases
     - 2-3 Operations use cases
     - 1-2 Platform/Enabler use cases
     - 1-2 Compliance/Regulatory use cases

   - If concentrated in one category, consider:
     - Is this intentional strategic focus?
     - Or is scoring biased?

8. **Document Top 10** (10 min):
   - Mark "Top 10 Status" = TRUE in spreadsheet
   - For each, write 1-sentence "Executive Note" explaining why it's Top 10
   - Example: "[UC-004](../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) Credit Risk: Highest WSJF (8.5), direct P&L impact ($3-5M annual), supports strategic risk management pillar"

9. **Identify "Bubble" Use Cases** (10 min):
   - Ranks 11-13 are "bubble" - close but didn't make Top 10
   - Document these separately
   - If Top 10 use case fails (scope, budget, resource), bubble items are next in line

#### Deliverable
**Updated Spreadsheet** with:
- "Top 10 Status" column (TRUE for 10 use cases)
- "Executive Notes" for Top 10
- Value-Effort matrix visual (chart or separate slide)
- Portfolio balance summary (% in each quadrant)

---

## Creating the Top 10 List

### Top 10 Presentation Format

**For Programme Planning Audience** (Internal team, detailed)

#### Spreadsheet View
Sort by WSJF Rank, show columns:
| Rank | ID | Name | WSJF | CoD | Job Size | Wave | Category | Executive Note |

#### Narrative Summary (1-page)

**Template:**

```
TOP 10 AI USE CASES FOR BNZ AI PROGRAMME

Based on rigorous WSJF prioritization (SAFe economic model), the following 10 use cases
represent the highest value-to-effort ratio and strongest strategic alignment for immediate
investment. These use cases were selected from 24 candidates through:

1. DVF filtering (Desirability, Viability, Feasibility assessment)
2. WSJF scoring (Cost of Delay ÷ Job Size economic optimization)
3. Dependency validation (ensuring realistic sequencing)
4. Portfolio balancing (ensuring mix of quick wins and strategic investments)

TOP 10 USE CASES (Ranked by WSJF Score):

1. [Name] - WSJF [Score]
   - Value: [Key benefit]
   - Wave: [1/2/3]
   - Rationale: [1-2 sentences]

2. [Name] - WSJF [Score]
   ...

[Continue for all 10]

WAVE 1 FOCUS (Q1-Q3 2026):
[List which Top 10 use cases are in Wave 1, explain sequencing]

DEPENDENCIES:
[Note any critical dependencies among Top 10]

PORTFOLIO BALANCE:
- Quick Wins: [X] use cases
- Strategic Bets: [Y] use cases
- Platform Enablers: [Z] use cases

NEXT STEPS:
1. Executive approval of Top 10
2. Detailed business cases for Top 5 (see separate document)
3. Resource allocation planning
4. PI Planning for Wave 1 use cases
```

---

## Refining to Top 5

### Why Top 5?

**Executive Context**: Senior executives (C-suite, Board) typically:
- Have limited time (30-60 min presentation)
- Need simplified choices
- Want to see "best of the best"
- Focus on strategic impact, not operational details

**Top 5 Purpose**:
- Get executive approval for immediate investment
- Secure budget allocation
- Assign executive sponsors
- Communicate to broader organization

### Selection Criteria for Top 5

#### Step 1: Analyze Top 10 (30 min workshop)

**Participants**: Programme Lead, EA Lead, Finance Owner

**Questions to Ask**:

1. **Strategic Representation**:
   - Do the top 5 WSJF scores represent diverse strategic themes?
   - Or are they concentrated in one area (e.g., all Risk Management)?

2. **Wave 1 Alignment**:
   - Which Top 10 use cases are definitely Wave 1?
   - Can we commit to 5 in parallel, or is it too much?

3. **Storytelling**:
   - Which 5 tell the most compelling story to executives?
   - Which 5 demonstrate breadth of AI capability?

4. **Executive Sponsorship**:
   - Which 5 have clear executive sponsors already identified?
   - Which 5 align with known executive priorities?

#### Step 2: Apply Top 5 Rules

**Rule 1: Top 5 WSJF Scores** (Default)
- Simplest approach: Take WSJF Rank 1-5
- **Use if**: Top 5 are diverse, Wave 1-feasible, and tell good story

**Rule 2: Strategic Balance** (Override WSJF if needed)
- Ensure Top 5 span multiple strategic pillars:
  - 1-2 Revenue/Growth (e.g., [UC-001](../../use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) Partnership Banking, [UC-006](../../use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) HyperPersonalization)
  - 1-2 Risk/Compliance (e.g., [UC-004](../../use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) Credit Risk, [UC-011](../../use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) Fincrime)
  - 1 Operational Efficiency (e.g., [UC-005](../../use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md) Lending Ops, [UC-002](../../use-cases/UC-002/UC-002-Finance-v1.0.0.md) Finance)
  - 1 Platform/Enabler (e.g., [UC-009](../../use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) Data Products)

**Rule 3: Wave 1 Feasibility**
- All Top 5 should be deliverable in Wave 1 (Q1-Q3 2026)
- If WSJF Rank 3 has dependency on Rank 8, consider swapping

**Rule 4: Executive Alignment**
- Match to known CEO/Board priorities
- If CEO is focused on customer experience, ensure 2 CX use cases in Top 5

#### Step 3: Select and Validate

**Example Decision Process**:

```
WSJF Top 5 (Pure Ranking):
1. UC-004 Credit Risk (WSJF 8.7)
2. UC-001 Partnership Banking (WSJF 8.5)
3. UC-009 Data Products (WSJF 8.4)
4. UC-006 HyperPersonalization (WSJF 8.3)
5. UC-011 Fincrime (WSJF 8.2)

Strategic Check:
✓ Diverse: Risk (2), Customer (2), Platform (1)
✓ Wave 1 feasible: All are Wave 1
✓ Storytelling: Shows breadth of AI capability
✓ Executive sponsors: CEO (UC-001, UC-006), CRO (UC-004, UC-011), CDO (UC-009)

DECISION: Proceed with pure WSJF Top 5. No override needed.
```

**Alternative Scenario - Override Needed**:

```
WSJF Top 5 (Pure Ranking):
1. UC-004 Credit Risk
2. UC-011 Fincrime
3. UC-013 Fraud Ops
4. UC-015 Risk Functions
5. UC-008 Security AI

Strategic Check:
✗ Not diverse: All are Risk Management
✗ Doesn't demonstrate AI breadth
✗ CEO priority is customer experience - not represented

DECISION: Override WSJF. Replace Ranks 4-5 with:
- UC-001 Partnership Banking (WSJF Rank 6, customer experience)
- UC-006 HyperPersonalization (WSJF Rank 7, customer experience)

Adjusted Top 5:
1. UC-004 Credit Risk (Risk)
2. UC-011 Fincrime (Compliance)
3. UC-013 Fraud Ops (Operations)
4. UC-001 Partnership Banking (Customer Experience) ← Override
5. UC-006 HyperPersonalization (Customer Experience) ← Override

New Balance: Risk (2), Ops (1), Customer (2) ✓
```

#### Step 4: Document Rationale

For each Top 5 use case, prepare:

**1-Page Executive Brief** (per use case):
- **Use Case Name & ID**
- **WSJF Score & Rank**
- **Strategic Pillar**: Which strategic objective does this support?
- **Business Value** (2-3 bullets):
  - Quantified benefit (revenue, cost savings, risk reduction)
  - Customer impact
  - Competitive advantage
- **Implementation Summary**:
  - Wave assignment
  - Duration estimate
  - Key dependencies
  - Resource requirements
- **Risk & Mitigations**:
  - 2-3 key risks
  - Mitigation strategies
- **Success Metrics**:
  - How will we measure success?
  - 3-5 KPIs
- **Executive Sponsor**: Proposed C-level owner

---

## Executive Presentation Template

### Slide Deck Structure (15 slides, 30-min presentation)

#### Slide 1: Title
```
BNZ AI Programme: Top 5 Priority Use Cases
[Date]
Presented by: [Programme Lead, Enterprise Architect]
```

#### Slide 2: Executive Summary
```
RECOMMENDATION: Approve Top 5 AI use cases for immediate investment (Wave 1: Q1-Q3 2026)

- Total Investment: $X-XM over 9 months
- Expected Value: $X-XM annual benefit (ROI: X%)
- Strategic Alignment: [Map to Board priorities]
- Risk-Adjusted Approach: Platform investments + quick wins + strategic bets

DECISION NEEDED:
1. Approve Top 5 use cases for Wave 1 implementation
2. Assign executive sponsors
3. Allocate budget and resources
```

#### Slide 3: How We Got Here (Process Credibility)
```
RIGOROUS, DATA-DRIVEN PRIORITIZATION

Starting Point: 24 AI use cases identified across BNZ

Phase 1: DVF Filtering (Desirability, Viability, Feasibility)
→ Eliminated 6-9 infeasible use cases
→ 15-18 viable candidates

Phase 2: WSJF Scoring (SAFe Economic Model)
→ Scored on: Business Value, Time Criticality, Risk/Opportunity, Effort
→ Mathematically optimized for economic value flow
→ Top 10 use cases identified

Phase 3: Strategic Validation
→ Portfolio balanced across themes
→ Dependencies mapped and sequenced
→ Resource feasibility validated

Result: Top 5 use cases represent highest value, lowest risk, strategic fit
```

#### Slide 4: Prioritization Framework (Optional - for detail-oriented execs)
```
WSJF (WEIGHTED SHORTEST JOB FIRST) - SAFE INDUSTRY STANDARD

Formula: WSJF = Cost of Delay ÷ Job Size

Cost of Delay:
- User/Business Value: Revenue, cost savings, customer impact
- Time Criticality: Regulatory, competitive, contractual urgency
- Risk Reduction/Opportunity Enablement: Mitigates risk OR enables future capabilities

Job Size: Effort/duration to deliver

Why WSJF: Mathematically proven to maximize value flow, used by thousands of enterprises globally
```

#### Slide 5: The Top 5
```
TOP 5 AI USE CASES (RANKED BY WSJF)

1. [Name] - WSJF [Score]
   $[Value] benefit | [X] months | [Strategic Pillar]

2. [Name] - WSJF [Score]
   $[Value] benefit | [X] months | [Strategic Pillar]

3. [Name] - WSJF [Score]
   ...

4. [Name] - WSJF [Score]
   ...

5. [Name] - WSJF [Score]
   ...

TOTAL INVESTMENT: $X-XM
EXPECTED ANNUAL BENEFIT: $X-XM
ROI: [X]% over [Y] years
```

#### Slides 6-10: Deep Dive (1 slide per use case)
```
USE CASE [X]: [NAME]

WSJF SCORE: [X.X] | STRATEGIC PILLAR: [Risk/Customer/Ops/Platform]

THE OPPORTUNITY:
[2-3 sentences describing the business problem and AI solution]

QUANTIFIED BENEFITS:
• Revenue Impact: $[X-Y]M annually [or] [X]% increase
• Cost Savings: $[X]K in FTE/operational efficiency
• Customer Impact: [X]% improvement in [NPS/CSAT/retention]
• Risk Reduction: [Specific risk mitigated]

IMPLEMENTATION:
• Timeline: [X] months (Q[X] 2026 - Q[X] 2026)
• Investment: $[X]K
• Resources: [X] FTE, [dependencies listed]
• Key Milestones: [3-4 bullets]

SUCCESS METRICS:
• [Metric 1]: [Target]
• [Metric 2]: [Target]
• [Metric 3]: [Target]

RISKS & MITIGATIONS:
• [Risk 1]: [Mitigation]
• [Risk 2]: [Mitigation]
```

#### Slide 11: Portfolio Balance (Visual)
```
BALANCED PORTFOLIO ACROSS STRATEGIC PILLARS

[Pie chart or bar chart showing distribution]:
- Risk Management: [X] use cases
- Customer Experience: [X] use cases
- Operational Efficiency: [X] use case
- Platform/Enablers: [X] use case

[Value-Effort 2×2 Matrix]:
Shows Top 5 positioned in "Quick Wins" and "Strategic Bets" quadrants

MESSAGE: Diversified risk, immediate wins + long-term transformation
```

#### Slide 12: Wave 1 Roadmap
```
WAVE 1 DELIVERY TIMELINE (Q1-Q3 2026)

Q1 2026:
- Governance Platform setup (prerequisite for all)
- UC-[X]: [Name] - kickoff
- UC-[X]: [Name] - kickoff

Q2 2026:
- UC-[X]: [Name] - delivery
- UC-[X]: [Name] - delivery
- UC-[X]: [Name] - midpoint

Q3 2026:
- UC-[X]: [Name] - delivery
- UC-[X]: [Name] - delivery
- Wave 1 completion

PARALLEL DELIVERY: 2-3 use cases in flight simultaneously
EARLY VALUE: First use case live by Q2 2026
```

#### Slide 13: Investment & ROI
```
FINANCIAL SUMMARY

WAVE 1 INVESTMENT (9 months):
- Platform Infrastructure: $[X]M (governance, feature stores, model routing)
- Top 5 Use Cases: $[X]M (build, deploy, train)
- Total: $[X-Y]M

EXPECTED BENEFITS (Annual, Steady State):
- Revenue Increase: $[X]M
- Cost Savings: $[X]M
- Risk Reduction: $[X]M (avoided losses)
- Total: $[X-Y]M annually

ROI: [X]% | PAYBACK: [X] months | NPV: $[X]M (3-year)

INVESTMENT PROFILE: Typical for enterprise AI transformation
COMPARISON: [Benchmark vs. industry average if available]
```

#### Slide 14: Governance & Risk Management
```
HOW WE'LL ENSURE SUCCESS

GOVERNANCE:
- Executive Sponsors: C-level owner per use case
- AI Programme Board: Monthly review, decision authority
- Quarterly Recalibration: WSJF re-scoring, reprioritization

RISK MANAGEMENT:
- Pilot Approach: Start small (1-2 business units), scale based on success
- Dependency Tracking: Formal dependency management process
- Technical Risk: Proven 2025 best practices (not bleeding-edge)
- Change Management: 10% budget allocated per use case

COMPLIANCE:
- Model Risk Management: All ML models through MRM governance
- Privacy: GDPR/privacy by design
- Audit Trails: Comprehensive logging and explainability

SUCCESS METRICS: Tracked and reported monthly to Board
```

#### Slide 15: Decision & Next Steps
```
RECOMMENDATION & NEXT STEPS

SEEKING APPROVAL FOR:
1. Top 5 use cases for Wave 1 implementation (Q1-Q3 2026)
2. $[X-Y]M budget allocation
3. Resource commitment: [X] FTE (mix of internal + external)
4. Executive sponsor assignments:
   - UC-[X]: [Executive Name, Title]
   - UC-[X]: [Executive Name, Title]
   ...

IMMEDIATE NEXT STEPS (WEEK 1-4):
- Week 1: Finalize business cases for Top 5
- Week 2: Resource planning and allocation
- Week 3: Kick off platform infrastructure
- Week 4: Begin PI Planning for first PI

DECISION TIMELINE:
- Today: Present and discuss
- [Date + 1 week]: Board approval
- [Date + 2 weeks]: Implementation kickoff

CONTACTS:
[Programme Lead]: [email]
[Enterprise Architecture]: [email]
```

---

## Templates and Tools

### Spreadsheet Template Structure

**File: BNZ-Use-Case-Prioritization-Template.xlsx**

**Sheet 1: Use Case Inventory**
```
Columns:
A: ID (UC-001)
B: Name
C: Summary
D: Category
E: Strategic Theme
F: Owner/Architect

[Existing data]
```

**Sheet 2: DVF Scoring**
```
Columns:
A: ID (pull from Sheet 1)
B: Name (pull from Sheet 1)
C: Desirability Score (1-5)
D: Viability Score (1-5)
E: Feasibility Score (1-5)
F: DVF Total (=C+D+E)
G: DVF Status (=IF(AND(C>=3,D>=3,E>=3),"Pass","Fail"))
H: Notes

Conditional formatting:
- DVF Status "Pass" = green
- DVF Status "Fail" = red
```

**Sheet 3: WSJF Scoring**
```
Columns:
A: ID (pull from viable use cases only)
B: Name
C: User/Business Value (1,2,3,5,8,13,20)
D: Time Criticality (1,2,3,5,8,13,20)
E: Risk Reduction/Opportunity Enablement (1,2,3,5,8,13,20)
F: Cost of Delay (=C+D+E)
G: Job Size (1,2,3,5,8,13,20)
H: WSJF Score (=F/G, formatted to 2 decimal places)
I: WSJF Rank (=RANK(H,H$range,0))

Conditional formatting:
- Top 5 ranks = dark green
- Ranks 6-10 = light green
- Ranks 11-15 = yellow
- Ranks 16+ = gray
```

**Sheet 4: Dependencies & Scheduling**
```
Columns:
A: ID
B: Name
C: WSJF Rank (pull from Sheet 3)
D: Prerequisites (text list of IDs)
E: Enables (text list of IDs)
F: Earliest Start (Q1 2026, Q2 2026, etc.)
G: Recommended Wave (Wave 1/2/3)
H: Rationale (text)
```

**Sheet 5: Portfolio View**
```
Columns:
A: ID
B: Name
C: WSJF Rank
D: Cost of Delay
E: Job Size
F: Value Tier (=IF(D>=30,"High",IF(D>=15,"Medium","Low")))
G: Effort Tier (=IF(E>=13,"High",IF(E>=5,"Medium","Low")))
H: Quadrant (formula based on F & G)
I: Wave
J: Top 10 (TRUE/FALSE checkbox)
K: Top 5 (TRUE/FALSE checkbox)
L: Executive Notes
```

**Sheet 6: Dashboard (Charts)**
```
Charts:
1. Value-Effort 2×2 Matrix (scatter plot)
2. WSJF Ranking (horizontal bar chart, top 15)
3. Portfolio by Category (pie chart)
4. Portfolio by Wave (stacked bar)
5. Cost of Delay components (stacked bar showing U/BV, TC, RR/OE contribution)
```

### Download Links (Conceptual - Would Need to Create)

**Templates to Create**:
1. BNZ-Use-Case-Prioritization-Template.xlsx
2. DVF-Scoring-Workshop-Facilitation-Guide.docx
3. WSJF-Scoring-Workshop-Facilitation-Guide.docx
4. Top-5-Executive-Brief-Template.pptx
5. Use-Case-1-Page-Brief-Template.docx

---

## Summary: Key Takeaways

### The Process in Brief

```
Week 1-2: DVF Workshop
→ 24 use cases → 15-18 viable candidates

Week 3-4: WSJF Workshop
→ Score Cost of Delay and Job Size
→ Calculate WSJF = CoD ÷ Job Size
→ Rank 1-18 by WSJF

Week 5: Dependency Mapping
→ Identify prerequisites and enablements
→ Adjust sequence for dependencies
→ Assign to Waves (1, 2, 3)

Week 6: Portfolio Balancing
→ Create Value-Effort matrix
→ Select Top 10 (primarily WSJF Rank 1-10, adjusted for enablers)
→ Validate diversity and balance

Top 5 Selection:
→ Apply strategic balance rules
→ Ensure executive alignment
→ Select top 5 WSJF or override for storytelling

Executive Presentation:
→ 15 slides, 30-minute deck
→ Process, Top 5 details, portfolio balance, roadmap, investment, governance
→ Decision: Approve Top 5, assign sponsors, allocate budget
```

### Critical Success Factors

1. **Cross-Functional Participation**: Must have Business, Architecture, Finance, Risk in workshops
2. **Facilitator Discipline**: Keep workshops on time, force consensus, avoid analysis paralysis
3. **Data Transparency**: Share all scoring, show calculations, document assumptions
4. **Executive Engagement**: Get exec input early, validate strategic alignment, secure sponsorship
5. **Realistic Sequencing**: Respect dependencies, don't promise impossible timelines
6. **Continuous Communication**: Share progress weekly, manage stakeholder expectations

### Common Pitfalls to Avoid

1. **Skipping DVF Filter**: Wasting time scoring infeasible use cases
2. **Ignoring Dependencies**: High WSJF use case scheduled before prerequisite
3. **HiPPO Effect**: Highest Paid Person's Opinion overrides data
4. **Consensus Paralysis**: Unable to agree on scores, workshop stalls
5. **Gamesmanship**: Teams inflate scores to get their use case prioritized
6. **Static Prioritization**: Score once, never revisit despite changing conditions
7. **Presentation Overload**: 50-slide deck that loses executive attention

### Mitigations

1. **Facilitator Training**: Hire or train neutral facilitator for workshops
2. **Anonymous Scoring**: Use Planning Poker cards for simultaneous reveal
3. **Score Calibration**: Start with 2 example use cases to align mental models
4. **Documentation**: Record all assumptions, rationale, and decisions
5. **Stakeholder Pre-work**: Share materials 1 week before workshop
6. **Time Boxing**: Strict agenda, parking lot for tangents
7. **Executive Pre-brief**: 1-on-1 meetings before full Board presentation

---

## Final Checklist

### Before Week 1 Workshop
- [ ] Confirm 5-8 participants available
- [ ] Book 3-hour workshop room
- [ ] Prepare spreadsheet with ID, Name, Summary
- [ ] Send DVF scoring guidelines to participants 1 week ahead
- [ ] Identify 2 example use cases for calibration
- [ ] Assign facilitator

### After Week 2 (DVF Complete)
- [ ] Spreadsheet updated with DVF scores
- [ ] Viable candidates list (Pass status)
- [ ] Eliminated use cases documented with reasons
- [ ] Ready for WSJF workshops

### After Week 4 (WSJF Complete)
- [ ] All WSJF component scores entered
- [ ] WSJF calculated and ranked
- [ ] Assumptions documented for top 10
- [ ] Dependencies identified
- [ ] Ready for dependency mapping

### After Week 5 (Dependencies Complete)
- [ ] Dependency graph created
- [ ] Wave assignments made (Wave 1/2/3)
- [ ] Sequencing rationale documented
- [ ] Earliest start dates populated

### After Week 6 (Portfolio Complete)
- [ ] Value-Effort matrix created
- [ ] Top 10 selected and marked
- [ ] Executive notes written for Top 10
- [ ] Portfolio balance validated
- [ ] Ready for Top 5 selection

### Top 5 Finalization
- [ ] Top 5 selected with rationale
- [ ] 1-page briefs created for each Top 5
- [ ] Executive presentation deck drafted (15 slides)
- [ ] Financial summary validated with Finance
- [ ] Executive sponsors identified
- [ ] Presentation rehearsed

### Executive Presentation Day
- [ ] Deck finalized and distributed 24 hours ahead
- [ ] Backup materials prepared (detailed spreadsheet, dependency map)
- [ ] Room setup and technology tested
- [ ] Key stakeholders confirmed attendance
- [ ] Follow-up meeting scheduled for decision capture

---

**Good Luck!**

This guide provides everything needed to go from a simple spreadsheet to a Board-ready Top 5 presentation. The key is disciplined execution of the process, transparent data, and stakeholder engagement throughout.

For questions or clarifications, refer back to:
- [PRIORITIZATION-RESEARCH-CONSOLIDATED.md](PRIORITIZATION-RESEARCH-CONSOLIDATED.md) for framework details
- [USE-CASE-PRIORITISATION-FRAMEWORK.md](USE-CASE-PRIORITISATION-FRAMEWORK.md) for full BNZ-specific framework
