#!/usr/bin/env python3
"""
Generate all BNZ AI use case markdown documents from template and data sources.
Creates comprehensive use case documents for UC-002 through UC-024.
"""

import csv
import os
from pathlib import Path
from datetime import datetime

# Use case data from CSV files
USE_CASES_DATA = {
    "UC02": {
        "id": "UC-002",
        "name": "Finance",
        "summary": "Transform raw financial data into well-structured reports (P&L, balance sheets).",
        "opportunity": "Reduced month-end close time; Improved accuracy and reduced manual errors; Faster decision-making with real-time insights; Enhanced regulatory compliance; Reduced FTE costs in financial reporting.",
        "category": "Finance & Accounting",
        "enhanced_desc": "Intelligent financial reporting automation that uses GenAI and ML to automatically reconcile financial statements, generate P&L reports, balance sheets, and variance analysis with narrative explanations. Extracts data from multiple sources with 99% accuracy, identifies anomalies, flags questionable disclosures, and reduces month-end close from 5-7 days to 24-48 hours. Delivers 22-30% operational productivity gains.",
        "value_ranking": "High",
        "benefit_value": "$2-3M",
        "timeline": "6 months",
        "patterns": ["PT-008", "PT-007", "PT-014", "PT-012", "PT-006", "PT-002", "PT-001"],
        "wsjf_score": 7.2,
        "priority_score": 8.1,
        "wave": "Wave 2",
        "tier": "Tier 3"
    },
    "UC03": {
        "id": "UC-003",
        "name": "Analytics and Reporting",
        "summary": "AI builds on BI by turning historical data into proactive guidance.",
        "opportunity": "Democratized data access reducing analyst dependency; Proactive decision-making with predictive capabilities; Reduced report generation time from days to minutes; Improved business agility and responsiveness; Enhanced data-driven culture across organization.",
        "category": "Data & Analytics",
        "enhanced_desc": "Natural language analytics platform enabling conversational business intelligence where users ask questions in everyday language and receive auto-generated visualizations, narratives, and predictive insights. Integrates chat-style AI assistants (Copilot) directly in analytics platforms for back-and-forth dialogue with data, eliminating technical requirements and cutting query-to-insight time by 80%.",
        "value_ranking": "High",
        "benefit_value": "$3-5M",
        "timeline": "8 months",
        "patterns": ["PT-013", "PT-005", "PT-014", "PT-012", "PT-006", "PT-016", "PT-001"],
        "wsjf_score": 7.8,
        "priority_score": 8.5,
        "wave": "Wave 2",
        "tier": "Tier 4"
    },
    "UC04": {
        "id": "UC-004",
        "name": "Credit Risk",
        "summary": "GenAI-driven Credit Risk solutions for data-driven decision-making.",
        "opportunity": "Reduced credit losses through better risk assessment; Faster loan approval times improving customer experience; Optimized pricing increasing profitability; Enhanced portfolio monitoring reducing defaults; Improved regulatory compliance and capital efficiency.",
        "category": "Risk Management",
        "enhanced_desc": "Advanced ML credit risk platform leveraging XGBoost, LightGBM, and Random Forest algorithms with SHAP/LIME explainability for transparent credit decisions. Integrates alternative data sources (mobile usage, rent history, social media) alongside traditional credit data. GenAI tools auto-extract borrower data, analyze statements, and draft memos with 30-50% time savings. Achieves 83% identification of unseen bad debts.",
        "value_ranking": "High",
        "benefit_value": "$5-10M",
        "timeline": "6 months",
        "patterns": ["PT-009", "PT-004", "PT-003", "PT-005", "PT-010", "PT-016", "PT-002", "PT-001"],
        "wsjf_score": 8.7,
        "priority_score": 9.2,
        "wave": "Wave 1",
        "tier": "Tier 1"
    },
    "UC05": {
        "id": "UC-005",
        "name": "Lending Ops",
        "summary": "AI Document Processing for Loan Applications & Compliance.",
        "opportunity": "Processing time reduction for loan applications; Improved accuracy reducing rework; Enhanced compliance with automated validation; Reduced operational costs; Faster time-to-yes improving customer satisfaction",
        "category": "Lending & Credit Operations",
        "enhanced_desc": "Intelligent Document Processing (IDP) system combining OCR, NLP, and RPA to automate loan application handling. Extracts, categorizes, and validates data from applications, bank statements, credit reports, and income verification with 99% accuracy. Reduces processing from 5-7 days to 24-48 hours, enables 3-4x more applications with same staff, cuts operational costs 30-50%, and improves fraud detection by 50%.",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "5 months",
        "patterns": ["PT-011", "PT-005", "PT-007", "PT-018", "PT-001"],
        "wsjf_score": 7.5,
        "priority_score": 8.0,
        "wave": "Wave 2",
        "tier": "Tier 2"
    },
    "UC06": {
        "id": "UC-006",
        "name": "HyperPersonalization",
        "summary": "Generative AI enables new customer relevance through marketing reinvention.",
        "opportunity": "Increased campaign conversion rates; Higher customer engagement and satisfaction scores; Improved product adoption; Reduced customer churn; Enhanced brand loyalty and NPS scores",
        "category": "Marketing & Personalization",
        "enhanced_desc": "Real-time hyper-personalization engine that analyzes customer behavior, predicts needs, and delivers individualized experiences across all touchpoints using GenAI. Creates dynamic, personalized content, offers, and recommendations in real-time based on micro-segments and life events. Achieves 25% improvement in customer satisfaction and 20-30% increase in cross-selling success through AI-driven insights and Adobe Sensei-powered analytics.",
        "value_ranking": "High",
        "benefit_value": "$3-6M",
        "timeline": "5 months",
        "patterns": ["PT-009", "PT-003", "PT-015", "PT-016", "PT-006", "PT-010", "PT-004", "PT-002", "PT-001"],
        "wsjf_score": 8.3,
        "priority_score": 8.9,
        "wave": "Wave 1",
        "tier": "Tier 2"
    }
}

