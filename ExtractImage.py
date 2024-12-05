#!/usr/local/bin/python3
import os
from pdf2image import convert_from_path
pdf_path = "/Users/jbailey/Desktop/Jazlynn_Website/images/NEONProject.pdf"
output_folder = "/Users/jbailey/Desktop/Jazlynn_Website/images/"

# PDF to images
try:
    pages = convert_from_path(pdf_path, 300)
except Exception as e:
    print(f"Error: {e}")
    exit(1)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# each page as an image
for i, page in enumerate(pages):
    output_filename = os.path.join(output_folder, f'slide{i+1}.jpg')
    page.save(output_filename, 'JPEG')
    print(f"Saved {output_filename}")
