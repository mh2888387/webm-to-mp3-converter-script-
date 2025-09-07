# Youtube Converter

A simple command-line script to batch-rename media files by changing their extensions.  
Commonly used to convert downloaded YouTube WebM files into MP3 filenames.

## Features

- Rename all files with a given source extension (default `.webm`) to a new extension (default `.mp3`).
- Supports dry-run mode to preview changes without modifying any files.
- Cross-platform: works on Windows, macOS, and Linux.

## Requirements

- Python 3.6 or higher.

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/youtube-converter.git
cd youtube-converter

text

2. (Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows

text

3. Ensure the script is executable:

chmod +x youtube_converter.py

text

## Usage

./youtube_converter.py /path/to/downloads

text

### Options

- `directory` (required): Path to the folder containing files to rename.
- `--src-ext`: Source extension to replace (default: `.webm`).
- `--dst-ext`: Destination extension (default: `.mp3`).
- `--dry-run`: Show planned renames without performing them.

### Examples

1. Rename all `.webm` files to `.mp3`:

./youtube_converter.py "D:\Downloads\YouTube"

text

2. Dry-run to preview renames:

./youtube_converter.py /home/user/videos --dry-run

text

3. Rename `.m4a` to `.mp3` instead:

./youtube_converter.py /home/user/videos --src-ext .m4a --dst-ext .mp3

text

## License

MIT License. Feel free to fork and modify.