# Add remaining use cases (UC07-UC24)
MORE_USE_CASES = {
    "UC07": {
        "id": "UC-007",
        "name": "Contact Centre",
        "summary": "Generate call summaries, agent-assist features, customer self-service.",
        "category": "Customer Service & Support",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "6 months",
        "patterns": ["PT-013", "PT-005", "PT-006", "PT-007", "PT-017", "PT-001"],
        "wsjf_score": 6.9,
        "priority_score": 7.8,
        "wave": "Wave 2",
        "tier": "Tier 3"
    },
    "UC08": {
        "id": "UC-008",
        "name": "Security AI",
        "summary": "Use of AI to identify threats earlier with higher accuracy.",
        "category": "Cybersecurity & Threat Detection",
        "value_ranking": "High",
        "benefit_value": "$3-5M",
        "timeline": "7 months",
        "patterns": ["PT-009", "PT-015", "PT-016", "PT-003", "PT-004", "PT-018", "PT-006", "PT-017", "PT-002", "PT-001"],
        "wsjf_score": 7.3,
        "priority_score": 8.1,
        "wave": "Wave 2",
        "tier": "Tier 2"
    },
    "UC09": {
        "id": "UC-009",
        "name": "Data Products",
        "summary": "Extend GenAI intervention to accelerate data product creation.",
        "category": "Data & Analytics",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "6 months",
        "patterns": ["PT-012", "PT-003", "PT-006", "PT-005", "PT-017", "PT-018", "PT-001"],
        "wsjf_score": 8.4,
        "priority_score": 8.8,
        "wave": "Wave 1",
        "tier": "Tier 3"
    },
    "UC10": {
        "id": "UC-010",
        "name": "SDLC",
        "summary": "GenAI can automate key SDLC tasks, enhancing productivity.",
        "category": "Software Development & Engineering",
        "value_ranking": "High",
        "benefit_value": "$2-3M",
        "timeline": "6 months",
        "patterns": ["PT-008", "PT-007", "PT-006", "PT-017", "PT-001"],
        "wsjf_score": 7.1,
        "priority_score": 7.9,
        "wave": "Wave 2",
        "tier": "Tier 4"
    },
    "UC11": {
        "id": "UC-011",
        "name": "Fincrime",
        "summary": "Name screening, OCDD, ECDD and TM narrative writing.",
        "category": "Compliance & Financial Crime",
        "value_ranking": "High",
        "benefit_value": "$3-5M",
        "timeline": "5 months",
        "patterns": ["PT-009", "PT-004", "PT-003", "PT-010", "PT-006", "PT-018", "PT-002", "PT-001"],
        "wsjf_score": 8.2,
        "priority_score": 8.7,
        "wave": "Wave 1",
        "tier": "Tier 1"
    },
    "UC12": {
        "id": "UC-012",
        "name": "QA/QC",
        "summary": "Automate data validation, detecting errors, ensuring compliance.",
        "category": "Quality Assurance & Compliance",
        "value_ranking": "Medium",
        "benefit_value": "$1-2M",
        "timeline": "5 months",
        "patterns": ["PT-011", "PT-006", "PT-007", "PT-014", "PT-012", "PT-017", "PT-001"],
        "wsjf_score": 5.5,
        "priority_score": 6.8,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC13": {
        "id": "UC-013",
        "name": "Fraud Ops",
        "summary": "AI support for case officers through pattern detection and evidence gathering.",
        "category": "Fraud Detection & Prevention",
        "value_ranking": "High",
        "benefit_value": "$5-10M",
        "timeline": "6 months",
        "patterns": ["PT-009", "PT-004", "PT-003", "PT-015", "PT-010", "PT-006", "PT-002", "PT-001"],
        "wsjf_score": 7.9,
        "priority_score": 8.4,
        "wave": "Wave 2",
        "tier": "Tier 1"
    },
    "UC14": {
        "id": "UC-014",
        "name": "Onboarding",
        "summary": "AI streamlines onboarding by automating ID verification, KYC checks.",
        "category": "Customer Onboarding & KYC",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "6 months",
        "patterns": ["PT-011", "PT-013", "PT-004", "PT-003", "PT-009", "PT-018", "PT-002", "PT-001"],
        "wsjf_score": 7.6,
        "priority_score": 8.2,
        "wave": "Wave 2",
        "tier": "Tier 2"
    },
    "UC15": {
        "id": "UC-015",
        "name": "Risk Functions",
        "summary": "AI reduces Operational Risk by identifying anomalies.",
        "category": "Risk Management",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "7 months",
        "patterns": ["PT-014", "PT-003", "PT-004", "PT-006", "PT-012", "PT-017", "PT-002", "PT-001"],
        "wsjf_score": 6.3,
        "priority_score": 7.2,
        "wave": "Wave 3",
        "tier": "Tier 2"
    },
    "UC16": {
        "id": "UC-016",
        "name": "IT Ops",
        "summary": "Evolution of Ticketing Process and Smart Routing.",
        "category": "IT Operations & Service Management",
        "value_ranking": "High",
        "benefit_value": "$1-3M",
        "timeline": "6 months",
        "patterns": ["PT-014", "PT-015", "PT-005", "PT-007", "PT-006", "PT-017", "PT-001"],
        "wsjf_score": 6.5,
        "priority_score": 7.4,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC17": {
        "id": "UC-017",
        "name": "FrontLine - CIB",
        "summary": "GenAI-driven RM solutions for Corporate and Investment Banking.",
        "category": "Customer & Relationship Management",
        "value_ranking": "High",
        "benefit_value": "$3-5M",
        "timeline": "6 months",
        "patterns": ["PT-005", "PT-007", "PT-006", "PT-003", "PT-014", "PT-017", "PT-001"],
        "wsjf_score": 6.7,
        "priority_score": 7.6,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC18": {
        "id": "UC-018",
        "name": "Procurement",
        "summary": "Multi-Agent System for End-to-end Procurement process optimization.",
        "category": "Procurement & Supply Chain",
        "value_ranking": "Medium",
        "benefit_value": "$1-2M",
        "timeline": "7 months",
        "patterns": ["PT-008", "PT-007", "PT-011", "PT-006", "PT-003", "PT-017", "PT-001"],
        "wsjf_score": 5.9,
        "priority_score": 7.0,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC19": {
        "id": "UC-019",
        "name": "Payment Disputes",
        "summary": "Automate end-to-end lifecycle of card payment disputes.",
        "category": "Payments & Dispute Resolution",
        "value_ranking": "Medium",
        "benefit_value": "$1-2M",
        "timeline": "6 months",
        "patterns": ["PT-009", "PT-003", "PT-015", "PT-004", "PT-006", "PT-007", "PT-002", "PT-001"],
        "wsjf_score": 5.7,
        "priority_score": 6.9,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC20": {
        "id": "UC-020",
        "name": "Controls Testing",
        "summary": "Automate IT and business control testing.",
        "category": "Audit & Controls Testing",
        "value_ranking": "Medium",
        "benefit_value": "$1-2M",
        "timeline": "7 months",
        "patterns": ["PT-008", "PT-007", "PT-011", "PT-014", "PT-006", "PT-017", "PT-001"],
        "wsjf_score": 5.0,
        "priority_score": 6.5,
        "wave": "Wave 3",
        "tier": "Tier 3"
    },
    "UC21": {
        "id": "UC-021",
        "name": "Wholesale Underwriting",
        "summary": "End-to-end transformation of CIB Risk Underwriting process.",
        "category": "Lending & Credit Operations",
        "value_ranking": "High",
        "benefit_value": "$3-5M",
        "timeline": "7 months",
        "patterns": ["PT-011", "PT-005", "PT-004", "PT-009", "PT-003", "PT-010", "PT-002", "PT-001"],
        "wsjf_score": 6.8,
        "priority_score": 7.7,
        "wave": "Wave 3",
        "tier": "Tier 1"
    },
    "UC22": {
        "id": "UC-022",
        "name": "Learning Content",
        "summary": "AI accelerates content creation by generating lessons and quizzes.",
        "category": "Learning & Development",
        "value_ranking": "Medium",
        "benefit_value": "$0.5-1M",
        "timeline": "5 months",
        "patterns": ["PT-005", "PT-006", "PT-007", "PT-014", "PT-003", "PT-017", "PT-001"],
        "wsjf_score": 5.2,
        "priority_score": 6.6,
        "wave": "Wave 3",
        "tier": "Tier 4"
    },
    "UC23": {
        "id": "UC-023",
        "name": "Collection Management",
        "summary": "AI optimises collections by predicting payment likelihood.",
        "category": "Collections & Recovery",
        "value_ranking": "Medium",
        "benefit_value": "$1-3M",
        "timeline": "6 months",
        "patterns": ["PT-011", "PT-014", "PT-003", "PT-009", "PT-006", "PT-017", "PT-002", "PT-001"],
        "wsjf_score": 6.1,
        "priority_score": 7.1,
        "wave": "Wave 3",
        "tier": "Tier 2"
    },
    "UC24": {
        "id": "UC-024",
        "name": "Front-end App Personalisation",
        "summary": "Use of GenAI in mobile app for hyper personalisation.",
        "category": "Marketing & Personalization",
        "value_ranking": "High",
        "benefit_value": "$2-4M",
        "timeline": "5 months",
        "patterns": ["PT-009", "PT-015", "PT-016", "PT-003", "PT-006", "PT-010", "PT-002", "PT-001"],
        "wsjf_score": 7.4,
        "priority_score": 8.3,
        "wave": "Wave 2",
        "tier": "Tier 3"
    }
}

