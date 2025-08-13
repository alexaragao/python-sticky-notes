#!/bin/bash

VERSION="v1.0.0"

gh release create $VERSION \
  --title "$VERSION"

echo "Release $VERSION published!"
