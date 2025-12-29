#!/usr/bin/env python3
"""
Organize BNZ AI Use Case Files into Individual Sub-folders

This script:
1. Creates a sub-folder for each use case (UC-001 through UC-024)
2. Moves all related files into their respective sub-folders:
   - Markdown documents
   - Blueprint diagrams (.drawio)
   - Sequence diagrams (.drawio)
   - Any other use case specific files

Usage:
    python organize_use_cases.py [--dry-run]
    
Options:
    --dry-run    Show what would be moved without actually moving files
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
import argparse

# Define the base directory
BASE_DIR = Path(__file__).parent

# Define use case IDs
USE_CASE_IDS = [f"UC-{i:03d}" for i in range(1, 25)]  # UC-001 through UC-024

# Files to exclude from moving (keep in root)
EXCLUDE_FILES = {
    'organize_use_cases.py',
    'generate_use_cases.py',
    'create_prioritization_spreadsheet.py',
    'USE-CASE-TEMPLATE.md',
    'USE-CASE-TEMPLATE-GUIDE.md',
    'USE-CASE-TEMPLATE-README.md',
    'USE-CASE-GENERATION-SUMMARY.md',
    'USE-CASE-PRIORITISATION-FRAMEWORK.md',
    'USE-CASE-RESEARCH-2025-SUMMARY.md',
    'SPREADSHEET-USER-GUIDE.md',
    'README.md',
    'Plan.md',
    'ai-architecture-building-blocks.xlsx',
    'BNZ_AI_Use_Case_Prioritisation.xlsx',
    'BNZ_AI_Use_Case_Prioritisation-Solution.csv',
    'BNZ-Use-Cases.xlsx',
    'BNZ-Use-Cases.csv',
    'BNZ-Use-Cases-Enhanced-2025.csv',
    'BNZ List of AI use cases Dec 25.xlsx',
    'UseCase-Pattern-Mapping.csv',
    'Pattern-UseCase-Mapping.csv',
    'AI-Use-Cases-Quick-Reference.md',
    'AI-Use-Cases-Enhancement-Summary.md',
    'AI-Use-Cases-Data-Summary.md',
    'AI-Use-Cases-Categories-Summary.md',
}

# Directories to exclude
EXCLUDE_DIRS = {
    'patterns',
    'data',
    'scripts',
    'approach',
    '.git',
    '__pycache__',
}

def extract_use_case_id(filename: str) -> str or None:
    """
    Extract use case ID from filename.
    
    Patterns:
    - UC-001-*.md
    - UC-001-*.drawio
    - SCN-001-*.drawio (sequence diagrams)
    - UC01 (without hyphen)
    
    Returns use case ID in format UC-001 or None if not found.
    """
    # Pattern 1: UC-001 or UC-01
    match = re.match(r'^UC-?(\d{1,3})', filename, re.IGNORECASE)
    if match:
        num = int(match.group(1))
        return f"UC-{num:03d}"
    
    # Pattern 2: SCN-001 (sequence diagrams)
    match = re.match(r'^SCN-?(\d{1,3})', filename, re.IGNORECASE)
    if match:
        num = int(match.group(1))
        return f"UC-{num:03d}"
    
    return None

def get_files_to_organize() -> Dict[str, List[Path]]:
    """
    Scan directories and group files by use case ID.
    
    Returns:
        Dictionary mapping use case ID to list of file paths
    """
    files_by_uc = {uc_id: [] for uc_id in USE_CASE_IDS}
    
    # Scan root directory
    for item in BASE_DIR.iterdir():
        if item.is_file() and item.name not in EXCLUDE_FILES:
            uc_id = extract_use_case_id(item.name)
            if uc_id and uc_id in files_by_uc:
                files_by_uc[uc_id].append(item)
    
    # Scan use-cases directory (markdown documents)
    use_cases_dir = BASE_DIR / 'use-cases'
    if use_cases_dir.exists():
        for item in use_cases_dir.iterdir():
            if item.is_file() and item.name != 'README.md':
                uc_id = extract_use_case_id(item.name)
                if uc_id and uc_id in files_by_uc:
                    files_by_uc[uc_id].append(item)
    
    # Remove empty entries
    files_by_uc = {k: v for k, v in files_by_uc.items() if v}
    
    return files_by_uc

def create_directory_structure(dry_run: bool = False) -> Dict[str, Path]:
    """
    Create sub-directories for each use case.
    
    Returns:
        Dictionary mapping use case ID to directory path
    """
    directories = {}
    
    for uc_id in USE_CASE_IDS:
        uc_dir = BASE_DIR / uc_id
        directories[uc_id] = uc_dir
        
        if not dry_run:
            uc_dir.mkdir(exist_ok=True)
            print(f"✓ Created directory: {uc_id}/")
        else:
            print(f"[DRY RUN] Would create directory: {uc_id}/")
    
    return directories

def move_files(files_by_uc: Dict[str, List[Path]], directories: Dict[str, Path], dry_run: bool = False):
    """
    Move files to their respective use case directories.
    """
    total_files = sum(len(files) for files in files_by_uc.values())
    moved_count = 0
    
    print(f"\n{'='*80}")
    print(f"Moving {total_files} files to use case directories...")
    print(f"{'='*80}\n")
    
    for uc_id, files in sorted(files_by_uc.items()):
        if not files:
            continue
            
        print(f"\n{uc_id} ({len(files)} files):")
        print("-" * 80)
        
        for file_path in files:
            dest_path = directories[uc_id] / file_path.name
            
            if not dry_run:
                try:
                    shutil.move(str(file_path), str(dest_path))
                    print(f"  ✓ Moved: {file_path.name}")
                    moved_count += 1
                except Exception as e:
                    print(f"  ✗ Error moving {file_path.name}: {e}")
            else:
                print(f"  [DRY RUN] Would move: {file_path.name}")
                print(f"             From: {file_path.parent}")
                print(f"             To:   {dest_path.parent}")
                moved_count += 1
    
    return moved_count

def create_use_case_readme(uc_id: str, uc_dir: Path, files: List[Path], dry_run: bool = False):
    """
    Create a README.md in each use case directory listing the files.
    """
    # Get use case name from markdown file if it exists
    uc_name = uc_id
    md_files = [f for f in files if f.suffix == '.md']
    if md_files:
        # Extract name from filename
        name_match = re.match(r'UC-\d{3}-(.+)-v\d+\.\d+\.\d+\.md', md_files[0].name)
        if name_match:
            uc_name = name_match.group(1).replace('-', ' ')
    
    readme_content = f"""# {uc_id}: {uc_name}

