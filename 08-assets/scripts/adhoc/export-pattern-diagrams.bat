@echo off
REM ============================================================================
REM Script: export-pattern-diagrams.bat
REM Purpose: Export all draw.io diagrams in patterns folders to PNG images
REM Author: BNZ Enterprise Architecture
REM Date: 2025-12-06
REM ============================================================================

setlocal enabledelayedexpansion

REM Configuration
set "DRAWIO_PATH=C:\Program Files\draw.io\draw.io.exe"
set "PATTERNS_DIR=D:\Work\BNZ\ai-platform-architecture\03-building-blocks\patterns"
set "QUALITY=100"
set "SCALE=2"

REM Check if draw.io exists
if not exist "%DRAWIO_PATH%" (
    echo ERROR: draw.io not found at %DRAWIO_PATH%
    echo Please install draw.io or update the DRAWIO_PATH variable
    exit /b 1
)

echo ============================================================================
echo Draw.io Pattern Diagram Export Script
echo ============================================================================
echo.
echo Patterns directory: %PATTERNS_DIR%
echo Output format: PNG (quality=%QUALITY%, scale=%SCALE%)
echo.

REM Counter for processed files
set /a count=0
set /a success=0
set /a failed=0

REM Process each pattern folder
for /d %%P in ("%PATTERNS_DIR%\PT-*") do (
    echo.
    echo Processing folder: %%~nxP
    echo ----------------------------------------------------------------------------

    REM Process each .drawio file in the pattern folder
    for %%F in ("%%P\*.drawio") do (
        set /a count+=1
        set "INPUT_FILE=%%F"
        set "OUTPUT_FILE=%%P\%%~nF.png"

        echo   Exporting: %%~nxF

        "%DRAWIO_PATH%" --export --format png --output "!OUTPUT_FILE!" --quality %QUALITY% --scale %SCALE% "!INPUT_FILE!" 2>nul

        if exist "!OUTPUT_FILE!" (
            echo     -> Success: %%~nF.png
            set /a success+=1
        ) else (
            echo     -> FAILED: Could not export %%~nxF
            set /a failed+=1
        )
    )
)

echo.
echo ============================================================================
echo Export Complete
echo ============================================================================
echo Total files processed: %count%
echo Successful exports:    %success%
echo Failed exports:        %failed%
echo.

if %failed% gtr 0 (
    echo WARNING: Some exports failed. Check the output above for details.
    exit /b 1
) else (
    echo All diagrams exported successfully!
    exit /b 0
)
