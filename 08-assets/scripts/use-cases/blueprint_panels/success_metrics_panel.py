"""
Success Metrics & KPIs Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, parse_list_data


class SuccessMetricsPanel(PanelBase):
    """Success metrics and KPIs panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        bus_metrics = data.get('business_metrics', '')
        tech_metrics = data.get('technical_metrics', '')
        
        # Parse into bullet lists
        bus_list = parse_list_data(bus_metrics, '|', 5)
        tech_list = parse_list_data(tech_metrics, '|', 5)
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.TEAL, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 25, "Success Metrics & KPIs",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.TEAL))
        
        current_y = y + 45
        
        # Business Metrics
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Business Metrics:",
                                       font_size=11, font_style=1))
        bus_text = '\n'.join([f"• {m}" for m in bus_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 55, bus_text,
                                       font_size=9, v_align="top"))
        current_y += 80
        
        # Technical Metrics
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Technical Metrics:",
                                       font_size=11, font_style=1))
        tech_text = '\n'.join([f"• {m}" for m in tech_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 55, tech_text,
                                       font_size=9, v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = SuccessMetricsPanel(builder)
    return panel.create(data, position)

