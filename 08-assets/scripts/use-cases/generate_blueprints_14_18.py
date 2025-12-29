"""
Generate Draw.io blueprint files for use cases UC-014 through UC-018.
Based on the UC-001 template structure.
"""

import csv
import os
from pathlib import Path

# BNZ Colors
NAVY = "#003087"
ORANGE = "#FF6B35"
TEAL = "#00A651"
PURPLE = "#9C27B0"

# Use case metadata
use_cases = {
    14: {
        "id": "UC-014",
        "name": "Onboarding",
        "full_title": "AI-Powered Customer Onboarding",
        "description": "AI streamlines onboarding by automating ID verification, KYC checks, and document processing.",
        "benefits": "• Reduced onboarding time from days to hours\n• Improved customer experience and conversion rates by 25%\n• Enhanced compliance with automated checks\n• Lower operational costs by 40%\n• Reduced abandonment rates by 35%\n• 99% accuracy in document verification",
        "category": "Customer Operations",
        "value": "High",
        "ai_type": "GenAI + ML + CV",
        "cost": "$650K - $850K",
        "timeline": "6-9 months",
        "complexity": "High",
        "priority": "82/100",
    },
    15: {
        "id": "UC-015",
        "name": "Risk Functions",
        "full_title": "AI-Powered Operational Risk Management",
        "description": "AI reduces Operational Risk by identifying anomalies, predicting events, and optimizing capital allocation through advanced analytics.",
        "benefits": "• Improved risk detection reducing losses by 30%\n• Faster risk assessment and response times\n• Enhanced regulatory compliance and capital optimization\n• Reduced manual effort by 50%\n• Better enterprise-wide risk visibility\n• Predictive KRI dashboards",
        "category": "Risk & Compliance",
        "value": "High",
        "ai_type": "ML + GenAI",
        "cost": "$750K - $950K",
        "timeline": "9-12 months",
        "complexity": "High",
        "priority": "78/100",
    },
    16: {
        "id": "UC-016",
        "name": "IT Ops",
        "full_title": "AI-Enhanced IT Operations & Service Management",
        "description": "Evolution of Ticketing Process with Smart Routing, automated resolution, and predictive SLA management.",
        "benefits": "• Reduced mean time to resolution (MTTR) by 45%\n• Automated resolution of 60% of tickets\n• Improved SLA compliance to 98%+\n• Lower IT support costs by 35%\n• Better workload distribution\n• Enhanced user satisfaction scores",
        "category": "IT Operations",
        "value": "Medium",
        "ai_type": "GenAI + ML",
        "cost": "$550K - $750K",
        "timeline": "6-9 months",
        "complexity": "Medium",
        "priority": "75/100",
    },
    17: {
        "id": "UC-017",
        "name": "FrontLine CIB",
        "full_title": "AI-Powered Corporate & Investment Banking Relationship Management",
        "description": "GenAI-driven RM solutions for Corporate and Investment Banking including intelligence synthesis, deal forecasting, and client briefing automation.",
        "benefits": "• Increased wallet share with corporate clients by 15%\n• Enhanced deal win rates by 20%\n• Improved RM productivity by 2-3x\n• Better market intelligence and positioning\n• Reduced client attrition by 12%\n• Faster client briefing preparation",
        "category": "Customer & RM",
        "value": "High",
        "ai_type": "GenAI + ML",
        "cost": "$850K - $1.2M",
        "timeline": "9-12 months",
        "complexity": "High",
        "priority": "84/100",
    },
    18: {
        "id": "UC-018",
        "name": "Procurement",
        "full_title": "Multi-Agent Procurement Optimization",
        "description": "Multi-Agent System for End-to-end Procurement process optimization including sourcing, contract analysis, and supplier risk management.",
        "benefits": "• Cost savings of 15-20% through optimized sourcing\n• Reduced procurement cycle time by 50%\n• Improved supplier performance and risk management\n• Enhanced spend visibility and control\n• Lower invoice processing costs by 60%\n• 99% 3-way match accuracy",
        "category": "Operations",
        "value": "Medium",
        "ai_type": "Agentic AI",
        "cost": "$700K - $950K",
        "timeline": "9-12 months",
        "complexity": "High",
        "priority": "76/100",
    },
}


