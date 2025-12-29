# BNZ Use Case Prioritization Spreadsheet - User Guide

## File Location
`BNZ-Use-Case-Prioritization.xlsx`

## Overview

This Excel spreadsheet implements the complete WSJF prioritization framework with 7 integrated sheets:

1. **Use Case Inventory** - Master list of all 24 AI use cases
2. **DVF Filtering** - Desirability, Viability, Feasibility assessment
3. **WSJF Scoring** - Weighted Shortest Job First economic prioritization
4. **Dependencies & Schedule** - Dependency mapping and wave assignments
5. **Portfolio View** - Visual portfolio management with quadrants
6. **Scoring Guidelines** - Reference guide for scoring (read-only)
7. **Dashboard** - Summary statistics and Top 10 view

---

## How to Use This Spreadsheet

### STEP 1: Review Use Case Inventory (Sheet 1)

**Purpose**: Verify all 24 use cases are correct

**What's Pre-Populated**:
- All 24 BNZ AI use cases ([UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) to [UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md))
- Names, summaries, categories, strategic themes
- Owners/architects from your existing data

**Actions**:
- ✅ Review for accuracy
- ✅ Update summaries if needed
- ✅ Confirm owner/architect assignments

**Note**: This sheet is the data source for all other sheets. Changes here propagate automatically.

---

### STEP 2: Conduct DVF Filtering Workshop (Sheet 2)

**Purpose**: Filter 24 use cases down to 15-18 viable candidates

**What's Automated**:
- ✅ IDs and Names pulled from Sheet 1
- ✅ DVF Total calculation (sum of D, V, F scores)
- ✅ DVF Status (Pass/Fail based on all dimensions ≥3)
- ✅ Color coding (green = Pass, red = Fail)

**Manual Input Required**:

| Column | What to Enter | Scale |
|--------|---------------|-------|
| **C: Desirability** | Is it wanted by users/customers? | 1-5 |
| **D: Viability** | Is it financially viable and strategic? | 1-5 |
| **E: Feasibility** | Can we build it with current capabilities? | 1-5 |
| **H: Notes** | Document concerns or rationale | Text |

**Scoring Reference**:
- 5 = Excellent
- 4 = Good
- 3 = Acceptable (minimum passing grade)
- 2 = Poor
- 1 = Very Poor

**Workshop Process** (3 hours):
1. Each participant scores independently
2. Reveal scores and discuss outliers
3. Reach consensus on final score
4. Document rationale in Notes column

**Expected Outcome**:
- 15-18 use cases with "Pass" status
- 6-9 use cases with "Fail" status (to eliminate or defer)

**Key Decision**: Only "Pass" use cases proceed to WSJF scoring.

---

### STEP 3: Conduct WSJF Scoring Workshop (Sheet 3)

**Purpose**: Prioritize viable use cases using economic model

**What's Automated**:
- ✅ IDs and Names pulled from Sheet 1
- ✅ Cost of Delay calculation (sum of columns C, D, E)
- ✅ WSJF Score calculation (Cost of Delay ÷ Job Size)
- ✅ WSJF Rank (1 = highest priority)
- ✅ Color coding (dark green = Top 5, light green = Top 10, yellow = Top 15)

**Manual Input Required**:

| Column | What to Enter | Scale | Definition |
|--------|---------------|-------|------------|
| **C: User/Business Value** | Revenue, cost savings, customer impact | Fibonacci: 1,2,3,5,8,13,20 | Economic and customer value |
| **D: Time Criticality** | Regulatory deadlines, competitive urgency | Fibonacci: 1,2,3,5,8,13,20 | How time-sensitive |
| **E: Risk Reduction/Opp Enable** | Reduces risk OR enables future use cases | Fibonacci: 1,2,3,5,8,13,20 | Strategic value |
| **G: Job Size** | Effort/duration to deliver | Fibonacci: 1,2,3,5,8,13,20 | How much work required |

**Fibonacci Scale**: Use ONLY these numbers: 1, 2, 3, 5, 8, 13, 20
- Forces relative estimation (comparing use cases to each other)
- Prevents false precision
- Standard in SAFe

**Scoring Reference**: See Sheet 6 (Scoring Guidelines) for detailed criteria

**Workshop Process** (Two 3-hour sessions):

**Session 1: Score Cost of Delay Components**
1. Review scoring guidelines together
2. Calibrate with 2 example use cases
3. Silent individual scoring (Planning Poker style)
4. Discuss outliers and reach consensus
5. Enter final scores

**Session 2: Score Job Size & Calculate WSJF**
1. Estimate job sizes (person-months or relative size)
2. Review WSJF rankings
3. Sanity check: Do rankings make intuitive sense?
4. Document assumptions

