# Use Case File Organization - Summary

## ✅ Organization Complete

Successfully organized **102 files across 24 use case sub-directories** using the `organize_use_cases.py` script.

## What Was Done

### 1. Created Sub-Directories (24 directories)
Created individual sub-folders for each use case:
- `[UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md)/` through `[UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md)/`
- Each directory contains all files related to that specific use case

### 2. Moved Files (102 files)
Organized all use case-related files into their respective directories:
- **Markdown documents** (.md) - Use case documentation
- **Blueprint diagrams** (.drawio) - Architecture diagrams
- **Sequence diagrams** (.drawio) - Sequence/flow diagrams  
- **Generated diagrams** (.drawio) - Auto-generated diagrams

### 3. Created README Files (24 files)
Generated a `README.md` in each use case directory with:
- File inventory grouped by type
- Quick links to related resources
- Navigation back to parent directory

### 4. Updated Main README
Updated the main `README.md` with:
- New "Use Case Organization" section
- Links to all 24 use case directories
- File count per directory

## New Directory Structure

```
use-case-prioritisation/
│
├── UC-001/                          ← FrontLine - Partnership Banking (8 files)
│   ├── README.md
│   ├── UC-001-FrontLine-Partnership-Banking-v1.0.0.md
│   ├── UC-001-Partnership-Banking-Blueprint-v1.0.0.drawio
│   ├── UC-001-FrontLine---Partnership-Banking-Blueprint-Business-v1.0.0.drawio
│   ├── UC-001-FrontLine---Partnership-Banking-Blueprint-Standard-v1.0.0.drawio
│   ├── UC-001-FrontLine---Partnership-Banking-Blueprint-Technical-v1.0.0.drawio
│   ├── UC-001-FrontLine---Partnership-Banking-Blueprint-Sample-v1.0.0.drawio
│   ├── UC-001-FrontLine---Partnership-Banking-Generated-v1.0.0.drawio
│   └── SCN-001-FrontLine---Partnership-Banking-Sequence-v1.0.0.drawio
│
├── UC-002/                          ← Finance (4 files)
│   ├── README.md
│   ├── UC-002-Finance-v1.0.0.md
│   ├── UC-002-Finance-Blueprint-v1.0.0.drawio
│   ├── UC-002-Finance-Generated-v1.0.0.drawio
│   └── SCN-002-Finance-Sequence-v1.0.0.drawio
│
├── UC-003/                          ← Analytics and Reporting (4 files)
├── UC-004/                          ← Credit Risk (4 files)
├── UC-005/                          ← Lending Ops (4 files)
├── UC-006/                          ← HyperPersonalization (3 files)
├── UC-007/                          ← Contact Centre (4 files)
├── UC-008/                          ← Security AI (4 files)
├── UC-009/                          ← Data Products (4 files)
├── UC-010/                          ← SDLC (5 files)
├── UC-011/                          ← Fincrime (4 files)
├── UC-012/                          ← QA/QC (4 files)
├── UC-013/                          ← Fraud Ops (4 files)
├── UC-014/                          ← Onboarding (4 files)
├── UC-015/                          ← Risk Functions (5 files)
├── UC-016/                          ← IT Ops (4 files)
├── UC-017/                          ← FrontLine - CIB (4 files)
├── UC-018/                          ← Procurement (4 files)
├── UC-019/                          ← Payment Disputes (4 files)
├── UC-020/                          ← Controls Testing (5 files)
├── UC-021/                          ← Wholesale Underwriting (4 files)
├── UC-022/                          ← Learning Content (4 files)
├── UC-023/                          ← Collection Management (4 files)
└── UC-024/                          ← Front-end App Personalisation (4 files)
```

## Files Kept in Root Directory

The following files remain in the root `use-case-prioritisation/` directory:

### Documentation
- `README.md` - Main directory guide (updated)
- `USE-CASE-TEMPLATE.md` - Master template
- `USE-CASE-TEMPLATE-GUIDE.md` - Template usage guide
- `USE-CASE-TEMPLATE-README.md` - Quick reference
- `USE-CASE-PRIORITISATION-FRAMEWORK.md` - Prioritization framework
- `USE-CASE-RESEARCH-2025-SUMMARY.md` - Research summary
- `USE-CASE-GENERATION-SUMMARY.md` - Generation summary
- `SPREADSHEET-USER-GUIDE.md` - Spreadsheet guide
- `FILE-ORGANIZATION-SUMMARY.md` - This file

