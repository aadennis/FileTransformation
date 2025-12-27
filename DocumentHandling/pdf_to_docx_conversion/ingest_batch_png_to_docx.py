from docx import Document
from docx.shared import Inches
from pathlib import Path

def build_docx_from_images(image_folder: Path, output_docx: Path, image_width_in: float = 6.5):
    doc = Document()
    image_files = sorted(image_folder.glob("*.png"))

    for image_path in image_files:
        print(f"Inserting {image_path.name}...")
        doc.add_picture(str(image_path), width=Inches(image_width_in))

    doc.save(output_docx)
    print(f"Saved to {output_docx}")

def main():
    image_folder = Path("/mnt/c/temp/downloads/png_out")
    output_docx = image_folder.parent / "png_combined.docx"
    build_docx_from_images(image_folder, output_docx)

if __name__ == "__main__":
    main()
