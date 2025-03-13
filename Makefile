# Makefile

# Install dependencies for the project
install:
	pip install -r requirements.txt

# Runs the project locally (activate the virtual environment first!)
run:
	python src/app.py

# Run the tests
test:
	pytest

# MacOS specific commands

# Create the .icns file for the app
macos-create-icns:
	sh scripts/create_icns.sh assets/icon.png

# Build the app for MacOS
macos-build:
	python setup-macos.py py2app

# Clean the build and dist folders
macos-clean:
	rm -rf build dist
