#!/usr/bin/env python3
"""
Script to update Use Case documents:
1. Add Enterprise Architect assignments from architect-assignments.md
2. Update Status to "Preliminary"
3. Update Created Date and Last Modified to 2025-12-07
4. Remove quantified benefits in section 2.1 (keep only qualified benefits)
5. Update sections 2.2, 5, 6, 7 to "TBD"
6. Remove the last line with use case status and wave info
"""

import os
import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
UC_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"

# Architect assignments (from architect-assignments.md)
ARCHITECT_ASSIGNMENTS = {
    'UC-001': 'Dan Barratt, Hugh Walcott, Sarah Amundsen, Shawn Cawood',
    'UC-002': 'Brian Stapleton, Tracey Davis',
    'UC-003': 'Tracey Davis',
    'UC-004': 'Paul Furkert',
    'UC-005': 'Angus Cotton, Paul Furkert',
    'UC-006': 'Corina Elama',
    'UC-007': 'Dan Barratt',
    'UC-008': 'Francis Kataino, John Marshall, Mike Thompson',
    'UC-009': 'Tracey Davis',
    'UC-010': 'Glenn Bellam',
    'UC-011': 'Michael Lomas',
    'UC-012': 'Brian Stapleton, Michael Lomas',
    'UC-013': 'Michael Lomas',
    'UC-014': 'Brett Allport',
    'UC-015': 'TBD',  # GAP
    'UC-016': 'John Marshall',
    'UC-017': 'Dan Barratt, Shawn Cawood',
    'UC-018': 'Brian Stapleton',
    'UC-019': 'TBD',  # GAP
    'UC-020': 'TBD',  # GAP
    'UC-021': 'Lee Mauger, Shawn Cawood',
    'UC-022': 'Hugh Walcott',
    'UC-023': 'Paul Furkert',
    'UC-024': 'Brett Allport, Corina Elama, Sarah Amundsen',
}

def update_document_control(content, uc_id):
    """Update the Document Control section."""
    architect = ARCHITECT_ASSIGNMENTS.get(uc_id, 'TBD')

    # Update Status to Preliminary
    content = re.sub(
        r'\| \*\*Status\*\* \| `[^`]+` \|',
        '| **Status** | `Preliminary` |',
        content
    )

    # Update Created Date
    content = re.sub(
        r'\| \*\*Created Date\*\* \| `[^`]+` \|',
        '| **Created Date** | `2025-12-07` |',
        content
    )

    # Update Last Modified
    content = re.sub(
        r'\| \*\*Last Modified\*\* \| `[^`]+` \|',
        '| **Last Modified** | `2025-12-07` |',
        content
    )

    # Update Enterprise Architect
    content = re.sub(
        r'\| \*\*Enterprise Architect\*\* \| [^\|]+ \|',
        f'| **Enterprise Architect** | {architect} |',
        content
    )

    return content

def update_section_21_benefits(content):
    """Remove quantified benefits table and values, keep only qualified benefits."""

    # Replace the Quantified Benefits section with a simplified version
    # Pattern to match the Quantified Benefits table
    pattern = r'\*\*Quantified Benefits\*\*:[\s\S]*?\*\*Total Annual Benefit\*\*:[^\n]*\n'

    replacement = """**Qualitative Benefits**:
- Significant reduction in manual effort and processing time
- Improved accuracy and consistency of outputs
- Enhanced customer/employee experience
- Better compliance and audit trail
- Increased operational efficiency

"""

    content = re.sub(pattern, replacement, content)

    # Also remove the Benefit Realization Timeline if it has specific numbers
    pattern2 = r'\*\*Benefit Realization Timeline\*\*:[\s\S]*?(?=\n### |\n## |\n---)'
    content = re.sub(pattern2, '', content)

    return content

