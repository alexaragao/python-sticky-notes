# 🏗️ MacOS Packaging

This file contains more details on packaging the app for MacOS.

## ℹ️ Information
- For building the app for macOS, this project uses `py2app`.
- All settings for the app are in `setup-macos.py` file.

## 📝 Scripts
All scripts for macOS packaging are in the project [Makefile](../Makefile). 

### 🎨 Changing the icon
To change the app icon:
1. Replace `assets/icon.png` with your custom icon.
2. Run a script for create the `.icns` file:
```sh
make macos-create-icns
```

### 🏗️ Packaging
1. Run the build script:
```sh
make macos-build
```

## 🚨 IMPORTANT!
- Do not update `setuptools` package. It's been known that the versions above it [may causes crashes](https://github.com/ronaldoussoren/py2app/issues/531).
