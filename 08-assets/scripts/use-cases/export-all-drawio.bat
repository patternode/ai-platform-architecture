@echo off
REM ============================================
REM BNZ Draw.io to PNG Export Script
REM Simple batch version that calls draw.io directly
REM ============================================

setlocal enabledelayedexpansion

set "DRAWIO=C:\Program Files\draw.io\draw.io.exe"
set "BASE_DIR=%~dp0.."

echo.
echo ========================================
echo   BNZ Draw.io to PNG Export Script
echo ========================================
echo.

if not exist "%DRAWIO%" (
    echo ERROR: draw.io not found at %DRAWIO%
    exit /b 1
)

echo Using draw.io: %DRAWIO%
echo Base directory: %BASE_DIR%
echo.

set /a TOTAL=0
set /a EXPORTED=0
set /a FAILED=0

REM Export use-cases diagrams
echo Processing use-cases folder...
for /r "%BASE_DIR%\use-cases" %%f in (*.drawio) do (
    set /a TOTAL+=1
    set "INPUT=%%f"
    set "OUTPUT_DIR=%%~dpfimages"
    set "OUTPUT=%%~dpfimages\%%~nf.png"

    if not exist "!OUTPUT_DIR!" mkdir "!OUTPUT_DIR!"

    echo Exporting: %%~nf
    "%DRAWIO%" --export --format png --output "!OUTPUT!" --quality 100 --scale 2 "!INPUT!" >nul 2>&1

    if exist "!OUTPUT!" (
        set /a EXPORTED+=1
        echo   SUCCESS: %%~nf.png
    ) else (
        set /a FAILED+=1
        echo   FAILED: %%~nf
    )
)

REM Export patterns diagrams
echo.
echo Processing patterns folder...
for %%f in ("%BASE_DIR%\patterns\*.drawio") do (
    set /a TOTAL+=1
    set "INPUT=%%f"
    set "OUTPUT_DIR=%BASE_DIR%\patterns\images"
    set "OUTPUT=%BASE_DIR%\patterns\images\%%~nf.png"

    if not exist "!OUTPUT_DIR!" mkdir "!OUTPUT_DIR!"

    echo Exporting: %%~nf
    "%DRAWIO%" --export --format png --output "!OUTPUT!" --quality 100 --scale 2 "!INPUT!" >nul 2>&1

    if exist "!OUTPUT!" (
        set /a EXPORTED+=1
        echo   SUCCESS: %%~nf.png
    ) else (
        set /a FAILED+=1
        echo   FAILED: %%~nf
    )
)

echo.
echo ========================================
echo   Export Summary
echo ========================================
echo.
echo   Total files:    %TOTAL%
echo   Exported:       %EXPORTED%
echo   Failed:         %FAILED%
echo.

if %FAILED% gtr 0 exit /b 1
exit /b 0
