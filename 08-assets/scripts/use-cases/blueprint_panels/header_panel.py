"""
Header Panel Module
Creates the blueprint header with title and subtitle.
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase, StandardLayout


class HeaderPanel(PanelBase):
    """Header panel with title and subtitle."""
    
    def create(self, data: Dict, position: Position = None) -> List[str]:
        """
        Create header panel.
        
        Args:
            data: Dictionary with keys:
                - use_case_id: int
                - use_case_name: str
                - subtitle: str (optional, defaults to improved_description)
                - improved_description: str (fallback for subtitle)
            position: Position (ignored, header uses full width)
            
        Returns:
            List of XML cell strings
        """
        uc_id = data['use_case_id']
        uc_name = data['use_case_name']
        subtitle = data.get('subtitle') or data.get('improved_description', '')[:80]
        
        # Background - full page
        self.add_cell(self.builder.rectangle(
            0, 0, StandardLayout.PAGE_WIDTH, StandardLayout.PAGE_HEIGHT,
            BNZColors.GRAY, "none", stroke_width=0, rounded=False
        ))
        
        # Header background
        self.add_cell(self.builder.rectangle(
            0, 0, StandardLayout.PAGE_WIDTH, StandardLayout.HEADER_HEIGHT,
            BNZColors.NAVY, "none", stroke_width=0, rounded=False
        ))
        
        # Title
        self.add_cell(self.builder.text(
            30, 20, 900, 40,
            f"Use Case Blueprint: UC-{uc_id:03d} {uc_name}",
            font_size=28, font_style=1, font_color=BNZColors.WHITE
        ))
        
        # Subtitle (right-aligned)
        if subtitle:
            self.add_cell(self.builder.text(
                1520, 25, 370, 30,
                subtitle,
                font_size=16, font_color=BNZColors.WHITE, align="right"
            ))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict) -> List[str]:
    """
    Convenience function to create header panel.
    
    Args:
        builder: XMLCellBuilder instance
        data: Header data dictionary
        
    Returns:
        List of XML cell strings
    """
    panel = HeaderPanel(builder)
    return panel.create(data)

