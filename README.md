# PDF-Image-Deck-Generator

## Description

This is a Python script that takes a set of images from a specific folder and generates a PDF file with them. Each image is resized to a specific size, given a black border and a random number, and placed onto a PDF page.

## Dependencies

- Python 3.x
- PIL (Pillow)
- ReportLab

## Dependency Installation

Run the following commands to install the dependencies:

\`\`\`bash
pip install Pillow
pip install reportlab
\`\`\`

## Usage

1. Clone this repository.
2. Open the terminal and navigate to the project folder.
3. Run `python main.py`.
4. Follow the on-screen instructions to specify the folder with images.

## Main Functions

- `load_images_from_folder(folder_path)`: Loads all images from a folder into a list.
- `process_image(image_path, cell_size)`: Processes an image by resizing it and adding a black border and a random number.

## License

This is free and unencumbered software released into the public domain.

For more information, please refer to <http://unlicense.org/>
