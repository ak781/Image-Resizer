# Image Resizer Tool

## Objective
Resize and convert images in batch using Python and the Pillow library.

## Tools
- Python
- Pillow (PIL)

## Description
This script reads all images from a specified input folder, resizes them to a fixed size (default: 800x800 pixels), and saves the resized images to an output folder. It supports common image formats like `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`.

## Setup Instructions
1. Clone the Repository (or download the script):
   ```
   git clone https://github.com/ak781/Image-Resizer.git
   ```

2. Navigate to the Project Directory:
   ```
   cd image-resizer
   ```

3. Install Dependencies:
   ```
   pip install pillow
   ```

## Usage
1. Place the images you want to resize in a folder named `images_input`.

2. Run the script:
   ```
   python main.py
   ```

3. The resized images will be saved in the `images_output` folder.

## File Structure
```
image-resizer-tool/
│
├── main.py
├── images_input/         # Place original images here
└── images_output/        # Resized images will be saved here
```

## Customization
You can change the `resize_size` variable in the script to resize images to a different dimension.
```python
resize_size = (800, 800)  # Width x Height
```

## Outcome
Automates the task of resizing multiple images in bulk, saving time and effort.
