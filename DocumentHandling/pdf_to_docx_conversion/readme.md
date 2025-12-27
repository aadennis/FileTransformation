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

### Execution

```linux
python3 ./convert_batch_pdf_to_docx.py
```
