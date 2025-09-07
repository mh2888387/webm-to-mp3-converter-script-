# YouTube Converter

A CLI tool to batch-rename media files by changing extensions (e.g., `.webm` → `.mp3`).

## Features

- Rename all files with a specified source extension to a destination extension.
- Dry-run mode to preview changes without modifying files.
- Customizable source and destination extensions.

## Requirements

- Python 3.6+

## Installation

```bash
git clone https://github.com/yourusername/youtube-converter.git
cd youtube-converter
chmod +x youtube_converter.py
```

## Usage

```bash
./youtube_converter.py /path/to/downloads [--src-ext .webm] [--dst-ext .mp3] [--dry-run]
```

### Arguments

- `directory`: Path to folder containing files.
- `--src-ext`: Source extension (default: `.webm`).
- `--dst-ext`: Destination extension (default: `.mp3`).
- `--dry-run`: Show planned renames without executing.

## Examples

- Convert `.webm` → `.mp3`:
  ```bash
  ./youtube_converter.py ~/Downloads/videos
  ```
- Preview changes:
  ```bash
  ./youtube_converter.py ~/Downloads/videos --dry-run
  ```
- Convert `.m4a` → `.wav`:
  ```bash
  ./youtube_converter.py ~/Music --src-ext .m4a --dst-ext .wav
  ```

## License

MIT © Your Name