**Expected Outcome**:
- All viable use cases ranked 1-18 by WSJF score
- Top 5 in dark green, Top 10 in light green
- Assumptions documented

**Key Insight**: High WSJF = High value, Low effort = Do first!

---

### STEP 4: Map Dependencies (Sheet 4)

**Purpose**: Create realistic implementation sequence

**What's Automated**:
- ✅ IDs and Names pulled from Sheet 1
- ✅ WSJF Rank pulled from Sheet 3

**Manual Input Required**:

| Column | What to Enter | Format | Purpose |
|--------|---------------|--------|---------|
| **D: Prerequisites** | Use cases that must be done first | UC-XXX, UC-YYY | Technical dependencies |
| **E: Enables** | Use cases this one enables | UC-XXX, UC-YYY | Enablement relationships |
| **F: Earliest Start** | Realistic start date given dependencies | Q1 2026, Q2 2026, etc. | Sequencing |
| **G: Recommended Wave** | Which implementation wave | Wave 1, Wave 2, Wave 3 | Grouping |
| **H: Rationale** | Why this wave assignment | Text | Decision documentation |

**Wave Definitions**:
- **Wave 1** (Q1-Q3 2026): Foundation + Quick Wins (4-6 use cases)
- **Wave 2** (Q4 2026-Q3 2027): Scale + Leverage platforms (8-12 use cases)
- **Wave 3** (Q4 2027-Q2 2028): Complete + Optimize (remaining use cases)

**Workshop Process** (2 hours):
1. Create dependency graph (visual on whiteboard/Miro)
2. Identify critical path and bottleneck use cases
3. Assign waves respecting dependencies
4. Validate against WSJF rankings

**Key Decisions**:
- **Boost enablers**: If use case enables 3+ others, consider Wave 1 even if moderate WSJF
- **No orphans**: Don't schedule use case if prerequisite isn't scheduled
- **Respect capacity**: Don't overload single team

**Expected Outcome**:
- All use cases assigned to waves
- Dependencies documented
- Realistic sequencing that respects both WSJF and dependencies

---

### STEP 5: Create Portfolio View (Sheet 5)

**Purpose**: Balance portfolio and select Top 10

**What's Automated**:
- ✅ IDs, Names, WSJF Rank pulled from previous sheets
- ✅ Cost of Delay and Job Size pulled from Sheet 3
- ✅ Wave assignment pulled from Sheet 4
- ✅ **Value Tier** calculated automatically:
  - High = Cost of Delay ≥30
  - Medium = Cost of Delay 15-29
  - Low = Cost of Delay <15
- ✅ **Effort Tier** calculated automatically:
  - High = Job Size ≥13
  - Medium = Job Size 5-8
  - Low = Job Size ≤3
- ✅ **Quadrant** calculated automatically:
  - Quick Win = High Value, Low/Medium Effort
  - Strategic Bet = High Value, High Effort
  - Fill-in = Medium/Low Value, Low Effort
  - Avoid = Low Value, High Effort
- ✅ Color coding:
  - Green = Quick Win
  - Orange = Strategic Bet
  - Light Green = Fill-in
  - Red = Avoid

**Manual Input Required**:

| Column | What to Enter | Purpose |
|--------|---------------|---------|
| **J: Top 10** | Check TRUE for Top 10 use cases | Mark for detailed planning |
| **K: Top 5** | Check TRUE for Top 5 use cases | Mark for executive presentation |
| **L: Executive Notes** | 1-sentence summary for execs | Presentation talking points |

**Selection Process** (1 hour):

**Top 10 Selection**:
1. Start with WSJF Rank 1-10 as default
2. Adjust for:
   - Enablers (boost if enables 3+ use cases)
   - Dependencies (include prerequisites)
   - Portfolio balance (ensure category diversity)
3. Mark TRUE in column J

**Top 5 Selection**:
1. Review Top 10 for strategic balance
2. Ensure span across multiple pillars:
   - 1-2 Risk Management
   - 1-2 Customer Experience
   - 1 Operational Efficiency
   - 1 Platform/Enabler
3. Confirm all are Wave 1 feasible
4. Validate executive alignment
5. Mark TRUE in column K

**Portfolio Balance Check**:
Target distribution:
- 40% Quick Wins (immediate value)
- 40% Strategic Bets (transformation)
- 20% Fill-ins or Enablers
- 0% Avoid (should be eliminated in DVF)

**Expected Outcome**:
- 10 use cases marked as Top 10
- 5 use cases marked as Top 5
- Executive notes written for all Top 5
- Balanced portfolio confirmed

---

