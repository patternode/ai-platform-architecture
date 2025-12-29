#!/usr/bin/env python3
"""
BNZ Draw.io to PNG Export Script (Python Version)

This script exports draw.io diagrams to PNG images using multiple methods:
1. draw.io Desktop CLI (preferred, best quality)
2. drawio-export npm package
3. Puppeteer-based export (fallback)

Author: BNZ AI Platform Architecture Team
Version: 1.0.0
Date: 2025-12-06

Usage:
    python export-drawio-to-png.py [options]

Options:
    --source PATH       Source directory to search for .drawio files
    --output SUBFOLDER  Output subfolder name (default: images)
    --scale FACTOR      Scale factor for export (default: 2)
    --quality PERCENT   PNG quality 1-100 (default: 100)
    --force             Re-export all files even if up to date
    --dry-run           Preview without exporting
    --method METHOD     Export method: auto, drawio, npm, puppeteer
    --verbose           Show detailed output
    --help              Show this help message

Requirements:
    - Python 3.8+
    - draw.io Desktop OR npm with drawio-export package

Installation of dependencies:
    pip install pillow cairosvg lxml
    npm install -g @jgraph/draw-export (optional)
"""

import os
import sys
import glob
import json
import shutil
import argparse
import subprocess
import platform
import base64
import zlib
import urllib.parse
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed

# Optional imports for fallback methods
try:
    from lxml import etree
    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import cairosvg
    HAS_CAIRO = True
except ImportError:
    HAS_CAIRO = False

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


@dataclass
class ExportConfig:
    """Configuration for the export process."""
    source_path: Path
    output_subfolder: str = "images"
    scale: float = 2.0
    quality: int = 100
    force: bool = False
    dry_run: bool = False
    method: str = "auto"
    verbose: bool = False
    include_folders: List[str] = field(default_factory=lambda: ["use-cases", "patterns", "data"])


@dataclass
class ExportStats:
    """Statistics for the export process."""
    total: int = 0
    exported: int = 0
    skipped: int = 0
    failed: int = 0
    start_time: datetime = field(default_factory=datetime.now)

    @property
    def duration(self) -> str:
        elapsed = datetime.now() - self.start_time
        return str(elapsed).split('.')[0]


