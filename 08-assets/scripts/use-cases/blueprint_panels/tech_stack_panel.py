"""
Technical Stack Panel Module - Components & Technologies
From generate_uc_diagram.py
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class TechStackPanel(PanelBase):
    """Components & technologies panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        abbs = data['abbs']
        all_abbs = data['all_abbs']
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.ORANGE, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 30, "Components & Technologies",
                                       font_size=18, font_style=1,
                                       font_color=BNZColors.ORANGE))
        
        # Build component list
        component_entries = []
        seen_components = set()
        
        for abb in abbs:
            comp_name = abb.get('component_name', '')
            if not comp_name or comp_name in seen_components:
                continue
            seen_components.add(comp_name)
            
            # Get description
            description = abb.get('role_in_solution', '')
            
            # Find technologies
            technologies = []
            for full_abb in all_abbs:
                if (full_abb['name'] == abb['abb_name'] or 
                    full_abb['component name'] == comp_name):
                    sbbs = full_abb.get('candidate SBBs', '')
                    if sbbs:
                        for sbb in sbbs.split(',')[:3]:
                            sbb = sbb.strip()
                            if sbb and len(sbb) > 2 and sbb not in technologies:
                                technologies.append(sbb)
                    break
            
            tech_str = ', '.join(technologies[:4]) if technologies else 'Various technologies'
            
            component_entries.append({
                'name': comp_name,
                'description': description,
                'technologies': tech_str
            })
        
        # Display components
        current_y = y + 55
        row_height = 55
        
        for comp in component_entries[:12]:
            comp_text = f"<b>{comp['name']}</b> - {comp['description']}. <font color=\"{BNZColors.ORANGE}\"><i>{comp['technologies']}</i></font>."
            
            self.add_cell(self.builder.text(x+20, current_y, w-40, row_height-5,
                                           comp_text, font_size=10,
                                           font_color=BNZColors.DARK_GRAY,
                                           align="left", v_align="top"))
            
            current_y += row_height
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = TechStackPanel(builder)
    return panel.create(data, position)
