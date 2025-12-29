<#
.SYNOPSIS
    Export draw.io diagrams to PNG images for BNZ AI Platform Architecture use cases.

.DESCRIPTION
    This script finds all .drawio files in the use-case-prioritisation folder and exports
    them to PNG format using the draw.io desktop application CLI.

.PARAMETER DrawioPath
    Path to the draw.io executable. Default searches common installation locations.

.PARAMETER SourcePath
    Root path to search for .drawio files. Default is the use-case-prioritisation folder.

.PARAMETER OutputSubfolder
    Subfolder name for PNG outputs. Default is "images".

.PARAMETER Quality
    PNG export quality (1-100). Default is 100.

.PARAMETER Scale
    Scale factor for export. Default is 2 for high-resolution output.

.PARAMETER Transparent
    Export with transparent background. Default is false.

.PARAMETER AllPages
    Export all pages from multi-page diagrams. Default is true.

.EXAMPLE
    .\export-drawio-to-png.ps1
    Exports all diagrams with default settings.

.EXAMPLE
    .\export-drawio-to-png.ps1 -Scale 3 -Quality 100
    Exports with 3x scale and maximum quality.

.NOTES
    Author: BNZ AI Platform Architecture Team
    Version: 1.0.0
    Date: 2025-12-06

    Prerequisites:
    - draw.io Desktop application installed
    - PowerShell 5.1 or later
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string]$DrawioPath,

    [Parameter()]
    [string]$SourcePath,

    [Parameter()]
    [string]$OutputSubfolder = "images",

    [Parameter()]
    [ValidateRange(1, 100)]
    [int]$Quality = 100,

    [Parameter()]
    [ValidateRange(1, 5)]
    [double]$Scale = 2,

    [Parameter()]
    [switch]$Transparent,

    [Parameter()]
    [switch]$AllPages = $true,

    [Parameter()]
    [switch]$Force,

    [Parameter()]
    [switch]$DryRun,

    [Parameter()]
    [string[]]$IncludeFolders = @("use-cases", "patterns", "data")
)

# Script configuration
$ErrorActionPreference = "Continue"
$ProgressPreference = "Continue"

# Handle default SourcePath
if (-not $SourcePath) {
    $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
    $SourcePath = Split-Path -Parent $scriptDir
}

# Statistics tracking
$script:stats = @{
    TotalFiles = 0
    Exported = 0
    Skipped = 0
    Failed = 0
    StartTime = Get-Date
}

