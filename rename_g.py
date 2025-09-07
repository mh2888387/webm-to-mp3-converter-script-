#!/usr/bin/env python3
"""
youtube_converter.py

A simple script to batch-rename media files in a specified directory,
converting WebM filenames to MP3 filenames by changing the extension.
"""

import argparse
from pathlib import Path


def convert_extensions(
    directory: Path,
    src_ext: str = ".webm",
    dst_ext: str = ".mp3",
    dry_run: bool = False
) -> None:
    """
    Rename all files in `directory` ending with `src_ext` to `dst_ext`.

    Parameters:
    - directory: Path object pointing to the folder to process.
    - src_ext: Source file extension to replace (e.g., ".webm").
    - dst_ext: Destination file extension (e.g., ".mp3").
    - dry_run: If True, only print planned renames without executing them.
    """
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory.")
        return

    for file_path in directory.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == src_ext.lower():
            new_name = file_path.stem + dst_ext
            new_path = file_path.with_name(new_name)
            if dry_run:
                print(f"DRY RUN: {file_path.name} → {new_name}")
            else:
                try:
                    file_path.rename(new_path)
                    print(f"Renamed: {file_path.name} → {new_name}")
                except Exception as e:
                    print(f"Failed to rename {file_path.name}: {e}")


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Batch-convert file extensions (e.g., .webm → .mp3) in a directory."
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Path to the target directory containing files to rename."
    )
    parser.add_argument(
        "--src-ext",
        default=".webm",
        help="Source file extension to replace (default: .webm)."
    )
    parser.add_argument(
        "--dst-ext",
        default=".mp3",
        help="Destination file extension (default: .mp3)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a trial run without renaming any files."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    convert_extensions(
        directory=args.directory,
        src_ext=args.src_ext,
        dst_ext=args.dst_ext,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
