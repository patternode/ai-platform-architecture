"""
Summary Panel Module
Creates the use case summary panel with badges and description.
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class SummaryPanel(PanelBase):
    """Summary panel with use case overview."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        """
        Create summary panel.
        
        Args:
            data: Dictionary with keys:
                - use_case_id: int
                - category: str
                - value: str (High/Medium/Low)
                - ai_type: str
                - description: str
                - benefits: str
            position: Panel position and dimensions
            
        Returns:
            List of XML cell strings
        """
        x, y, w, h = position.x, position.y, position.width, position.height
        
        uc_id = int(data['use_case_id'])
        category = data.get('category', 'General')[:30]
        value = data.get('value', 'Medium')
        ai_type = data.get('ai_type', 'AI/ML')[:20]
        description = data.get('description', '')[:300]
        benefits = data.get('benefits', '')[:400]
        
        # Panel background
        self.add_cell(self.builder.rectangle(
            x, y, w, h, BNZColors.WHITE, BNZColors.NAVY, stroke_width=2
        ))
        
        # Header
        self.add_cell(self.builder.text(
            x+20, y+15, w-40, 30, "Use Case Summary",
            font_size=18, font_style=1, font_color=BNZColors.NAVY
        ))
        
        # Badge row
        badge_y = y + 55
        
        # ID Badge
        self.add_cell(self.builder.text(
            x+20, badge_y, 120, 25, f"ID: UC-{uc_id:03d}",
            font_size=12, font_style=1, bg_color=BNZColors.BLUE_BOX,
            font_color=BNZColors.DARK_GRAY, align="left"
        ))
        
        # Category Badge
        self.add_cell(self.builder.text(
            x+155, badge_y, 200, 25, f"Category: {category}",
            font_size=12, font_style=1, bg_color=BNZColors.BLUE_BOX,
            font_color=BNZColors.DARK_GRAY, align="left"
        ))
        
        # Value Badge
        self.add_cell(self.builder.text(
            x+370, badge_y, 100, 25, f"Value: {value}",
            font_size=12, font_style=1, bg_color=BNZColors.LIGHT_TEAL,
            font_color=BNZColors.TEAL, align="left"
        ))
        
        # AI Type Badge
        self.add_cell(self.builder.text(
            x+485, badge_y, 75, 25, ai_type,
            font_size=10, font_style=1, bg_color=BNZColors.LIGHT_ORANGE,
            border_color=BNZColors.ORANGE, font_color=BNZColors.ORANGE,
            align="center"
        ))
        
        # Description
        self.add_cell(self.builder.text(
            x+20, y+90, w-40, 20, "Description:",
            font_size=12, font_style=1
        ))
        
        self.add_cell(self.builder.text(
            x+20, y+110, w-40, 50, description,
            font_size=11, font_color=BNZColors.DARK_GRAY, v_align="top"
        ))
        
        # Benefits
        self.add_cell(self.builder.text(
            x+20, y+165, w-40, 20, "Anticipated Benefits:",
            font_size=12, font_style=1
        ))
        
        # Format benefits as bullet points if not already
        if benefits and not benefits.startswith('•'):
            benefit_parts = [b.strip() for b in benefits.split(';') if b.strip()]
            benefits = '\n'.join([f"• {b}" for b in benefit_parts[:5]])
        
        self.add_cell(self.builder.text(
            x+20, y+185, w-40, h-205, benefits,
            font_size=11, font_color=BNZColors.DARK_GRAY, v_align="top"
        ))
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    """
    Convenience function to create summary panel.
    
    Args:
        builder: XMLCellBuilder instance
        data: Summary data dictionary
        position: Panel position
        
    Returns:
        List of XML cell strings
    """
    panel = SummaryPanel(builder)
    return panel.create(data, position)

