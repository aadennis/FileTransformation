# PDF to Word Image Compiler

This Python script (`convert_batch_pdf_to_docx.py`) automates the process of converting a batch of single-page PDF files into a single Word document, with each page represented as a high-resolution image.

## 📌 Features

- Converts each single-page PDF to a high-quality PNG image using `pdf2image`
- Inserts each image into a Word document using `python-docx`
- Automatically cleans up old images before each run
- Maintains the order of pages based on filename sorting

## 🛠 Requirements

- Python 3.7+
- Linux or WSL (Windows Subsystem for Linux)

### Install Dependencies

```bash
sudo apt update
sudo apt install poppler-utils
pip install pdf2image pillow python-docx
```

## 📂 Folder Structure

Place your single-page PDFs in a folder (e.g., `/mnt/sc/temp/downloads/`). The script will:

- Convert them to PNGs in a subfolder called `png_out/`
- Create a Word document named `png_combined.docx` in the same parent folder

## 🚀 Usage

Run the script directly:

```bash
python3 pdf_to_word_images.py
```

## 🧩 Customization

- Change `dpi` in `convert_pdfs_to_pngs()` to adjust image quality
- Modify `image_width_in` in `build_docx_from_images()` to scale images differently
- Update `input_folder` in `main()` to point to your desired PDF directory

## 📝 Notes

- This script assumes each PDF contains a single page
- Output Word document is image-based (not editable text)
- Ideal for preserving layout and visual fidelity

## 📄 License

MIT License — feel free to use, modify, and share.