### Data Files
- `BNZ-Use-Cases.csv` - Original use case data
- `BNZ-Use-Cases-Enhanced-2025.csv` - Enhanced data
- `BNZ-Use-Cases.xlsx` - Excel version
- `BNZ List of AI use cases Dec 25.xlsx` - Latest list
- `UseCase-Pattern-Mapping.csv` - Pattern mappings
- `Pattern-UseCase-Mapping.csv` - Reverse mappings
- `ai-architecture-building-blocks.xlsx` - ABB catalog
- `BNZ_AI_Use_Case_Prioritisation.xlsx` - Prioritization spreadsheet
- `BNZ_AI_Use_Case_Prioritisation-Solution.csv` - Solution data

### Scripts
- `organize_use_cases.py` - This organization script
- `generate_use_cases.py` - Use case generation script
- `create_prioritization_spreadsheet.py` - Spreadsheet creation

### Summary Files
- `AI-Use-Cases-Quick-Reference.md`
- `AI-Use-Cases-Enhancement-Summary.md`
- `AI-Use-Cases-Data-Summary.md`
- `AI-Use-Cases-Categories-Summary.md`
- `Plan.md`

### Directories
- `patterns/` - Architecture patterns (PT-001 to PT-018)
- `data/` - Additional data files and analysis
- `scripts/` - Blueprint and diagram generation scripts
- `approach/` - Prioritization approach and research
- `use-cases/` - Now only contains README.md (kept for reference)

## File Organization by Use Case

