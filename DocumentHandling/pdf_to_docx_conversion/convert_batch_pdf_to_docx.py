# run as linux!
# Setup instructions:
# sudo apt update
# sudo apt install poppler-utils
# pip install pdf2image pillow python-docx

from docx import Document
from docx.shared import Inches
from pathlib import Path
from pdf2image import convert_from_path

def convert_pdfs_to_pngs(input_folder: Path, output_folder: Path, dpi: int = 300):
    """
    Converts all single-page PDF files in the input folder to PNG images.
    Cleans the output folder before writing new images.
    """
    # Remove any existing PNGs in the output folder
    if output_folder.exists():
        for old_png in output_folder.glob("*.png"):
            old_png.unlink()
    output_folder.mkdir(exist_ok=True)

    # Find and sort all PDF files in the input folder
    pdf_files = sorted(f for f in input_folder.glob("*.pdf") if f.is_file())

    for pdf_file in pdf_files:
        try:
            print(f"Converting {pdf_file.name}...")
            # Convert PDF to image(s) at specified DPI
            images = convert_from_path(pdf_file, dpi=dpi)
            # Save the first (and only) page as PNG
            out_name = output_folder / (pdf_file.stem + ".png")
            images[0].save(out_name, "PNG")
        except Exception as e:
            print(f"Failed to convert {pdf_file.name}: {e}")

    print(f"Converted {len(pdf_files)} PDFs to PNGs.")

def build_docx_from_images(image_folder: Path, output_docx: Path, image_width_in: float = 6.5):
    """
    Creates a Word document with each PNG image inserted on its own page.
    Images are scaled to the specified width (default 6.5 inches).
    """
    doc = Document()
    image_files = sorted(image_folder.glob("*.png"))

    for image_path in image_files:
        print(f"Inserting {image_path.name}...")
        doc.add_picture(str(image_path), width=Inches(image_width_in))

    doc.save(output_docx)
    print(f"Inserted {len(image_files)} images into '{output_docx}'.")

def main():
    # Define input and output paths
    input_folder = Path("/mnt/sc/temp/downloads/")
    output_folder = input_folder / "png_out"
    output_docx = output_folder.parent / "png_combined.docx"

    # Run conversion and document creation
    convert_pdfs_to_pngs(input_folder, output_folder)
    build_docx_from_images(output_folder, output_docx)

if __name__ == "__main__":
    main()