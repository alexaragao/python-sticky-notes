from setuptools import setup

APP = ['src/app.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['PyQt5'],
    'iconfile': 'assets/icon.icns',
    'plist': {
        'CFBundleName': 'Sticky Notes',
        'CFBundleIdentifier': 'com.alexaragao.stickynotes',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
