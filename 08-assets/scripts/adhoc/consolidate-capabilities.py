#!/usr/bin/env python3
"""
Consolidate capabilities from multiple CSV files and capability-model.md into a single CSV file.
Adds a Level column and assigns simple CP-nnn identifiers.
Includes all original columns: maturity levels, success metrics, etc.
"""

import csv
import re
from pathlib import Path

# Paths
PARTS_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\02-capabilities\parts")
CAPABILITY_MODEL = Path(r"D:\Work\BNZ\ai-platform-architecture\02-capabilities\capability-model.md")
OUTPUT_FILE = Path(r"D:\Work\BNZ\ai-platform-architecture\02-capabilities\capabilities-consolidated.csv")

# CSV files to process (excluding decision matrix which has different format)
CSV_FILES = [
    "agentic-ai-capabilities.csv",
    "ai-practices-capabilities.csv",
    "embedded-ai-capabilities.csv",
    "governance-capabilities.csv",
    "knowledge-capabilities.csv",
    "models-capabilities.csv",
]

# All possible column names from CSV files (normalized)
ALL_COLUMNS = [
    'ID',
    'L0_Domain',
    'L1_Group',
    'Level',
    'Source',
    'Primary_Capability',
    'Capability_Name',
    'Definition',
    'Key_Components',
    'Technologies',
    'BNZ_Status',
    'Priority',
    'Maturity_Basic',
    'Maturity_Intermediate',
    'Maturity_Advanced',
    'Maturity_Optimized',
    'Success_Metrics',
]

# L0 Domains from capability-l0-l1.drawio
L0_DOMAINS = {
    'Experiences': 'Experiences',
    'Agentic AI': 'Agentic AI',
    'Generative AI': 'Generative AI',
    'Foundations': 'Foundations',
    'Enabling': 'Enabling',
}

# L1 Groups mapped to L0 Domains (from capability-l0-l1.drawio)
L1_TO_L0_MAPPING = {
    # Experiences L1s
    'Workplace AI': 'Experiences',
    'SaaS AI': 'Experiences',
    'AI Solutions': 'Experiences',
    'Channels': 'Experiences',
    'Personalisation': 'Experiences',
    # Agentic AI L1s
    'Agents': 'Agentic AI',
    'Low Code Agentic': 'Agentic AI',
    'High Code Agentic': 'Agentic AI',
    # Generative AI L1s
    'LLMs': 'Generative AI',
    'RAG': 'Generative AI',
    'Content': 'Generative AI',
    # Foundations L1s
    'Models': 'Foundations',
    'Data & Knowledge': 'Foundations',
    'Integration': 'Foundations',
    'Security': 'Foundations',
    'Infrastructure': 'Foundations',
    # Enabling L1s
    'Transformation & Governance': 'Enabling',
    'Technologies & Enablement': 'Enabling',
    'Engineering & Practices': 'Enabling',
}

# Map source CSV files to L1 Groups
SOURCE_TO_L1_MAPPING = {
    'Agents': 'Agents',
    'AI Practices': 'Engineering & Practices',
    'Embedded AI': 'AI Solutions',
    'Governance': 'Transformation & Governance',
    'Data & Knowledge': 'Data & Knowledge',
    'Models': 'Models',
}


def normalize_column_name(col: str) -> str:
    """Normalize column name to match our standard names."""
    col = col.strip()

    # Map variations to standard names
    mappings = {
        'Primary Capability': 'Primary_Capability',
        'Sub-Capability': 'Capability_Name',
        'Definition': 'Definition',
        'Key Components': 'Key_Components',
        'Technologies': 'Technologies',
        'BNZ Status': 'BNZ_Status',
        'Priority': 'Priority',
        'Maturity-Basic': 'Maturity_Basic',
        'Maturity - Basic': 'Maturity_Basic',
        'Maturity-Intermediate': 'Maturity_Intermediate',
        'Maturity - Intermediate': 'Maturity_Intermediate',
        'Maturity-Advanced': 'Maturity_Advanced',
        'Maturity - Advanced': 'Maturity_Advanced',
        'Maturity-Optimized': 'Maturity_Optimized',
        'Maturity - Optimized': 'Maturity_Optimized',
        'Success Metrics': 'Success_Metrics',
    }

    return mappings.get(col, col.replace(' ', '_').replace('-', '_'))


