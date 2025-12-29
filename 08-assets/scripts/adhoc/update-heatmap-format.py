#!/usr/bin/env python3
"""
Update ABB heatmap diagram with new format:
- First line: AB-XXX Name (count/24)
- Remaining space: Enhanced description
"""
import re
import csv
import html

# Read ENHANCED descriptions
descriptions = {}
with open(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-descriptions-enhanced.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Remove hyphen from key: AB-050 -> ab050
        key = row['abb_id'].lower().replace('-', '')
        descriptions[key] = {
            'name': row['name'],
            'description': row['description'],
            'original_id': row['abb_id'].upper()  # Keep AB-050 format for display
        }

# Read usage data to get counts - normalize keys
usage = {}
with open(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-usage-by-usecase.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Remove hyphen from key: AB-050 -> ab050
        key = row['ABB ID'].lower().replace('-', '')
        usage[key] = int(row['Use Case Count'])

# Read the diagram
with open(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-usage-heatmap.drawio", 'r', encoding='utf-8') as f:
    content = f.read()

# Build replacement mapping
replacements = {}
for key in descriptions.keys():
    abb_id_display = descriptions[key]['original_id']  # AB-050
    name = descriptions[key]['name']
    desc = descriptions[key]['description']
    count = usage.get(key, 0)

    # XML escape the description (& already escaped by html.escape)
    desc_escaped = html.escape(desc)

    # Create new value - use XML-escaped entities for draw.io
    # Format: <b>AB-050 Name (count/24)</b><br><span style="font-size:9px">Description</span>
    new_value = f"&lt;b&gt;{abb_id_display} {name} ({count}/24)&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;font-size:9px&quot;&gt;{desc_escaped}&lt;/span&gt;"

    replacements[key] = new_value

print(f"Built {len(replacements)} replacements")
print(f"Sample keys: {list(replacements.keys())[:3]}")

# Process line by line and replace
lines = content.split('\n')
updated_lines = []
update_count = 0

for line in lines:
    # Check if line contains an ABB cell (id="ab050" format)
    match = re.search(r'<mxCell id="(ab\d+)" value="[^"]*"', line)
    if match:
        cell_id = match.group(1)  # e.g., "ab050"
        if cell_id in replacements:
            # Replace the value attribute
            old_value_pattern = r'(value=")[^"]*(")'
            new_line = re.sub(old_value_pattern, r'\g<1>' + replacements[cell_id] + r'\g<2>', line)
            updated_lines.append(new_line)
            update_count += 1
            print(f"Updated {cell_id}")
            continue
    updated_lines.append(line)

# Write the updated diagram
with open(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-usage-heatmap.drawio", 'w', encoding='utf-8') as f:
    f.write('\n'.join(updated_lines))

print(f"\nDiagram updated successfully!")
print(f"Updated {update_count} ABB cells with enhanced descriptions")
