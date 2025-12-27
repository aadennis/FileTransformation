# run as linux!
# sudo apt update
# sudo apt install poppler-utils
# pip install pdf2image pillow

from pdf2image import convert_from_path
from pathlib import Path

# Folder containing your cc30bar-*.pdf files
input_folder = Path(r"/mnt/sc/temp/downloads/")
output_folder = input_folder / "png_out"
output_folder.mkdir(exist_ok=True)

# Loop through PDFs in alphabetical order
for pdf_file in sorted(input_folder.glob("*.pdf")):
    print(f"Converting {pdf_file.name}...")
    
    # Convert the single page PDF to a list of images (usually length 1)
    images = convert_from_path(pdf_file, dpi=300)
    
    # Save the first (and only) page as PNG
    out_name = output_folder / (pdf_file.stem + ".png")
    images[0].save(out_name, "PNG")

print("Done.")