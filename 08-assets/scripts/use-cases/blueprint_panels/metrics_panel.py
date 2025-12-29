"""
Metrics & Dependencies Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class MetricsPanel(PanelBase):
    """Metrics and dependencies panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.NAVY, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+15, y+15, w-30, 25,
                                       "Key Metrics & Dependencies",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.NAVY))
        
        # Content
        platform = data.get('platform', '')[:40]
        data_sources = data.get('data_sources', '')[:40]
        ai_type = data.get('ai_type', '')[:30]
        deployment = data.get('deployment', '')[:30]
        users = data.get('estimated_users', '')
        
        content = f"""<b>Platform:</b> {platform}
<b>Data:</b> {data_sources}
<b>AI:</b> {ai_type}
<b>Deployment:</b> {deployment}
<b>Users:</b> {users}"""
        
        self.add_cell(self.builder.text(x+15, y+45, w-30, h-60, content,
                                       font_size=10, font_color=BNZColors.DARK_GRAY,
                                       v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = MetricsPanel(builder)
    return panel.create(data, position)