### STEP 6: Reference Scoring Guidelines (Sheet 6)

**Purpose**: Quick reference during scoring workshops

**Content**:
- WSJF scoring criteria for each component (User/Business Value, Time Criticality, RR/OE, Job Size)
- DVF scoring criteria for each dimension (Desirability, Viability, Feasibility)
- Examples and key questions

**Usage**: Keep this sheet open during workshops for quick reference

**Note**: This is a read-only reference sheet. No input required.

---

### STEP 7: Review Dashboard (Sheet 7)

**Purpose**: Executive summary and validation

**What's Automated**:
- ✅ Total use case count
- ✅ DVF Pass/Fail counts
- ✅ Top 10 and Top 5 counts
- ✅ Wave distribution counts
- ✅ Quadrant distribution counts

**Usage**:
- Quick validation of portfolio balance
- Summary statistics for presentations
- Sanity checks (e.g., "Do we have 5 in Top 5?")

**Manual Enhancement**:
- Add charts/graphs if desired
- Create pivot tables for deeper analysis
- Export summary for executive presentations

---

## Key Formulas Explained

### DVF Status (Sheet 2, Column G)
```excel
=IF(AND(C2>=3,D2>=3,E2>=3),"Pass","Fail")
```
- Checks if ALL three DVF dimensions score ≥3
- If yes: "Pass"
- If no: "Fail"

### Cost of Delay (Sheet 3, Column F)
```excel
=C2+D2+E2
```
- Sums User/Business Value, Time Criticality, and RR/OE
- Higher CoD = more value lost by delaying

### WSJF Score (Sheet 3, Column H)
```excel
=IF(G2>0,F2/G2,0)
```
- Divides Cost of Delay by Job Size
- Prevents division by zero
- Higher WSJF = higher priority

### WSJF Rank (Sheet 3, Column I)
```excel
=IF(H2>0,RANK(H2,H$2:H$25,0),"")
```
- Ranks use cases by WSJF score
- 1 = highest WSJF (highest priority)
- Blank if WSJF is zero

### Value Tier (Sheet 5, Column F)
```excel
=IF(D2>=30,"High",IF(D2>=15,"Medium","Low"))
```
- Categorizes Cost of Delay into tiers
- High: CoD ≥30, Medium: 15-29, Low: <15

### Quadrant (Sheet 5, Column H)
```excel
=IF(F2="High",IF(G2="Low","Quick Win","Strategic Bet"),IF(F2="Medium","Fill-in","Avoid"))
```
- Combines Value Tier and Effort Tier
- Maps to 2×2 portfolio matrix

---

## Conditional Formatting Rules

### Sheet 2: DVF Status
- **Green background**: DVF Status = "Pass"
- **Red background**: DVF Status = "Fail"

### Sheet 3: WSJF Rank
- **Dark Green**: Rank 1-5 (Top 5)
- **Light Green**: Rank 6-10 (Top 10)
- **Yellow**: Rank 11-15 (Next tier)
- **No color**: Rank 16+

### Sheet 5: Quadrant
- **Green**: Quick Win
- **Orange**: Strategic Bet
- **Light Green**: Fill-in
- **Red**: Avoid

---

## Tips for Success

### During Workshops

1. **Use Planning Poker Cards**: Prevents anchoring bias (everyone reveals simultaneously)
2. **Calibrate First**: Score 2 example use cases together before starting
3. **Time-box Discussions**: 5 minutes max per use case to avoid paralysis
4. **Document Assumptions**: Capture rationale in Notes columns
5. **Facilitator Discipline**: Keep workshop on track, park tangents

### Common Pitfalls

1. **Ignoring DVF Filter**: Don't skip to WSJF without DVF filtering first
2. **Not Using Fibonacci**: Teams try to use precise numbers (15, 17) instead of Fibonacci (13, 20)
3. **Underscoring RR/OE**: Platform/enabler use cases appear low priority if RR/OE not scored properly
4. **HiPPO Effect**: Highest Paid Person overrides data - use anonymous scoring
5. **Static Prioritization**: Score once and never revisit - set quarterly reviews

### Validation Checks

