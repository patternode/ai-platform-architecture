# Quick Reference: Use Case Markdown → Word Conversion

## Installation

```powershell
# Install Pandoc (required)
choco install pandoc

# Verify installation
pandoc --version
```

## Common Commands

### Convert All Use Cases
```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1
```

### Convert One Use Case
```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -UseCaseId "UC-019"
```

### Preview (No Changes)
```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -DryRun
```

### Overwrite Existing
```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Force
```

### Test Round-Trip Quality
```powershell
.\08-assets\scripts\use-cases\convert-use-cases-to-docx.ps1 -Validate
```

## Batch File Shortcut

```cmd
REM From anywhere in the repo
08-assets\scripts\use-cases\convert-use-cases-to-docx.bat
```

## Output Location

Word files are saved in the same folder as the markdown:
```
01-motivation/03-use-cases/use-cases/UC-019/
├── UC-019-Payment-Disputes-v1.0.0.md      # Original
└── UC-019-Payment-Disputes-v1.0.0.docx    # Generated ✓
```

## What Gets Preserved

✅ **100% Preserved**:
- YAML frontmatter
- Headers (H1-H6)
- Lists (ordered/unordered)
- Tables
- Code blocks
- Links
- Bold/italic/strikethrough

⚠️ **Mostly Preserved**:
- Whitespace (normalized)
- Line breaks (standardized)

## Customizing BNZ Styling

1. Run script once to create template:
   ```powershell
   .\convert-use-cases-to-docx.ps1
   ```

2. Edit template in Word:
   ```
   08-assets\scripts\use-cases\reference-template.docx
   ```

3. Apply BNZ colors:
   - Headings: BNZ Navy Blue (#003087)
   - Accents: BNZ Orange (#FF6B35)
   - Body: Calibri 11pt

4. Re-run conversion to apply styling

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pandoc not found | `choco install pandoc` |
| Old Pandoc version | `choco upgrade pandoc` |
| Already exists | Use `-Force` flag |
| Low similarity | Simplify markdown, remove HTML |

## Get Help

```powershell
Get-Help .\convert-use-cases-to-docx.ps1 -Full
```

## Full Documentation

See: `README-docx-conversion.md`
