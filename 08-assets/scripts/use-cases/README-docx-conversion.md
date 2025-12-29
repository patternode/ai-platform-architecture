# Use Case Markdown to Word Conversion

## Overview

This folder contains scripts for converting BNZ AI Use Case markdown documents to Microsoft Word format with **high-fidelity round-trip conversion** capability. The goal is to ensure that:

```
Source Markdown → Word (.docx) → Target Markdown
```

Results in the source and target markdown being functionally identical.

## Scripts

| Script | Purpose | Documentation |
|--------|---------|---------------|
| `convert-use-cases-to-docx.ps1` | Batch convert markdown files to Word | See below |

## Prerequisites

### Required Software

1. **Pandoc 2.19+** (universal document converter)
   - Download: https://pandoc.org/installing.html
   - Or via Chocolatey: `choco install pandoc`
   - Verify installation: `pandoc --version`

2. **PowerShell 5.1 or later**
   - Check version: `$PSVersionTable.PSVersion`

### Optional Software

- **Microsoft Word** (for manual template customization)

## Quick Start

### Convert All Use Cases

```powershell
# From repository root
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1
```

### Convert Specific Use Case

```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -UseCaseId "UC-019"
```

### Dry Run (Preview)

```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -DryRun
```

### Validate Round-Trip Quality

```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Validate
```

## Script Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `-UseCaseId` | String | Specific use case ID (e.g., "UC-019") | All use cases |
| `-OutputDir` | String | Output directory for Word files | Same as markdown |
| `-DryRun` | Switch | Preview without converting | False |
| `-Force` | Switch | Overwrite existing .docx files | False |
| `-Validate` | Switch | Test round-trip conversion quality | False |

## Examples

### Basic Conversion

```powershell
# Convert all use cases
.\convert-use-cases-to-docx.ps1

# Convert specific use case
.\convert-use-cases-to-docx.ps1 -UseCaseId "UC-019"

# Convert and overwrite existing files
.\convert-use-cases-to-docx.ps1 -Force
```

### Advanced Usage

```powershell
# Convert to specific output directory
.\convert-use-cases-to-docx.ps1 -OutputDir "D:\Exports\UseCases"

# Preview what would be converted
.\convert-use-cases-to-docx.ps1 -DryRun

# Convert and validate round-trip quality
.\convert-use-cases-to-docx.ps1 -Validate

# Convert specific use case with validation
.\convert-use-cases-to-docx.ps1 -UseCaseId "UC-019" -Validate -Force
```

## Round-Trip Conversion Strategy

### Pandoc Configuration

The script uses Pandoc with settings optimized for markdown fidelity:

```powershell
pandoc input.md -o output.docx \
  --from=markdown+yaml_metadata_block+pipe_tables+backtick_code_blocks+fenced_code_attributes \
  --to=docx \
  --standalone \
  --table-of-contents \
  --toc-depth=3 \
  --number-sections \
  --highlight-style=tango \
  --reference-doc=reference-template.docx
```

### Markdown Extensions Enabled

| Extension | Purpose | Preservation |
|-----------|---------|--------------|
| `yaml_metadata_block` | YAML frontmatter | ✓ Full |
| `pipe_tables` | Markdown tables | ✓ Full |
| `backtick_code_blocks` | Code blocks with ``` | ✓ Full |
| `fenced_code_attributes` | Language syntax highlighting | ✓ Full |

### What Gets Preserved

✅ **Fully Preserved**:
- YAML frontmatter/metadata
- Markdown headers (H1-H6)
- Lists (ordered, unordered, nested)
- Tables with pipe syntax
- Code blocks with syntax highlighting
- Links (inline and reference)
- Bold, italic, strikethrough
- Blockquotes
- Horizontal rules

⚠️ **Mostly Preserved** (minor formatting differences):
- Whitespace normalization
- Line breaks (may be normalized)
- Link reference definitions (may be inlined)

❌ **Not Preserved**:
- HTML comments (`<!-- -->`)
- Raw HTML tags
- Custom CSS/styling
- Specific markdown flavors (e.g., GitHub-specific)

### Validation Process

When using `-Validate` flag, the script:

1. Converts markdown → Word
2. Converts Word → markdown (round-trip)
3. Compares original and round-trip markdown
4. Reports similarity percentage

**Perfect Match**: 100% - Files are functionally identical
**High Similarity**: 95-99% - Minor whitespace differences
**Moderate Similarity**: 90-94% - Some formatting differences
**Low Similarity**: <90% - Significant differences (investigate)

## BNZ Styling Template

### Reference Template

The script automatically creates a `reference-template.docx` file with default styling. This template controls:

- Font families and sizes
- Heading styles (H1-H6)
- Table formatting
- Code block styling
- Link colors
- Paragraph spacing

### Customizing the Template

1. **Locate the template**:
   ```powershell
   D:\Work\BNZ\ai-platform-architecture\08-assets\scripts\use-cases\reference-template.docx
   ```

2. **Open in Microsoft Word**

3. **Modify styles**:
   - Home → Styles → Modify
   - Update fonts to BNZ approved fonts (Calibri/Arial)
   - Set heading colors to BNZ Navy Blue (#003087)
   - Set accent colors to BNZ Orange (#FF6B35)

4. **Save template** (keep filename)

5. **Re-run conversion** to apply new styling

### BNZ Visual Standards

Apply these standards when customizing the template:

| Element | Standard |
|---------|----------|
| **Body Font** | Calibri 11pt |
| **Heading Font** | Calibri Bold |
| **Primary Color** | BNZ Navy Blue (#003087) |
| **Accent Color** | BNZ Orange (#FF6B35) |
| **Table Borders** | 1pt Medium Gray (#666666) |
| **Code Font** | Consolas 10pt |

See: `05-governance/standards/visual-design/visual-design-standard.md`

## Troubleshooting

### Pandoc Not Found

**Error**: `Pandoc is not installed or not in PATH`

**Solution**:
```powershell
# Install via Chocolatey
choco install pandoc

