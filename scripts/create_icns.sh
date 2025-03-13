#!/bin/bash

# Check if an argument (icon.png file) is provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 <path_to_icon.png>"
  exit 1
fi

ICON_PNG=$1

# Check if the file exists
if [ ! -f "$ICON_PNG" ]; then
  echo "File '$ICON_PNG' does not exist."
  exit 1
fi

# Create a temporary directory for the icon set
ICONSET_DIR="icon.iconset"
rm -rf "$ICONSET_DIR"
mkdir "$ICONSET_DIR"

# Sizes for the iconset
SIZES=(16 32 64 128 256 512 1024)

# Generate resized images
for SIZE in "${SIZES[@]}"; do
  sips -z $SIZE $SIZE "$ICON_PNG" --out "$ICONSET_DIR/icon_${SIZE}x${SIZE}.png"
  
  # Create @2x sizes for Retina displays (skip 16x16)
  if [ $SIZE -ne 16 ]; then
    sips -z $((SIZE * 2)) $((SIZE * 2)) "$ICON_PNG" --out "$ICONSET_DIR/icon_${SIZE}x${SIZE}@2x.png"
  fi
done

# Create the .icns file using iconutil
ICON_ICNS="${ICON_PNG%.png}.icns"
iconutil -c icns "$ICONSET_DIR" -o "$ICON_ICNS"

# Clean up the temporary icon set directory
rm -rf "$ICONSET_DIR"

echo "Icon created successfully: $ICON_ICNS"
