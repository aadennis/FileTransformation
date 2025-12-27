# run as linux!
# sudo apt update
# sudo apt install poppler-utils
# pip install pdf2image pillow

from pdf2image import convert_from_path
from pathlib import Path

def convert_pdfs_to_pngs(input_folder: Path, output_folder: Path, dpi: int = 300):
    output_folder.mkdir(exist_ok=True)
    pdf_files = sorted(input_folder.glob("*.pdf"))

    for pdf_file in pdf_files:
        print(f"Converting {pdf_file.name}...")
        images = convert_from_path(pdf_file, dpi=dpi)
        out_name = output_folder / (pdf_file.stem + ".png")
        images[0].save(out_name, "PNG")

    print("Done.")

def main():
    input_folder = Path("/mnt/c/temp/downloads/")
    output_folder = input_folder / "png_out"
    convert_pdfs_to_pngs(input_folder, output_folder)

if __name__ == "__main__":
    main()