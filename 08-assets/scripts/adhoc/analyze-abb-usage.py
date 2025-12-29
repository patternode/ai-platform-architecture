"""
Analyze ABB usage across use cases.
For each ABB, count unique use cases that reference it.
"""

import os
import re
from collections import defaultdict
from pathlib import Path

# Base paths
UC_BASE = r"d:\Work\BNZ\ai-platform-architecture\01-motivation\03-use-cases\use-cases"
ABB_BASE = r"d:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abbs"

def get_abb_name(abb_id):
    """Get ABB name from the ABB directory."""
    abb_dir = os.path.join(ABB_BASE, abb_id)
    if not os.path.exists(abb_dir):
        return f"Unknown ({abb_id})"

    # Look for markdown files in the directory
    for file in os.listdir(abb_dir):
        if file.endswith('.md') and file.startswith(abb_id):
            # Extract name from filename: AB-XXX-Name-v1.0.0.md
            parts = file.replace('.md', '').split('-')
            if len(parts) >= 3:
                # Join all parts between ID and version
                name_parts = []
                for i, part in enumerate(parts):
                    if i <= 1:  # Skip AB and XXX
                        continue
                    if part.startswith('v') and '.' in part:  # Version number
                        break
                    name_parts.append(part)
                return ' '.join(name_parts)

    return f"Unknown ({abb_id})"

def find_abb_references(use_case_dir):
    """Find all ABB references in a use case directory."""
    abb_refs = set()

    # Look for markdown files in the use case directory
    for file in os.listdir(use_case_dir):
        if file.endswith('.md'):
            file_path = os.path.join(use_case_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find all AB-XXX patterns
                    matches = re.findall(r'AB-\d{3}', content)
                    abb_refs.update(matches)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return abb_refs

def main():
    # Dictionary to store ABB -> set of use cases
    abb_to_use_cases = defaultdict(set)

    # Get all use case directories (UC-001 through UC-024)
    use_case_dirs = sorted([d for d in os.listdir(UC_BASE) if d.startswith('UC-')])

    print(f"Found {len(use_case_dirs)} use case directories")

    # Process each use case
    for uc_dir in use_case_dirs:
        uc_path = os.path.join(UC_BASE, uc_dir)
        if os.path.isdir(uc_path):
            abb_refs = find_abb_references(uc_path)
            for abb in abb_refs:
                abb_to_use_cases[abb].add(uc_dir)
            print(f"  {uc_dir}: Found {len(abb_refs)} unique ABBs")

    # Create results list with counts
    results = []
    for abb_id in sorted(abb_to_use_cases.keys()):
        use_cases = abb_to_use_cases[abb_id]
        abb_name = get_abb_name(abb_id)
        results.append((abb_id, abb_name, len(use_cases)))

    # Sort by use case count (descending), then by ABB ID
    results.sort(key=lambda x: (-x[2], x[0]))

    # Print results
    print("\n" + "="*80)
    print("ABB USAGE ANALYSIS")
    print("="*80)
    print(f"{'ABB ID':<10} | {'ABB Name':<60} | {'UC Count':<10}")
    print("-"*80)

    for abb_id, abb_name, count in results:
        print(f"{abb_id:<10} | {abb_name:<60} | {count:<10}")

    print("-"*80)
    print(f"Total ABBs referenced: {len(results)}")
    print(f"Total use cases analyzed: {len(use_case_dirs)}")

    # Also save to a CSV file
    output_file = os.path.join(ABB_BASE, 'abb-usage-analysis.csv')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("ABB ID,ABB Name,Use Case Count,Use Cases\n")
        for abb_id in sorted(abb_to_use_cases.keys()):
            use_cases = sorted(abb_to_use_cases[abb_id])
            abb_name = get_abb_name(abb_id)
            count = len(use_cases)
            use_case_list = ';'.join(use_cases)
            f.write(f'"{abb_id}","{abb_name}",{count},"{use_case_list}"\n')

    print(f"\nDetailed CSV report saved to: {output_file}")

if __name__ == "__main__":
    main()
