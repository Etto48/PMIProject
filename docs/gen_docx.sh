#!/usr/bin/env bash

# For the love of god, I'd like to know why we have to convert
# from tex to docx. Why tex is not enough? What's better in docx?
# To this day, I still don't know. But I have to do it.

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

MAIN_PATH=main.tex
DOCX_PATH=main.docx
TEMPLATE_PATH=template.docx

pandoc "$MAIN_PATH" -o "$DOCX_PATH" --reference-doc="$TEMPLATE_PATH" --dpi=1000
python3 fix_docx.py