#!/usr/bin/env python3
"""
Complete Blueprint Generator for BNZ AI Use Cases
Generates comprehensive solution blueprints with all panels matching reference format.
"""

import csv
import sys
from collections import defaultdict
from typing import List, Dict

# BNZ Visual Design Standards v2.0
class BNZColors:
    NAVY = "#003087"
    ORANGE = "#FF6B35"
    TEAL = "#00A651"
    PURPLE = "#9C27B0"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#E6F0FA"
    LIGHT_ORANGE = "#FFE5DC"
    LIGHT_TEAL = "#E6F7ED"
    LIGHT_PURPLE = "#F3E5F5"
    GRAY = "#F5F5F5"
    DARK_GRAY = "#333333"
    LIGHT_GRAY_2 = "#CCCCCC"
    BLUE_BOX = "#6699CC"
    YELLOW = "#FFFDE7"
    RED = "#CC0000"

def escape_xml(text):
    """Escape special characters for XML."""
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
            .replace("\n", "&#xa;"))

def load_csv(filename):
    """Load CSV file and return list of dicts."""
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

class BlueprintBuilder:
    """Builder class for creating draw.io blueprint XML."""
    
    def __init__(self):
        self.cells = []
        self.cell_id = 1000
        self.abb_positions = {}
    
    def next_id(self):
        """Generate next cell ID."""
        self.cell_id += 1
        return f"cell-{self.cell_id}"
    
    def add_cell(self, cell_xml):
        """Add a cell to the blueprint."""
        self.cells.append(cell_xml)
    
    def create_rectangle(self, x, y, width, height, fill_color, stroke_color,
                        stroke_width=1, rounded=True, dashed=False, arc_size=10):
        """Create a rectangle cell."""
        cell_id = self.next_id()
        style_parts = [
            "rounded=1" if rounded else "rounded=0",
            "whiteSpace=wrap",
            "html=1",
            f"fillColor={fill_color}",
            f"strokeColor={stroke_color}",
            f"strokeWidth={stroke_width}",
        ]
        if rounded:
            style_parts.append(f"arcSize={arc_size}")
        if dashed:
            style_parts.append("dashed=1")
        
        style = ";".join(style_parts) + ";"
        
        return f'''<mxCell id="{cell_id}" value="" style="{style}" parent="1" vertex="1">
      <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
    </mxCell>'''
    
    def create_text(self, x, y, width, height, text, font_size=10, font_style=0,
                   font_color="#000000", align="left", v_align="middle",
                   bg_color="none", border_color="none", font_family="Helvetica"):
        """Create a text cell."""
        cell_id = self.next_id()
        text_escaped = escape_xml(text)
        
        style = f"text;html=1;strokeColor={border_color};fillColor={bg_color};align={align};verticalAlign={v_align};whiteSpace=wrap;rounded=0;fontSize={font_size};fontStyle={font_style};fontColor={font_color};fontFamily={font_family};"
        
        return f'''<mxCell id="{cell_id}" value="{text_escaped}" style="{style}" parent="1" vertex="1">
      <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
    </mxCell>'''
    
    def build_diagram(self, use_case_id, use_case_name):
        """Build complete draw.io XML."""
        xml = f'''<mxfile host="AI Blueprint Generator" agent="Python Script" version="24.0.0">
  <diagram name="UC-{use_case_id:03d} {use_case_name} Blueprint" id="uc{use_case_id:03d}-blueprint">
    <mxGraphModel dx="1765" dy="1034" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(self.cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        return xml

def create_header(builder: BlueprintBuilder, summary: Dict):
    """Create header section."""
    uc_id = int(summary['use_case_id'])
    uc_name = summary['use_case_name']
    improved_desc = summary.get('improved_description', '')[:80]
    
    # Background
    builder.add_cell(builder.create_rectangle(0, 0, 1920, 1080, BNZColors.GRAY, "none",
                                             stroke_width=0, rounded=False))
    
    # Header background
    builder.add_cell(builder.create_rectangle(0, 0, 1920, 80, BNZColors.NAVY, "none",
                                             stroke_width=0, rounded=False))
    
    # Title
    builder.add_cell(builder.create_text(30, 20, 900, 40,
                                        f"Use Case Blueprint: UC-{uc_id:03d} {uc_name}",
                                        font_size=28, font_style=1,
                                        font_color=BNZColors.WHITE))
    
    # Subtitle
    builder.add_cell(builder.create_text(1520, 25, 370, 30,
                                        improved_desc,
                                        font_size=16, font_color=BNZColors.WHITE,
                                        align="right"))

def create_summary_panel(builder: BlueprintBuilder, summary: Dict):
    """Create summary panel with badges and description."""
    uc_id = int(summary['use_case_id'])
    category = summary.get('category', 'General')[:30]
    value = summary.get('value', 'Medium')
    ai_type = summary.get('ai_type', 'AI/ML')[:20]
    description = summary.get('description', '')[:300]
    benefits = summary.get('benefits', '')[:400]
    
    # Panel background
    builder.add_cell(builder.create_rectangle(30, 110, 580, 280, BNZColors.WHITE,
                                             BNZColors.NAVY, stroke_width=2))
    
    # Header
    builder.add_cell(builder.create_text(50, 125, 540, 30, "Use Case Summary",
                                        font_size=18, font_style=1,
                                        font_color=BNZColors.NAVY))
    
    # Badges row
    builder.add_cell(builder.create_text(50, 165, 120, 25, f"ID: UC-{uc_id:03d}",
                                        font_size=12, font_style=1,
                                        bg_color=BNZColors.BLUE_BOX,
                                        font_color=BNZColors.DARK_GRAY, align="left"))
    
    builder.add_cell(builder.create_text(185, 165, 200, 25, f"Category: {category}",
                                        font_size=12, font_style=1,
                                        bg_color=BNZColors.BLUE_BOX,
                                        font_color=BNZColors.DARK_GRAY, align="left"))
    
    builder.add_cell(builder.create_text(400, 165, 100, 25, f"Value: {value}",
                                        font_size=12, font_style=1,
                                        bg_color=BNZColors.LIGHT_TEAL,
                                        font_color=BNZColors.TEAL, align="left"))
    
    builder.add_cell(builder.create_text(515, 165, 75, 25, ai_type,
                                        font_size=10, font_style=1,
                                        bg_color=BNZColors.LIGHT_ORANGE,
                                        border_color=BNZColors.ORANGE,
                                        font_color=BNZColors.ORANGE, align="center"))
    
    # Description
    builder.add_cell(builder.create_text(50, 200, 540, 20, "Description:",
                                        font_size=12, font_style=1))
    
    builder.add_cell(builder.create_text(50, 220, 540, 50, description,
                                        font_size=11, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))
    
    # Benefits
    builder.add_cell(builder.create_text(50, 275, 540, 20, "Anticipated Benefits:",
                                        font_size=12, font_style=1))
    
    # Format benefits as bullet points if not already
    if benefits and not benefits.startswith('•'):
        benefit_parts = [b.strip() for b in benefits.split(';') if b.strip()]
        benefits = '\n'.join([f"• {b}" for b in benefit_parts[:5]])
    
    builder.add_cell(builder.create_text(50, 295, 540, 80, benefits,
                                        font_size=11, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))

def create_metrics_panel(builder: BlueprintBuilder, metrics: Dict):
    """Create metrics and dependencies panel."""
    platform = metrics.get('platform', 'Cloud Platform')[:40]
    data_sources = metrics.get('data_sources', 'Customer data')[:40]
    ai_type = metrics.get('ai_type', 'AI/ML')[:30]
    deployment = metrics.get('deployment', 'Hybrid Cloud')[:30]
    users = metrics.get('estimated_users', '100+')
    
    # Panel background
    builder.add_cell(builder.create_rectangle(30, 410, 285, 140, BNZColors.WHITE,
                                             BNZColors.NAVY, stroke_width=2))
    
    # Header
    builder.add_cell(builder.create_text(45, 425, 255, 25, "Key Metrics & Dependencies",
                                        font_size=16, font_style=1,
                                        font_color=BNZColors.NAVY))
    
    # Content
    content = f'''<b>Platform:</b> {escape_xml(platform)}