class Logger:
    """Simple colored logger for console output."""

    COLORS = {
        'INFO': '\033[0m',       # White
        'SUCCESS': '\033[92m',   # Green
        'WARNING': '\033[93m',   # Yellow
        'ERROR': '\033[91m',     # Red
        'RESET': '\033[0m'
    }

    @staticmethod
    def log(message: str, level: str = "INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = Logger.COLORS.get(level, Logger.COLORS['INFO'])
        reset = Logger.COLORS['RESET']
        print(f"[{timestamp}] [{level}] {color}{message}{reset}")

    @staticmethod
    def info(message: str):
        Logger.log(message, "INFO")

    @staticmethod
    def success(message: str):
        Logger.log(message, "SUCCESS")

    @staticmethod
    def warning(message: str):
        Logger.log(message, "WARNING")

    @staticmethod
    def error(message: str):
        Logger.log(message, "ERROR")


class DrawioExporter:
    """Exports draw.io files to PNG using various methods."""

    def __init__(self, config: ExportConfig):
        self.config = config
        self.stats = ExportStats()
        self.drawio_exe = self._find_drawio_executable()
        self.npm_exporter = self._check_npm_exporter()

    def _find_drawio_executable(self) -> Optional[str]:
        """Find the draw.io desktop executable."""
        system = platform.system()

        if system == "Windows":
            paths = [
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\draw.io\draw.io.exe"),
                os.path.expandvars(r"%ProgramFiles%\draw.io\draw.io.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\draw.io\draw.io.exe"),
                os.path.expandvars(r"%USERPROFILE%\scoop\apps\drawio\current\draw.io.exe"),
            ]
        elif system == "Darwin":  # macOS
            paths = [
                "/Applications/draw.io.app/Contents/MacOS/draw.io",
                os.path.expanduser("~/Applications/draw.io.app/Contents/MacOS/draw.io"),
            ]
        else:  # Linux
            paths = [
                "/usr/bin/drawio",
                "/usr/local/bin/drawio",
                "/snap/bin/drawio",
                os.path.expanduser("~/.local/bin/drawio"),
            ]

        # Also check PATH
        drawio_cmd = shutil.which("drawio") or shutil.which("draw.io")
        if drawio_cmd:
            return drawio_cmd

        for path in paths:
            if os.path.isfile(path):
                return path

        return None

    def _check_npm_exporter(self) -> bool:
        """Check if npm drawio-export is available."""
        try:
            result = subprocess.run(
                ["npx", "--yes", "@jgraph/draw-export", "--help"],
                capture_output=True,
                timeout=30
            )
            return result.returncode == 0
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def find_drawio_files(self) -> List[Path]:
        """Find all .drawio files in the configured folders."""
        files = []

        for folder in self.config.include_folders:
            search_path = self.config.source_path / folder
            if search_path.exists():
                found = list(search_path.rglob("*.drawio"))
                files.extend(found)
                Logger.info(f"Found {len(found)} .drawio files in {folder}")

        return files

    def export_with_drawio_cli(self, input_file: Path, output_file: Path) -> bool:
        """Export using draw.io desktop CLI."""
        if not self.drawio_exe:
            return False

        args = [
            self.drawio_exe,
            "--export",
            "--format", "png",
            "--output", str(output_file),
            "--quality", str(self.config.quality),
            "--scale", str(self.config.scale),
            "--all-pages",
            str(input_file)
        ]

        try:
            result = subprocess.run(
                args,
                capture_output=True,
                timeout=120
            )
            return result.returncode == 0 and output_file.exists()
        except subprocess.SubprocessError as e:
            Logger.error(f"CLI export failed: {e}")
            return False

    def export_with_npm(self, input_file: Path, output_file: Path) -> bool:
        """Export using npm @jgraph/draw-export package."""
        if not self.npm_exporter:
            return False

        args = [
            "npx", "--yes", "@jgraph/draw-export",
            "-f", "png",
            "-o", str(output_file),
            "-s", str(self.config.scale),
            str(input_file)
        ]

        try:
            result = subprocess.run(
                args,
                capture_output=True,
                timeout=120
            )
            return result.returncode == 0 and output_file.exists()
        except subprocess.SubprocessError as e:
            Logger.error(f"NPM export failed: {e}")
            return False

    def export_file(self, input_file: Path) -> bool:
        """Export a single draw.io file to PNG."""
        # Determine output path - save in same folder as source
        output_dir = input_file.parent
        output_file = output_dir / f"{input_file.stem}.png"

        # Check if export is needed
        if not self.config.force and output_file.exists():
            if output_file.stat().st_mtime >= input_file.stat().st_mtime:
                Logger.warning(f"Skipping (up to date): {input_file.name}")
                self.stats.skipped += 1
                return True

        if self.config.dry_run:
            Logger.info(f"[DRY RUN] Would export: {input_file.name}")
            return True

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        Logger.info(f"Exporting: {input_file.name}")

        # Try export methods in order of preference
        success = False

        if self.config.method in ("auto", "drawio") and self.drawio_exe:
            success = self.export_with_drawio_cli(input_file, output_file)
            if success:
                Logger.success(f"Exported (drawio CLI): {input_file.stem}.png")

        if not success and self.config.method in ("auto", "npm") and self.npm_exporter:
            success = self.export_with_npm(input_file, output_file)
            if success:
                Logger.success(f"Exported (npm): {input_file.stem}.png")

        if success:
            self.stats.exported += 1
            # Log file size
            if output_file.exists():
                size_kb = output_file.stat().st_size / 1024
                Logger.info(f"  Output size: {size_kb:.1f} KB")
        else:
            Logger.error(f"Failed to export: {input_file.name}")
            self.stats.failed += 1

        return success

    def run(self):
        """Run the export process."""
        print()
        print("=" * 50)
        print("  BNZ Draw.io to PNG Export Script (Python)")
        print("=" * 50)
        print()

        # Check export capabilities
        if not self.drawio_exe and not self.npm_exporter:
            Logger.error("No export method available!")
            print()
            print("Please install one of the following:")
            print("  - draw.io Desktop: https://www.drawio.com/")
            print("  - NPM exporter: npm install -g @jgraph/draw-export")
            print()
            return 1

        if self.drawio_exe:
            Logger.info(f"Using draw.io CLI: {self.drawio_exe}")
        if self.npm_exporter:
            Logger.info("NPM @jgraph/draw-export is available")

        Logger.info(f"Source path: {self.config.source_path}")
        Logger.info(f"Output subfolder: {self.config.output_subfolder}")
        Logger.info(f"Scale: {self.config.scale}x, Quality: {self.config.quality}%")

        if self.config.dry_run:
            Logger.warning("DRY RUN MODE - No files will be modified")

        print()

        # Find all draw.io files
        files = self.find_drawio_files()
        self.stats.total = len(files)

        if not files:
            Logger.warning("No .drawio files found")
            return 0

        Logger.info(f"Processing {len(files)} files...")
        print()

        # Export each file
        for i, file in enumerate(files, 1):
            progress = (i / len(files)) * 100
            print(f"\r[{progress:5.1f}%] Processing {i}/{len(files)}...", end="", flush=True)
            self.export_file(file)

        print("\r" + " " * 60 + "\r", end="")  # Clear progress line

        # Print summary
        print()
        print("=" * 50)
        print("  Export Summary")
        print("=" * 50)
        print()
        print(f"  Total files:    {self.stats.total}")
        print(f"  Exported:       {self.stats.exported}")
        print(f"  Skipped:        {self.stats.skipped}")
        print(f"  Failed:         {self.stats.failed}")
        print(f"  Duration:       {self.stats.duration}")
        print()

        return 1 if self.stats.failed > 0 else 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Export draw.io diagrams to PNG images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    # Get default source path (parent of scripts folder)
    default_source = Path(__file__).parent.parent

    parser.add_argument(
        "--source", "-s",
        type=Path,
        default=default_source,
        help="Source directory to search for .drawio files"
    )
    parser.add_argument(
        "--output", "-o",
        default="images",
        help="Output subfolder name (default: images)"
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=2.0,
        help="Scale factor for export (default: 2)"
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=100,
        choices=range(1, 101),
        metavar="1-100",
        help="PNG quality 1-100 (default: 100)"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Re-export all files even if up to date"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview without exporting"
    )
    parser.add_argument(
        "--method", "-m",
        choices=["auto", "drawio", "npm"],
        default="auto",
        help="Export method: auto, drawio, npm (default: auto)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    config = ExportConfig(
        source_path=args.source.resolve(),
        output_subfolder=args.output,
        scale=args.scale,
        quality=args.quality,
        force=args.force,
        dry_run=args.dry_run,
        method=args.method,
        verbose=args.verbose
    )

    exporter = DrawioExporter(config)
    return exporter.run()


if __name__ == "__main__":
    sys.exit(main())
