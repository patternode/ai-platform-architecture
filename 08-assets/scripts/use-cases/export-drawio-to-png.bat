@echo off
REM ============================================
REM BNZ Draw.io to PNG Export Script (Batch Wrapper)
REM ============================================
REM
REM This batch file runs the PowerShell export script with default settings.
REM For advanced options, run the PowerShell script directly.
REM
REM Usage:
REM   export-drawio-to-png.bat                    - Export all diagrams
REM   export-drawio-to-png.bat --dry-run          - Preview without exporting
REM   export-drawio-to-png.bat --force            - Re-export all files
REM   export-drawio-to-png.bat --help             - Show help
REM
REM ============================================

setlocal enabledelayedexpansion

REM Get the script directory
set "SCRIPT_DIR=%~dp0"
set "PS_SCRIPT=%SCRIPT_DIR%export-drawio-to-png.ps1"

REM Check if PowerShell script exists
if not exist "%PS_SCRIPT%" (
    echo ERROR: PowerShell script not found: %PS_SCRIPT%
    exit /b 1
)

REM Parse arguments
set "PS_ARGS="
:parse_args
if "%~1"=="" goto :run_script
if /i "%~1"=="--dry-run" set "PS_ARGS=%PS_ARGS% -DryRun"
if /i "%~1"=="--force" set "PS_ARGS=%PS_ARGS% -Force"
if /i "%~1"=="--help" goto :show_help
if /i "%~1"=="-h" goto :show_help
shift
goto :parse_args

:show_help
echo.
echo BNZ Draw.io to PNG Export Script
echo ================================
echo.
echo Usage: %~nx0 [options]
echo.
echo Options:
echo   --dry-run    Preview exports without actually creating files
echo   --force      Re-export all files even if PNG is up to date
echo   --help, -h   Show this help message
echo.
echo For advanced options, run the PowerShell script directly:
echo   powershell -ExecutionPolicy Bypass -File "%PS_SCRIPT%" -Help
echo.
exit /b 0

:run_script
echo.
echo Starting draw.io to PNG export...
echo.

REM Run PowerShell script with bypass execution policy
powershell -ExecutionPolicy Bypass -File "%PS_SCRIPT%" %PS_ARGS%

set "EXIT_CODE=%ERRORLEVEL%"

if %EXIT_CODE% neq 0 (
    echo.
    echo Export completed with errors. Exit code: %EXIT_CODE%
) else (
    echo.
    echo Export completed successfully!
)

exit /b %EXIT_CODE%
