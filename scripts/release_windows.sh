#!/bin/bash

VERSION="v1.0.0"
WINDOWS_EXE="dist/Sticky Notes.exe"

gh release upload $VERSION \
  "$WINDOWS_EXE#stickynotes-windows.exe"

echo "Windows release $VERSION uploaded!"
