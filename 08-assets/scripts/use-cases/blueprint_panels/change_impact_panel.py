"""
Change Impact & Readiness Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class ChangeImpactPanel(PanelBase):
    """Change impact and readiness panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        complexity = data.get('complexity', 'Medium')
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.ORANGE, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+15, y+15, w-30, 25,
                                       "Change Impact & Readiness",
                                       font_size=14, font_style=1,
                                       font_color=BNZColors.ORANGE))
        
        # Content based on complexity
        if complexity == 'High':
            org_impact = 'High - Significant role transformation'
            training = '40+ hrs per user'
            resistance = 'Medium - Pilot essential'
        elif complexity == 'Medium':
            org_impact = 'Medium - Process changes'
            training = '20-30 hrs per user'
            resistance = 'Low-Medium - Change mgmt needed'
        else:
            org_impact = 'Low - Minimal changes'
            training = '10-15 hrs per user'
            resistance = 'Low - Incremental adoption'
        
        content = f"""<b>Organizational Impact:</b> {org_impact}
<b>Training:</b> {training}
<b>User Resistance Risk:</b> {resistance}

<b>Technical Readiness:</b> Medium
• Data quality improvement needed
• System upgrades may be required"""
        
        self.add_cell(self.builder.text(x+15, y+45, w-30, h-60, content,
                                       font_size=9, font_color=BNZColors.DARK_GRAY,
                                       v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = ChangeImpactPanel(builder)
    return panel.create(data, position)