## Use Case Files

This directory contains all files related to **{uc_id}: {uc_name}**.

### Files in This Directory

"""
    
    # Group files by type
    markdown_files = [f for f in files if f.suffix == '.md']
    blueprint_files = [f for f in files if 'Blueprint' in f.name and f.suffix == '.drawio']
    sequence_files = [f for f in files if 'Sequence' in f.name and f.suffix == '.drawio']
    generated_files = [f for f in files if 'Generated' in f.name and f.suffix == '.drawio']
    other_files = [f for f in files if f not in markdown_files + blueprint_files + sequence_files + generated_files]
    
    if markdown_files:
        readme_content += "#### Use Case Document\n"
        for f in markdown_files:
            readme_content += f"- 📄 **{f.name}** - Main use case documentation\n"
        readme_content += "\n"
    
    if blueprint_files:
        readme_content += "#### Architecture Diagrams (Blueprint)\n"
        for f in blueprint_files:
            readme_content += f"- 🏗️ **{f.name}**\n"
        readme_content += "\n"
    
    if sequence_files:
        readme_content += "#### Sequence Diagrams\n"
        for f in sequence_files:
            readme_content += f"- 🔄 **{f.name}**\n"
        readme_content += "\n"
    
    if generated_files:
        readme_content += "#### Generated Diagrams\n"
        for f in generated_files:
            readme_content += f"- 📊 **{f.name}**\n"
        readme_content += "\n"
    
    if other_files:
        readme_content += "#### Other Files\n"
        for f in other_files:
            readme_content += f"- 📎 **{f.name}**\n"
        readme_content += "\n"
    
    readme_content += f"""
## Related Resources

- **Main Use Case Document**: See the .md file above for comprehensive documentation
- **Architecture Patterns**: See `../patterns/` directory for referenced patterns
- **Prioritization Framework**: See `../USE-CASE-PRIORITISATION-FRAMEWORK.md`
- **All Use Cases**: See parent directory for other use cases

## Quick Links

- [Back to Use Case Prioritisation](../)
- [Use Case Template](../USE-CASE-TEMPLATE.md)
- [Architecture Patterns](../patterns/)

---

**Last Updated**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}
"""
    
    readme_path = uc_dir / 'README.md'
    
    if not dry_run:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"  ✓ Created README.md")
    else:
        print(f"  [DRY RUN] Would create README.md")

def update_main_readme(files_by_uc: Dict[str, List[Path]], dry_run: bool = False):
    """
    Update the main README.md to reflect the new organization.
    """
    readme_path = BASE_DIR / 'README.md'
    
    # Read existing README if it exists
    existing_content = ""
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()
    
    # Create new section for organized use cases
    new_section = """
