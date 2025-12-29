"""
Governance & Compliance Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class GovernancePanel(PanelBase):
    """Governance and compliance panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.PURPLE, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+15, y+15, w-30, 25,
                                       "Governance & Compliance",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.PURPLE))
        
        # Content
        content = f"""<b>Data Residency:</b> {data.get('data_residency', '')[:40]}
<b>Privacy:</b> {data.get('privacy_compliance', '')[:40]}
<b>Model Governance:</b> {data.get('model_governance', '')[:35]}
<b>Audit:</b> {data.get('audit_requirements', '')[:30]}
<b>Security:</b> {data.get('security_requirements', '')[:40]}
<b>Explainability:</b> {data.get('explainability', '')[:30]}"""
        
        self.add_cell(self.builder.text(x+15, y+45, w-30, h-60, content,
                                       font_size=10, font_color=BNZColors.DARK_GRAY,
                                       v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = GovernancePanel(builder)
    return panel.create(data, position)
