#!/usr/bin/env python3
"""
remove_password_pdf.py
Usage:
  python remove_password_pdf.py input.pdf output.pdf --password "secret"
"""

import argparse
import sys
from pathlib import Path

import pikepdf


def unlock_pdf(input_path: Path, output_path: Path, password: str):
    # Open using provided password (if empty string, tries without password)
    try:
        if password:
            pdf = pikepdf.open(input_path, password=password)
        else:
            pdf = pikepdf.open(input_path)
    except pikepdf._qpdf.PasswordError:
        print("ERROR: Wrong password.", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ERROR: Failed to open PDF: {e}", file=sys.stderr)
        return 3

    # Save without encryption
    try:
        pdf.save(output_path)
        pdf.close()
    except Exception as e:
        print(f"ERROR: Failed to save unlocked PDF: {e}", file=sys.stderr)
        return 4

    print(f"Unlocked PDF saved to: {output_path}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Remove password from a PDF (requires correct password)."
    )
    parser.add_argument("input", type=Path, help="Encrypted PDF file path")
    parser.add_argument("output", type=Path, help="Output unlocked PDF path")
    parser.add_argument(
        "--password",
        "-p",
        type=str,
        default="",
        help="Password of the PDF (user password)",
    )
    args = parser.parse_args()

    if not args.input.exists():
        print("ERROR: Input file does not exist.", file=sys.stderr)
        sys.exit(1)

    rc = unlock_pdf(args.input, args.output, args.password)
    sys.exit(rc)


if __name__ == "__main__":
    main()
