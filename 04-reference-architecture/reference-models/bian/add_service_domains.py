import csv
import xml.etree.ElementTree as ET
from collections import defaultdict

def parse_csv_data(csv_file):
    """Parse CSV file and organize data by Business Area and Business Domain"""
    data = defaultdict(lambda: defaultdict(list))
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Handle BOM character in CSV header
            type_key = list(row.keys())[0]  # Get first key which contains 'Type'
            if 'Service Domain' in row[type_key]:
                business_area = row['BusinessArea']
                business_domain = row['BusinessDomain'] 
                service_domain = row['ServiceDomain']
                data[business_area][business_domain].append(service_domain)
    
    return data

def calculate_service_domain_positions(parent_x, parent_y, parent_width, parent_height, service_domains, cols=3):
    """Calculate positions for Service Domain boxes within a Business Domain"""
    positions = []
    count = len(service_domains)
    if count == 0:
        return positions
    
    # Calculate grid layout
    rows = (count + cols - 1) // cols  # Ceiling division
    
    # Margins and spacing
    margin = 8
    spacing_x = 4
    spacing_y = 4
    
    # Available space
    available_width = parent_width - (2 * margin)
    available_height = parent_height - (2 * margin) - 25  # Account for parent title
    
    # Box dimensions
    box_width = (available_width - (cols - 1) * spacing_x) / cols
    box_height = (available_height - (rows - 1) * spacing_y) / rows
    
    # Generate positions
    for i, service_domain in enumerate(service_domains):
        row = i // cols
        col = i % cols
        
        x = parent_x + margin + col * (box_width + spacing_x)
        y = parent_y + margin + 25 + row * (box_height + spacing_y)  # +25 for parent title
        
        positions.append({
            'name': service_domain,
            'x': x,
            'y': y,
            'width': box_width,
            'height': box_height
        })
    
    return positions

