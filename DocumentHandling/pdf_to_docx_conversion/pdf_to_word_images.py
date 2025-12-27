# run as linux!
# Setup instructions:
# sudo apt update
# sudo apt install mupdf-tools
# pip install python-docx

from docx import Document
from docx.shared import Inches
from pathlib import Path
import subprocess

def convert_pdfs_to_pngs(input_folder: Path, output_folder: Path, dpi: int = 300):
    """
    Converts all single-page PDF files in the input folder to PNG images using mutool.
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
        out_name = output_folder / (pdf_file.stem + ".png")
        try:
            print(f"Converting {pdf_file.name} with mutool...")
            subprocess.run([
                "mutool", "convert",
                "-O", f"resolution={dpi}",
                "-o", str(out_name),
                str(pdf_file)
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"mutool failed on {pdf_file.name}: {e}")

    print(f"Processed {len(pdf_files)} PDFs.")

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
    resolution = 300
    convert_pdfs_to_pngs(input_folder, output_folder, dpi=300)
    build_docx_from_images(output_folder, output_docx)

if __name__ == "__main__":
    main()
