"""
Costing & Prioritization Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class CostingPanel(PanelBase):
    """Costing and prioritization panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        cost = data.get('estimated_cost', '$500K')
        timeline = data.get('timeline', '6-9 months')
        complexity = data.get('complexity', 'Medium')
        priority = data.get('priority_score', '50/100')
        wsjf_bv = data.get('wsjf_business_value', '6')
        wsjf_tc = data.get('wsjf_time_criticality', '5')
        wsjf_rr = data.get('wsjf_risk_reduction', '4')
        wsjf_js = data.get('wsjf_job_size', '8')
        wsjf_score = data.get('wsjf_score', '1.88')
        cost_breakdown = data.get('cost_breakdown', 'Infrastructure 30% | Licensing 35% | Development 25% | Change Mgmt 10%')
        stakeholders = data.get('stakeholders', 'Enterprise Architecture')
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.GRAY,
                                            BNZColors.LIGHT_GRAY_2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+10, w-40, 25, "Costing & Prioritization",
                                       font_size=14, font_style=1,
                                       font_color=BNZColors.NAVY))
        
        current_y = y + 40
        
        # Cost fields
        fields = [
            ("Estimated Cost:", cost, BNZColors.RED),
            ("Timeline:", timeline, BNZColors.DARK_GRAY),
            ("Complexity:", complexity, BNZColors.ORANGE if complexity == 'High' else BNZColors.DARK_GRAY),
            ("Priority Score:", priority, BNZColors.TEAL),
        ]
        
        for label, value, color in fields:
            self.add_cell(self.builder.text(x+20, current_y, 120, 18, label,
                                           font_size=10, font_style=1))
            self.add_cell(self.builder.text(x+150, current_y, w-170, 18, value,
                                           font_size=10, font_color=color,
                                           font_style=1, align="right"))
            current_y += 23
        
        # Cost breakdown
        self.add_cell(self.builder.rectangle(x+20, current_y, w-40, 20, BNZColors.YELLOW, "none"))
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, cost_breakdown,
                                       font_size=8, align="left"))
        current_y += 25
        
        # Dependencies
        self.add_cell(self.builder.text(x+20, current_y, w-40, 18, "Key Dependencies:",
                                       font_size=10, font_style=1))
        current_y += 20
        deps_text = "• Cloud infrastructure & licensing\n• Data quality & availability\n• System integration readiness\n• Skilled resources"
        self.add_cell(self.builder.text(x+20, current_y, w-40, 55, deps_text,
                                       font_size=9, v_align="top"))
        current_y += 60
        
        # WSJF
        self.add_cell(self.builder.text(x+20, current_y, 120, 18, "WSJF Score:",
                                       font_size=10, font_style=1))
        wsjf_text = f"BV: {wsjf_bv} | TC: {wsjf_tc} | RR: {wsjf_rr} | JS: {wsjf_js} -> {wsjf_score}"
        self.add_cell(self.builder.text(x+150, current_y, w-170, 22, wsjf_text,
                                       font_size=8, align="right", v_align="top"))
        current_y += 25
        
        # Stakeholders
        self.add_cell(self.builder.text(x+20, current_y, 120, 18, "Stakeholders:",
                                       font_size=10, font_style=1))
        self.add_cell(self.builder.text(x+150, current_y, w-170, 18, f"Owner: {stakeholders[:30]}",
                                       font_size=8, font_color=BNZColors.DARK_GRAY,
                                       align="right"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = CostingPanel(builder)
    return panel.create(data, position)