def generate_service_domain_xml(service_domain_info, parent_id, cell_id):
    """Generate XML element for a Service Domain box"""
    name = service_domain_info['name']
    x = service_domain_info['x']
    y = service_domain_info['y'] 
    width = service_domain_info['width']
    height = service_domain_info['height']
    
    # Clean name for display (remove long prefixes if needed)
    display_name = name
    if len(display_name) > 25:
        # Split long names
        words = display_name.split()
        if len(words) > 2:
            mid = len(words) // 2
            display_name = ' '.join(words[:mid]) + '\\n' + ' '.join(words[mid:])
    
    cell_elem = ET.Element('mxCell')
    cell_elem.set('id', f'sd-{cell_id}')
    cell_elem.set('value', display_name)
    cell_elem.set('style', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F3FF;strokeColor=#4A90E2;fontSize=10;strokeWidth=1;spacingLeft=2;spacingBottom=2;spacingRight=2;spacingTop=2;fontColor=#2C5282;')
    cell_elem.set('parent', '1')
    cell_elem.set('vertex', '1')
    
    geometry = ET.SubElement(cell_elem, 'mxGeometry')
    geometry.set('x', str(int(x)))
    geometry.set('y', str(int(y)))
    geometry.set('width', str(int(width)))
    geometry.set('height', str(int(height)))
    geometry.set('as', 'geometry')
    
    return cell_elem

def update_drawio_with_service_domains(drawio_file, csv_file, output_file):
    """Update the draw.io file with Service Domain boxes"""
    
    # Parse CSV data
    data = parse_csv_data(csv_file)
    
    # Parse existing draw.io file
    tree = ET.parse(drawio_file)
    root = tree.getroot()
    
    # Find the mxGraphModel and root elements
    graph_model = root.find('.//mxGraphModel')
    if graph_model is None:
        print("Could not find mxGraphModel")
        return
    
    graph_root = graph_model.find('root')
    if graph_root is None:
        print("Could not find root element")
        return
    
    # Map of Business Domain names to their existing XML elements and positions
    bd_elements = {}
    
    # Find existing Business Domain elements and extract their positions
    for cell in graph_root.findall('mxCell'):
        cell_id = cell.get('id', '')
        if cell_id.startswith('bd-'):
            value = cell.get('value', '')
            geometry = cell.find('mxGeometry')
            if geometry is not None:
                x = float(geometry.get('x', 0))
                y = float(geometry.get('y', 0))
                width = float(geometry.get('width', 0))
                height = float(geometry.get('height', 0))
                bd_elements[value] = {
                    'id': cell_id,
                    'x': x, 'y': y, 'width': width, 'height': height
                }
    
    # Business Area to Business Domain mapping based on the CSV
    ba_to_bd_mapping = {
        'Sales and Service': ['Channel Specific', 'Cross Channel', 'Marketing', 'Sales', 'Customer Management', 'Servicing'],
        'Operations and Execution': ['Loans and Deposits', 'Investment Management', 'Trade Banking', 'Wholesale Trading', 'Cards', 'Market Operations', 'Corporate Financing & Advisory', 'Consumer Services', 'Cross Product Operations', 'Payments', 'Account Management', 'Operational Services', 'Collateral Administration'],
        'Reference Data': ['Party', 'External Agency', 'Market Data', 'Product Management'],
        'Business Support': ['IT Management', 'Non-IT / HR Services', 'Buildings Equipment', 'Business Command', 'Finance', 'Human Resources', 'Knowledge & IP', 'Corporate Relations', 'Business Direction', 'Document Mgmt']
    }
    
    cell_counter = 1000  # Start counter for new Service Domain cells
    
    # Generate Service Domain boxes for each Business Domain
    for business_area, business_domains in data.items():
        print(f"Processing Business Area: {business_area}")
        
        for business_domain, service_domains in business_domains.items():
            print(f"  Processing Business Domain: {business_domain} ({len(service_domains)} service domains)")
            
            # Create mapping for business domain names between CSV and diagram
            name_mapping = {
                'Loans and Deposits': 'Loans and\nDeposits',
                'Investment Management': 'Investment\nManagement', 
                'Wholesale Trading': 'Wholesale\nTrading',
                'Market Operations': 'Market\nOperations',
                'Corporate Financing and Advisory Services': 'Corporate Financing\n& Advisory',
                'Consumer Services': 'Consumer\nServices',
                'Account Management': 'Account\nManagement',
                'Operational Services': 'Operational\nServices',
                'Collateral Administration': 'Collateral\nAdministration',
                'Bank Portfolio and Treasury': 'Bank Portfolio\nand Treasury',
                'Regulations and Compliance': 'Regulations and\nCompliance',
                'Non-IT and Non-HR Enterprise Services': 'Non-IT / HR\nServices',
                'Buildings Equipment and Facilities': 'Buildings\nEquipment',
                'Business Command and Control': 'Business\nCommand',
                'Human Resource Management': 'Human\nResources',
                'Knowledge and Intellectual Property': 'Knowledge\n& IP',
                'Corporate Relations': 'Corporate\nRelations',
                'Business Direction': 'Business\nDirection',
                'Document Management and Archive': 'Document\nMgmt'
            }
            
            # Find the corresponding Business Domain element
            bd_key = None
            search_name = name_mapping.get(business_domain, business_domain)
            
            for bd_name in bd_elements.keys():
                # Direct match or mapped name match
                if (bd_name == business_domain or 
                    bd_name == search_name or
                    business_domain in bd_name or
                    bd_name in business_domain):
                    bd_key = bd_name
                    break
            
            if bd_key and bd_key in bd_elements:
                bd_info = bd_elements[bd_key]
                
                # Determine number of columns based on number of service domains
                cols = 2 if len(service_domains) <= 4 else 3
                if len(service_domains) > 12:
                    cols = 4
                
                # Calculate positions for Service Domain boxes
                positions = calculate_service_domain_positions(
                    bd_info['x'], bd_info['y'], bd_info['width'], bd_info['height'],
                    service_domains, cols
                )
                
                # Generate XML elements for Service Domains
                for pos_info in positions:
                    sd_element = generate_service_domain_xml(pos_info, bd_info['id'], cell_counter)
                    graph_root.append(sd_element)
                    cell_counter += 1
                    
            else:
                print(f"    Warning: Could not find Business Domain element for '{business_domain}'")
    
    # Write updated XML to output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Updated diagram saved to: {output_file}")

if __name__ == "__main__":
    csv_file = "d:/Work/BNZ/work-bnz/02-architecture/01-capability/01-Inputs/bian/bian-service-landscape-hierarchy.csv"
    drawio_file = "d:/Work/BNZ/work-bnz/02-architecture/01-capability/01-Inputs/bian/bian-hierarchy-L1-L3.drawio"
    output_file = "d:/Work/BNZ/work-bnz/02-architecture/01-capability/01-Inputs/bian/bian-hierarchy-L1-L3-enhanced.drawio"
    
    update_drawio_with_service_domains(drawio_file, csv_file, output_file)