def parse_csv_capabilities(csv_path: Path, source_name: str) -> list:
    """Parse capabilities from a CSV file, preserving all columns."""
    capabilities = []

    # Get L1 Group from source name
    l1_group = SOURCE_TO_L1_MAPPING.get(source_name, source_name)
    # Get L0 Domain from L1 Group
    l0_domain = L1_TO_L0_MAPPING.get(l1_group, '')

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Normalize column names
            normalized_row = {}
            for key, value in row.items():
                norm_key = normalize_column_name(key)
                normalized_row[norm_key] = value.strip() if value else ''

            primary = normalized_row.get('Primary_Capability', '').strip()
            sub = normalized_row.get('Capability_Name', '').strip()

            if not primary or not sub:
                continue

            # Determine level
            if primary.startswith('NAB-Aligned:'):
                level = "L1"
            else:
                level = "L2"

            # Build capability record with all columns
            cap = {
                'L0_Domain': l0_domain,
                'L1_Group': l1_group,
                'Source': source_name,
                'Level': level,
                'Primary_Capability': primary,
                'Capability_Name': sub if sub != 'N/A - Overarching Capability' else primary.replace('NAB-Aligned:', '').strip(),
                'Definition': normalized_row.get('Definition', ''),
                'Key_Components': normalized_row.get('Key_Components', ''),
                'Technologies': normalized_row.get('Technologies', ''),
                'BNZ_Status': normalized_row.get('BNZ_Status', ''),
                'Priority': normalized_row.get('Priority', ''),
                'Maturity_Basic': normalized_row.get('Maturity_Basic', ''),
                'Maturity_Intermediate': normalized_row.get('Maturity_Intermediate', ''),
                'Maturity_Advanced': normalized_row.get('Maturity_Advanced', ''),
                'Maturity_Optimized': normalized_row.get('Maturity_Optimized', ''),
                'Success_Metrics': normalized_row.get('Success_Metrics', ''),
            }

            capabilities.append(cap)

    return capabilities


