from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from docx import Document
from fpdf import FPDF
import os

# === 1. Setup ===
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pdf_path = r"C:\Users\...pdf"

# === 2. Output folder ===
output_folder = os.path.join(os.path.expanduser("~"), "Documents", "OCR_Results")
os.makedirs(output_folder, exist_ok=True)

# === 3. Convert PDF to images ===
pages = convert_from_path(pdf_path)

# === 4. OCR all pages ===
all_text = ""
for i, page in enumerate(pages):
    print(f"\n--- Page {i+1} ---")
    text = pytesseract.image_to_string(page)
    print(text)
    all_text += f"\n\n--- Page {i+1} ---\n{text}"

# === 5. Save DOCX ===
docx_output = os.path.join(output_folder, "ocr_output.docx")
doc = Document()
doc.add_paragraph(all_text)
doc.save(docx_output)
print(f"DOCX saved to: {docx_output}")

# === 6. Save PDF ===
pdf_output = os.path.join(output_folder, "ocr_output.pdf")
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

for line in all_text.splitlines():
    if line.strip() == "":
        pdf.ln()
    else:
        pdf.multi_cell(0, 10, line)

pdf.output(pdf_output)
print(f"PDF saved to: {pdf_output}")
