import pandas as pd
import re

def build_dataframe(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    blocks = []
    current_block = []

    for line in lines:
        if line.startswith("00:") or line.startswith("01:"):
            if current_block:
                blocks.append(" ".join(current_block))
                current_block = []
        current_block.append(line)

    if current_block:
        blocks.append(" ".join(current_block))

    # Parse blocks into structured rows
    rows = []
    for block in blocks:
        match = re.match(r"\d{2}:\d{2}:\d{2}\s+—\s+(Speaker\s+[12])\s+(.*)", block)
        if match:
            speaker, text = match.groups()
            speaker_id = 1 if speaker == "Speaker 1" else 2
            rows.append([speaker_id, text, "", ""])

    df = pd.DataFrame(rows, columns=["Speaker", "Text", "Col3", "Col4"])
    print(df)

# Example usage
build_dataframe("input_transcript.txt")
