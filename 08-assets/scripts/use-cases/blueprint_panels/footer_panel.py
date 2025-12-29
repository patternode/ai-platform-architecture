"""
Footer Panel Module
"""

from typing import Dict, List
from .base import XMLCellBuilder, Position


class FooterPanel:
    """Document footer panel."""
    
    def __init__(self, builder: XMLCellBuilder):
        self.builder = builder
    
    def create(self, data: Dict) -> str:
        """
        Create footer.
        
        Args:
            data: Dictionary with 'enterprise_architect' key
            
        Returns:
            XML cell string
        """
        ea = data.get('enterprise_architect', 'Enterprise Architecture').replace('\n', ' ')
        footer_text = f"Blueprint Version: 1.0.0 | Created: Dec 2024 | Classification: Internal | Owner: {ea} | Compliant with BNZ Visual Design Standards v2.0"
        
        return self.builder.text(30, 1055, 1860, 20, footer_text,
                                font_size=9, font_color="#666666",
                                align="center")


def create(builder: XMLCellBuilder, data: Dict) -> str:
    panel = FooterPanel(builder)
    return panel.create(data)

