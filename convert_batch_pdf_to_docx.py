# run as linux!
# sudo apt update
# sudo apt install poppler-utils
# pip install pdf2image pillow python-docx

from docx import Document
from docx.shared import Inches
from pathlib import Path
from pdf2image import convert_from_path

def convert_pdfs_to_pngs(input_folder: Path, output_folder: Path, dpi: int = 300):
    for old_png in output_folder.glob("*.png"):
        old_png.unlink()
    output_folder.mkdir(exist_ok=True)
    pdf_files = sorted(input_folder.glob("*.pdf"))

    for pdf_file in pdf_files:
        try:
            print(f"Converting {pdf_file.name}...")
            images = convert_from_path(pdf_file, dpi=dpi)
            out_name = output_folder / (pdf_file.stem + ".png")
            images[0].save(out_name, "PNG")
        except Exception as e:
            print(f"Failed to convert {pdf_file.name}: {e}")

    print(f"Converted {len(pdf_files)} PDFs to PNGs.")

def build_docx_from_images(image_folder: Path, output_docx: Path, image_width_in: float = 6.5):
    doc = Document()
    image_files = sorted(image_folder.glob("*.png"))

    for image_path in image_files:
        print(f"Inserting {image_path.name}...")
        doc.add_picture(str(image_path), width=Inches(image_width_in))

    doc.save(output_docx)
    print(f"Inserted {len(image_files)} images into {output_docx.name}.")

def main():
    input_folder = Path("/mnt/sc/temp/downloads/")
    output_folder = input_folder / "png_out"
    output_docx = output_folder.parent / "png_combined.docx"
    
    convert_pdfs_to_pngs(input_folder, output_folder)
    build_docx_from_images(output_folder, output_docx)

if __name__ == "__main__":
    main()