def parse_capability_model(md_path: Path) -> list:
    """Parse capabilities from capability-model.md."""
    capabilities = []

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Map capability-model.md L0 codes to drawio L0 domains
    l0_code_to_domain = {
        'CAP-L0-GOV': 'Enabling',
        'CAP-L0-DAT': 'Foundations',
        'CAP-L0-MOD': 'Foundations',
        'CAP-L0-GEN': 'Generative AI',
        'CAP-L0-AGT': 'Agentic AI',
        'CAP-L0-INT': 'Foundations',
        'CAP-L0-OBS': 'Enabling',
        'CAP-L0-SEC': 'Foundations',
        'CAP-L0-EXP': 'Experiences',
        'CAP-L0-DEV': 'Enabling',
    }

    # Map capability-model.md L0 codes to default drawio L1 groups
    # Note: GEN has multiple L1s, so we use L1-specific mapping below
    l0_code_to_l1 = {
        'CAP-L0-GOV': 'Transformation & Governance',
        'CAP-L0-DAT': 'Data & Knowledge',
        'CAP-L0-MOD': 'Models',
        'CAP-L0-GEN': 'Content',  # Default for GEN, but L1s are mapped specifically
        'CAP-L0-AGT': 'Agents',
        'CAP-L0-INT': 'Integration',
        'CAP-L0-OBS': 'Technologies & Enablement',
        'CAP-L0-SEC': 'Security',
        'CAP-L0-EXP': 'AI Solutions',
        'CAP-L0-DEV': 'Engineering & Practices',
    }

    # Map capability-model.md L1 IDs to drawio L1 groups
    # This provides finer-grained mapping for domains with multiple L1s
    l1_id_to_l1_group = {
        # Generative AI L1s map to specific drawio L1 groups
        'CAP-L1-GEN-01': 'LLMs',       # LLM Orchestration -> LLMs
        'CAP-L1-GEN-02': 'RAG',        # Retrieval-Augmented Generation -> RAG
        'CAP-L1-GEN-03': 'Content',    # Content Generation -> Content
        'CAP-L1-GEN-04': 'Content',    # Document Intelligence -> Content
    }

    # Parse L0 domains from the table
    l0_pattern = r'\| (CAP-L0-\w+) \| ([^|]+) \| ([^|]+) \|'
    l0_matches = re.findall(l0_pattern, content)

    for l0_id, domain, description in l0_matches:
        domain = domain.strip()
        description = description.strip()
        l0_domain = l0_code_to_domain.get(l0_id, '')
        l1_group = l0_code_to_l1.get(l0_id, '')
        capabilities.append({
            'L0_Domain': l0_domain,
            'L1_Group': l1_group,
            'Source': 'capability-model',
            'Level': 'L0',
            'Primary_Capability': f"{l0_id}: {domain}",
            'Capability_Name': domain,
            'Definition': description,
            'Key_Components': '',
            'Technologies': '',
            'BNZ_Status': '',
            'Priority': '',
            'Maturity_Basic': '',
            'Maturity_Intermediate': '',
            'Maturity_Advanced': '',
            'Maturity_Optimized': '',
            'Success_Metrics': '',
        })

    # Build L1 ID to L0 code mapping by parsing the markdown structure
    l1_to_l0_code = {}
    # Parse sections to find which L0 each L1 belongs to
    sections = re.split(r'### (CAP-L0-\w+):', content)
    current_l0 = None
    for section in sections:
        l0_match = re.match(r'(CAP-L0-\w+)', section)
        if l0_match:
            current_l0 = l0_match.group(1)
        elif current_l0:
            l1_ids = re.findall(r'#### (CAP-L1-[\w-]+):', section)
            for l1_id in l1_ids:
                l1_to_l0_code[l1_id] = current_l0

    # Parse L1 groups (#### headers)
    l1_pattern = r'#### (CAP-L1-[\w-]+): ([^\n]+)'
    l1_matches = re.findall(l1_pattern, content)

    for l1_id, name in l1_matches:
        name = name.strip()
        parent_l0_code = l1_to_l0_code.get(l1_id, '')
        l0_domain = l0_code_to_domain.get(parent_l0_code, '')
        # Use L1-specific mapping if available, otherwise fall back to L0 default
        l1_group = l1_id_to_l1_group.get(l1_id, l0_code_to_l1.get(parent_l0_code, ''))
        capabilities.append({
            'L0_Domain': l0_domain,
            'L1_Group': l1_group,
            'Source': 'capability-model',
            'Level': 'L1',
            'Primary_Capability': l1_id,
            'Capability_Name': name,
            'Definition': f"L1 Capability Group: {name}",
            'Key_Components': '',
            'Technologies': '',
            'BNZ_Status': '',
            'Priority': '',
            'Maturity_Basic': '',
            'Maturity_Intermediate': '',
            'Maturity_Advanced': '',
            'Maturity_Optimized': '',
            'Success_Metrics': '',
        })

    # Build L2 ID to L0 code and L1 ID mapping
    l2_to_l0_code = {}
    l2_to_l1_id = {}
    current_l0 = None
    current_l1 = None

    # Parse the content line by line to track L0 -> L1 -> L2 hierarchy
    for line in content.split('\n'):
        l0_match = re.match(r'### (CAP-L0-\w+):', line)
        if l0_match:
            current_l0 = l0_match.group(1)
            current_l1 = None
        l1_match = re.match(r'#### (CAP-L1-[\w-]+):', line)
        if l1_match:
            current_l1 = l1_match.group(1)
        l2_match = re.search(r'\| (CAP-L2-[\w-]+) \|', line)
        if l2_match and current_l0:
            l2_id = l2_match.group(1)
            l2_to_l0_code[l2_id] = current_l0
            if current_l1:
                l2_to_l1_id[l2_id] = current_l1

    # Parse L2 capabilities from tables
    # Pattern for L2 capability rows: | CAP-L2-XXX-XX-XX | Name | Description | Patterns | ABBs |
    l2_pattern = r'\| (CAP-L2-[\w-]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|'
    l2_matches = re.findall(l2_pattern, content)

    for l2_id, name, description, patterns, abbs in l2_matches:
        name = name.strip()
        description = description.strip()
        patterns = patterns.strip()
        abbs = abbs.strip()
        parent_l0_code = l2_to_l0_code.get(l2_id, '')
        parent_l1_id = l2_to_l1_id.get(l2_id, '')
        l0_domain = l0_code_to_domain.get(parent_l0_code, '')
        # Use L1-specific mapping if available, otherwise fall back to L0 default
        l1_group = l1_id_to_l1_group.get(parent_l1_id, l0_code_to_l1.get(parent_l0_code, ''))

        capabilities.append({
            'L0_Domain': l0_domain,
            'L1_Group': l1_group,
            'Source': 'capability-model',
            'Level': 'L2',
            'Primary_Capability': l2_id,
            'Capability_Name': name,
            'Definition': description,
            'Key_Components': f"Patterns: {patterns}",
            'Technologies': f"ABBs: {abbs}",
            'BNZ_Status': '',
            'Priority': '',
            'Maturity_Basic': '',
            'Maturity_Intermediate': '',
            'Maturity_Advanced': '',
            'Maturity_Optimized': '',
            'Success_Metrics': '',
        })

    return capabilities


