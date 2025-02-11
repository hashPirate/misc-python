import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import io

def append_image_to_pdf(imagePath,pdfPath,outputPath):
    packet = io.BytesIO()
    can = canvas.Canvas(packet,pagesize=letter)
    can.drawImage(imagePath,100,500,width=400,height=300) 
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(pdfPath)
    writer = PdfWriter()
    for page_num in range(len(existing_pdf.pages)):
        writer.add_page(existing_pdf.pages[page_num])
    writer.add_page(new_pdf.pages[0])
    with open(outputPath, "wb") as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append an image to the end of a PDF file.")
    parser.add_argument("image_path",help="Path to the image file.")
    parser.add_argument("pdf_path",help="Path to the original PDF file.")
    parser.add_argument("output_pdf_path",help="Path to save the modified PDF with the image appended.")
    args = parser.parse_args()
    append_image_to_pdf(args.image_path,args.pdf_path,args.output_pdf_path)
