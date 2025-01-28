#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

SVG_DIR=svg
PDF_DIR=figures

GTK_PATH=""

for svg in $SVG_DIR/*.svg; do
    pdf=$(basename "$svg" .svg).pdf
    echo "Converting $svg to $pdf"
    inkscape -D "$svg" -o "$PDF_DIR/$pdf"
done