def main():
    all_capabilities = []

    # Parse CSV files
    source_mapping = {
        "agentic-ai-capabilities.csv": "Agents",
        "ai-practices-capabilities.csv": "AI Practices",
        "embedded-ai-capabilities.csv": "Embedded AI",
        "governance-capabilities.csv": "Governance",
        "knowledge-capabilities.csv": "Data & Knowledge",
        "models-capabilities.csv": "Models",
    }

    for csv_file in CSV_FILES:
        csv_path = PARTS_DIR / csv_file
        if csv_path.exists():
            source_name = source_mapping.get(csv_file, csv_file)
            caps = parse_csv_capabilities(csv_path, source_name)
            all_capabilities.extend(caps)
            print(f"Parsed {len(caps)} capabilities from {csv_file}")
        else:
            print(f"Warning: {csv_file} not found")

    # Parse capability model
    if CAPABILITY_MODEL.exists():
        caps = parse_capability_model(CAPABILITY_MODEL)
        all_capabilities.extend(caps)
        print(f"Parsed {len(caps)} capabilities from capability-model.md")
    else:
        print("Warning: capability-model.md not found")

    # Define complete L0->L1 structure from capability-l0-l1.drawio
    # This ensures all L1 groups have at least placeholder capabilities
    COMPLETE_L0_L1_STRUCTURE = {
        'Experiences': ['Workplace AI', 'SaaS AI', 'AI Solutions', 'Channels', 'Personalisation'],
        'Agentic AI': ['Agents', 'Low Code Agentic', 'High Code Agentic'],
        'Generative AI': ['LLMs', 'RAG', 'Content'],
        'Foundations': ['Models', 'Data & Knowledge', 'Integration', 'Security', 'Infrastructure'],
        'Enabling': ['Transformation & Governance', 'Technologies & Enablement', 'Engineering & Practices'],
    }

    # Placeholder L2 capabilities for missing L1 groups
    PLACEHOLDER_L2_CAPABILITIES = {
        'Workplace AI': [
            ('M365 Copilot Integration', 'Integration with Microsoft 365 Copilot for productivity AI'),
            ('Productivity AI Tools', 'AI-powered tools for workplace productivity enhancement'),
        ],
        'SaaS AI': [
            ('Embedded AI Features', 'AI features embedded within third-party SaaS applications'),
            ('Vendor AI Management', 'Management and governance of vendor-provided AI capabilities'),
        ],
        'Channels': [
            ('Multi-Channel Orchestration', 'Orchestrate AI experiences across multiple channels'),
            ('Channel-Specific Optimization', 'Optimize AI responses for specific channel characteristics'),
        ],
        'Personalisation': [
            ('Customer Segmentation', 'AI-driven customer segmentation for personalized experiences'),
            ('Behavioral Analytics', 'Analyze customer behavior for personalization insights'),
        ],
        'Low Code Agentic': [
            ('Copilot Studio Agents', 'Build agents using Microsoft Copilot Studio'),
            ('Power Platform Automation', 'AI-powered automation using Power Platform'),
            ('AgentForce Integration', 'Salesforce AgentForce agent development'),
        ],
        'High Code Agentic': [
            ('LangGraph Workflows', 'Build complex agent workflows using LangGraph'),
            ('CrewAI Multi-Agent', 'Multi-agent orchestration using CrewAI framework'),
            ('Semantic Kernel Agents', 'Agent development using Microsoft Semantic Kernel'),
        ],
        'Infrastructure': [
            ('GPU Compute Clusters', 'GPU-enabled compute infrastructure for AI workloads'),
            ('AI Model Storage', 'Scalable storage for AI models and artifacts'),
            ('Container Orchestration', 'Kubernetes-based container orchestration for AI services'),
            ('Network Security', 'Network security controls for AI infrastructure'),
        ],
    }

    # Find which L1 groups are missing from current capabilities
    existing_l1_groups = set(cap.get('L1_Group', '') for cap in all_capabilities)
    placeholder_count = 0

    for l0_domain, l1_groups in COMPLETE_L0_L1_STRUCTURE.items():
        for l1_group in l1_groups:
            if l1_group not in existing_l1_groups and l1_group in PLACEHOLDER_L2_CAPABILITIES:
                # Add placeholder L2 capabilities for this missing L1 group
                for cap_name, cap_def in PLACEHOLDER_L2_CAPABILITIES[l1_group]:
                    all_capabilities.append({
                        'L0_Domain': l0_domain,
                        'L1_Group': l1_group,
                        'Source': 'placeholder',
                        'Level': 'L2',
                        'Primary_Capability': f"PLACEHOLDER-{l1_group.replace(' ', '-').upper()}",
                        'Capability_Name': cap_name,
                        'Definition': cap_def,
                        'Key_Components': '',
                        'Technologies': '',
                        'BNZ_Status': 'Planned',
                        'Priority': '',
                        'Maturity_Basic': '',
                        'Maturity_Intermediate': '',
                        'Maturity_Advanced': '',
                        'Maturity_Optimized': '',
                        'Success_Metrics': '',
                    })
                    placeholder_count += 1

    if placeholder_count > 0:
        print(f"Added {placeholder_count} placeholder capabilities for missing L1 groups")

    # Define L0 domain order (matching drawio layout)
    l0_order = {'Experiences': 0, 'Agentic AI': 1, 'Generative AI': 2, 'Foundations': 3, 'Enabling': 4, '': 5}
    # Define L1 group order within each L0
    l1_order = {
        # Experiences
        'Workplace AI': 0, 'SaaS AI': 1, 'AI Solutions': 2, 'Channels': 3, 'Personalisation': 4,
        # Agentic AI
        'Agents': 5, 'Low Code Agentic': 6, 'High Code Agentic': 7,
        # Generative AI
        'LLMs': 8, 'RAG': 9, 'Content': 10,
        # Foundations
        'Models': 11, 'Data & Knowledge': 12, 'Integration': 13, 'Security': 14, 'Infrastructure': 15,
        # Enabling
        'Transformation & Governance': 16, 'Technologies & Enablement': 17, 'Engineering & Practices': 18,
        '': 99
    }
    level_order = {'L0': 0, 'L1': 1, 'L2': 2}

    # Sort capabilities by L0 Domain, L1 Group, Level, then Primary Capability
    all_capabilities.sort(key=lambda x: (
        l0_order.get(x.get('L0_Domain', ''), 99),
        l1_order.get(x.get('L1_Group', ''), 99),
        level_order.get(x['Level'], 3),
        x['Primary_Capability']
    ))

    # Assign CP-nnn identifiers
    for i, cap in enumerate(all_capabilities, start=1):
        cap['ID'] = f"CP-{i:03d}"

    # Write consolidated CSV
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=ALL_COLUMNS)
        writer.writeheader()
        writer.writerows(all_capabilities)

    print(f"\n=== Summary ===")
    print(f"Total capabilities consolidated: {len(all_capabilities)}")

    # Count by L0 Domain
    l0_counts = {}
    for cap in all_capabilities:
        l0 = cap.get('L0_Domain', 'Unknown')
        l0_counts[l0] = l0_counts.get(l0, 0) + 1

    print("\nBy L0 Domain:")
    for l0 in ['Experiences', 'Agentic AI', 'Generative AI', 'Foundations', 'Enabling']:
        if l0 in l0_counts:
            print(f"  {l0}: {l0_counts[l0]}")

    # Count by L1 Group
    l1_counts = {}
    for cap in all_capabilities:
        l1 = cap.get('L1_Group', 'Unknown')
        l1_counts[l1] = l1_counts.get(l1, 0) + 1

    print("\nBy L1 Group:")
    for l1, count in sorted(l1_counts.items()):
        if l1:
            print(f"  {l1}: {count}")

    # Count by level
    level_counts = {}
    for cap in all_capabilities:
        level = cap['Level']
        level_counts[level] = level_counts.get(level, 0) + 1

    print("\nBy Level:")
    for level, count in sorted(level_counts.items()):
        print(f"  {level}: {count}")

    # Count by source
    source_counts = {}
    for cap in all_capabilities:
        source = cap['Source']
        source_counts[source] = source_counts.get(source, 0) + 1

    print("\nBy Source:")
    for source, count in sorted(source_counts.items()):
        print(f"  {source}: {count}")

    # Count capabilities with maturity info
    with_maturity = sum(1 for cap in all_capabilities if cap.get('Maturity_Basic'))
    print(f"\nCapabilities with maturity definitions: {with_maturity}")

    print(f"\nOutput written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
