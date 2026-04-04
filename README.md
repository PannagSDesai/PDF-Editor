# PDF Editor - Password Remover

A simple Python script to batch remove passwords from PDF files.

## Description

The `remove_password.py` script automates the process of removing password protection from multiple PDF files at once. It scans a specific folder for encrypted PDFs, prompts you for the password once, and creates unprotected copies of all the PDFs without modifying the original files.

## Prerequisites

- Python 3.x
- `pymupdf` library

## Installation

1. Clone or download this repository.
2. Install the required dependency using pip:
   ```bash
   pip install pymupdf
   ```

## Usage

1. Create a folder named `Documents` in the same directory as the script.
2. Place all your password-protected PDF files inside the `Documents` folder.
3. Run the script from the terminal or command prompt:
   ```bash
   python remove_password.py
   ```
4. The script will securely prompt you to enter the password for the PDFs. (Note: All files in the folder must share the same password for batch processing).
5. The script will generate unprotected versions of the PDFs in the `Documents` folder with the suffix `_unprotected.pdf`.

## How it works

- The script checks if a `Documents` folder exists.
- It asks you to enter the password silently.
- It iterates over all `.pdf` files in the folder.
- For each file, it tries to authenticate using the provided password.
- If successful, it saves a new copy of the file with `encryption=pymupdf.PDF_ENCRYPT_NONE`, effectively stripping the password.

## Important Note

Please make sure to add your protected files under the `Documents` folder, otherwise the script will not find any files to process.
