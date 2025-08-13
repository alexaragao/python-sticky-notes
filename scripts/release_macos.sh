#!/bin/bash

VERSION="v1.0.0"
MACOS_APP="dist/Sticky Notes.app"
MACOS_BINARY="dist/stickynotes-macos.dmg"

# Create the .dmg file
hdiutil create -volname "Sticky Notes" -srcfolder "$MACOS_APP" -ov -format UDZO "$MACOS_BINARY"

gh release upload $VERSION $MACOS_BINARY

echo "macOS release $VERSION uploaded!"
