"""
Interface Catalogue Panel Module
From generate_uc_diagram.py
"""

from typing import Dict, List
from .base import XMLCellBuilder, BNZColors, Position, PanelBase


class InterfacesPanel(PanelBase):
    """Interface catalogue panel."""
    
    def create(self, data: Dict, position: Position) -> List[str]:
        x, y, w, h = position.x, position.y, position.width, position.height
        interfaces = data['interfaces']
        
        # Panel background
        self.add_cell(self.builder.rectangle(x, y, w, h, BNZColors.WHITE,
                                            BNZColors.TEAL, stroke_width=2))
        
        # Header
        self.add_cell(self.builder.text(x+20, y+15, w-40, 30, "Interface Catalogue",
                                       font_size=18, font_style=1,
                                       font_color=BNZColors.TEAL))
        
        # Table header
        header_y = y + 55
        self.add_cell(self.builder.rectangle(x+20, header_y, w-40, 25,
                                            "#6699CC", BNZColors.TEAL))
        
        # Column headers
        col_widths = [30, 120, 120, 360, 310]
        col_x = x + 20
        headers = ["ID", "From", "To", "Description", "Datasets"]
        
        for header, col_w in zip(headers, col_widths):
            self.add_cell(self.builder.text(col_x+3, header_y+3, col_w-6, 20, header,
                                           font_size=10, font_style=1,
                                           font_color=BNZColors.DARK_GRAY, align="left"))
            col_x += col_w
        
        # Table rows
        row_y = header_y + 25
        row_height = 26
        
        for interface in interfaces[:25]:  # Limit to 25 rows
            col_x = x + 20
            
            # ID
            solution_iface_id = interface.get('solution_interface_id', interface.get('interface_id', ''))
            self.add_cell(self.builder.text(col_x+3, row_y, col_widths[0]-6, row_height,
                                           str(solution_iface_id), font_size=10,
                                           font_color=BNZColors.DARK_GRAY, v_align="top"))
            col_x += col_widths[0]
            
            # From
            source = interface.get('source_abb_name', '')[:18]
            self.add_cell(self.builder.text(col_x+3, row_y, col_widths[1]-6, row_height,
                                           source, font_size=10,
                                           font_color=BNZColors.DARK_GRAY, v_align="top"))
            col_x += col_widths[1]
            
            # To
            target = interface.get('target_abb_name', '')[:18]
            self.add_cell(self.builder.text(col_x+3, row_y, col_widths[2]-6, row_height,
                                           target, font_size=10,
                                           font_color=BNZColors.DARK_GRAY, v_align="top"))
            col_x += col_widths[2]
            
            # Description
            description = interface.get('interface_description', '')
            self.add_cell(self.builder.text(col_x+3, row_y, col_widths[3]-6, row_height,
                                           description, font_size=10,
                                           font_color=BNZColors.DARK_GRAY, v_align="top"))
            col_x += col_widths[3]
            
            # Datasets
            datasets = interface.get('datasets_exchanged', '')
            self.add_cell(self.builder.text(col_x+3, row_y, col_widths[4]-6, row_height,
                                           datasets, font_size=10,
                                           font_color=BNZColors.DARK_GRAY, v_align="top"))
            
            row_y += row_height
        
        return self.get_cells()


def create(builder: XMLCellBuilder, data: Dict, position: Position) -> List[str]:
    panel = InterfacesPanel(builder)
    return panel.create(data, position)
