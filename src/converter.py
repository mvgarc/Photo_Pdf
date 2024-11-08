# `import os` is a Python statement that imports the `os` module, which provides a way to interact
# with the operating system. This module allows you to perform various operating system-related tasks
# such as file operations, directory operations, and environment variables manipulation.
import os
# The statement `from PIL import Image` is importing the `Image` module from the Python Imaging
# Library (PIL) or its fork Pillow. This module provides functionality for working with images in
# various formats, such as opening, manipulating, and saving images. It allows you to perform tasks
# like image processing, resizing, cropping, and applying filters to images in your Python code.
# The statement `from PIL import Image` is importing the `Image` module from the Python Imaging
# Library (PIL) or its fork Pillow. This module provides functionality for working with images in
# various formats, such as opening, manipulating, and saving images. It allows you to perform tasks
# like image processing, resizing, cropping, and applying filters to images in your Python code.
from PIL import Image
# `import pytesseract` is a Python statement that imports the `pytesseract` module. `pytesseract` is a
# Python wrapper for Google's Tesseract-OCR Engine, which is used for optical character recognition
# (OCR). By importing `pytesseract`, you can utilize its functionality to extract text from images or
# scanned documents in your Python code. This module allows you to perform tasks like reading text
# from images, PDFs, or other scanned documents, making it easier to work with textual content in such
# formats.
import pytesseract
# The statement `from docx import Document` is importing the `Document` class from the `docx` module.
# This module allows you to work with Microsoft Word (.docx) files in Python. By importing the
# `Document` class, you can create, read, and manipulate Word documents programmatically using Python
# code. This can include tasks such as creating new documents, modifying existing documents,
# extracting text, formatting, adding tables, images, and more.
from docx import Document
# `from fpdf import FPDF` is a Python statement that imports the `FPDF` class from the `fpdf` module.
# FPDF is a popular library for creating PDF documents in Python. By importing the `FPDF` class, you
# can utilize its functionality to generate PDF files programmatically. This includes tasks such as
# adding text, images, and shapes to the PDF, setting fonts and styles, creating multi-page documents,
# and more. It provides a convenient way to create custom PDF documents from within your Python code.
from fpdf import FPDF

# This line of code `pytesseract.pytesseract.tesseract_cmd = r'C:\Program
# Files\Tesseract-OCR\tesseract.exe'` is setting the path to the Tesseract executable file on your
# system.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_image_to_text(image_path):
    """
    The function `convert_image_to_text` takes an image file path as input, uses pytesseract to extract
    text from the image, and returns the extracted text.
    
    :param image_path: The `image_path` parameter in the `convert_image_to_text` function is a string
    that represents the file path to the image file that you want to convert to text. This function uses
    pytesseract library to perform optical character recognition (OCR) on the image and extract the text
    content from it
    :return: The function `convert_image_to_text` returns the text extracted from the image located at
    the specified `image_path`.
    """
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def save_to_word(text, output_path):
    """
    The function `save_to_word` saves the input text to a Word document at the specified output path.
    
    :param text: The `text` parameter in the `save_to_word` function is the content that you want to
    save to a Word document. This content will be added as a paragraph in the Word document
    :param output_path: The `output_path` parameter in the `save_to_word` function is the file path
    where you want to save the Word document. You should provide the full file path including the file
    name and extension (e.g., "C:/Documents/output.docx")
    """
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def save_to_pdf(text, output_path):
    """
    The function `save_to_pdf` takes a text input and saves it as a PDF file at the specified output
    path.
    
    :param text: The `text` parameter in the `save_to_pdf` function is the content that you want to save
    to a PDF file. This content will be written to the PDF file specified by the `output_path` parameter
    :param output_path: The `output_path` parameter in the `save_to_pdf` function is the file path where
    the generated PDF file will be saved. It should be a string representing the full path including the
    file name and extension (e.g., "C:/Documents/output.pdf")
    """
    pdf = FPDF
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0,10, text)
    pdf.output(output_path)

def batch_convert_images_to_docs(image_folder, output_folder):
    """
    The function `batch_convert_images_to_docs` converts images in a specified folder to text, saves the
    text to Word and PDF files in an output folder, and prints a message for each conversion.
    
    :param image_folder: The `image_folder` parameter in the `batch_convert_images_to_docs` function
    refers to the directory path where the input images are located. This function is designed to batch
    convert images in this folder to both Word (.docx) and PDF formats
    :param output_folder: The `output_folder` parameter in the `batch_convert_images_to_docs` function
    is the directory where the converted Word (.docx) and PDF files will be saved. This function creates
    the output folder if it doesn't already exist and saves the converted files in that location
    """
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(image_folder,filename)
            base_filename = os.path.splitext(filename)[0]
            text = convert_image_to_text(image_path)
            word_path = os.path.join(output_folder, f"{base_filename}.docx")
            save_to_word(text, word_path)
            pdf_path = os.path.join(output_folder, f"{base_filename}.pdf")
            save_to_pdf(text, pdf_path)
            print(f"Convertido: {filename} a Word y PDF")

script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, "..", "assets", "input_images")
input_folder = os.path.abspath(input_folder)
