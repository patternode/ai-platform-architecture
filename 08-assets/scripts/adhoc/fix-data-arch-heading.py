#!/usr/bin/env python3
"""
Fix Data Architecture section heading level in use case markdown documents.
Change ### 4. Data Architecture to ## 4. Data Architecture
"""

import os
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(r"d:\Work\BNZ\ai-platform-architecture")
USE_CASES_DIR = BASE_DIR / "01-motivation" / "03-use-cases" / "use-cases"


def fix_data_arch_heading(file_path):
    """Fix Data Architecture heading level in a use case file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix the main Data Architecture heading
    content = re.sub(r'### 4\. Data Architecture', '## 4. Data Architecture', content)

    # Also fix the subheadings to be ### level (not ####)
    content = re.sub(r'#### 4\.1 BIAN Service Domain Alignment', '### 4.1 BIAN Service Domain Alignment', content)
    content = re.sub(r'#### 4\.2 Data Inputs', '### 4.2 Data Inputs', content)
    content = re.sub(r'#### 4\.3 Data Transformations', '### 4.3 Data Transformations', content)
    content = re.sub(r'#### 4\.4 Data Outputs', '### 4.4 Data Outputs', content)
    content = re.sub(r'#### 4\.5 Data Quality Requirements', '### 4.5 Data Quality Requirements', content)
    content = re.sub(r'#### 4\.6 Data Governance', '### 4.6 Data Governance', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def main():
    """Main function to fix Data Architecture heading in all use case files."""
    print("Fixing Data Architecture heading level...")

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

        if fix_data_arch_heading(md_file):
            print(f"  Fixed {uc_id}")
            fixed += 1
        else:
            print(f"  Skipped {uc_id} - no changes needed")

    print(f"\nCompleted: {fixed} files fixed")


if __name__ == '__main__':
    main()
