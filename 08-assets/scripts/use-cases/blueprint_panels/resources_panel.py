"""
Resource Requirements Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, parse_list_data


class ResourcesPanel(PanelBase):
    """Resource requirements panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        
        team_comp = data.get('team_composition', '')
        skills = data.get('critical_skills', '')
        
        # Parse team composition
        team_list = parse_list_data(team_comp, '|', 9)
        team_formatted = []
        for t in team_list:
            if ':' in t:
                role, fte = t.split(':', 1)
                team_formatted.append(f"<b>{role.strip()}:</b> {fte.strip()}")
            else:
                team_formatted.append(t)
        
        # Parse skills
        skill_list = parse_list_data(skills, '|', 6)
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.PURPLE, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 25, "Resource Requirements",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.PURPLE))
        
        current_y = y + 45
        
        # Core Team
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Core Team (FTE):",
                                       font_size=11, font_style=1))
        team_text = '\n'.join(team_formatted)
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 105, team_text,
                                       font_size=9, v_align="top"))
        current_y += 130
        
        # Critical Skills
        self.add_cell(self.builder.text(x+20, current_y, w-40, 20, "Critical Skills:",
                                       font_size=11, font_style=1))
        skills_text = '\n'.join([f"• {s}" for s in skill_list])
        self.add_cell(self.builder.text(x+20, current_y+20, w-40, 70, skills_text,
                                       font_size=9, v_align="top"))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = ResourcesPanel(builder)
    return panel.create(data, position)

