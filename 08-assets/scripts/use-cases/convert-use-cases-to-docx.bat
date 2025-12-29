@echo off
REM Convenience wrapper for use case markdown to Word conversion
REM Run this from any location - it will find the script

setlocal

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"

REM Execute the PowerShell script with all arguments passed through
powershell.exe -ExecutionPolicy Bypass -File "%SCRIPT_DIR%convert-use-cases-to-docx.ps1" %*

endlocal
