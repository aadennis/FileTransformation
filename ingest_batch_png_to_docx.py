from docx import Document
from docx.shared import Inches
from pathlib import Path

# Folder containing your PNGs
image_folder = Path("/mnt/c/temp/downloads/png_out")
output_docx = image_folder.parent / "png_combined.docx"

# Create a new Word document
doc = Document()

# Sort images by filename
image_files = sorted(image_folder.glob("*.png"))

for i, image_path in enumerate(image_files):
    print(f"Inserting {image_path.name}...")
    
    # Add image (scale to page width if needed)
    doc.add_picture(str(image_path), width=Inches(6.5))
    
    # Add a page break after each image except the last
    if i < len(image_files) - 1:
        doc.add_page_break()

# Save the document
doc.save(output_docx)
print(f"Saved to {output_docx}")