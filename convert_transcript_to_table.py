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
                blocks.append(current_block)
                current_block = []
        current_block.append(line)

    if current_block:
        blocks.append(current_block)

    rows = []
    last_minute = None

    for i, block in enumerate(blocks):
        if len(block) < 2:
            continue  # skip incomplete blocks

        header = block[0]
        text = " ".join(block[1:])  # join all following lines as text

        match = re.match(r"(\d{2}):(\d{2}):(\d{2})\s+Speaker\s+(1|2)", header)
        if match:
            hh, mm, ss, speaker_id = match.groups()
            timestamp = f"{hh}:{mm}:{ss}"
            minute = int(mm)
            speaker_id = int(speaker_id)

            # Column 3: timestamp only if first row or minute changes
            if i == 0 or minute != last_minute:
                col3 = f"[{timestamp}]"
                last_minute = minute
            else:
                col3 = ""

            index = i + 1  # 1-based index
            rows.append([index, speaker_id, text, col3])

    df = pd.DataFrame(rows, columns=["Index", "Speaker", "Text", "Timestamp Marker"])
    print(df)

    # Save to pipe-delimited file
    df.to_csv("output_transcript.txt", sep="|", index=False, encoding="utf-8")
    print("✅ Pipe-delimited file saved as output_transcript.txt")

# Example usage
build_dataframe_with_index("erp.txt")
