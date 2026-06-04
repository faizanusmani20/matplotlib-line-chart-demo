# QR Code Generator

A simple Python application that generates QR codes from text or URLs and saves them as image files.

## Features

* Generate QR codes from any text or URL
* Save QR codes as image files
* Custom file naming
* Lightweight and beginner-friendly

## Requirements

* Python 3.x
* qrcode library
* Pillow (installed automatically with qrcode)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

Create and activate a virtual environment (recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install qrcode[pil]
```

## Usage

Run the program:

```bash
python qr_generator.py
```

Example:

```text
Enter the text or Url: https://www.google.com
Enter file name: google_qr.png
File saved as google_qr.png
```

The QR code image will be saved in the current directory.

## Project Structure

```text
qr-code-generator/
│
├── qr_generator.py
├── README.md
└── .gitignore
```

## .gitignore

Create a `.gitignore` file and add:

```gitignore
venv/
__pycache__/
*.pyc
```

This prevents virtual environment files and Python cache files from being uploaded to GitHub.

## Future Improvements

* Add a graphical user interface (GUI)
* Support custom QR code colors
* Add logo embedding
* Generate multiple QR codes in batch

## License

This project is open source and available under the MIT License.
