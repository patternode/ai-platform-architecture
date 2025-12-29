#!/usr/bin/env python3
"""
Script to update Use Case section 2.2 Cost Estimate with detailed TBD placeholders.
"""

import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
UC_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"

SECTION_22_REPLACEMENT = """### 2.2 Cost Estimate

**Development Costs**: TBD

**Ongoing Costs (Annual)**: TBD

**Investment Payback Period**: TBD

**3-Year ROI**: TBD

"""

def update_section_22(file_path):
    """Update section 2.2 Cost Estimate with detailed TBD placeholders."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, "Unicode decode error"

    original_content = content

    # Find section 2.2 and replace content until next section (### 2.3, ---, or ## 3.)
    pattern = r'### 2\.2 Cost Estimate\n[\s\S]*?(?=### 2\.3 |---\n\n## 3\.|## 3\.)'

    content = re.sub(pattern, SECTION_22_REPLACEMENT, content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None

    return False, None

def main():
    print("=" * 60)
    print("Update Section 2.2 Cost Estimate")
    print("=" * 60)

    updated_files = []
    errors = []

    for uc_folder in sorted(UC_ROOT.iterdir()):
        if not uc_folder.is_dir() or not uc_folder.name.startswith('UC-'):
            continue

        # Find the main UC markdown file (not README.md)
        md_files = [f for f in uc_folder.glob('UC-*.md') if f.name != 'README.md']

        if not md_files:
            continue

        for md_file in md_files:
            updated, error = update_section_22(md_file)

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

    print("\nDone!")

if __name__ == "__main__":
    main()
