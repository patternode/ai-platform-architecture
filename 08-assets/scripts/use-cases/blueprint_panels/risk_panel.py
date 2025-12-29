"""
Risk Assessment Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, parse_list_data


class RiskPanel(PanelBase):
    """Risk assessment panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        tech_risks = data.get('technical_risks', '')
        bus_risks = data.get('business_risks', '')
        mitigations = data.get('key_mitigations', '')
        
        # Parse into bullet lists
        tech_list = parse_list_data(tech_risks, '|', 4)
        bus_list = parse_list_data(bus_risks, '|', 4)
        mit_list = parse_list_data(mitigations, '|', 3)
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.RED, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+6, w-40, 25, "Risk Assessment",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.RED))
        
        current_y = y + 36
        
        # Technical Risks
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Technical Risks:",
                                       font_size=11, font_style=1))
        tech_text = '\n'.join([f"• {r}" for r in tech_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 45, tech_text,
                                       font_size=9, v_align="top"))
        current_y += 70
        
        # Business Risks
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Business Risks:",
                                       font_size=11, font_style=1))
        bus_text = '\n'.join([f"• {r}" for r in bus_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 45, bus_text,
                                       font_size=9, v_align="top"))
        current_y += 70
        
        # Mitigations
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Key Mitigations:",
                                       font_size=11, font_style=1))
        mit_text = '\n'.join([f"• {m}" for m in mit_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 35, mit_text,
                                       font_size=9, v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = RiskPanel(builder)
    return panel.create(data, position)

