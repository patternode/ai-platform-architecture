#!/usr/bin/env python3
"""Generate a draw.io sequence diagram for a scenario."""

import csv
import sys
from collections import OrderedDict

# BNZ Colors
class BNZColors:
    NAVY = "#003087"
    ORANGE = "#FF6B35"
    TEAL = "#00A651"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#E6F0FA"
    DARK_GRAY = "#333333"
    LIGHT_GRAY = "#F5F5F5"

def escape_xml(text):
    """Escape special characters for XML."""
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))

def generate_sequence_diagram(uc_id):
    """Generate a draw.io sequence diagram for the specified use case."""
    
    # Read scenario
    with open('use-case-scenarios.csv', 'r', encoding='utf-8') as f:
        scenarios = {r['use_case_id']: r for r in csv.DictReader(f)}
    
    scenario = scenarios.get(str(uc_id))
    if not scenario:
        print(f"Scenario not found for UC-{uc_id}")
        return
    
    # Read sequence steps
    with open('scenario-sequence-steps.csv', 'r', encoding='utf-8') as f:
        all_steps = list(csv.DictReader(f))
    
    steps = [s for s in all_steps if s['use_case_id'] == str(uc_id)]
    
    if not steps:
        print(f"No steps found for UC-{uc_id}")
        return
    
    # Extract unique participants in order of appearance
    participants = OrderedDict()
    for step in steps:
        if step['from_component'] not in participants:
            participants[step['from_component']] = len(participants)
        if step['to_component'] not in participants:
            participants[step['to_component']] = len(participants)
    
    participant_list = list(participants.keys())
    
    print(f"Generating sequence diagram for: {scenario['scenario_name']}")
    print(f"  Participants: {len(participant_list)}")
    print(f"  Steps: {len(steps)}")
    
    # Diagram dimensions
    page_width = 1920
    page_height = 1080
    margin = 50
    header_height = 160
    participant_height = 60
    participant_width = 140
    lifeline_start_y = header_height + participant_height + 20
    step_height = 50
    
    # Calculate participant spacing
    available_width = page_width - 2 * margin
    participant_spacing = available_width // (len(participant_list) + 1)
    
    # Start building XML
    cells = []
    cell_id = 1000
    
    def next_id():
        nonlocal cell_id
        cell_id += 1
        return f"cell-{cell_id}"
    
    # Background
    cells.append(f'''<mxCell id="{next_id()}" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={BNZColors.LIGHT_GRAY};strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="0" y="0" width="{page_width}" height="{page_height}" as="geometry" />
    </mxCell>''')
    
    # Header
    cells.append(f'''<mxCell id="{next_id()}" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={BNZColors.NAVY};strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="0" y="0" width="{page_width}" height="{header_height}" as="geometry" />
    </mxCell>''')
    
    # Title
    title = f"Sequence Diagram: {escape_xml(scenario['scenario_name'])}"
    cells.append(f'''<mxCell id="{next_id()}" value="{title}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontStyle=1;fontColor={BNZColors.WHITE};fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{margin}" y="15" width="{page_width - 2*margin}" height="30" as="geometry" />
    </mxCell>''')
    
    # Subtitle
    subtitle = f"UC-{uc_id:03d} | {escape_xml(scenario['use_case_name'])} | Actor: {escape_xml(scenario['actor'])}"
    cells.append(f'''<mxCell id="{next_id()}" value="{subtitle}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=0;fontColor={BNZColors.WHITE};fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{margin}" y="50" width="{page_width - 2*margin}" height="20" as="geometry" />
    </mxCell>''')
    
    # Scenario Description
    description = escape_xml(scenario.get('scenario_description', ''))
    cells.append(f'''<mxCell id="{next_id()}" value="{description}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=0;fontColor={BNZColors.WHITE};fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{margin}" y="75" width="{page_width - 2*margin}" height="30" as="geometry" />
    </mxCell>''')
    
    # Trigger and Expected Outcome
    trigger = escape_xml(scenario.get('trigger', ''))
    outcome = escape_xml(scenario.get('expected_outcome', ''))
    trigger_outcome = f"Trigger: {trigger} | Outcome: {outcome}"
    cells.append(f'''<mxCell id="{next_id()}" value="{trigger_outcome}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor={BNZColors.WHITE};fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{margin}" y="110" width="{page_width - 2*margin}" height="40" as="geometry" />
    </mxCell>''')
    
    # Participant boxes and lifelines
    participant_x_positions = {}
    lifeline_end_y = lifeline_start_y + len(steps) * step_height + 50
    
    for i, participant in enumerate(participant_list):
        x = margin + (i + 1) * participant_spacing - participant_width // 2
        y = header_height + 10
        participant_x_positions[participant] = x + participant_width // 2
        
        # Participant box
        cells.append(f'''<mxCell id="{next_id()}" value="{escape_xml(participant)}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={BNZColors.NAVY};strokeColor={BNZColors.NAVY};strokeWidth=2;fontSize=10;fontStyle=1;fontColor={BNZColors.WHITE};fontFamily=Helvetica;align=center;verticalAlign=middle;" parent="1" vertex="1">
      <mxGeometry x="{x}" y="{y}" width="{participant_width}" height="{participant_height}" as="geometry" />
    </mxCell>''')
        
        # Lifeline (dashed vertical line)
        lifeline_x = x + participant_width // 2
        cells.append(f'''<mxCell id="{next_id()}" value="" style="endArrow=none;html=1;strokeColor={BNZColors.DARK_GRAY};strokeWidth=1;dashed=1;dashPattern=5 5;fontFamily=Helvetica;" parent="1" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="{lifeline_x}" y="{lifeline_start_y}" as="sourcePoint" />
        <mxPoint x="{lifeline_x}" y="{lifeline_end_y}" as="targetPoint" />
      </mxGeometry>
    </mxCell>''')
    
    # Sequence messages
    for i, step in enumerate(steps):
        from_comp = step['from_component']
        to_comp = step['to_component']
        msg = step['action_description']
        is_sync = step.get('is_sync', 'Sync')
        
        from_x = participant_x_positions.get(from_comp, margin)
        to_x = participant_x_positions.get(to_comp, margin + 200)
        y = lifeline_start_y + (i + 1) * step_height
        
        # Determine arrow style and color
        is_self_call = from_comp == to_comp
        if is_self_call:
            # Self-call (loop back)
            arrow_style = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor={BNZColors.TEAL};strokeWidth=1.5;fontFamily=Helvetica;"
            # Draw self-referencing arrow
            cells.append(f'''<mxCell id="{next_id()}" value="" style="{arrow_style}" parent="1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{from_x}" y="{y}" as="sourcePoint" />
            <mxPoint x="{from_x + 30}" y="{y + 20}" as="targetPoint" />
            <Array as="points">
              <mxPoint x="{from_x + 40}" y="{y}" />
              <mxPoint x="{from_x + 40}" y="{y + 20}" />
            </Array>
          </mxGeometry>
        </mxCell>''')
        else:
            # Determine direction and color
            going_right = to_x > from_x
            if is_sync == 'Async':
                arrow_color = BNZColors.ORANGE
                arrow_style = "dashed=1;dashPattern=3 3;"
            else:
                arrow_color = BNZColors.TEAL
                arrow_style = ""
            
            # Arrow
            cells.append(f'''<mxCell id="{next_id()}" value="" style="endArrow=classic;html=1;strokeColor={arrow_color};strokeWidth=1.5;{arrow_style}fontFamily=Helvetica;" parent="1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{from_x}" y="{y}" as="sourcePoint" />
            <mxPoint x="{to_x}" y="{y}" as="targetPoint" />
          </mxGeometry>
        </mxCell>''')
        
        # Message label - use sequence_step (1, 2, 3...) not solution_interface_id
        label_x = min(from_x, to_x) + abs(to_x - from_x) // 2
        label_width = max(200, abs(to_x - from_x) - 20)
        seq_num = step['sequence_step']
        label_text = f"{seq_num}. {escape_xml(msg[:50])}" if len(msg) > 50 else f"{seq_num}. {escape_xml(msg)}"
        
        cells.append(f'''<mxCell id="{next_id()}" value="{label_text}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=bottom;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=0;fontColor={BNZColors.DARK_GRAY};fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{label_x - label_width//2}" y="{y - 18}" width="{label_width}" height="15" as="geometry" />
    </mxCell>''')
    
    # Footer
    footer_text = f"Generated from scenario-sequence-steps.csv | {len(steps)} steps | {len(participant_list)} participants"
    cells.append(f'''<mxCell id="{next_id()}" value="{footer_text}" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#666666;fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{margin}" y="{page_height - 30}" width="{page_width - 2*margin}" height="20" as="geometry" />
    </mxCell>''')
    
    # Build complete XML
    uc_name_clean = scenario['use_case_name'].replace(' ', '-').replace('/', '-').replace(',', '')
    xml = f'''<mxfile host="AI Blueprint Generator" agent="Python Script" version="24.0.0">
  <diagram name="Sequence-{scenario['scenario_id']}" id="seq-{uc_id:03d}">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_width}" pageHeight="{page_height}" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    # Save file
    filename = f"../SCN-{uc_id:03d}-{uc_name_clean}-Sequence-v1.0.0.drawio"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml)
    
    print(f"  ✓ Saved: {filename}")


if __name__ == '__main__':
    print("="*60)
    print("BNZ Sequence Diagram Generator")
    print("="*60)
    print()
    
    if len(sys.argv) > 1:
        # Generate for specific use case
        uc_id = int(sys.argv[1])
        if uc_id < 1 or uc_id > 24:
            print("Error: Use case ID must be between 1 and 24")
            sys.exit(1)
        generate_sequence_diagram(uc_id)
    else:
        # Generate for all use cases
        print("No use case ID specified - generating ALL sequence diagrams (1-24)")
        print()
        for uc_id in range(1, 25):
            generate_sequence_diagram(uc_id)
    
    print()
    print("="*60)
    print("✅ Sequence diagram generation complete!")
    print("="*60)

