import pandas as pd
import re

def build_dataframe_with_index(input_file):
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

    rows = []
    last_minute = None

    for i, block in enumerate(blocks):
        match = re.match(r"(\d{2}):(\d{2}):(\d{2})\s+—\s+(Speaker\s+[12])\s+(.*)", block)
        if match:
            hh, mm, ss, speaker, text = match.groups()
            timestamp = f"{hh}:{mm}:{ss}"
            minute = int(mm)
            speaker_id = 1 if speaker == "Speaker 1" else 2

            # Column 3: timestamp only if first row or minute changes
            if i == 0 or minute != last_minute:
                col3 = f"[{timestamp}]"
                last_minute = minute
            else:
                col3 = ""

            index = i + 1  # 1-based index
            rows.append([speaker_id, text, col3, index])

    df = pd.DataFrame(rows, columns=["Speaker", "Text", "Timestamp Marker", "Index"])
    print(df)

    # Save to pipe-delimited file
    df.to_csv("output_transcript.txt", sep="|", index=False, encoding="utf-8")
    print("✅ Pipe-delimited file saved as output_transcript.txt")

# Example usage
build_dataframe_with_index("input_transcript.txt")
