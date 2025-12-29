"""
Info Boxes Panel Module
Creates small info boxes: External Systems, Data Volume, Performance, Legend
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, parse_list_data


class InfoBoxesPanel(PanelBase):
    """Small info boxes panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        """
        Create info boxes.
        
        Args:
            data: Dictionary with keys:
                - external_systems: str
                - data_volume_metrics: str
                - performance_targets: str
            position: Base position (x, y) - boxes are positioned relative to this
            
        Returns:
            List of XML cell strings
        """
        y = position.y  # All boxes at same Y
        
        # External Systems Box
        ext_systems = parse_list_data(data.get('external_systems', ''), '|', 4)
        systems_text = '\n'.join([f"• {s}" for s in ext_systems])
        
        self.add_cell(self.builder.rectangle(1050, y, 130, 55, BNZColors.YELLOW,
                                            "#FFA000", stroke_width=1))
        self.add_cell(self.builder.text(1058, y+3, 114, 12, "External Systems",
                                       font_size=9, font_style=1))
        self.add_cell(self.builder.text(1058, y+18, 114, 35, systems_text,
                                       font_size=8, v_align="top"))
        
        # Data Volume Box
        vol_metrics = parse_list_data(data.get('data_volume_metrics', ''), '|', 4)
        vol_text = '\n'.join([f"• {v}" for v in vol_metrics])
        
        self.add_cell(self.builder.rectangle(1200, y, 110, 55, "#E1F5FE",
                                            "#0288D1", stroke_width=1))
        self.add_cell(self.builder.text(1208, y+3, 94, 12, "Data Volume",
                                       font_size=9, font_style=1))
        self.add_cell(self.builder.text(1208, y+18, 94, 35, vol_text,
                                       font_size=7, v_align="top"))
        
        # Performance Box
        perf_targets = parse_list_data(data.get('performance_targets', ''), '|', 4)
        perf_text = '\n'.join([f"• {p}" for p in perf_targets])
        
        self.add_cell(self.builder.rectangle(1320, y, 120, 55, BNZColors.LIGHT_PURPLE,
                                            BNZColors.PURPLE, stroke_width=1))
        self.add_cell(self.builder.text(1328, y+3, 104, 12, "Performance Targets",
                                       font_size=9, font_style=1))
        self.add_cell(self.builder.text(1328, y+18, 104, 35, perf_text,
                                       font_size=7, v_align="top"))
        
        # Legend Box
        self.add_cell(self.builder.rectangle(850, y, 180, 55, BNZColors.WHITE,
                                            BNZColors.LIGHT_GRAY_2, stroke_width=1, dashed=True))
        self.add_cell(self.builder.text(858, y+3, 164, 12, "Legend",
                                       font_size=9, font_style=1))
        
        legend_lines = [
            "Presentation    Data Sources",
            "AI Services       Bidirectional",
            "Data & Knowledge  Unidirectional"
        ]
        legend_text = '\n'.join(legend_lines)
        self.add_cell(self.builder.text(858, y+18, 164, 35, legend_text,
                                       font_size=8))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = InfoBoxesPanel(builder)
    return panel.create(data, position)

