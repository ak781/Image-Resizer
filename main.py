import os
from PIL import Image

# Folder containing input images
input_folder = 'images_input'
output_folder = 'images_output'

# Desired size (width, height)
resize_size = (800, 800)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            resized_img = img.resize(resize_size)
            resized_img.save(output_path)

print("All images resized and saved to:", output_folder)
