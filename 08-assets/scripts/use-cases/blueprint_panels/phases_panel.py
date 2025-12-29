"""
Implementation Roadmap/Phases Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, parse_list_data


class PhasesPanel(PanelBase):
    """Implementation roadmap with phases."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        phases = data['phases']
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.ORANGE, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 25, "Implementation Roadmap",
                                       font_size=16, font_style=1,
                                       font_color=BNZColors.ORANGE))
        
        # Phase boxes in grid layout
        phase_count = len(phases)
        box_width = 180
        box_height = 85
        spacing = 15
        
        start_y = y + 50
        
        if phase_count <= 2:
            # Single row
            for i, phase in enumerate(phases):
                box_x = x + 20 + i * (box_width + spacing)
                self._create_phase_box(phase, box_x, start_y, box_width, box_height)
        elif phase_count == 3:
            # 2 on top, 1 on bottom
            self._create_phase_box(phases[0], x+20, start_y, box_width, box_height)
            self._create_phase_box(phases[1], x+20+box_width+spacing, start_y, box_width, box_height)
            self._create_phase_box(phases[2], x+20, start_y+box_height+spacing, box_width, box_height)
        else:
            # 2x2 grid
            for i in range(min(4, phase_count)):
                row = i // 2
                col = i % 2
                box_x = x + 20 + col * (box_width + spacing)
                box_y = start_y + row * (box_height + spacing)
                self._create_phase_box(phases[i], box_x, box_y, box_width, box_height)
        
        return self.get_cells()
    
    def _create_phase_box(self, phase: Dict, x: int, y: int, w: int, h: int):
        """Create a single phase box."""
        phase_num = int(phase.get('phase_number', phase.get('phase_id', 1)))
        phase_name = phase.get('phase_name', 'Phase')
        timeline = phase.get('timeline', '')
        activities = phase.get('key_activities', '')
        
        # Box background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.BLUE_BOX,
                                            BNZColors.NAVY, stroke_width=1))
        
        # Title
        self.add_cell(self.builder.text(x+10, y+5, w-20, 20,
                                       f"Phase {phase_num}: {phase_name}",
                                       font_size=11, font_style=1,
                                       font_color=BNZColors.NAVY, v_align="top"))
        
        # Timeline badge
        self.add_cell(self.builder.rectangle(x+10, y+25, 70, 15,
                                            BNZColors.NAVY, BNZColors.NAVY))
        self.add_cell(self.builder.text(x+10, y+25, 70, 15, timeline,
                                       font_size=8, font_style=1,
                                       font_color=BNZColors.WHITE, align="center"))
        
        # Activities
        activity_list = parse_list_data(activities, '|', 4)
        activities_text = '\n'.join([f"• {a}" for a in activity_list])
        self.add_cell(self.builder.text(x+10, y+45, w-20, 35, activities_text,
                                       font_size=8, v_align="top"))


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = PhasesPanel(builder)
    return panel.create(data, position)

