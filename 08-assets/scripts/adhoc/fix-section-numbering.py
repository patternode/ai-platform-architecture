#!/usr/bin/env python3
"""
Fix section numbering in use case markdown documents after Data Architecture section was added.
"""

import os
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(r"d:\Work\BNZ\ai-platform-architecture")
USE_CASES_DIR = BASE_DIR / "01-motivation" / "03-use-cases" / "use-cases"


def fix_section_numbering(file_path):
    """Fix section numbering in a use case file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the expected section order and numbers
    # After adding Data Architecture (section 4), the numbering should be:
    # 1. Executive Summary
    # 2. Business Case
    # 3. Target State Solution
    # 4. Data Architecture
    # 5. Architecture Patterns
    # 6. Implementation Plan
    # 7. Prioritization Scoring
    # 8. Risk Management
    # 9. Success Metrics & KPIs
    # 10. References

    section_order = [
        ('Executive Summary', 1),
        ('Business Case', 2),
        ('Target State Solution', 3),
        ('Data Architecture', 4),
        ('Architecture Patterns', 5),
        ('Implementation Plan', 6),
        ('Prioritization Scoring', 7),
        ('Risk Management', 8),
        ('Success Metrics', 9),
        ('References', 10),
    ]

    changes_made = False

    for section_name, expected_num in section_order:
        # Match "## N. Section Name" where N is any number
        pattern = rf'## \d+\. {re.escape(section_name)}'
        replacement = f'## {expected_num}. {section_name}'

        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                changes_made = True

    # Also fix "### 4. Data Architecture" to be consistent
    content = re.sub(r'### 4\. Data Architecture', '## 4. Data Architecture', content)

    # Fix any "### 3.6" that should be under section 3 (not renumbered)
    # These are subsections of Target State Solution

    if changes_made or '### 4. Data Architecture' in content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def main():
    """Main function to fix section numbering in all use case files."""
    print("Fixing section numbering in use case files...")

    # Get all use case directories
    uc_dirs = sorted([d for d in USE_CASES_DIR.iterdir() if d.is_dir() and d.name.startswith('UC-')])

    fixed = 0

    for uc_dir in uc_dirs:
        uc_id = uc_dir.name

        # Find the main markdown file
        md_files = list(uc_dir.glob(f'{uc_id}-*.md'))
        if not md_files:
            continue

        md_file = md_files[0]

        if fix_section_numbering(md_file):
            print(f"  Fixed {uc_id}")
            fixed += 1
        else:
            print(f"  Skipped {uc_id} - no changes needed")

    print(f"\nCompleted: {fixed} files fixed")


if __name__ == '__main__':
    main()