def update_section_22_costs(content):
    """Replace section 2.2 Cost Estimate with TBD."""

    # Find section 2.2 and replace content until section 2.3
    pattern = r'(### 2\.2 Cost Estimate\n)[\s\S]*?(?=### 2\.3 )'

    replacement = r"""\1
TBD - Cost estimates to be developed during detailed planning phase.

"""

    content = re.sub(pattern, replacement, content)

    return content

def update_section_5_implementation(content):
    """Replace section 5 Implementation Plan with TBD."""

    # Find section 5 and replace content until section 6
    pattern = r'(## 5\. Implementation Plan\n)[\s\S]*?(?=## 6\. )'

    replacement = r"""\1
TBD - Implementation plan to be developed during detailed planning phase.

---

"""

    content = re.sub(pattern, replacement, content)

    return content

def update_section_6_prioritization(content):
    """Replace section 6 Prioritization Scoring with TBD."""

    # Find section 6 and replace content until section 7
    pattern = r'(## 6\. Prioritization Scoring\n)[\s\S]*?(?=## 7\. )'

    replacement = r"""\1
TBD - Prioritization scoring to be completed during portfolio planning.

---

"""

    content = re.sub(pattern, replacement, content)

    return content

def update_section_7_risk(content):
    """Replace section 7 Risk Management with TBD."""

    # Find section 7 and replace content until section 8
    pattern = r'(## 7\. Risk Management\n)[\s\S]*?(?=## 8\. )'

    replacement = r"""\1
TBD - Risk assessment to be completed during detailed planning phase.

---

"""

    content = re.sub(pattern, replacement, content)

    return content

def remove_status_line(content):
    """Remove the last status/wave line."""

    # Remove lines like "**Use Case Status**: Priority 1, ..."
    # and "Use Case Status: Priority 2, Planned Wave Assignment: Wave 2"
    patterns = [
        r'\n\*\*Use Case Status\*\*:[^\n]*\n',
        r'\nUse Case Status:[^\n]*\n',
        r'\n\*\*WSJF Score\*\*:[^\n]*\n',
        r'\n\*\*Composite Priority Score\*\*:[^\n]*\n',
        r'\n\*\*Expected ROI\*\*:[^\n]*\n',
        r'\n\*\*Strategic Impact\*\*:[^\n]*\n',
    ]

    for pattern in patterns:
        content = re.sub(pattern, '\n', content)

    # Clean up trailing whitespace and empty lines at end
    content = content.rstrip() + '\n'

    return content

def process_use_case(file_path):
    """Process a single use case file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, "Unicode decode error"

    original_content = content

    # Extract UC ID from filename
    match = re.match(r'(UC-\d{3})', file_path.name)
    if not match:
        return False, "Could not extract UC ID"

    uc_id = match.group(1)

    # Apply all updates
    content = update_document_control(content, uc_id)
    content = update_section_21_benefits(content)
    content = update_section_22_costs(content)
    content = update_section_5_implementation(content)
    content = update_section_6_prioritization(content)
    content = update_section_7_risk(content)
    content = remove_status_line(content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None

    return False, None

def main():
    print("=" * 60)
    print("Use Case Document Update Script")
    print("=" * 60)

    updated_files = []
    errors = []

    for uc_folder in sorted(UC_ROOT.iterdir()):
        if not uc_folder.is_dir() or not uc_folder.name.startswith('UC-'):
            continue

        # Find the main UC markdown file (not README.md)
        md_files = [f for f in uc_folder.glob('UC-*.md') if f.name != 'README.md']

        if not md_files:
            print(f"  No UC file found in {uc_folder.name}")
            continue

        for md_file in md_files:
            updated, error = process_use_case(md_file)

            if error:
                errors.append((md_file.name, error))
                print(f"  Error: {md_file.name}: {error}")
            elif updated:
                updated_files.append(md_file.name)
                print(f"  Updated: {md_file.name}")
            else:
                print(f"  Skipped (no changes): {md_file.name}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files updated: {len(updated_files)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors:")
        for name, error in errors:
            print(f"  - {name}: {error}")

    print("\nDone!")

if __name__ == "__main__":
    main()
