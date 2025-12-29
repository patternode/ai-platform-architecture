#!/usr/bin/env python3
"""
BNZ AI Use Case Integrity Verification Script

This script verifies the integrity and completeness of all use case information:
- Checks all 24 use case directories exist
- Verifies required files are present
- Validates markdown document structure
- Checks diagram files
- Generates comprehensive integrity report
- Optionally fixes common issues

Usage:
    python verify_use_case_integrity.py [--fix] [--verbose]
    
Options:
    --fix       Automatically fix common issues (create missing READMEs, etc.)
    --verbose   Show detailed progress information
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
import argparse
from datetime import datetime

# Define the base directory
BASE_DIR = Path(__file__).parent

# Expected use case IDs
EXPECTED_USE_CASES = [f"UC-{i:03d}" for i in range(1, 25)]  # UC-001 through UC-024

# Use case metadata (from existing data)
USE_CASE_METADATA = {
    "UC-001": {"name": "FrontLine - Partnership Banking", "wave": "Wave 1", "priority": "Priority 1"},
    "UC-002": {"name": "Finance", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-003": {"name": "Analytics and Reporting", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-004": {"name": "Credit Risk", "wave": "Wave 1", "priority": "Priority 1"},
    "UC-005": {"name": "Lending Ops", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-006": {"name": "HyperPersonalization", "wave": "Wave 1", "priority": "Priority 1"},
    "UC-007": {"name": "Contact Centre", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-008": {"name": "Security AI", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-009": {"name": "Data Products", "wave": "Wave 1", "priority": "Priority 1"},
    "UC-010": {"name": "SDLC", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-011": {"name": "Fincrime", "wave": "Wave 1", "priority": "Priority 1"},
    "UC-012": {"name": "QA/QC", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-013": {"name": "Fraud Ops", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-014": {"name": "Onboarding", "wave": "Wave 2", "priority": "Priority 2"},
    "UC-015": {"name": "Risk Functions", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-016": {"name": "IT Ops", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-017": {"name": "FrontLine - CIB", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-018": {"name": "Procurement", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-019": {"name": "Payment Disputes", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-020": {"name": "Controls Testing", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-021": {"name": "Wholesale Underwriting", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-022": {"name": "Learning Content", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-023": {"name": "Collection Management", "wave": "Wave 3", "priority": "Priority 3"},
    "UC-024": {"name": "Front-end App Personalisation", "wave": "Wave 2", "priority": "Priority 2"},
}

# Required files for each use case
REQUIRED_FILES = {
    "markdown": "*.md",  # Use case document
    "readme": "README.md",  # Directory README
    "sequence": "SCN-*.drawio",  # Sequence diagram
}

# Optional files
OPTIONAL_FILES = {
    "blueprint": "*Blueprint*.drawio",  # Blueprint diagrams (multiple variants)
    "generated": "*Generated*.drawio",  # Generated diagrams
}

class UseCaseIntegrityChecker:
    """Main integrity checker class."""
    
    def __init__(self, verbose: bool = False, fix: bool = False):
        self.verbose = verbose
        self.fix = fix
        self.issues = []
        self.warnings = []
        self.fixed = []
        self.stats = {
            "total_use_cases": 0,
            "complete": 0,
            "missing_files": 0,
            "invalid_structure": 0,
            "missing_directories": 0,
        }
    
    def log(self, message: str, level: str = "info"):
        """Log message with level."""
        if level == "error":
            self.issues.append(message)
            print(f"  ✗ ERROR: {message}")
        elif level == "warning":
            self.warnings.append(message)
            print(f"  ⚠ WARNING: {message}")
        elif level == "fixed":
            self.fixed.append(message)
            print(f"  ✓ FIXED: {message}")
        elif level == "success":
            print(f"  ✓ {message}")
        elif self.verbose:
            print(f"  ℹ {message}")
    
    def check_directory_exists(self, uc_id: str) -> bool:
        """Check if use case directory exists."""
        uc_dir = BASE_DIR / uc_id
        if not uc_dir.exists():
            self.log(f"{uc_id}: Directory not found", "error")
            self.stats["missing_directories"] += 1
            return False
        return True
    
    def find_files_by_pattern(self, uc_dir: Path, pattern: str) -> List[Path]:
        """Find files matching pattern in directory."""
        return list(uc_dir.glob(pattern))
    
    def check_required_files(self, uc_id: str, uc_dir: Path) -> Dict[str, bool]:
        """Check if all required files are present."""
        results = {}
        
        # Check markdown document
        md_files = self.find_files_by_pattern(uc_dir, "*.md")
        md_files = [f for f in md_files if f.name != "README.md"]
        
        if not md_files:
            self.log(f"{uc_id}: Missing use case markdown document", "error")
            results["markdown"] = False
            self.stats["missing_files"] += 1
        elif len(md_files) > 1:
            self.log(f"{uc_id}: Multiple markdown documents found: {[f.name for f in md_files]}", "warning")
            results["markdown"] = True
        else:
            results["markdown"] = True
            if self.verbose:
                self.log(f"{uc_id}: Found {md_files[0].name}", "info")
        
        # Check README
        readme = uc_dir / "README.md"
        if not readme.exists():
            self.log(f"{uc_id}: Missing README.md", "warning")
            results["readme"] = False
            self.stats["missing_files"] += 1
        else:
            results["readme"] = True
        
        # Check sequence diagram
        seq_files = self.find_files_by_pattern(uc_dir, "SCN-*.drawio")
        if not seq_files:
            self.log(f"{uc_id}: Missing sequence diagram (SCN-*.drawio)", "warning")
            results["sequence"] = False
        else:
            results["sequence"] = True
            if self.verbose:
                self.log(f"{uc_id}: Found {len(seq_files)} sequence diagram(s)", "info")
        
        # Check blueprint diagrams (optional but expected)
        blueprint_files = self.find_files_by_pattern(uc_dir, "*Blueprint*.drawio")
        if not blueprint_files:
            self.log(f"{uc_id}: No blueprint diagrams found (optional)", "warning")
            results["blueprint"] = False
        else:
            results["blueprint"] = True
            if self.verbose:
                self.log(f"{uc_id}: Found {len(blueprint_files)} blueprint diagram(s)", "info")
        
        return results
    
    def validate_markdown_document(self, uc_id: str, uc_dir: Path) -> bool:
        """Validate the structure of the markdown document."""
        md_files = [f for f in uc_dir.glob("*.md") if f.name != "README.md"]
        
        if not md_files:
            return False
        
        md_file = md_files[0]
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for required sections
            required_sections = [
                "# " + uc_id,  # Title
                "## Document Control",
                "## 1. Executive Summary",
                "## 2. Business Case",
                "## 6. Prioritization Scoring",
            ]
            
            missing_sections = []
            for section in required_sections:
                if section not in content:
                    missing_sections.append(section)
            
            if missing_sections:
                self.log(f"{uc_id}: Markdown document missing sections: {missing_sections}", "warning")
                return False
            
            # Check if it's just a stub (very short)
            if len(content) < 1000:
                self.log(f"{uc_id}: Markdown document appears to be a stub (< 1000 chars)", "warning")
                return False
            
            return True
            
        except Exception as e:
            self.log(f"{uc_id}: Error reading markdown document: {e}", "error")
            return False
    
    def create_readme_if_missing(self, uc_id: str, uc_dir: Path) -> bool:
        """Create README.md if missing (fix mode)."""
        readme_path = uc_dir / "README.md"
        
        if readme_path.exists():
            return False
        
        if not self.fix:
            return False
        
        # Get use case metadata
        metadata = USE_CASE_METADATA.get(uc_id, {"name": uc_id, "wave": "TBD", "priority": "TBD"})
        uc_name = metadata["name"]
        
        # Get files in directory
        all_files = list(uc_dir.glob("*"))
        md_files = [f for f in all_files if f.suffix == ".md" and f.name != "README.md"]
        drawio_files = [f for f in all_files if f.suffix == ".drawio"]
        blueprint_files = [f for f in drawio_files if "Blueprint" in f.name]
        sequence_files = [f for f in drawio_files if "SCN-" in f.name]
        generated_files = [f for f in drawio_files if "Generated" in f.name]
        other_files = [f for f in drawio_files if f not in blueprint_files + sequence_files + generated_files]
        
        # Create README content
        readme_content = f"""# {uc_id}: {uc_name}

