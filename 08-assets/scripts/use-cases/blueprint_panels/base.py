"""
Base module for blueprint panel system.
Provides shared utilities, colors, and XML building functions.
"""

from typing import Dict, List, Tuple


# BNZ Visual Design Standards v2.0
class BNZColors:
    """BNZ brand colors and design system."""
    NAVY = "#003087"
    ORANGE = "#FF6B35"
    TEAL = "#00A651"
    PURPLE = "#9C27B0"
    WHITE = "#FFFFFF"
    LIGHT_BLUE = "#E6F0FA"
    LIGHT_ORANGE = "#FFE5DC"
    LIGHT_TEAL = "#E6F7ED"
    LIGHT_PURPLE = "#F3E5F5"
    GRAY = "#F5F5F5"
    DARK_GRAY = "#333333"
    LIGHT_GRAY_2 = "#CCCCCC"
    BLUE_BOX = "#6699CC"
    YELLOW = "#FFFDE7"
    RED = "#CC0000"


class Position:
    """Helper class for positioning."""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = x + width // 2
        self.center_y = y + height // 2
    
    def __repr__(self):
        return f"Position({self.x}, {self.y}, {self.width}x{self.height})"


def escape_xml(text: str) -> str:
    """
    Escape special characters for XML.
    
    Args:
        text: Text to escape
        
    Returns:
        XML-safe string
    """
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
            .replace("\n", "&#xa;"))


class XMLCellBuilder:
    """Builder for creating draw.io XML cells."""
    
    def __init__(self):
        self.cell_id_counter = 1000
    
    def next_id(self) -> str:
        """Generate next unique cell ID."""
        self.cell_id_counter += 1
        return f"cell-{self.cell_id_counter}"
    
    def rectangle(self, x: int, y: int, width: int, height: int,
                 fill_color: str, stroke_color: str, stroke_width: int = 1,
                 rounded: bool = True, dashed: bool = False, arc_size: int = 10,
                 cell_id: str = None) -> str:
        """
        Create a rectangle cell.
        
        Args:
            x, y: Position
            width, height: Dimensions
            fill_color: Fill color (hex or 'none')
            stroke_color: Border color (hex or 'none')
            stroke_width: Border width in pixels
            rounded: Whether corners are rounded
            dashed: Whether border is dashed
            arc_size: Corner radius if rounded
            cell_id: Optional custom cell ID
            
        Returns:
            XML string for the cell
        """
        cell_id = cell_id or self.next_id()
        
        style_parts = [
            "rounded=1" if rounded else "rounded=0",
            "whiteSpace=wrap",
            "html=1",
            f"fillColor={fill_color}",
            f"strokeColor={stroke_color}",
            f"strokeWidth={stroke_width}",
        ]
        
        if rounded:
            style_parts.append(f"arcSize={arc_size}")
        if dashed:
            style_parts.append("dashed=1")
        
        style = ";".join(style_parts) + ";"
        
        return f'''<mxCell id="{cell_id}" value="" style="{style}" parent="1" vertex="1">
      <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
    </mxCell>'''
    
    def text(self, x: int, y: int, width: int, height: int, text: str,
            font_size: int = 10, font_style: int = 0, font_color: str = "#000000",
            align: str = "left", v_align: str = "middle",
            bg_color: str = "none", border_color: str = "none",
            font_family: str = "Helvetica", cell_id: str = None) -> str:
        """
        Create a text cell.
        
        Args:
            x, y: Position
            width, height: Dimensions
            text: Text content
            font_size: Font size in points
            font_style: 0=normal, 1=bold, 2=italic, 3=bold+italic
            font_color: Text color (hex)
            align: Horizontal alignment (left, center, right)
            v_align: Vertical alignment (top, middle, bottom)
            bg_color: Background color (hex or 'none')
            border_color: Border color (hex or 'none')
            font_family: Font family name
            cell_id: Optional custom cell ID
            
        Returns:
            XML string for the cell
        """
        cell_id = cell_id or self.next_id()
        text_escaped = escape_xml(text)
        
        style = (f"text;html=1;strokeColor={border_color};fillColor={bg_color};"
                f"align={align};verticalAlign={v_align};whiteSpace=wrap;rounded=0;"
                f"fontSize={font_size};fontStyle={font_style};fontColor={font_color};"
                f"fontFamily={font_family};")
        
        return f'''<mxCell id="{cell_id}" value="{text_escaped}" style="{style}" parent="1" vertex="1">
      <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
    </mxCell>'''
    
    def arrow(self, source_x: int, source_y: int, target_x: int, target_y: int,
             stroke_color: str, stroke_width: int = 2, label: str = "",
             dashed: bool = False, cell_id: str = None) -> str:
        """
        Create an arrow connection.
        
        Args:
            source_x, source_y: Start point
            target_x, target_y: End point
            stroke_color: Arrow color (hex)
            stroke_width: Arrow width in pixels
            label: Optional label text
            dashed: Whether arrow is dashed
            cell_id: Optional custom cell ID
            
        Returns:
            XML string for the arrow cell
        """
        cell_id = cell_id or self.next_id()
        label_escaped = escape_xml(label)
        
        style_parts = [
            "endArrow=classic",
            "html=1",
            f"strokeColor={stroke_color}",
            f"strokeWidth={stroke_width}",
            "fontFamily=Helvetica",
        ]
        
        if dashed:
            style_parts.extend(["dashed=1", "dashPattern=3 3"])
        
        style = ";".join(style_parts) + ";"
        
        return f'''<mxCell id="{cell_id}" value="{label_escaped}" style="{style}" parent="1" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="{source_x}" y="{source_y}" as="sourcePoint" />
        <mxPoint x="{target_x}" y="{target_y}" as="targetPoint" />
      </mxGeometry>
    </mxCell>'''


