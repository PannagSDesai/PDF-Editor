from setuptools import logging
import os
from pypdf import PdfWriter
import logging     


def quality(input_path, output_path, quality=80):
    writer = PdfWriter(clone_from=input_path)
    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=quality)
    writer.write(output_path)

def losless_quality(input_path, output_path):
    logging.warning("This is a CPU intensive process, Please be patient")
    writer = PdfWriter(clone_from=input_path)
    for page in writer.pages:
        page.compress_content_streams()
    writer.write(output_path)
    

quality_choices = {
    1: 20,
    2: 40,
    3: 60,
    4: 80,
    5: 100
}

if os.path.exists("Documents"):
    for i in os.listdir("Documents"):
        if i.endswith(".pdf"):
            quality("Documents/" + i, "Documents/" + i + "_compressed.pdf")
else:
    print("No files to process, Please make sure to add your Protected files under the documents")