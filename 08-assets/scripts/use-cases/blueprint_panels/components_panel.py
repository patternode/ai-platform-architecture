"""
Components Panel Module - Solution Architecture
From generate_uc_diagram.py
"""

from typing import Dict, List
from collections import defaultdict
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, escape_xml


def get_layer_color(layer_name: str) -> tuple:
    """Get background and stroke color for a layer."""
    layer_lower = layer_name.lower()
    if 'presentation' in layer_lower:
        return "#6699CC", BNZColors.NAVY
    elif 'ai' in layer_lower or 'ml' in layer_lower:
        return "#FFB399", BNZColors.ORANGE
    elif 'data' in layer_lower or 'knowledge' in layer_lower:
        return "#E6F7ED", BNZColors.TEAL
    elif 'integration' in layer_lower:
        return "#FFF4E6", BNZColors.ORANGE
    elif 'application' in layer_lower:
        return "#F3E5F5", "#9C27B0"
    else:
        return BNZColors.GRAY, BNZColors.DARK_GRAY


class ComponentsPanel(PanelBase):
    """Solution architecture panel with ABBs organized by layer."""
    
    def __init__(self, builder: XMLCellBuilder):
        super().__init__(builder)
        self.abb_positions = {}
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        abbs = data['abbs']
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.NAVY, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 30,
                                       "Solution Architecture - ABBs",
                                       font_size=18, font_style=1,
                                       font_color=BNZColors.NAVY))
        
        # Group ABBs by layer
        layers = defaultdict(list)
        for abb in abbs:
            layers[abb['architecture_layer']].append(abb)
        
        # Layer order (top to bottom)
        layer_order = [
            'Presentation Layer',
            'Application Services Layer',
            'AI/ML Services Layer',
            'Data & Knowledge Layer',
            'Integration Layer'
        ]
        
        current_y = y + 60
        layer_height = 110
        abb_width = 140
        abb_height = 45
        abb_spacing = 15
        
        for layer_name in layer_order:
            layer_abbs = layers.get(layer_name, [])
            if not layer_abbs:
                continue
            
            # Layer background
            bg_color, stroke_color = get_layer_color(layer_name)
            self.add_cell(self.builder.rectangle(x+20, current_y, w-40, layer_height,
                                                bg_color, stroke_color,
                                                stroke_width=1, dashed=True))
            
            # Layer label
            self.add_cell(self.builder.text(x+30, current_y+5, 200, 20,
                                           layer_name, font_size=10, font_style=1,
                                           font_color=stroke_color))
            
            # ABB boxes
            abbs_per_row = (w - 60) // (abb_width + abb_spacing)
            for idx, abb in enumerate(layer_abbs):
                row = idx // abbs_per_row
                col = idx % abbs_per_row
                
                abb_x = x + 30 + col * (abb_width + abb_spacing)
                abb_y = current_y + 30 + row * (abb_height + 10)
                
                abb_id = str(abb['abb_id'])
                cell_id = f"abb-{abb_id}"
                
                # Store position
                self.abb_positions[abb_id] = {
                    'x': abb_x, 'y': abb_y,
                    'width': abb_width, 'height': abb_height,
                    'center_x': abb_x + abb_width // 2,
                    'center_y': abb_y + abb_height // 2
                }
                
                # ABB box
                box_xml = f'''<mxCell id="{cell_id}" value="{escape_xml(abb['abb_name'])}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={BNZColors.WHITE};strokeColor={stroke_color};strokeWidth=2;fontSize=10;fontStyle=1;fontColor={BNZColors.DARK_GRAY};fontFamily=Helvetica;align=center;verticalAlign=middle;" parent="1" vertex="1">
          <mxGeometry x="{abb_x}" y="{abb_y}" width="{abb_width}" height="{abb_height}" as="geometry" />
        </mxCell>'''
                self.cells.append(box_xml)
            
            current_y += layer_height + 15
        
        return self.get_cells()
    
    def get_abb_positions(self) -> Dict:
        return self.abb_positions


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> Dict:
    panel = ComponentsPanel(builder)
    cells = panel.create(data, position)
    return {
        'cells': cells,
        'abb_positions': panel.get_abb_positions()
    }

