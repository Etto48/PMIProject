#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

MAIN_PATH=main.tex
DOCX_PATH=main.docx
TEMPLATE_PATH=template.docx

pandoc "$MAIN_PATH" -o "$DOCX_PATH" --reference-doc="$TEMPLATE_PATH"