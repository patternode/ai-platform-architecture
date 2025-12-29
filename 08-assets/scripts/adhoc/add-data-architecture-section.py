#!/usr/bin/env python3
"""
Add Data Architecture section to all use case markdown documents.
Uses BIAN domain mapping to populate the Data Products section.
"""

import os
import re
import csv
from pathlib import Path

# Configuration
BASE_DIR = Path(r"d:\Work\BNZ\ai-platform-architecture")
USE_CASES_DIR = BASE_DIR / "01-motivation" / "03-use-cases" / "use-cases"
BIAN_MAPPING_FILE = BASE_DIR / "01-motivation" / "03-use-cases" / "bian-domain-mapping.csv"

# Load BIAN domain mapping
def load_bian_mapping():
    """Load BIAN domain mapping from CSV file."""
    mapping = {}
    with open(BIAN_MAPPING_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uc_id = row['use_case_id']
            if uc_id not in mapping:
                mapping[uc_id] = {
                    'use_case_name': row['use_case_name'],
                    'business_category': row['business_category'],
                    'domains': []
                }
            mapping[uc_id]['domains'].append({
                'business_area': row['bian_business_area'],
                'business_domain': row['bian_business_domain'],
                'service_domain': row['bian_service_domain'],
                'relevance': row['domain_relevance'],
                'link': row['bian_link']
            })
    return mapping

# Data architecture template with BIAN mapping
def generate_data_architecture_section(uc_id, bian_data):
    """Generate the Data Architecture section content for a use case."""

    # Get use case specific info
    uc_name = bian_data.get('use_case_name', uc_id)
    business_category = bian_data.get('business_category', 'TBD')
    domains = bian_data.get('domains', [])

    # Group domains by relevance
    primary_domains = [d for d in domains if d['relevance'] == 'Primary']
    secondary_domains = [d for d in domains if d['relevance'] == 'Secondary']

    # Build data inputs table based on domains
    data_inputs = []
    for domain in domains:
        sd = domain['service_domain']
        ba = domain['business_area']
        rel = domain['relevance']

        # Map service domains to typical data sources
        data_inputs.append({
            'source': f"{sd} ({ba})",
            'type': get_data_type_for_domain(sd),
            'volume': 'TBD',
            'frequency': 'Real-time' if rel == 'Primary' else 'Batch daily',
            'format': 'JSON via API',
            'availability': 'Requires integration'
        })

    # Build section content
    section = f"""### 4. Data Architecture

#### 4.1 BIAN Service Domain Alignment

This use case aligns with the following BIAN 13.0 Service Domains for data product identification:

**Primary Service Domains** (Core Data Products):

| Service Domain | Business Domain | Business Area | BIAN Reference |
|----------------|-----------------|---------------|----------------|
"""

    for d in primary_domains:
        section += f"| {d['service_domain']} | {d['business_domain']} | {d['business_area']} | [Link]({d['link']}) |\n"

    if secondary_domains:
        section += """
**Secondary Service Domains** (Supporting Data Products):

| Service Domain | Business Domain | Business Area | BIAN Reference |
|----------------|-----------------|---------------|----------------|
"""
        for d in secondary_domains:
            section += f"| {d['service_domain']} | {d['business_domain']} | {d['business_area']} | [Link]({d['link']}) |\n"

    section += f"""
#### 4.2 Data Inputs

| Data Source | Data Type | Volume | Frequency | Format | Availability |
|-------------|-----------|--------|-----------|--------|--------------|
"""

    for inp in data_inputs[:6]:  # Limit to 6 most relevant
        section += f"| {inp['source']} | {inp['type']} | {inp['volume']} | {inp['frequency']} | {inp['format']} | {inp['availability']} |\n"

    section += """
#### 4.3 Data Transformations

1. **Data Aggregation**: Combine data from multiple BIAN Service Domains into unified view
2. **Feature Engineering**: Calculate derived features for ML model consumption
3. **Data Quality Validation**: Apply business rules and quality checks
4. **Context Enrichment**: Add business context from reference data domains

#### 4.4 Data Outputs

| Output Type | Description | Destination | Format | Frequency |
|-------------|-------------|-------------|--------|-----------|
| Processed Results | AI/ML model outputs | Downstream systems | JSON via API | Real-time |
| Analytics Data | Aggregated metrics and KPIs | Analytics Dashboard | JSON | Daily |
| Audit Trail | Processing logs and decisions | Audit System | JSON | Real-time |

#### 4.5 Data Quality Requirements

- **Accuracy**: 99%+ for critical business data
- **Completeness**: No missing critical fields
- **Timeliness**: Real-time for operational data, daily batch for analytics
- **Consistency**: Standardized formats across all sources

#### 4.6 Data Governance

- **Classification**: Confidential (contains business-sensitive data)
- **Retention**: Per regulatory requirements and BNZ data retention policy
- **Privacy**: Full PII protection where applicable, consent-based data usage
- **Lineage**: Full data lineage from source systems to AI outputs

---

"""

    return section


def get_data_type_for_domain(service_domain):
    """Map service domain to typical data type."""
    domain_type_map = {
        'Customer Relationship Management': 'Customer profile, interactions',
        'Customer Behavior Insights': 'Behavioral analytics',
        'Lead and Opportunity Management': 'Sales pipeline data',
        'Customer Case Management': 'Case records, resolutions',
        'Financial Statements': 'Financial records',
        'Financial Control': 'Control data, reconciliation',
        'Credit Risk Models': 'Credit scores, risk metrics',
        'Fraud Model': 'Fraud indicators, patterns',
        'Regulatory Compliance': 'Compliance records',
        'System Development': 'SDLC artifacts',
        'Collections': 'Collection records',
        'Payment Order': 'Payment transactions',
    }
    return domain_type_map.get(service_domain, 'Domain-specific data')


def process_use_case_file(file_path, uc_id, bian_mapping):
    """Process a single use case file and add Data Architecture section."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Data Architecture section already exists
    if '### 4. Data Architecture' in content or '### 4.2 Data Architecture' in content:
        print(f"  Skipping {uc_id} - Data Architecture section already exists")
        return False

    # Get BIAN data for this use case
    bian_data = bian_mapping.get(uc_id, {
        'use_case_name': uc_id,
        'business_category': 'TBD',
        'domains': []
    })

    # Generate the Data Architecture section
    data_arch_section = generate_data_architecture_section(uc_id, bian_data)

    # Find where to insert (before "## 4. Architecture Patterns" or similar)
    # Different documents have different section numbering

    # Pattern 1: ## 4. Architecture Patterns
    pattern1 = r'(---\n\n)(## 4\. Architecture Patterns)'
    # Pattern 2: ## 5. Architecture Patterns (if 4 exists)
    pattern2 = r'(---\n\n)(## 5\. Architecture Patterns)'

    if re.search(pattern1, content):
        # Insert before ## 4. Architecture Patterns and renumber it to ## 5
        new_content = re.sub(
            pattern1,
            r'\1' + data_arch_section + r'## 5. Architecture Patterns',
            content
        )
        # Also renumber subsequent sections
        new_content = renumber_sections(new_content, start_from=5)
    elif re.search(pattern2, content):
        # Insert before ## 5. Architecture Patterns
        new_content = re.sub(
            pattern2,
            r'\1' + data_arch_section + r'\2',
            content
        )
    else:
        # Try to find any Architecture Patterns section
        arch_pattern = r'(---\n\n)(## \d+\. Architecture Patterns)'
        match = re.search(arch_pattern, content)
        if match:
            section_num = int(re.search(r'## (\d+)\.', match.group(2)).group(1))
            new_content = re.sub(
                arch_pattern,
                r'\1' + data_arch_section + f'## {section_num + 1}. Architecture Patterns',
                content
            )
            new_content = renumber_sections(new_content, start_from=section_num + 1)
        else:
            print(f"  Warning: Could not find insertion point for {uc_id}")
            return False

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Added Data Architecture section to {uc_id}")
    return True


def renumber_sections(content, start_from):
    """Renumber sections starting from a given number."""
    # This is a simplified renumbering - adjust as needed
    # For sections after Architecture Patterns
    section_map = {
        'Architecture Patterns': start_from,
        'Implementation Plan': start_from + 1,
        'Prioritization Scoring': start_from + 2,
        'Risk Management': start_from + 3,
        'Success Metrics': start_from + 4,
        'References': start_from + 5,
    }

    for section_name, new_num in section_map.items():
        # Match ## N. Section Name where N is any number
        pattern = rf'## \d+\. {section_name}'
        replacement = f'## {new_num}. {section_name}'
        content = re.sub(pattern, replacement, content)

    return content


def main():
    """Main function to process all use case files."""
    print("Loading BIAN domain mapping...")
    bian_mapping = load_bian_mapping()
    print(f"  Loaded {len(bian_mapping)} use case mappings")

    print("\nProcessing use case files...")

    # Get all use case directories
    uc_dirs = sorted([d for d in USE_CASES_DIR.iterdir() if d.is_dir() and d.name.startswith('UC-')])

    processed = 0
    skipped = 0

    for uc_dir in uc_dirs:
        uc_id = uc_dir.name

        # Skip UC-001 as it already has the section
        if uc_id == 'UC-001':
            print(f"  Skipping {uc_id} - reference document")
            skipped += 1
            continue

        # Find the main markdown file
        md_files = list(uc_dir.glob(f'{uc_id}-*.md'))
        if not md_files:
            print(f"  Warning: No markdown file found for {uc_id}")
            continue

        # Use the first matching file (should be the main doc)
        md_file = md_files[0]

        if process_use_case_file(md_file, uc_id, bian_mapping):
            processed += 1
        else:
            skipped += 1

    print(f"\nCompleted: {processed} files processed, {skipped} skipped")


if __name__ == '__main__':
    main()