class PanelBase:
    """
    Base class for all panel modules.
    Provides common structure and utilities.
    """
    
    def __init__(self, builder: XMLCellBuilder):
        """
        Initialize panel with XML builder.
        
        Args:
            builder: XMLCellBuilder instance
        """
        self.builder = builder
        self.cells = []
    
    def add_cell(self, cell_xml: str):
        """Add a cell to this panel."""
        self.cells.append(cell_xml)
    
    def get_cells(self) -> List[str]:
        """Get all cells for this panel."""
        return self.cells
    
    def create(self, data: Dict, position: Position) -> List[str]:
        """
        Create panel cells.
        
        Args:
            data: Panel data dictionary
            position: Panel position and dimensions
            
        Returns:
            List of XML cell strings
        """
        raise NotImplementedError("Subclasses must implement create()")


def build_diagram(cells: List[str], use_case_id: int, use_case_name: str) -> str:
    """
    Build complete draw.io XML from cells.
    
    Args:
        cells: List of XML cell strings
        use_case_id: Use case number
        use_case_name: Use case name
        
    Returns:
        Complete draw.io XML
    """
    xml = f'''<mxfile host="AI Blueprint Generator" agent="Python Script" version="24.0.0">
  <diagram name="UC-{use_case_id:03d} {use_case_name} Blueprint" id="uc{use_case_id:03d}-blueprint">
    <mxGraphModel dx="1765" dy="1034" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# Standard blueprint dimensions
class StandardLayout:
    """Standard layout dimensions for BNZ blueprints."""
    PAGE_WIDTH = 1920
    PAGE_HEIGHT = 1080
    MARGIN = 30
    
    # Header
    HEADER_HEIGHT = 80
    
    # Left column (summary, metrics, governance, change, decision)
    LEFT_COL_X = 30
    LEFT_COL_WIDTH = 580
    
    # Metrics panels (2 columns)
    METRICS_WIDTH = 285
    
    # Center (components, interface catalog)
    CENTER_X = 640
    CENTER_WIDTH = 840
    COMPONENTS_HEIGHT = 640
    
    # Right column (tech stack, risks, success metrics)
    RIGHT_COL_X = 1510
    RIGHT_COL_WIDTH = 380
    
    # Bottom sections
    INTERFACE_CATALOG_Y = 740
    INTERFACE_CATALOG_HEIGHT = 310
    
    PHASES_Y = 770
    PHASES_WIDTH = 420
    PHASES_HEIGHT = 280
    
    RESOURCES_X = 1080
    RESOURCES_WIDTH = 410
    
    # Footer
    FOOTER_Y = 1055
    FOOTER_HEIGHT = 20


# Utility functions

def parse_list_data(text: str, separator: str = "|", max_items: int = None) -> List[str]:
    """
    Parse pipe-separated or similar text into list.
    
    Args:
        text: Text to parse
        separator: Separator character
        max_items: Maximum number of items to return
        
    Returns:
        List of parsed items
    """
    if not text:
        return []
    
    items = [item.strip() for item in text.split(separator) if item.strip()]
    
    if max_items:
        items = items[:max_items]
    
    return items


def format_bullet_list(items: List[str], bullet: str = "•") -> str:
    """
    Format list as bullet points.
    
    Args:
        items: List of items
        bullet: Bullet character
        
    Returns:
        Formatted string with bullets
    """
    return "\n".join([f"{bullet} {item}" for item in items])