<b>Data:</b> {escape_xml(data_sources)}
<b>AI:</b> {escape_xml(ai_type)}
<b>Deployment:</b> {escape_xml(deployment)}
<b>Users:</b> {escape_xml(users)}'''
    
    builder.add_cell(builder.create_text(45, 455, 255, 80, content,
                                        font_size=10, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))

def create_governance_panel(builder: BlueprintBuilder, governance: Dict):
    """Create governance and compliance panel."""
    data_res = governance.get('data_residency', 'New Zealand/Australia')[:40]
    privacy = governance.get('privacy_compliance', 'Privacy Act')[:40]
    model_gov = governance.get('model_governance', 'Human-in-loop')[:35]
    audit = governance.get('audit_requirements', 'Logging')[:30]
    security = governance.get('security_requirements', 'Zero Trust')[:40]
    explain = governance.get('explainability', 'XAI')[:30]
    
    # Panel background
    builder.add_cell(builder.create_rectangle(325, 410, 285, 140, BNZColors.WHITE,
                                             BNZColors.PURPLE, stroke_width=2))
    
    # Header
    builder.add_cell(builder.create_text(340, 425, 255, 25, "Governance & Compliance",
                                        font_size=16, font_style=1,
                                        font_color=BNZColors.PURPLE))
    
    # Content
    content = f'''<b>Data Residency:</b> {escape_xml(data_res)}
