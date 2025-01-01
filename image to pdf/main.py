from PIL import Image
import os
import pandas as pd

# Load the CSV file
csv_file_path = 'sheet.csv'
data = pd.read_csv(csv_file_path)

# Ensure the 'full name' column is stripped of any extra spaces
data['full name'] = data['full name'].str.strip()

# Directory where the images are stored
image_directory = './Image/'  # Update with your image directory path
output_directory = './output_pdfs/'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through the rows in the DataFrame
for index, row in data.iterrows():
    image_path = os.path.join(image_directory, f"{index + 1}.jpg")
    pdf_name = f"{row['full name']}.pdf"
    pdf_path = os.path.join(output_directory, pdf_name)

    # Check if the image file exists
    if os.path.exists(image_path):
        # Open the image and convert it to RGB (if not already in RGB mode)
        with Image.open(image_path) as img:
            img_rgb = img.convert('RGB')
            img_rgb.save(pdf_path)
        print(f"Converted {image_path} to {pdf_path}")
    else:
        print(f"Image {image_path} not found. Skipping.")

print("Conversion complete. PDFs are saved in the output directory.")
