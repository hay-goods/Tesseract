from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Set Tesseract executable path (only needed on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Full path to the PDF
pdf_path = r"C:\Users\...\data_analysis_epi_review.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_path)

# OCR each page
for i, page in enumerate(pages):
    print(f"\n--- Page {i+1} ---")
    print(pytesseract.image_to_string(page))

# Example: OCR an image
##img = Image.open("sample_image.png")
##text = pytesseract.image_to_string(img)
##print("Image OCR Result:\n", text)

# Example: OCR from a PDF
##pages = convert_from_path("sample_doc.pdf")
##for i, page in enumerate(pages):
##    print(f"\n--- Page {i+1} ---")
##    print(pytesseract.image_to_string(page))

##python ocr_example.py