# Logging function
function Write-Log {
    param(
        [string]$Message,
        [ValidateSet("INFO", "SUCCESS", "WARNING", "ERROR")]
        [string]$Level = "INFO"
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $color = switch ($Level) {
        "INFO"    { "White" }
        "SUCCESS" { "Green" }
        "WARNING" { "Yellow" }
        "ERROR"   { "Red" }
    }

    Write-Host "[$timestamp] [$Level] $Message" -ForegroundColor $color
}

# Find draw.io executable
function Find-DrawioExecutable {
    param([string]$CustomPath)

    if ($CustomPath -and (Test-Path $CustomPath)) {
        return $CustomPath
    }

    # Common installation paths for draw.io on Windows
    $cmdResult = Get-Command "draw.io.exe" -ErrorAction SilentlyContinue
    $cmdSource = if ($cmdResult) { $cmdResult.Source } else { $null }

    $possiblePaths = @(
        "$env:LOCALAPPDATA\Programs\draw.io\draw.io.exe",
        "$env:ProgramFiles\draw.io\draw.io.exe",
        "${env:ProgramFiles(x86)}\draw.io\draw.io.exe",
        "$env:LOCALAPPDATA\draw.io\draw.io.exe",
        # Chocolatey installation
        "$env:ChocolateyInstall\lib\drawio\tools\draw.io.exe",
        # Scoop installation
        "$env:USERPROFILE\scoop\apps\drawio\current\draw.io.exe",
        # Microsoft Store / MSIX or PATH
        $cmdSource
    )

    foreach ($path in $possiblePaths) {
        if ($path -and (Test-Path $path)) {
            Write-Log "Found draw.io at: $path" "SUCCESS"
            return $path
        }
    }

    # Try to find via registry
    $registryPaths = @(
        "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\draw.io.exe",
        "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\draw.io.exe"
    )

    foreach ($regPath in $registryPaths) {
        if (Test-Path $regPath) {
            $exePath = (Get-ItemProperty -Path $regPath -ErrorAction SilentlyContinue).'(Default)'
            if ($exePath -and (Test-Path $exePath)) {
                Write-Log "Found draw.io via registry: $exePath" "SUCCESS"
                return $exePath
            }
        }
    }

    return $null
}

# Find all draw.io files
function Get-DrawioFiles {
    param(
        [string]$RootPath,
        [string[]]$Folders
    )

    $files = @()

    foreach ($folder in $Folders) {
        $searchPath = Join-Path $RootPath $folder
        if (Test-Path $searchPath) {
            $found = Get-ChildItem -Path $searchPath -Filter "*.drawio" -Recurse -File
            $files += $found
            Write-Log "Found $($found.Count) .drawio files in $folder" "INFO"
        }
    }

    return $files
}

# Export a single draw.io file to PNG
function Export-DrawioToPng {
    param(
        [string]$DrawioExe,
        [System.IO.FileInfo]$InputFile,
        [string]$OutputFolder,
        [int]$Quality,
        [double]$Scale,
        [bool]$Transparent,
        [bool]$AllPages,
        [bool]$Force,
        [bool]$DryRun
    )

    # Create output directory if needed
    if (-not (Test-Path $OutputFolder)) {
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $OutputFolder -Force | Out-Null
        }
        Write-Log "Created output folder: $OutputFolder" "INFO"
    }

    # Generate output filename
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($InputFile.Name)
    $outputFile = Join-Path $OutputFolder "$baseName.png"

    # Check if output already exists and is newer
    if (-not $Force -and (Test-Path $outputFile)) {
        $outputInfo = Get-Item $outputFile
        if ($outputInfo.LastWriteTime -ge $InputFile.LastWriteTime) {
            Write-Log "Skipping (up to date): $baseName" "WARNING"
            $script:stats.Skipped++
            return $true
        }
    }

    # Build export arguments
    $arguments = @(
        "--export"
        "--format", "png"
        "--output", "`"$outputFile`""
        "--quality", $Quality
        "--scale", $Scale
    )

    if ($Transparent) {
        $arguments += "--transparent"
    }

    if ($AllPages) {
        $arguments += "--all-pages"
    }

    $arguments += "`"$($InputFile.FullName)`""

    if ($DryRun) {
        Write-Log "[DRY RUN] Would export: $baseName -> $outputFile" "INFO"
        return $true
    }

    Write-Log "Exporting: $baseName" "INFO"

    try {
        # Build argument string
        $argString = $arguments -join " "

        # Use cmd /c to run and suppress output
        $process = Start-Process -FilePath "cmd.exe" `
            -ArgumentList "/c", "`"$DrawioExe`" $argString >nul 2>&1" `
            -NoNewWindow `
            -Wait `
            -PassThru

        # Give it a moment and check if output file exists
        Start-Sleep -Milliseconds 500

        if (Test-Path $outputFile) {
            $fileSize = (Get-Item $outputFile).Length / 1KB
            Write-Log "Exported: $baseName ($([math]::Round($fileSize, 1)) KB)" "SUCCESS"
            $script:stats.Exported++
            return $true
        }
        else {
            Write-Log "Failed to export: $baseName (Exit code: $($process.ExitCode))" "ERROR"
            $script:stats.Failed++
            return $false
        }
    }
    catch {
        Write-Log "Error exporting $baseName : $_" "ERROR"
        $script:stats.Failed++
        return $false
    }
}

# Main execution
function Main {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  BNZ Draw.io to PNG Export Script" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""

    # Find draw.io executable
    $drawioExe = Find-DrawioExecutable -CustomPath $DrawioPath

    if (-not $drawioExe) {
        Write-Log "draw.io executable not found!" "ERROR"
        Write-Host ""
        Write-Host "Please install draw.io Desktop from: https://www.drawio.com/" -ForegroundColor Yellow
        Write-Host "Or specify the path using -DrawioPath parameter" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Alternative installation methods:" -ForegroundColor Cyan
        Write-Host "  - Chocolatey: choco install drawio" -ForegroundColor White
        Write-Host "  - Scoop: scoop install drawio" -ForegroundColor White
        Write-Host "  - Winget: winget install JGraph.Draw" -ForegroundColor White
        Write-Host ""
        exit 1
    }

    Write-Log "Using draw.io: $drawioExe" "INFO"
    Write-Log "Source path: $SourcePath" "INFO"
    Write-Log "Output subfolder: $OutputSubfolder" "INFO"
    Write-Log "Scale: ${Scale}x, Quality: $Quality%" "INFO"

    if ($DryRun) {
        Write-Log "DRY RUN MODE - No files will be modified" "WARNING"
    }

    Write-Host ""

    # Find all draw.io files
    $drawioFiles = Get-DrawioFiles -RootPath $SourcePath -Folders $IncludeFolders
    $script:stats.TotalFiles = $drawioFiles.Count

    if ($drawioFiles.Count -eq 0) {
        Write-Log "No .drawio files found in specified folders" "WARNING"
        exit 0
    }

    Write-Log "Found $($drawioFiles.Count) draw.io files to process" "INFO"
    Write-Host ""

    # Process each file
    $current = 0
    foreach ($file in $drawioFiles) {
        $current++
        $percentComplete = [math]::Round(($current / $drawioFiles.Count) * 100)

        Write-Progress -Activity "Exporting draw.io diagrams" `
            -Status "Processing $($file.Name)" `
            -PercentComplete $percentComplete `
            -CurrentOperation "$current of $($drawioFiles.Count)"

        # Determine output folder (same directory as source file)
        $outputFolder = $file.DirectoryName

        Export-DrawioToPng -DrawioExe $drawioExe `
            -InputFile $file `
            -OutputFolder $outputFolder `
            -Quality $Quality `
            -Scale $Scale `
            -Transparent $Transparent.IsPresent `
            -AllPages $AllPages.IsPresent `
            -Force $Force.IsPresent `
            -DryRun $DryRun.IsPresent
    }

    Write-Progress -Activity "Exporting draw.io diagrams" -Completed

    # Print summary
    $duration = (Get-Date) - $script:stats.StartTime

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  Export Summary" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Total files:    $($script:stats.TotalFiles)" -ForegroundColor White
    Write-Host "  Exported:       $($script:stats.Exported)" -ForegroundColor Green
    Write-Host "  Skipped:        $($script:stats.Skipped)" -ForegroundColor Yellow
    Write-Host "  Failed:         $($script:stats.Failed)" -ForegroundColor Red
    Write-Host "  Duration:       $($duration.ToString('mm\:ss'))" -ForegroundColor White
    Write-Host ""

    if ($script:stats.Failed -gt 0) {
        exit 1
    }
}

# Run main function
Main
