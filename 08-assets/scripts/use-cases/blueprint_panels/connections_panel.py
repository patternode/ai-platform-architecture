"""
Connections Panel Module
From generate_uc_diagram.py
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors


def calculate_edge_connection_points(source_pos: Dict, target_pos: Dict) -> tuple:
    """Calculate edge connection points. Returns (exit_x, exit_y, entry_x, entry_y)."""
    dx = target_pos['center_x'] - source_pos['center_x']
    dy = target_pos['center_y'] - source_pos['center_y']
    
    if abs(dx) > abs(dy):
        if dx > 0:
            return 1.0, 0.5, 0.0, 0.5
        else:
            return 0.0, 0.5, 1.0, 0.5
    else:
        if dy > 0:
            return 0.5, 1.0, 0.5, 0.0
        else:
            return 0.5, 0.0, 0.5, 1.0


def create(builder: XMLCellBuilder, data: Dict, abb_positions: Dict) -> List[str]:
    """Create connection lines between ABBs."""
    cells = []
    interfaces = data['interfaces']
    
    for interface in interfaces:
        source_id = str(interface.get('source_abb_id'))
        target_id = str(interface.get('target_abb_id'))
        
        if source_id not in abb_positions or target_id not in abb_positions:
            continue
        
        source_pos = abb_positions[source_id]
        target_pos = abb_positions[target_id]
        
        # Determine arrow color
        source_layer = interface.get('source_layer', '')
        if 'AI' in source_layer or 'ML' in source_layer:
            arrow_color = BNZColors.ORANGE
        elif 'Data' in source_layer or 'Knowledge' in source_layer:
            arrow_color = BNZColors.TEAL
        elif 'Integration' in source_layer:
            arrow_color = BNZColors.ORANGE
        else:
            arrow_color = BNZColors.NAVY
        
        # Calculate connection points
        exit_x, exit_y, entry_x, entry_y = calculate_edge_connection_points(source_pos, target_pos)
        
        # Label
        label = interface.get('solution_interface_id', '')
        
        # Create arrow
        cell_id = builder.next_id()
        label_id = builder.next_id()
        
        arrow_xml = f'''<mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;strokeColor={arrow_color};strokeWidth=1.5;fontFamily=Helvetica;curved=1;exitX={exit_x};exitY={exit_y};exitDx=0;exitDy=0;entryX={entry_x};entryY={entry_y};entryDx=0;entryDy=0;exitPerimeter=0;entryPerimeter=0;" parent="1" source="abb-{source_id}" target="abb-{target_id}" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{source_pos['x']}" y="{source_pos['y']}" as="sourcePoint" />
            <mxPoint x="{target_pos['x']}" y="{target_pos['y']}" as="targetPoint" />
          </mxGeometry>
        </mxCell>'''
        
        if label:
            label_xml = f'''<mxCell id="{label_id}" value="{label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=7;fontStyle=1;backgroundColor=#FFFFFF;borderColor={arrow_color};fontFamily=Helvetica;" parent="{cell_id}" vertex="1" connectable="0">
            <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
              <mxPoint as="offset" />
            </mxGeometry>
          </mxCell>'''
            cells.append(arrow_xml + label_xml)
        else:
            cells.append(arrow_xml)
    
    return cells