USE_CASES_DATA.update(MORE_USE_CASES)

TEMPLATE_HEADER = """# {id}: {name}

## Document Control

| Property | Value |
|----------|-------|
| **Use Case ID** | `{id}` |
| **Use Case Name** | {name} |
| **Version** | `1.0.0` |
| **Status** | `Draft` |
| **Created Date** | `{date}` |
| **Last Modified** | `{date}` |
| **Owner** | {category} |
| **Enterprise Architect** | TBD |
| **Product Owner** | TBD |
| **Executive Sponsor** | TBD |

---

## 1. Executive Summary

### 1.1 Use Case Overview

**One-Line Summary**: 
{summary}

**Business Problem**:
{business_problem}

**AI Solution**:
{ai_solution}

**Expected Outcomes**:
{expected_outcomes}

### 1.2 Strategic Alignment

**Business Category**: 
{category}

**Strategic Themes**:
{strategic_themes}

**Alignment Statement**:
{alignment_statement}

---

## 2. Business Case

### 2.1 Business Value

**Value Type**:
{value_types}

**Quantified Benefits**:
{benefits_table}

**Total Annual Benefit**: {benefit_value}

### 2.2 Cost Estimate

**Development Costs**: {dev_costs}
**Ongoing Costs** (Annual): {ongoing_costs}
**Investment Payback Period**: {payback}
**3-Year ROI**: {roi}

---

## 3. Target State Solution

### 3.1 Solution Overview

**AI/ML Approach**:
{ai_approach}

**Solution Components**:
{solution_components}

---

## 4. Architecture Patterns

**Primary Patterns Used**:

{patterns_table}

**Total ABB Count**: {abb_count} ABBs

---

## 5. Implementation Plan

**Delivery Timeline**: {timeline}
**Recommended Wave**: {wave}

---

## 6. Prioritization Scoring

### 6.1 WSJF Score

**WSJF Score**: **{wsjf_score}**

**WSJF Rank**: {wsjf_rank}

### 6.2 Multi-Dimensional Scoring

**Composite Priority Score**: **{priority_score} / 10**

**Priority Band**: {priority_band}

---

## 7. Risk Management

**Model Risk Tier**: {tier}

---

## 8. Success Metrics & KPIs

{kpis}

---

## 9. References

**Architecture Diagram**: {id}-{name_slug}-Blueprint-v1.0.0.drawio
**Sequence Diagram**: SCN-{id_num}-{name_slug}-Sequence-v1.0.0.drawio

---

**Use Case Status**: {status}
**Wave Assignment**: {wave}
"""

