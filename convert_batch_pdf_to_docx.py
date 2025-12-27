# run as linux!
# sudo apt update
# sudo apt install poppler-utils
# pip install pdf2image pillow python-docx

from docx import Document
from docx.shared import Inches
from pathlib import Path
from pdf2image import convert_from_path

def convert_pdfs_to_pngs(input_folder: Path, output_folder: Path, dpi: int = 300):
    output_folder.mkdir(exist_ok=True)
    pdf_files = sorted(input_folder.glob("*.pdf"))

    for pdf_file in pdf_files:
        print(f"Converting {pdf_file.name}...")
        images = convert_from_path(pdf_file, dpi=dpi)
        out_name = output_folder / (pdf_file.stem + ".png")
        images[0].save(out_name, "PNG")

    print("Done.")

def build_docx_from_images(image_folder: Path, output_docx: Path, image_width_in: float = 6.5):
    doc = Document()
    image_files = sorted(image_folder.glob("*.png"))

    for image_path in image_files:
        print(f"Inserting {image_path.name}...")
        doc.add_picture(str(image_path), width=Inches(image_width_in))

    doc.save(output_docx)
    print(f"Saved to {output_docx}")

def main():
    input_folder = Path("/mnt/c/temp/downloads/")
    output_folder = input_folder / "png_out"
    convert_pdfs_to_pngs(input_folder, output_folder)

    image_folder = Path("/mnt/c/temp/downloads/png_out")
    output_docx = image_folder.parent / "png_combined.docx"
    build_docx_from_images(image_folder, output_docx)

if __name__ == "__main__":
    main()