| Use Case | Files | Types |
|----------|-------|-------|
| [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) | 8 | 1 MD, 6 Blueprint, 1 Sequence |
| [UC-002](use-cases/UC-002/UC-002-Finance-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-003](use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-004](use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-005](use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) | 3 | 1 MD, 1 Blueprint, 1 Sequence |
| [UC-007](use-cases/UC-007/UC-007-Contact-Centre-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-008](use-cases/UC-008/UC-008-Security-AI-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-009](use-cases/UC-009/UC-009-Data-Products-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-010](use-cases/UC-010/UC-010-SDLC-v1.0.0.md) | 5 | 1 MD, 3 Blueprint, 1 Sequence |
| [UC-011](use-cases/UC-011/UC-011-Fincrime-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-012](use-cases/UC-012/UC-012-QA-QC-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-013](use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-014](use-cases/UC-014/UC-014-Onboarding-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-015](use-cases/UC-015/UC-015-Risk-Functions-v1.0.0.md) | 5 | 1 MD, 3 Blueprint, 1 Sequence |
| [UC-016](use-cases/UC-016/UC-016-IT-Ops-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-017](use-cases/UC-017/UC-017-FrontLine---CIB-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-018](use-cases/UC-018/UC-018-Procurement-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-019](use-cases/UC-019/UC-019-Payment-Disputes-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-020](use-cases/UC-020/UC-020-Controls-Testing-v1.0.0.md) | 5 | 1 MD, 3 Blueprint, 1 Sequence |
| [UC-021](use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-022](use-cases/UC-022/UC-022-Learning-Content-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-023](use-cases/UC-023/UC-023-Collection-Management-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| [UC-024](use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md) | 4 | 1 MD, 2 Blueprint, 1 Sequence |
| **Total** | **102** | **24 MD, 54 Blueprint, 24 Sequence** |

## Benefits of This Organization

### 1. **Improved Navigation**
- Each use case has its own dedicated folder
- Easy to find all files related to a specific use case
- Clear separation between use cases

### 2. **Better Organization**
- Related files grouped together
- Reduced clutter in root directory
- Consistent structure across all use cases

### 3. **Enhanced Discoverability**
- Each directory has a README with file inventory
- Clear file naming conventions maintained
- Easy to identify file types (Blueprint, Sequence, Generated)

### 4. **Simplified Maintenance**
- Easy to add new files to specific use case
- Simple to update or replace files
- Clear ownership per use case

### 5. **Improved Collaboration**
- Product Owners can focus on their use case directory
- Enterprise Architects can work on specific use cases
- Reduced risk of file conflicts

## Script Features

The `organize_use_cases.py` script includes:

### Core Functionality
- ✅ Automatic use case ID extraction from filenames
- ✅ Handles multiple file naming patterns ([UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md), UC01, SCN-001)
- ✅ Creates sub-directories for all 24 use cases
- ✅ Moves files to appropriate directories
- ✅ Generates README.md in each directory
- ✅ Updates main README.md

### Safety Features
- ✅ **Dry-run mode** (`--dry-run`) to preview changes
- ✅ Excludes template and framework files
- ✅ Preserves important root-level files
- ✅ Error handling for move operations
- ✅ Comprehensive logging and progress reporting

### Smart Organization
- ✅ Groups files by type in README (Blueprint, Sequence, Generated)
- ✅ Extracts use case names from filenames
- ✅ Creates navigation links in READMEs
- ✅ Maintains file version numbers

## Usage Examples

### Preview Changes (Dry Run)
```bash
python organize_use_cases.py --dry-run
```

### Perform Organization
```bash
python organize_use_cases.py
```

### Re-run if Needed
The script is idempotent - can be run multiple times safely. It will:
- Create directories if they don't exist
- Move files that aren't already in correct location
- Update READMEs

## Navigation

### To Access a Specific Use Case
```
cd UC-001/          # FrontLine - Partnership Banking
cd UC-004/          # Credit Risk
cd UC-009/          # Data Products
```

### To View All Use Cases
```
ls UC-*/            # List all use case directories
ls UC-*/README.md   # List all use case READMEs
```

### To Find a Specific File Type
```
ls UC-*/SCN-*.drawio    # All sequence diagrams
ls UC-*/*Blueprint*.drawio  # All blueprint diagrams
ls UC-*/*.md        # All markdown documents
```

## Integration with Existing Workflow

This organization complements the existing structure:

### Prioritization Workflow
1. **Review** use case documents in individual directories
2. **Reference** patterns from `patterns/` directory
3. **Use** prioritization spreadsheet in root
4. **Follow** framework in `USE-CASE-PRIORITISATION-FRAMEWORK.md`

### Development Workflow
1. **Navigate** to specific use case directory (e.g., `[UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md)/`)
2. **Review** markdown document for requirements
3. **Reference** blueprint diagrams for architecture
4. **Use** sequence diagrams for implementation flow

### Documentation Workflow
1. **Update** markdown document in use case directory
2. **Add** new diagrams to use case directory
3. **Update** README.md if adding new file types
4. **Commit** changes per use case

## Maintenance

### Adding New Files
To add a new file to a use case:
1. Save file with proper naming convention (UC-XXX-*.*)
2. Move to appropriate directory (UC-XXX/)
3. Update README.md if it's a new file type

### Adding New Use Cases
If UC-025 or beyond are added:
1. Update `USE_CASE_IDS` in `organize_use_cases.py`
2. Run script to create new directory
3. Add files following naming convention

### Reorganizing
If reorganization is needed:
1. Run `organize_use_cases.py --dry-run` to preview
2. Review changes
3. Run `organize_use_cases.py` to execute

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Use Cases Organized** | 24 |
| **Files Moved** | 102 |
| **Directories Created** | 24 |
| **READMEs Generated** | 24 |
| **Markdown Documents** | 24 |
| **Blueprint Diagrams** | 54 |
| **Sequence Diagrams** | 24 |
| **Average Files per Use Case** | 4.25 |
| **Largest Use Case** | [UC-001](use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md) (8 files) |
| **Smallest Use Case** | [UC-006](use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md) (3 files) |

## Success Criteria

✅ All use case files organized into sub-directories  
✅ Each directory contains all related files  
✅ README.md created in each directory  
✅ Main README.md updated with new structure  
✅ Root directory cleaned up (only framework files remain)  
✅ Script can be re-run safely  
✅ Dry-run mode available for testing  
✅ Comprehensive logging and error handling  

## Next Steps

### Immediate
1. ✅ Review the new organization (you are here)
2. ✅ Verify all files are in correct directories
3. ✅ Test navigation and file access

### Short Term
1. Update any scripts or tools that reference old file locations
2. Update documentation links if needed
3. Communicate new structure to team

### Ongoing
1. Maintain organization when adding new files
2. Update READMEs as files are added/removed
3. Run organize script periodically to catch any misplaced files

## Questions or Issues?

### File Not Found?
- Check the use case directory (UC-XXX/)
- Check if it's in the excluded files list (root directory)
- Run `organize_use_cases.py --dry-run` to see where it would go

### Need to Reorganize?
- Run `organize_use_cases.py` again (safe to re-run)
- Use `--dry-run` first to preview changes

### Script Issues?
- Check Python version (requires Python 3.6+)
- Review error messages in output
- Contact Enterprise Architecture team

---

**Organization Date**: 2025-12-05  
**Script**: `organize_use_cases.py`  
**Status**: Complete ✅  
**Files Organized**: 102 files across 24 use cases  
**Maintained By**: BNZ Enterprise Architecture