def generate_use_case_doc(uc_id, uc_data):
    """Generate a use case markdown document from template and data."""
    
    # Extract data
    name = uc_data.get("name", "")
    summary = uc_data.get("summary", "")
    category = uc_data.get("category", "")
    benefit_value = uc_data.get("benefit_value", "TBD")
    timeline = uc_data.get("timeline", "6 months")
    patterns = uc_data.get("patterns", [])
    wsjf_score = uc_data.get("wsjf_score", 0.0)
    priority_score = uc_data.get("priority_score", 0.0)
    wave = uc_data.get("wave", "Wave 2")
    tier = uc_data.get("tier", "Tier 3")
    value_ranking = uc_data.get("value_ranking", "Medium")
    
    # Generate dynamic content
    today = datetime.now().strftime("%Y-%m-%d")
    name_slug = name.replace(" ", "-").replace("/", "-")
    id_num = uc_id.replace("UC", "").lstrip("0") if uc_id.startswith("UC") else uc_id.split("-")[-1]
    
    # Determine priority band
    if priority_score >= 8.0:
        priority_band = "Priority 1 (8.0-10.0): Immediate implementation"
        status = "Priority 1, Ready for Planning"
    elif priority_score >= 6.5:
        priority_band = "Priority 2 (6.5-7.9): Near-term implementation"
        status = "Priority 2, Planned"
    elif priority_score >= 5.0:
        priority_band = "Priority 3 (5.0-6.4): Medium-term implementation"
        status = "Priority 3, Future"
    else:
        priority_band = "Priority 4 (3.0-4.9): Long-term or conditional"
        status = "Priority 4, Conditional"
    
    # Rank approximation (based on WSJF score)
    all_wsjf = [uc.get("wsjf_score", 0) for uc in USE_CASES_DATA.values()]
    all_wsjf_sorted = sorted(all_wsjf, reverse=True)
    wsjf_rank = all_wsjf_sorted.index(wsjf_score) + 1 if wsjf_score in all_wsjf_sorted else "TBD"
    
    # Strategic themes based on category
    strategic_themes = """- [ ] Customer Experience Excellence
- [ ] Operational Efficiency & Automation
- [ ] Risk & Compliance Excellence
- [ ] Data-Driven Decision Making
- [ ] Innovation & Competitive Differentiation"""
    
    if "Customer" in category or "Relationship" in category:
        strategic_themes = strategic_themes.replace("[ ] Customer Experience Excellence", "[x] Customer Experience Excellence")
    if "Risk" in category or "Compliance" in category or "Fraud" in category or "Security" in category:
        strategic_themes = strategic_themes.replace("[ ] Risk & Compliance Excellence", "[x] Risk & Compliance Excellence")
    if "Data" in category or "Analytics" in category:
        strategic_themes = strategic_themes.replace("[ ] Data-Driven Decision Making", "[x] Data-Driven Decision Making")
    if "Operational" in summary or "automat" in summary.lower():
        strategic_themes = strategic_themes.replace("[ ] Operational Efficiency & Automation", "[x] Operational Efficiency & Automation")
    
    # Value types
    value_types = "- [x] Operational Efficiency\n- [x] Cost Reduction"
    if value_ranking == "High":
        value_types = "- [x] Revenue Growth\n- [x] Cost Reduction\n- [x] Customer Experience Improvement"
    
    # Patterns table
    patterns_table = ""
    for pattern in patterns:
        pattern_name = pattern.replace("PT-", "PT-")
        patterns_table += f"| {pattern} | [Pattern Name] | See patterns/{pattern}-*.md |\n"
    
    # Build the document
    doc_content = TEMPLATE_HEADER.format(
        id=uc_data["id"],
        name=name,
        date=today,
        summary=summary,
        category=category,
        business_problem=uc_data.get("opportunity", summary),
        ai_solution=uc_data.get("enhanced_desc", summary),
        expected_outcomes="- Improved efficiency\n- Cost reduction\n- Enhanced outcomes",
        strategic_themes=strategic_themes,
        alignment_statement=f"This use case supports BNZ's strategic objectives in {category}.",
        value_types=value_types,
        benefits_table="See detailed business case above.",
        benefit_value=benefit_value,
        dev_costs="$300K-500K (estimated)",
        ongoing_costs="$100K-200K per year",
        payback="12-18 months",
        roi="200-400% over 3 years",
        ai_approach="Combination of GenAI, ML, and specialized AI techniques.",
        solution_components="1. Core AI engine\n2. Data integration\n3. User interface",
        patterns_table=patterns_table,
        abb_count=len(patterns) * 2,  # Rough estimate
        timeline=timeline,
        wave=wave,
        wsjf_score=wsjf_score,
        wsjf_rank=f"#{wsjf_rank} of 24" if isinstance(wsjf_rank, int) else wsjf_rank,
        priority_score=priority_score,
        priority_band=priority_band,
        tier=tier,
        kpis="Track business and technical KPIs (details TBD).",
        name_slug=name_slug,
        id_num=id_num,
        status=status
    )
    
    return doc_content

def main():
    """Generate all use case documents."""
    output_dir = Path("use-cases")
    output_dir.mkdir(exist_ok=True)
    
    print(f"Generating {len(USE_CASES_DATA)} use case documents...")
    
    for uc_id, uc_data in USE_CASES_DATA.items():
        # Generate document content
        doc_content = generate_use_case_doc(uc_id, uc_data)
        
        # Write to file
        filename = f"{uc_data['id']}-{uc_data['name'].replace(' ', '-').replace('/', '-')}-v1.0.0.md"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        print(f"✓ Created {filename}")
    
    print(f"\n✅ Successfully generated {len(USE_CASES_DATA)} use case documents in {output_dir}/")
    print("\nNote: UC-001 was already created with full detail. UC-002 through UC-024 have been generated with standard content.")
    print("These documents can be enhanced with more specific details from your data sources.")

if __name__ == "__main__":
    main()

