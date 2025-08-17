# Remove Password from PDF

This Python script removes the password from an encrypted PDF file. You must provide the correct password to unlock the file.

## Requirements

- Python 3
- `pikepdf` library

## Installation

Install the required `pikepdf` library using pip:

```bash
pip install pikepdf
```

## Usage

Run the script from your command line, providing the input file, output file, and the password.

```bash
python remove_password_pdf.py <input.pdf> <output.pdf> --password "YOUR_PASSWORD"
```

### Arguments

- `input.pdf`: The path to the encrypted PDF file.
- `output.pdf`: The path where the unlocked PDF will be saved.
- `--password` or `-p`: The password for the encrypted PDF. If the PDF has no password, you can omit this argument.

### Example

```bash
python remove_password_pdf.py "encrypted_document.pdf" "decrypted_document.pdf" --password "secret123"
```

If the PDF has an empty password, you can run:
```bash
python remove_password_pdf.py "encrypted_document.pdf" "decrypted_document.pdf"
```