After scoring, validate:
- ✅ Do Top 5 span multiple strategic pillars?
- ✅ Are there any "Avoid" quadrant use cases? (Should have been eliminated in DVF)
- ✅ Do dependencies make sense? (High WSJF use case shouldn't depend on low WSJF prerequisite)
- ✅ Is portfolio balanced? (40% quick wins, 40% strategic bets)
- ✅ Are all Top 5 Wave 1 feasible?

---

## Maintenance & Updates

### Quarterly Recalibration

**When**: End of each PI (every 10-12 weeks)

**Process**:
1. Re-score WSJF for top 10 use cases
2. Update DVF if new information available
3. Adjust wave assignments if delays occur
4. Re-validate Top 5 selection

**Triggers for Re-prioritization**:
- Strategic priority shift
- Regulatory change
- Technology breakthrough or failure
- Resource constraint changes
- Market/competitive changes

### Adding New Use Cases

1. Add row in Sheet 1 (Use Case Inventory)
2. Complete DVF assessment in Sheet 2
3. If Pass, complete WSJF scoring in Sheet 3
4. Map dependencies in Sheet 4
5. Review portfolio impact in Sheet 5

---

## Exporting for Presentations

### Top 10 List for Programme Planning

**Steps**:
1. Go to Sheet 5 (Portfolio View)
2. Filter: Top 10 = TRUE
3. Sort by WSJF Rank ascending
4. Copy columns: ID, Name, WSJF Rank, Wave, Executive Notes
5. Paste into Word/PowerPoint

### Top 5 for Executive Presentation

**Steps**:
1. Go to Sheet 5 (Portfolio View)
2. Filter: Top 5 = TRUE
3. Sort by WSJF Rank ascending
4. Use Executive Notes column for presentation talking points
5. Create slide per use case (see template in PRACTICAL-PRIORITIZATION-GUIDE.md)

### Portfolio Charts

**Recommended Charts**:
1. **WSJF Ranking**: Horizontal bar chart (Top 15)
   - Data: Sheet 3, Columns B (Name) and H (WSJF Score)
   - Sort descending by WSJF Score

2. **Portfolio Quadrants**: 2×2 scatter plot
   - X-axis: Job Size (Sheet 5, Column E)
   - Y-axis: Cost of Delay (Sheet 5, Column D)
   - Labels: Use case IDs
   - Color by Quadrant

3. **Wave Distribution**: Stacked bar chart
   - Data: Sheet 7 (Dashboard), Rows 9-11
   - Shows count per wave

4. **Category Distribution**: Pie chart
   - Data: Sheet 1, Column D (Category)
   - Use pivot table to count by category

---

## Support & Questions

### For Framework Questions
- See [PRIORITIZATION-RESEARCH-CONSOLIDATED.md](PRIORITIZATION-RESEARCH-CONSOLIDATED.md) for detailed framework explanations
- See [PRACTICAL-PRIORITIZATION-GUIDE.md](PRACTICAL-PRIORITIZATION-GUIDE.md) for step-by-step workshop instructions
- See [USE-CASE-PRIORITISATION-FRAMEWORK.md](USE-CASE-PRIORITISATION-FRAMEWORK.md) for complete BNZ framework

### For Excel Technical Issues
- Ensure formulas are calculating: File → Options → Formulas → Automatic Calculation
- If colors don't update: Home → Conditional Formatting → Manage Rules
- If cross-sheet formulas break: Don't rename sheets

### For Workshop Facilitation
- Review workshop scripts in PRACTICAL-PRIORITIZATION-GUIDE.md
- Consider hiring external facilitator for first workshop
- Use video conferencing for distributed teams (share screen of live spreadsheet)

---

## Quick Start Checklist

### Before Week 1 Workshop
- [ ] Open BNZ-Use-Case-Prioritization.xlsx
- [ ] Verify all 24 use cases in Sheet 1
- [ ] Print Sheet 6 (Scoring Guidelines) for all participants
- [ ] Book 3-hour workshop room
- [ ] Send pre-read materials 1 week ahead

### Week 1-2: DVF Workshop
- [ ] Complete Sheet 2 (DVF Filtering)
- [ ] Identify 15-18 "Pass" use cases
- [ ] Document rationale for "Fail" use cases

### Week 3-4: WSJF Workshop
- [ ] Complete Sheet 3 (WSJF Scoring)
- [ ] Review WSJF rankings
- [ ] Document assumptions for Top 10

### Week 5: Dependencies
- [ ] Complete Sheet 4 (Dependencies & Schedule)
- [ ] Assign all use cases to waves
- [ ] Validate against WSJF rankings

### Week 6: Portfolio & Selection
- [ ] Complete Sheet 5 (Portfolio View)
- [ ] Mark Top 10 (column J)
- [ ] Mark Top 5 (column K)
- [ ] Write Executive Notes (column L)

### Ready for Presentation
- [ ] Review Sheet 7 (Dashboard) for summary stats
- [ ] Export Top 5 for executive deck
- [ ] Create supporting charts
- [ ] Rehearse presentation

---

**Version**: 1.0
**Last Updated**: December 5, 2025
**Created for**: BNZ AI Platform Architecture Programme