## Use Case Organization

All use case files have been organized into individual sub-directories:

"""
    
    for uc_id in USE_CASE_IDS:
        if uc_id in files_by_uc:
            file_count = len(files_by_uc[uc_id])
            new_section += f"- **[{uc_id}/]({uc_id}/)** - {file_count} files\n"
    
    new_section += """
Each use case directory contains:
- Use case markdown document
- Architecture diagrams (Blueprint)
- Sequence diagrams
- Related files
- README.md with file inventory

"""
    
    if not dry_run:
        # Append to existing README or create new one
        if "## Use Case Organization" in existing_content:
            # Replace existing section
            lines = existing_content.split('\n')
            new_lines = []
            skip = False
            for line in lines:
                if line.startswith("## Use Case Organization"):
                    skip = True
                    new_lines.append(new_section.strip())
                elif skip and line.startswith("##"):
                    skip = False
                    new_lines.append(line)
                elif not skip:
                    new_lines.append(line)
            updated_content = '\n'.join(new_lines)
        else:
            updated_content = existing_content + "\n\n" + new_section
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"\n✓ Updated main README.md")
    else:
        print(f"\n[DRY RUN] Would update main README.md")

def cleanup_empty_directories(dry_run: bool = False):
    """
    Remove empty directories after moving files.
    """
    use_cases_dir = BASE_DIR / 'use-cases'
    
    if use_cases_dir.exists():
        remaining_files = list(use_cases_dir.glob('*'))
        # Keep only README.md
        if len(remaining_files) <= 1 and all(f.name == 'README.md' for f in remaining_files):
            if not dry_run:
                # Don't delete, just note it
                print(f"\n✓ use-cases/ directory now only contains README.md (kept for reference)")
            else:
                print(f"\n[DRY RUN] use-cases/ directory would only contain README.md")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Organize BNZ AI use case files into individual sub-folders',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python organize_use_cases.py --dry-run    # Preview changes without moving files
  python organize_use_cases.py              # Actually organize files
        """
    )
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be moved without actually moving files')
    
    args = parser.parse_args()
    
    print("="*80)
    print("BNZ AI Use Case File Organization")
    print("="*80)
    
    if args.dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be moved\n")
    
    # Step 1: Scan for files
    print("\nStep 1: Scanning for use case files...")
    files_by_uc = get_files_to_organize()
    
    total_use_cases = len(files_by_uc)
    total_files = sum(len(files) for files in files_by_uc.values())
    
    print(f"✓ Found {total_files} files across {total_use_cases} use cases")
    
    # Show summary
    print("\nSummary by Use Case:")
    print("-" * 80)
    for uc_id, files in sorted(files_by_uc.items()):
        if files:
            print(f"  {uc_id}: {len(files):2d} files")
    
    if not files_by_uc:
        print("\n⚠️  No use case files found to organize!")
        return
    
    # Step 2: Create directories
    print("\n" + "="*80)
    print("Step 2: Creating use case directories...")
    print("="*80)
    directories = create_directory_structure(dry_run=args.dry_run)
    
    # Step 3: Move files
    moved_count = move_files(files_by_uc, directories, dry_run=args.dry_run)
    
    # Step 4: Create README files
    print("\n" + "="*80)
    print("Step 4: Creating README.md files in each directory...")
    print("="*80 + "\n")
    for uc_id, files in files_by_uc.items():
        if files:
            create_use_case_readme(uc_id, directories[uc_id], files, dry_run=args.dry_run)
    
    # Step 5: Update main README
    print("\n" + "="*80)
    print("Step 5: Updating main README.md...")
    print("="*80)
    update_main_readme(files_by_uc, dry_run=args.dry_run)
    
    # Step 6: Cleanup
    print("\n" + "="*80)
    print("Step 6: Cleanup...")
    print("="*80)
    cleanup_empty_directories(dry_run=args.dry_run)
    
    # Final summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Use cases organized: {total_use_cases}")
    print(f"Files moved: {moved_count}")
    print(f"Directories created: {len(directories)}")
    
    if args.dry_run:
        print("\n⚠️  DRY RUN COMPLETE - No files were actually moved")
        print("Run without --dry-run to perform the actual organization")
    else:
        print("\n✅ ORGANIZATION COMPLETE!")
        print(f"\nAll use case files are now organized in individual sub-directories:")
        print(f"  {BASE_DIR}/UC-001/")
        print(f"  {BASE_DIR}/UC-002/")
        print(f"  ...")
        print(f"  {BASE_DIR}/UC-024/")
    
    print("="*80)

if __name__ == "__main__":
    main()

