"""
Decision Factors Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class DecisionPanel(PanelBase):
    """Decision factors panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        overall_risk = data.get('overall_risk', 'Medium')
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.TEAL, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+15, y+15, w-30, 25,
                                       "Decision Factors",
                                       font_size=14, font_style=1,
                                       font_color=BNZColors.TEAL))
        
        # Strengths
        strengths = """<b>Strengths (Go):</b>
• Business value identified
• Technology available
• Clear success metrics
• Stakeholder support"""
        
        self.add_cell(self.builder.text(x+15, y+45, w-30, 45, strengths,
                                       font_size=9, font_color=BNZColors.DARK_GRAY,
                                       v_align="top"))
        
        # Concerns
        concerns = f"""<b>Concerns (Mitigate):</b>
• Risk level: {overall_risk}
• Data dependencies
• Change management
• Regulatory considerations"""
        
        self.add_cell(self.builder.text(x+15, y+95, w-30, 45, concerns,
                                       font_size=9, font_color=BNZColors.DARK_GRAY,
                                       v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = DecisionPanel(builder)
    return panel.create(data, position)
