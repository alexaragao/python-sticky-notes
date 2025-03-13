@echo off

set description="A simple sticky notes application"

python -m nuitka ^
    --standalone ^
    --onefile ^
    --mingw64 ^
    --windows-icon-from-ico=assets/icon.ico ^
    --windows-console-mode=disable ^
    --windows-product-name="Sticky Notes" ^
    --windows-file-version=1.0.0 ^
    --windows-file-description=%description% ^
    --enable-plugin=pyqt5 ^
    --output-dir=dist  ^
    --output-filename="stickynotes-windows.exe" ^
    src/app.py