## Use Case Files

This directory contains all files related to **{uc_id}: {uc_name}**.

### Files in This Directory

"""
        
        if md_files:
            readme_content += "#### Use Case Document\n"
            for f in md_files:
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
- **Architecture Patterns**: See `../../patterns/` directory for referenced patterns
- **Prioritization Framework**: See `../../USE-CASE-PRIORITISATION-FRAMEWORK.md`
- **All Use Cases**: See parent directory for other use cases

## Quick Links

- [Back to Use Cases](../)
- [Use Case Template](../../USE-CASE-TEMPLATE.md)
- [Architecture Patterns](../../patterns/)

---

**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
**Wave**: {metadata['wave']}
**Priority**: {metadata['priority']}
"""
        
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            self.log(f"{uc_id}: Created README.md", "fixed")
            return True
        except Exception as e:
            self.log(f"{uc_id}: Failed to create README.md: {e}", "error")
            return False
    
    def check_use_case(self, uc_id: str) -> Dict:
        """Perform comprehensive check on a single use case."""
        result = {
            "uc_id": uc_id,
            "exists": False,
            "complete": False,
            "files": {},
            "issues": []
        }
        
        # Check directory exists
        if not self.check_directory_exists(uc_id):
            result["issues"].append("Directory not found")
            return result
        
        result["exists"] = True
        uc_dir = BASE_DIR / uc_id
        
        # Check required files
        file_results = self.check_required_files(uc_id, uc_dir)
        result["files"] = file_results
        
        # Try to fix missing README if in fix mode
        if not file_results.get("readme", False):
            if self.create_readme_if_missing(uc_id, uc_dir):
                file_results["readme"] = True
        
        # Validate markdown document
        if file_results.get("markdown", False):
            if not self.validate_markdown_document(uc_id, uc_dir):
                result["issues"].append("Markdown document validation failed")
        
        # Check if complete
        required_complete = file_results.get("markdown", False) and file_results.get("readme", False)
        if required_complete:
            result["complete"] = True
            self.stats["complete"] += 1
        else:
            self.stats["invalid_structure"] += 1
        
        return result
    
    def check_all_use_cases(self) -> List[Dict]:
        """Check all use cases."""
        results = []
        
        print("\n" + "="*80)
        print("BNZ AI Use Case Integrity Check")
        print("="*80)
        print(f"Checking {len(EXPECTED_USE_CASES)} use cases...")
        print("="*80 + "\n")
        
        for uc_id in EXPECTED_USE_CASES:
            self.stats["total_use_cases"] += 1
            
            metadata = USE_CASE_METADATA.get(uc_id, {})
            uc_name = metadata.get("name", "Unknown")
            
            print(f"\n{uc_id}: {uc_name}")
            print("-" * 80)
            
            result = self.check_use_case(uc_id)
            results.append(result)
            
            if result["complete"]:
                self.log(f"Complete and valid", "success")
            elif not result["exists"]:
                self.log(f"Directory missing", "error")
            else:
                self.log(f"Incomplete or has issues", "warning")
        
        return results
    
    def generate_report(self, results: List[Dict]):
        """Generate comprehensive integrity report."""
        print("\n" + "="*80)
        print("INTEGRITY CHECK REPORT")
        print("="*80)
        
        # Summary statistics
        print("\n📊 Summary Statistics:")
        print("-" * 80)
        print(f"Total Use Cases:        {self.stats['total_use_cases']}")
        print(f"Complete & Valid:       {self.stats['complete']}")
        print(f"Incomplete/Invalid:     {self.stats['invalid_structure']}")
        print(f"Missing Directories:    {self.stats['missing_directories']}")
        print(f"Missing Files:          {self.stats['missing_files']}")
        
        completion_rate = (self.stats['complete'] / self.stats['total_use_cases'] * 100) if self.stats['total_use_cases'] > 0 else 0
        print(f"\nCompletion Rate:        {completion_rate:.1f}%")
        
        # Issues summary
        if self.issues:
            print(f"\n❌ Issues Found: {len(self.issues)}")
            print("-" * 80)
            for issue in self.issues[:10]:  # Show first 10
                print(f"  • {issue}")
            if len(self.issues) > 10:
                print(f"  ... and {len(self.issues) - 10} more issues")
        
        # Warnings summary
        if self.warnings:
            print(f"\n⚠️  Warnings: {len(self.warnings)}")
            print("-" * 80)
            for warning in self.warnings[:10]:  # Show first 10
                print(f"  • {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more warnings")
        
        # Fixed items
        if self.fixed:
            print(f"\n✅ Items Fixed: {len(self.fixed)}")
            print("-" * 80)
            for fixed_item in self.fixed:
                print(f"  • {fixed_item}")
        
        # Detailed results by wave
        print("\n📋 Use Cases by Wave:")
        print("-" * 80)
        
        for wave in ["Wave 1", "Wave 2", "Wave 3"]:
            wave_ucs = [uc for uc in EXPECTED_USE_CASES if USE_CASE_METADATA.get(uc, {}).get("wave") == wave]
            complete_count = sum(1 for r in results if r["uc_id"] in wave_ucs and r["complete"])
            
            print(f"\n{wave} ({complete_count}/{len(wave_ucs)} complete):")
            for uc_id in wave_ucs:
                result = next((r for r in results if r["uc_id"] == uc_id), None)
                if result:
                    status = "✓" if result["complete"] else "✗"
                    uc_name = USE_CASE_METADATA.get(uc_id, {}).get("name", "Unknown")
                    print(f"  {status} {uc_id}: {uc_name}")
        
        # Recommendations
        print("\n💡 Recommendations:")
        print("-" * 80)
        
        if self.stats['missing_directories'] > 0:
            print(f"  1. Create missing directories for {self.stats['missing_directories']} use cases")
        
        if self.stats['missing_files'] > 0:
            print(f"  2. Add missing files (READMEs, documents, diagrams)")
            if not self.fix:
                print(f"     Run with --fix to automatically create missing READMEs")
        
        if self.warnings:
            print(f"  3. Review and address {len(self.warnings)} warnings")
        
        if completion_rate < 100:
            print(f"  4. Work on completing the {self.stats['invalid_structure']} incomplete use cases")
        
        # Overall status
        print("\n" + "="*80)
        if completion_rate == 100 and not self.issues:
            print("✅ ALL USE CASES COMPLETE AND VALID!")
        elif completion_rate >= 90:
            print("⚠️  MOSTLY COMPLETE - Minor issues to address")
        elif completion_rate >= 70:
            print("⚠️  PARTIALLY COMPLETE - Some work needed")
        else:
            print("❌ SIGNIFICANT ISSUES - Major work required")
        print("="*80 + "\n")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Verify integrity of BNZ AI use case information',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python verify_use_case_integrity.py              # Check integrity
  python verify_use_case_integrity.py --verbose    # Detailed output
  python verify_use_case_integrity.py --fix        # Fix common issues
  python verify_use_case_integrity.py --fix --verbose  # Fix with details
        """
    )
    parser.add_argument('--fix', action='store_true',
                       help='Automatically fix common issues (create missing READMEs)')
    parser.add_argument('--verbose', action='store_true',
                       help='Show detailed progress information')
    
    args = parser.parse_args()
    
    # Create checker
    checker = UseCaseIntegrityChecker(verbose=args.verbose, fix=args.fix)
    
    # Run checks
    results = checker.check_all_use_cases()
    
    # Generate report
    checker.generate_report(results)
    
    # Return exit code based on results
    if checker.issues:
        return 1  # Errors found
    elif checker.warnings and not args.fix:
        return 2  # Warnings found
    else:
        return 0  # All good

if __name__ == "__main__":
    exit(main())

