#!/usr/bin/env python3
"""
Generate draw.io diagram for a use case with three panels:
1. Components Panel (ABBs by layer)
2. Tech Stack Panel (Technologies)
3. Interfaces Catalog Panel (Interface table)

Usage: python generate_uc_diagram.py <use_case_id>
Example: python generate_uc_diagram.py 1
"""

import csv
import html
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


class BNZColors:
    """BNZ Visual Design Standards v2.0"""
    NAVY = "#003087"
    ORANGE = "#FF6B35"
    TEAL = "#00A651"
    LIGHT_BLUE = "#6699CC"
    GRAY = "#F5F5F5"
    WHITE = "#FFFFFF"
    DARK_GRAY = "#333333"
    LIGHT_GRAY = "#CCCCCC"
    
    # Layer colors
    PRESENTATION = "#6699CC"
    AI_SERVICES = "#FFB399"
    DATA_KNOWLEDGE = "#E6F7ED"
    INTEGRATION = "#FFF4E6"
    APPLICATION = "#F3E5F5"


def load_csv(filepath: str) -> List[Dict]:
    """Load CSV file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def escape_xml(text: str) -> str:
    """Escape text for XML"""
    if not text:
        return ""
    text = str(text).replace('\n', '&#xa;')
    text = html.escape(text, quote=True)
    return text


def get_layer_color(layer: str) -> Tuple[str, str]:
    """Get background and stroke color for layer"""
    layer_lower = layer.lower()
    if 'presentation' in layer_lower:
        return BNZColors.PRESENTATION, BNZColors.NAVY
    elif 'ai' in layer_lower or 'ml' in layer_lower:
        return BNZColors.AI_SERVICES, BNZColors.ORANGE
    elif 'data' in layer_lower or 'knowledge' in layer_lower:
        return BNZColors.DATA_KNOWLEDGE, BNZColors.TEAL
    elif 'integration' in layer_lower:
        return BNZColors.INTEGRATION, BNZColors.ORANGE
    elif 'application' in layer_lower:
        return BNZColors.APPLICATION, "#9C27B0"
    else:
        return BNZColors.GRAY, BNZColors.DARK_GRAY


class DrawIOBuilder:
    """Build draw.io XML structure"""
    
    def __init__(self, use_case_name: str):
        self.use_case_name = use_case_name
        self.cell_id = 1000
        self.cells = []
        self.abb_positions = {}  # Track ABB box positions for connections
        
    def next_id(self) -> str:
        """Generate next cell ID"""
        self.cell_id += 1
        return f"cell-{self.cell_id}"
    
    def add_cell(self, cell_xml: str):
        """Add a cell to the diagram"""
        self.cells.append(cell_xml)
    
    def create_rectangle(self, x: int, y: int, width: int, height: int,
                        fill_color: str, stroke_color: str, stroke_width: int = 2,
                        rounded: bool = True, dashed: bool = False) -> str:
        """Create a rectangle cell"""
        cell_id = self.next_id()
        arc_size = "10" if rounded else "0"
        dash_pattern = ";dashed=1" if dashed else ""
        
        return f'''<mxCell id="{cell_id}" value="" style="rounded={1 if rounded else 0};whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth={stroke_width};arcSize={arc_size}{dash_pattern};" parent="1" vertex="1">
          <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
        </mxCell>'''
    
    def create_text(self, x: int, y: int, width: int, height: int, text: str,
                   font_size: int = 10, font_style: int = 0, font_color: str = "#000000",
                   align: str = "left", v_align: str = "middle",
                   bg_color: str = "none", border_color: str = "none") -> str:
        """Create a text cell"""
        cell_id = self.next_id()
        text_escaped = escape_xml(text)
        
        return f'''<mxCell id="{cell_id}" value="{text_escaped}" style="text;html=1;strokeColor={border_color};fillColor={bg_color};align={align};verticalAlign={v_align};whiteSpace=wrap;rounded=0;fontSize={font_size};fontStyle={font_style};fontColor={font_color};fontFamily=Helvetica;" parent="1" vertex="1">
          <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
        </mxCell>'''
    
    def create_abb_box(self, x: int, y: int, width: int, height: int,
                       abb_name: str, abb_id: str, fill_color: str, stroke_color: str) -> str:
        """Create an ABB component box"""
        # Use predictable cell ID based on ABB ID for connection referencing
        cell_id = f"abb-{abb_id}"
        text_escaped = escape_xml(abb_name)
        
        # Store position for connection drawing
        self.abb_positions[abb_id] = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'center_x': x + width // 2,
            'center_y': y + height // 2,
            'name': abb_name,
            'cell_id': cell_id
        }
        
        return f'''<mxCell id="{cell_id}" value="{text_escaped}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fill_color};strokeColor={stroke_color};strokeWidth=2;fontSize=10;fontStyle=1;fontColor={BNZColors.DARK_GRAY};fontFamily=Helvetica;align=center;verticalAlign=middle;" parent="1" vertex="1">
          <mxGeometry x="{x}" y="{y}" width="{width}" height="{height}" as="geometry" />
        </mxCell>'''
    
    def create_arrow(self, source_x: int, source_y: int, target_x: int, target_y: int,
                    stroke_color: str, label: str = "") -> str:
        """Create an arrow connection"""
        cell_id = self.next_id()
        label_escaped = escape_xml(label)
        label_cell = f'''<mxCell id="{self.next_id()}" value="{label_escaped}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=8;fontStyle=1;backgroundColor=#FFFFFF;borderColor={stroke_color};" parent="{cell_id}" vertex="1" connectable="0">
            <mxGeometry x="-0.2" y="1" relative="1" as="geometry">
              <mxPoint as="offset" />
            </mxGeometry>
          </mxCell>''' if label else ""
        
        return f'''<mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;strokeColor={stroke_color};strokeWidth=2;fontFamily=Helvetica;" parent="1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{source_x}" y="{source_y}" as="sourcePoint" />
            <mxPoint x="{target_x}" y="{target_y}" as="targetPoint" />
          </mxGeometry>
        </mxCell>{label_cell}'''
    
    def build_diagram(self, uc_id: int, uc_name: str) -> str:
        """Build complete diagram XML"""
        uc_name_clean = uc_name.replace(' ', '-').replace('/', '-').replace(',', '')
        
        xml = f'''<mxfile host="AI Blueprint Generator" agent="Python Script" version="24.0.0">
  <diagram name="UC-{uc_id:03d} {uc_name_clean}" id="uc{uc_id:03d}-blueprint">
    <mxGraphModel dx="1765" dy="1034" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(self.cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        return xml


def create_components_panel(builder: DrawIOBuilder, abbs: List[Dict], x: int, y: int, 
                           width: int, height: int):
    """Create the components panel with ABBs organized by layer"""
    # Panel background
    builder.add_cell(builder.create_rectangle(x, y, width, height, 
                                              BNZColors.WHITE, BNZColors.NAVY))
    
    # Panel header
    builder.add_cell(builder.create_text(x + 20, y + 15, width - 40, 30,
                                        "Solution Architecture - ABBs",
                                        font_size=18, font_style=1, 
                                        font_color=BNZColors.NAVY))
    
    # Group ABBs by layer
    layers = defaultdict(list)
    for abb in abbs:
        layer = abb['architecture_layer']
        layers[layer].append(abb)
    
    # Define layer order (top to bottom)
    layer_order = [
        'Presentation Layer',
        'Application Services Layer',
        'AI/ML Services Layer',
        'Data & Knowledge Layer',
        'Integration Layer'
    ]
    
    current_y = y + 60
    layer_height = 110
    abb_width = 140
    abb_height = 45
    abb_spacing = 15
    
    for layer_name in layer_order:
        layer_abbs = layers.get(layer_name, [])
        if not layer_abbs:
            continue
        
        # Layer background
        bg_color, stroke_color = get_layer_color(layer_name)
        builder.add_cell(builder.create_rectangle(x + 20, current_y, width - 40, 
                                                  layer_height, bg_color, stroke_color,
                                                  stroke_width=1, dashed=True))
        
        # Layer label
        builder.add_cell(builder.create_text(x + 30, current_y + 5, 200, 20,
                                            layer_name, font_size=10, font_style=1,
                                            font_color=stroke_color))
        
        # ABB boxes
        abbs_per_row = (width - 60) // (abb_width + abb_spacing)
        for idx, abb in enumerate(layer_abbs):
            row = idx // abbs_per_row
            col = idx % abbs_per_row
            
            abb_x = x + 30 + col * (abb_width + abb_spacing)
            abb_y = current_y + 30 + row * (abb_height + 10)
            
            builder.add_cell(builder.create_abb_box(abb_x, abb_y, abb_width, abb_height,
                                                    abb['abb_name'], abb['abb_id'],
                                                    BNZColors.WHITE, stroke_color))
        
        current_y += layer_height + 15


def create_tech_stack_panel(builder: DrawIOBuilder, components: List[Dict],
                            all_abbs: List[Dict], x: int, y: int, 
                            width: int, height: int):
    """Create the components panel with name, description, and technologies"""
    # Panel background
    builder.add_cell(builder.create_rectangle(x, y, width, height,
                                              BNZColors.WHITE, BNZColors.ORANGE))
    
    # Panel header
    builder.add_cell(builder.create_text(x + 20, y + 15, width - 40, 30,
                                        "Components & Technologies",
                                        font_size=18, font_style=1,
                                        font_color=BNZColors.ORANGE))
    
    # Build component list with technologies
    component_entries = []
    seen_components = set()
    
    for abb in components:
        comp_name = abb.get('component_name', '')
        if not comp_name or comp_name in seen_components:
            continue
        seen_components.add(comp_name)
        
        # Get description from role_in_solution
        description = abb.get('role_in_solution', '')
        
        # Find matching technologies (SBBs)
        technologies = []
        for full_abb in all_abbs:
            if (full_abb['name'] == abb['abb_name'] or 
                full_abb['component name'] == comp_name):
                sbbs = full_abb.get('candidate SBBs', '')
                if sbbs:
                    for sbb in sbbs.split(',')[:3]:  # Limit to 3 SBBs per ABB
                        sbb = sbb.strip()
                        if sbb and len(sbb) > 2 and sbb not in technologies:
                            technologies.append(sbb)
                break
        
        tech_str = ', '.join(technologies[:4]) if technologies else 'Various technologies'
        
        component_entries.append({
            'name': comp_name,
            'description': description,
            'technologies': tech_str
        })
    
    # Display components
    current_y = y + 55
    row_height = 55
    
    for comp in component_entries[:12]:  # Limit to 12 components
        # Component text with HTML formatting
        comp_text = f"<b>{comp['name']}</b> - {comp['description']}. <font color=\"{BNZColors.ORANGE}\"><i>{comp['technologies']}</i></font>."
        
        builder.add_cell(builder.create_text(x + 20, current_y, width - 40, row_height - 5,
                                            comp_text, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            align="left", v_align="top"))
        
        current_y += row_height


def calculate_edge_connection_points(source_pos: Dict, target_pos: Dict) -> tuple:
    """
    Calculate the best connection points on the edges of boxes.
    Returns (exit_x, exit_y, entry_x, entry_y) as normalized coordinates (0-1).
    """
    source_center_x = source_pos['center_x']
    source_center_y = source_pos['center_y']
    target_center_x = target_pos['center_x']
    target_center_y = target_pos['center_y']
    
    # Calculate relative position
    dx = target_center_x - source_center_x
    dy = target_center_y - source_center_y
    
    # Determine dominant direction
    if abs(dx) > abs(dy):
        # Horizontal connection is dominant
        if dx > 0:
            # Target is to the right: exit right, enter left
            exit_x, exit_y = 1.0, 0.5
            entry_x, entry_y = 0.0, 0.5
        else:
            # Target is to the left: exit left, enter right
            exit_x, exit_y = 0.0, 0.5
            entry_x, entry_y = 1.0, 0.5
    else:
        # Vertical connection is dominant
        if dy > 0:
            # Target is below: exit bottom, enter top
            exit_x, exit_y = 0.5, 1.0
            entry_x, entry_y = 0.5, 0.0
        else:
            # Target is above: exit top, enter bottom
            exit_x, exit_y = 0.5, 0.0
            entry_x, entry_y = 0.5, 1.0
    
    return exit_x, exit_y, entry_x, entry_y


def create_abb_connections(builder: DrawIOBuilder, interfaces: List[Dict]):
    """Create connection arrows between ABBs based on interfaces"""
    
    for interface in interfaces:
        source_id = interface.get('source_abb_id')
        target_id = interface.get('target_abb_id')
        solution_iface_id = interface.get('solution_interface_id', '')
        
        # Check if both ABBs are positioned
        if source_id not in builder.abb_positions or target_id not in builder.abb_positions:
            continue
        
        source_pos = builder.abb_positions[source_id]
        target_pos = builder.abb_positions[target_id]
        
        # Calculate edge connection points
        exit_x, exit_y, entry_x, entry_y = calculate_edge_connection_points(source_pos, target_pos)
        
        # Determine arrow color based on layer
        source_layer = interface.get('source_layer', '')
        if 'AI' in source_layer or 'ML' in source_layer:
            arrow_color = BNZColors.ORANGE
        elif 'Data' in source_layer or 'Knowledge' in source_layer:
            arrow_color = BNZColors.TEAL
        elif 'Integration' in source_layer:
            arrow_color = BNZColors.ORANGE
        else:
            arrow_color = BNZColors.NAVY
        
        # Create arrow with label using solution-specific interface ID
        label = solution_iface_id
        
        # Get cell IDs for source and target ABBs
        # We need to find the cell IDs that were created for these ABBs
        # For now, we'll use absolute positioning with edge anchoring
        
        # Draw connection with edge anchoring
        cell_id = builder.next_id()
        label_id = builder.next_id()
        
        arrow_xml = f'''<mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;strokeColor={arrow_color};strokeWidth=1.5;fontFamily=Helvetica;curved=1;exitX={exit_x};exitY={exit_y};exitDx=0;exitDy=0;entryX={entry_x};entryY={entry_y};entryDx=0;entryDy=0;exitPerimeter=0;entryPerimeter=0;" parent="1" source="abb-{source_id}" target="abb-{target_id}" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{source_pos['x']}" y="{source_pos['y']}" as="sourcePoint" />
            <mxPoint x="{target_pos['x']}" y="{target_pos['y']}" as="targetPoint" />
          </mxGeometry>
        </mxCell>'''
        
        if label:
            label_xml = f'''<mxCell id="{label_id}" value="{label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=7;fontStyle=1;backgroundColor=#FFFFFF;borderColor={arrow_color};fontFamily=Helvetica;" parent="{cell_id}" vertex="1" connectable="0">
            <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
              <mxPoint as="offset" />
            </mxGeometry>
          </mxCell>'''
            builder.add_cell(arrow_xml + label_xml)
        else:
            builder.add_cell(arrow_xml)


def create_interfaces_panel(builder: DrawIOBuilder, interfaces: List[Dict],
                            x: int, y: int, width: int, height: int):
    """Create the interfaces catalog panel"""
    # Panel background
    builder.add_cell(builder.create_rectangle(x, y, width, height,
                                              BNZColors.WHITE, BNZColors.TEAL))
    
    # Panel header
    builder.add_cell(builder.create_text(x + 20, y + 15, width - 40, 30,
                                        "Interface Catalogue",
                                        font_size=18, font_style=1,
                                        font_color=BNZColors.TEAL))
    
    # Table header
    header_y = y + 55
    builder.add_cell(builder.create_rectangle(x + 20, header_y, width - 40, 25,
                                              BNZColors.LIGHT_BLUE, BNZColors.TEAL))
    
    # Column headers - optimized widths (Protocol removed)
    col_widths = [30, 120, 120, 360, 310]
    col_x = x + 20
    headers = ["ID", "From", "To", "Description", "Datasets"]
    
    for header, w in zip(headers, col_widths):
        builder.add_cell(builder.create_text(col_x + 3, header_y + 3, w - 6, 20,
                                            header, font_size=10, font_style=1,
                                            font_color=BNZColors.DARK_GRAY,
                                            align="left"))
        col_x += w
    
    # Table rows - adjusted for font size 10
    row_y = header_y + 25
    row_height = 26
    
    for interface in interfaces[:25]:  # Limit to 25 rows
        col_x = x + 20
        
        # Solution Interface ID (sequential within use case)
        solution_iface_id = interface.get('solution_interface_id', interface.get('interface_id', ''))
        builder.add_cell(builder.create_text(col_x + 3, row_y, col_widths[0] - 6, row_height,
                                            solution_iface_id, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            v_align="top"))
        col_x += col_widths[0]
        
        # From
        source = interface['source_abb_name'][:18]
        builder.add_cell(builder.create_text(col_x + 3, row_y, col_widths[1] - 6, row_height,
                                            source, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            v_align="top"))
        col_x += col_widths[1]
        
        # To
        target = interface['target_abb_name'][:18]
        builder.add_cell(builder.create_text(col_x + 3, row_y, col_widths[2] - 6, row_height,
                                            target, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            v_align="top"))
        col_x += col_widths[2]
        
        # Description - no truncation
        description = interface.get('interface_description', '')
        builder.add_cell(builder.create_text(col_x + 3, row_y, col_widths[3] - 6, row_height,
                                            description, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            v_align="top"))
        col_x += col_widths[3]
        
        # Datasets - no truncation
        datasets = interface['datasets_exchanged']
        builder.add_cell(builder.create_text(col_x + 3, row_y, col_widths[4] - 6, row_height,
                                            datasets, font_size=10,
                                            font_color=BNZColors.DARK_GRAY,
                                            v_align="top"))
        
        row_y += row_height


def generate_use_case_diagram(use_case_id: int):
    """Generate diagram for a use case"""
    print(f"Generating diagram for UC-{use_case_id:03d}...")
    
    # Load data
    print("  Loading data files...")
    use_cases = load_csv("BNZ List of AI use cases Dec 25.csv")
    abbs_catalog = load_csv("solution-abb-catalog.csv")
    interfaces_catalog = load_csv("solution-interfaces-catalog.csv")
    all_abbs = load_csv("ai-architecture-building-blocks.csv")
    
    # Find use case
    use_case = None
    for uc in use_cases:
        if uc['ID'] and int(uc['ID']) == use_case_id:
            use_case = uc
            break
    
    if not use_case:
        print(f"  ✗ Use case UC-{use_case_id:03d} not found!")
        return
    
    uc_name = use_case.get('AI Use Case ', '').strip()
    print(f"  Use Case: {uc_name}")
    
    # Filter ABBs for this use case
    uc_abbs = [abb for abb in abbs_catalog if abb['use_case_id'] == str(use_case_id)]
    print(f"  ABBs: {len(uc_abbs)}")
    
    # Filter interfaces for this use case
    uc_interfaces = [iface for iface in interfaces_catalog 
                     if iface['use_case_id'] == str(use_case_id)]
    print(f"  Interfaces: {len(uc_interfaces)}")
    
    if not uc_abbs:
        print(f"  ✗ No ABBs found for this use case!")
        return
    
    # Create diagram builder
    builder = DrawIOBuilder(uc_name)
    
    # Background
    builder.add_cell(builder.create_rectangle(0, 0, 1920, 1080,
                                              BNZColors.GRAY, "none", 
                                              stroke_width=0, rounded=False))
    
    # Header
    builder.add_cell(builder.create_rectangle(0, 0, 1920, 80,
                                              BNZColors.NAVY, "none",
                                              stroke_width=0, rounded=False))
    
    builder.add_cell(builder.create_text(30, 20, 1200, 40,
                                        f"Use Case Blueprint: UC-{use_case_id:03d} {uc_name}",
                                        font_size=24, font_style=1,
                                        font_color=BNZColors.WHITE))
    
    # Create the three panels
    print("  Creating components panel...")
    create_components_panel(builder, uc_abbs, 30, 110, 840, 640)
    
    print("  Creating ABB connections...")
    create_abb_connections(builder, uc_interfaces)
    
    print("  Creating components & technologies panel...")
    create_tech_stack_panel(builder, uc_abbs, all_abbs, 900, 110, 380, 600)
    
    print("  Creating interfaces panel...")
    create_interfaces_panel(builder, uc_interfaces, 900, 730, 980, 320)
    
    # Footer
    builder.add_cell(builder.create_text(30, 1055, 1860, 20,
                                        f"Blueprint v1.0.0 | UC-{use_case_id:03d}",
                                        font_size=9, font_color="#666666",
                                        align="center"))
    
    # Generate XML
    diagram_xml = builder.build_diagram(use_case_id, uc_name)
    
    # Save file
    uc_name_clean = uc_name.replace(' ', '-').replace('/', '-').replace(',', '')[:50]
    filename = f"../UC-{use_case_id:03d}-{uc_name_clean}-Generated-v1.0.0.drawio"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(diagram_xml)
    
    print(f"  ✓ Saved: {filename}")
    print()


def main():
    """Main function"""
    print("="*60)
    print("BNZ Use Case Diagram Generator")
    print("="*60)
    print()
    
    if len(sys.argv) < 2:
        # Generate for all use cases
        print("No use case ID specified - generating ALL diagrams (1-24)")
        print()
        for use_case_id in range(1, 25):
            generate_use_case_diagram(use_case_id)
    else:
        # Generate for specific use case
        try:
            use_case_id = int(sys.argv[1])
            if use_case_id < 1 or use_case_id > 24:
                print("Error: Use case ID must be between 1 and 24")
                sys.exit(1)
        except ValueError:
            print("Error: Use case ID must be a number")
            sys.exit(1)
        
        generate_use_case_diagram(use_case_id)
    
    print("="*60)
    print("✅ Diagram generation complete!")
    print("="*60)


if __name__ == "__main__":
    main()