# Or download from https://pandoc.org/installing.html
# Then add to PATH
```

### Old Pandoc Version

**Warning**: `Pandoc version X.X is older than recommended 2.19`

**Solution**:
```powershell
# Upgrade via Chocolatey
choco upgrade pandoc

# Or download latest from https://pandoc.org/installing.html
```

### Conversion Fails

**Error**: `Failed: UC-XXX-...`

**Solution**:
1. Check markdown file is valid
2. Ensure no special characters in filename
3. Run with verbose output: `$VerbosePreference = 'Continue'`
4. Check Pandoc logs

### Low Round-Trip Similarity

**Warning**: `Round-trip similarity: 85%`

**Causes**:
- Complex nested formatting
- Custom HTML in markdown
- Non-standard markdown extensions

**Solution**:
1. Simplify markdown structure
2. Remove raw HTML
3. Use standard markdown syntax only

### Reference Template Not Applied

**Warning**: `No reference template found, using default styling`

**Solution**:
```powershell
# Delete existing template to regenerate
Remove-Item .\reference-template.docx

# Re-run script to create fresh template
.\convert-use-cases-to-docx.ps1
```

## File Locations

### Input Files

```
01-motivation/03-use-cases/use-cases/
├── UC-001/
│   └── UC-001-...-v1.0.0.md          # Source markdown
├── UC-002/
│   └── UC-002-...-v1.0.0.md
└── ...
```

### Output Files

By default, Word files are created alongside markdown files:

```
01-motivation/03-use-cases/use-cases/
├── UC-001/
│   ├── UC-001-...-v1.0.0.md          # Original
│   └── UC-001-...-v1.0.0.docx        # Generated ✓
├── UC-002/
│   ├── UC-002-...-v1.0.0.md
│   └── UC-002-...-v1.0.0.docx        # Generated ✓
└── ...
```

### Custom Output Directory

```powershell
# Specify custom output location
.\convert-use-cases-to-docx.ps1 -OutputDir "D:\Exports\UseCases"
```

Results in:
```
D:\Exports\UseCases/
├── UC-001-...-v1.0.0.docx
├── UC-002-...-v1.0.0.docx
└── ...
```

## Best Practices

### For Authors

1. **Use Standard Markdown**: Stick to CommonMark/GFM syntax
2. **Avoid HTML**: Don't embed raw HTML in markdown
3. **Simple Tables**: Use pipe tables, avoid complex colspan/rowspan
4. **Code Blocks**: Always use ``` with language identifiers
5. **YAML Frontmatter**: Keep metadata structured and simple

### For Conversions

1. **Test First**: Use `-DryRun` before bulk conversion
2. **Validate**: Run with `-Validate` on a sample before converting all
3. **Backup**: Keep original markdown files (script doesn't modify them)
4. **Customize Template**: Set up reference template before bulk conversion
5. **Check Output**: Review first few converted files manually

### For Distribution

1. **Word Only for Review**: Markdown is source of truth
2. **Regenerate if Needed**: Re-convert from markdown rather than editing Word
3. **Version Control**: Commit both .md and .docx to git if needed
4. **Naming Convention**: Word files use same name as markdown (different extension)

## Integration with Workflows

### Manual Review Process

```powershell
# 1. Convert use cases for stakeholder review
.\convert-use-cases-to-docx.ps1 -Validate

# 2. Distribute Word files to reviewers
# 3. Collect feedback in Word comments
# 4. Manually update markdown source files
# 5. Regenerate Word files
.\convert-use-cases-to-docx.ps1 -Force
```

### CI/CD Integration

```yaml
# Example GitHub Actions workflow
- name: Convert Use Cases to Word
  run: |
    .\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Force
    
- name: Commit Word Files
  run: |
    git add "01-motivation/03-use-cases/**/*.docx"
    git commit -m "Update Word versions of use cases"
```

### Automated Testing

```powershell
# Test round-trip quality as part of PR checks
.\convert-use-cases-to-docx.ps1 -Validate

# Fail if similarity is below threshold
# (can be added to script or CI pipeline)
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-06 | Initial release with round-trip validation |

## Support

For issues or questions:
1. Check this README for troubleshooting
2. Review Pandoc documentation: https://pandoc.org/MANUAL.html
3. Contact BNZ Architecture Team
4. Raise issue in repository

## References

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [Pandoc Markdown Extensions](https://pandoc.org/MANUAL.html#pandocs-markdown)
- [BNZ Visual Design Standards](../../../05-governance/standards/visual-design/visual-design-standard.md)
- [Use Case Template Guide](../../../01-motivation/03-use-cases/USE-CASE-TEMPLATE-GUIDE.md)
