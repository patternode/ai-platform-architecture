# BNZ Use Case Automation Scripts

This folder contains automation scripts for managing and converting BNZ AI Platform Architecture use cases.

## Available Scripts

### 1. Markdown to Word Conversion

| Script | Type | Description |
|--------|------|-------------|
| `convert-use-cases-to-docx.ps1` | PowerShell | Convert markdown to Word with high-fidelity round-trip |
| `convert-use-cases-to-docx.bat` | Batch | Convenience wrapper for PowerShell script |

**Documentation**:
- 📖 [Full Documentation](README-docx-conversion.md)
- ⚡ [Quick Start Guide](QUICK-START-docx-conversion.md)
- 📋 [Implementation Summary](IMPLEMENTATION-SUMMARY.md)

**Quick Example**:
```powershell
# Convert all use cases to Word
.\convert-use-cases-to-docx.ps1

# Convert and validate round-trip quality
.\convert-use-cases-to-docx.ps1 -Validate
```

**Requirements**: Pandoc 2.19+ (`choco install pandoc`)

---

### 2. Draw.io Export Scripts

| Script | Platform | Description |
|--------|----------|-------------|
| `export-drawio-to-png.ps1` | Windows (PowerShell) | Full-featured PowerShell script |
| `export-drawio-to-png.bat` | Windows (CMD) | Batch wrapper for easy execution |
| `export-drawio-to-png.py` | Cross-platform | Python script with multiple export methods |

## Prerequisites

You need **one** of the following installed:

### Option 1: draw.io Desktop (Recommended)
- Download from: https://www.drawio.com/
- Installation methods:
  ```powershell
  # Windows - Chocolatey
  choco install drawio

  # Windows - Scoop
  scoop install drawio

  # Windows - Winget
  winget install JGraph.Draw
  ```

### Option 2: NPM Exporter
```bash
npm install -g @jgraph/draw-export
```

### Option 3: Python Dependencies (for Python script)
```bash
pip install pillow cairosvg lxml
```

## Usage

### Quick Start (Windows)

Double-click `export-drawio-to-png.bat` or run from command line:

```cmd
cd D:\Work\BNZ\ai-platform-architecture\01-motivation\03-use-cases\use-case-prioritisation\scripts
export-drawio-to-png.bat
```

### PowerShell Script

```powershell
# Basic usage - export all diagrams
.\export-drawio-to-png.ps1

# Preview what would be exported (dry run)
.\export-drawio-to-png.ps1 -DryRun

# Force re-export all files
.\export-drawio-to-png.ps1 -Force

# Custom scale and quality
.\export-drawio-to-png.ps1 -Scale 3 -Quality 100

# Specify custom draw.io path
.\export-drawio-to-png.ps1 -DrawioPath "C:\Program Files\draw.io\draw.io.exe"

# Export with transparent background
.\export-drawio-to-png.ps1 -Transparent
```

### Python Script

```bash
# Basic usage
python export-drawio-to-png.py

# Preview (dry run)
python export-drawio-to-png.py --dry-run

# Force re-export
python export-drawio-to-png.py --force

# Custom options
python export-drawio-to-png.py --scale 3 --quality 100

# Specify export method
python export-drawio-to-png.py --method drawio   # Use draw.io CLI only
python export-drawio-to-png.py --method npm      # Use NPM exporter only
python export-drawio-to-png.py --method auto     # Try all methods (default)
```

## Parameters

### PowerShell Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `-DrawioPath` | String | Auto-detect | Path to draw.io executable |
| `-SourcePath` | String | Parent folder | Root path to search for .drawio files |
| `-OutputSubfolder` | String | `images` | Subfolder name for PNG outputs |
| `-Quality` | Int (1-100) | `100` | PNG export quality |
| `-Scale` | Double (1-5) | `2` | Scale factor for high-res output |
| `-Transparent` | Switch | `$false` | Export with transparent background |
| `-AllPages` | Switch | `$true` | Export all pages from multi-page diagrams |
| `-Force` | Switch | `$false` | Re-export all files |
| `-DryRun` | Switch | `$false` | Preview without exporting |
| `-IncludeFolders` | String[] | `@("use-cases", "patterns", "data")` | Folders to search |

### Python Parameters

| Parameter | Short | Default | Description |
|-----------|-------|---------|-------------|
| `--source` | `-s` | Parent folder | Source directory to search |
| `--output` | `-o` | `images` | Output subfolder name |
| `--scale` | | `2` | Scale factor for export |
| `--quality` | | `100` | PNG quality (1-100) |
| `--force` | `-f` | `False` | Re-export all files |
| `--dry-run` | `-n` | `False` | Preview without exporting |
| `--method` | `-m` | `auto` | Export method: auto, drawio, npm |
| `--verbose` | `-v` | `False` | Show detailed output |

## Output Structure

The scripts create an `images` subfolder next to each `.drawio` file:

```
use-cases/
├── UC-001/
│   ├── UC-001-Partnership-Banking-Blueprint-v1.0.0.drawio
│   ├── SCN-001-FrontLine---Partnership-Banking-Sequence-v1.0.0.drawio
│   └── images/
│       ├── UC-001-Partnership-Banking-Blueprint-v1.0.0.png
│       └── SCN-001-FrontLine---Partnership-Banking-Sequence-v1.0.0.png
├── UC-002/
│   ├── UC-002-Finance-Blueprint-v1.0.0.drawio
│   └── images/
│       └── UC-002-Finance-Blueprint-v1.0.0.png
...
```

## File Statistics

Current diagram inventory:
- **Use Case Diagrams**: 54+ files (Blueprints, Sequences, Generated)
- **Pattern Diagrams**: 18 files (PT-001 through PT-018)
- **Total**: 92+ draw.io diagrams

## Incremental Export

By default, scripts only export files where:
- The PNG doesn't exist, OR
- The .drawio file is newer than the PNG

Use `--force` or `-Force` to re-export all files.

## Troubleshooting

### draw.io not found

If you get "draw.io executable not found":

1. Install draw.io Desktop from https://www.drawio.com/
2. Or specify the path explicitly:
   ```powershell
   .\export-drawio-to-png.ps1 -DrawioPath "C:\Path\To\draw.io.exe"
   ```

### Export fails silently

Some complex diagrams may fail. Try:
- Reducing scale factor: `-Scale 1`
- Opening the diagram in draw.io Desktop to check for errors

### Permission errors

Run PowerShell as Administrator or check file permissions.

### Timeout issues

For very large diagrams, increase timeout in the script or export manually.

## Integration with CI/CD

Example GitHub Actions workflow:

```yaml
name: Export Diagrams

on:
  push:
    paths:
      - '**/*.drawio'

jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install draw.io
        run: |
          wget https://github.com/jgraph/drawio-desktop/releases/download/v24.4.0/drawio-amd64-24.4.0.deb
          sudo apt install -y ./drawio-amd64-24.4.0.deb

      - name: Export diagrams
        run: |
          python scripts/export-drawio-to-png.py --force

      - name: Commit PNG files
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add "**/images/*.png"
          git commit -m "Update exported PNG diagrams" || echo "No changes"
          git push
```

## License

Internal use only - Bank of New Zealand
