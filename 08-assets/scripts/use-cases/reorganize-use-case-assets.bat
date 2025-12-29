@echo off
REM ============================================
REM BNZ Use Case Asset Reorganization Script
REM Renames 'images' folders to 'assets' and moves .drawio files into them
REM ============================================

setlocal enabledelayedexpansion

set "BASE_DIR=%~dp0..\use-cases"

echo.
echo ========================================
echo   BNZ Use Case Asset Reorganization
echo ========================================
echo.
echo Base directory: %BASE_DIR%
echo.

set /a RENAMED=0
set /a MOVED=0
set /a ERRORS=0

REM Process each UC-XXX folder
for /d %%d in ("%BASE_DIR%\UC-*") do (
    echo.
    echo Processing: %%~nxd

    set "UC_DIR=%%d"
    set "IMAGES_DIR=%%d\images"
    set "ASSETS_DIR=%%d\assets"

    REM Step 1: Rename 'images' to 'assets' if it exists
    if exist "!IMAGES_DIR!" (
        if exist "!ASSETS_DIR!" (
            echo   WARNING: Both 'images' and 'assets' exist, merging...
            REM Move contents from images to assets
            for %%f in ("!IMAGES_DIR!\*.*") do (
                move "%%f" "!ASSETS_DIR!\" >nul 2>&1
                if !errorlevel! equ 0 (
                    echo   Merged: %%~nxf
                ) else (
                    echo   ERROR merging: %%~nxf
                    set /a ERRORS+=1
                )
            )
            REM Remove empty images folder
            rmdir "!IMAGES_DIR!" 2>nul
        ) else (
            ren "!IMAGES_DIR!" "assets" >nul 2>&1
            if !errorlevel! equ 0 (
                echo   Renamed: images -> assets
                set /a RENAMED+=1
            ) else (
                echo   ERROR: Failed to rename images folder
                set /a ERRORS+=1
            )
        )
    ) else if not exist "!ASSETS_DIR!" (
        REM Create assets folder if neither exists
        mkdir "!ASSETS_DIR!" >nul 2>&1
        echo   Created: assets folder
    )

    REM Step 2: Move all .drawio files into assets folder
    for %%f in ("!UC_DIR!\*.drawio") do (
        if exist "%%f" (
            move "%%f" "!ASSETS_DIR!\" >nul 2>&1
            if !errorlevel! equ 0 (
                echo   Moved: %%~nxf
                set /a MOVED+=1
            ) else (
                echo   ERROR moving: %%~nxf
                set /a ERRORS+=1
            )
        )
    )
)

echo.
echo ========================================
echo   Reorganization Summary
echo ========================================
echo.
echo   Folders renamed:    %RENAMED%
echo   Files moved:        %MOVED%
echo   Errors:             %ERRORS%
echo.

if %ERRORS% gtr 0 exit /b 1
exit /b 0