<b>Privacy:</b> {escape_xml(privacy)}
<b>Model Governance:</b> {escape_xml(model_gov)}
<b>Audit:</b> {escape_xml(audit)}
<b>Security:</b> {escape_xml(security)}
<b>Explainability:</b> {escape_xml(explain)}'''
    
    builder.add_cell(builder.create_text(340, 455, 255, 80, content,
                                        font_size=10, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))

def create_change_impact_panel(builder: BlueprintBuilder, risks: Dict, costing: Dict):
    """Create change impact and readiness panel."""
    complexity = costing.get('complexity', 'Medium')
    
    # Panel background
    builder.add_cell(builder.create_rectangle(30, 570, 285, 150, BNZColors.WHITE,
                                             BNZColors.ORANGE, stroke_width=2))
    
    # Header
    builder.add_cell(builder.create_text(45, 585, 255, 25, "Change Impact & Readiness",
                                        font_size=14, font_style=1,
                                        font_color=BNZColors.ORANGE))
    
    # Content based on complexity
    if complexity == 'High':
        org_impact = 'High - Significant role transformation required'
        training = '40+ hrs per user'
        resistance = 'Medium - Early adopter pilot essential'
    elif complexity == 'Medium':
        org_impact = 'Medium - Process changes required'
        training = '20-30 hrs per user'
        resistance = 'Low-Medium - Change management needed'
    else:
        org_impact = 'Low - Minimal process changes'
        training = '10-15 hrs per user'
        resistance = 'Low - Incremental adoption'
    
    content = f'''<b>Organizational Impact:</b> {org_impact}
<b>Training:</b> {training}
<b>User Resistance Risk:</b> {resistance}

<b>Technical Readiness:</b> Medium
• Data quality improvement needed
• System upgrades may be required'''
    
    builder.add_cell(builder.create_text(45, 615, 255, 95, content,
                                        font_size=9, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))

def create_decision_panel(builder: BlueprintBuilder, risks: Dict):
    """Create decision factors panel."""
    overall_risk = risks.get('overall_risk', 'Medium')
    
    # Panel background
    builder.add_cell(builder.create_rectangle(325, 570, 285, 150, BNZColors.WHITE,
                                             BNZColors.TEAL, stroke_width=2))
    
    # Header
    builder.add_cell(builder.create_text(340, 585, 255, 25, "Decision Factors",
                                        font_size=14, font_style=1,
                                        font_color=BNZColors.TEAL))
    
    # Strengths
    strengths = '''<b>Strengths (Go):</b>
✓ Business value identified
✓ Technology available
✓ Clear success metrics
✓ Stakeholder support'''
    
    builder.add_cell(builder.create_text(340, 615, 255, 45, strengths,
                                        font_size=9, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))
    
    # Concerns
    concerns = f'''<b>Concerns (Mitigate):</b>
⚠ Risk level: {overall_risk}
⚠ Data dependencies
⚠ Change management
⚠ Regulatory considerations'''
    
    builder.add_cell(builder.create_text(340, 665, 255, 45, concerns,
                                        font_size=9, font_color=BNZColors.DARK_GRAY,
                                        v_align="top"))



