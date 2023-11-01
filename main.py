from PIL import Image
import os

 # Specify the input folder containing JPEG images
input_folder = "C:\\Users\\Laptop\\Downloads\\init"

 # Specify the output folder for WebP images
output_folder = "C:\\Users\\Laptop\\Downloads\\outit"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
files = os.listdir(input_folder)

# Initialize a counter to keep track of the number of files converted
conversion_count = 0

for file in files:
    # Check if the file is a JPEG or PNG image
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        # Open the image
        image = Image.open(os.path.join(input_folder, file))

        # Generate the output filename by replacing the extension with .webp
        output_filename = os.path.splitext(file)[0] + ".webp"

        # Save the image in WebP format to the output folder
        image.save(os.path.join(output_folder, output_filename), "webp")
        
        # Increment the conversion count
        conversion_count += 1

        # Print the name of the output file

print(f"Conversion complete. {conversion_count} files converted.")