def load_abb_data(csv_path):
    """Load ABB data from CSV"""
    abbs = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            use_case_id = int(row['use case id'])
            if use_case_id not in abbs:
                abbs[use_case_id] = []
            abbs[use_case_id].append(row)
    return abbs


def get_template_header(uc_id, uc_name, uc_title):
    """Generate draw.io XML header"""
    return f'''<mxfile host="Electron" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/29.0.3 Chrome/140.0.7339.249 Electron/38.7.0 Safari/537.36" version="29.0.3">
  <diagram name="{uc_id} {uc_name} Blueprint" id="{uc_id.lower()}-blueprint">
    <mxGraphModel dx="1765" dy="1034" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />'''


def get_template_footer():
    """Generate draw.io XML footer"""
    return '''      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''


def escape_xml(text):
    """Escape special XML characters"""
    return (text.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&apos;')
            .replace('\n', '&#xa;'))


def generate_blueprint(uc_num, abb_data):
    """Generate complete blueprint XML for a use case"""
    uc = use_cases[uc_num]
    uc_id = uc['id']
    uc_name = uc['name']
    uc_title = uc['full_title']

    xml_parts = [get_template_header(uc_id, uc_name, uc_title)]

    # Background
    xml_parts.append('''
        <mxCell id="bg" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=none;" parent="1" vertex="1">
          <mxGeometry width="1920" height="1080" as="geometry" />
        </mxCell>''')

    # Header
    xml_parts.append(f'''
        <mxCell id="header-bg" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={NAVY};strokeColor=none;" parent="1" vertex="1">
          <mxGeometry width="1920" height="80" as="geometry" />
        </mxCell>
        <mxCell id="header-title" value="Use Case Blueprint: {uc_id} {uc_name}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=28;fontStyle=1;fontColor=#FFFFFF;fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="30" y="20" width="900" height="40" as="geometry" />
        </mxCell>
        <mxCell id="header-subtitle" value="{escape_xml(uc_title)}" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontColor=#FFFFFF;fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="1520" y="25" width="370" height="30" as="geometry" />
        </mxCell>''')

    # Summary Panel
    xml_parts.append(f'''
        <mxCell id="summary-panel" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={NAVY};strokeWidth=2;arcSize=10;" parent="1" vertex="1">
          <mxGeometry x="30" y="110" width="580" height="280" as="geometry" />
        </mxCell>
        <mxCell id="summary-header" value="Use Case Summary" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor={NAVY};fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="50" y="125" width="540" height="30" as="geometry" />
        </mxCell>
        <mxCell id="summary-id" value="ID: {uc_id}" style="text;html=1;strokeColor=none;fillColor=#6699CC;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=12;fontStyle=1;fontFamily=Helvetica;fontColor=#333333;" parent="1" vertex="1">
          <mxGeometry x="50" y="165" width="120" height="25" as="geometry" />
        </mxCell>
        <mxCell id="summary-category" value="Category: {uc['category']}" style="text;html=1;strokeColor=none;fillColor=#6699CC;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=12;fontStyle=1;fontFamily=Helvetica;fontColor=#333333;" parent="1" vertex="1">
          <mxGeometry x="185" y="165" width="200" height="25" as="geometry" />
        </mxCell>
        <mxCell id="summary-value" value="Value: {uc['value']}" style="text;html=1;strokeColor=none;fillColor=#E6F7ED;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=12;fontStyle=1;fontFamily=Helvetica;fontColor={TEAL};" parent="1" vertex="1">
          <mxGeometry x="400" y="165" width="100" height="25" as="geometry" />
        </mxCell>
        <mxCell id="badge-ai-type" value="{uc['ai_type']}" style="text;html=1;strokeColor={ORANGE};fillColor=#FFE5DC;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=10;fontStyle=1;fontColor={ORANGE};fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="515" y="165" width="75" height="25" as="geometry" />
        </mxCell>
        <mxCell id="summary-desc-label" value="Description:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="50" y="200" width="540" height="20" as="geometry" />
        </mxCell>
        <mxCell id="summary-desc" value="{escape_xml(uc['description'])}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#333333;" parent="1" vertex="1">
          <mxGeometry x="50" y="220" width="540" height="50" as="geometry" />
        </mxCell>
        <mxCell id="summary-benefits-label" value="Anticipated Benefits:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="50" y="275" width="540" height="20" as="geometry" />
        </mxCell>
        <mxCell id="summary-benefits" value="{escape_xml(uc['benefits'])}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#333333;" parent="1" vertex="1">
          <mxGeometry x="50" y="295" width="540" height="80" as="geometry" />
        </mxCell>''')

    # Component Architecture Panel - this would need ABB data
    xml_parts.append(f'''
        <mxCell id="component-panel" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={NAVY};strokeWidth=2;arcSize=10;" parent="1" vertex="1">
          <mxGeometry x="640" y="110" width="840" height="640" as="geometry" />
        </mxCell>
        <mxCell id="component-header" value="Solution Architecture - Architecture Building Blocks (ABBs)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=18;fontStyle=1;fontColor={NAVY};" parent="1" vertex="1">
          <mxGeometry x="660" y="125" width="600" height="30" as="geometry" />
        </mxCell>''')

    # Footer - Cost & Prioritization
    xml_parts.append(f'''
        <mxCell id="footer-bg" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#CCCCCC;" parent="1" vertex="1">
          <mxGeometry x="1510" y="770" width="380" height="280" as="geometry" />
        </mxCell>
        <mxCell id="footer-header" value="Costing &amp; Prioritization" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;fontColor={NAVY};" parent="1" vertex="1">
          <mxGeometry x="1530" y="780" width="340" height="25" as="geometry" />
        </mxCell>
        <mxCell id="footer-cost-label" value="Estimated Cost:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1530" y="810" width="120" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-cost-value" value="{uc['cost']}" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#CC0000;fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1660" y="810" width="210" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-timeline-label" value="Timeline:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1530" y="833" width="120" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-timeline-value" value="{uc['timeline']}" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;" parent="1" vertex="1">
          <mxGeometry x="1660" y="833" width="210" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-complexity-label" value="Complexity:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1530" y="856" width="120" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-complexity-value" value="{uc['complexity']}" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor={ORANGE};fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1660" y="856" width="210" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-priority-label" value="Priority Score:" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1530" y="879" width="120" height="18" as="geometry" />
        </mxCell>
        <mxCell id="footer-priority-value" value="{uc['priority']}" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor={TEAL};fontStyle=1;" parent="1" vertex="1">
          <mxGeometry x="1660" y="879" width="210" height="18" as="geometry" />
        </mxCell>
        <mxCell id="doc-info" value="Blueprint Version: 1.0.0 | Created: Dec 2024 | Classification: Internal | Owner: Strategy &amp; Architecture | Compliant with BNZ Visual Design Standards v2.0" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666;fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="30" y="1055" width="1860" height="20" as="geometry" />
        </mxCell>''')

    xml_parts.append(get_template_footer())

    return '\n'.join(xml_parts)


def main():
    # Paths
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    data_dir = base_dir / 'data'
    output_dir = base_dir

    # Load ABB data
    abb_csv = data_dir / 'ai-solution-components.csv'
    abb_data = load_abb_data(abb_csv)

    # Generate blueprints for UC-014 through UC-018
    for uc_num in [14, 15, 16, 17, 18]:
        uc = use_cases[uc_num]
        uc_id = uc['id']
        uc_name = uc['name']

        # Generate XML
        blueprint_xml = generate_blueprint(uc_num, abb_data.get(uc_num, []))

        # Write to file
        output_file = output_dir / f"{uc_id}-{uc_name.replace(' ', '-')}-Blueprint-v1.0.0.drawio"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(blueprint_xml)

        print(f"Created: {output_file.name}")


if __name__ == '__main__':
    main()
