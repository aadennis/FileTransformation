import pandas as pd
import re

def build_dataframe_with_index(input_file):
    """
    Read a transcript text file, group lines into timestamp/speaker blocks,
    and build a DataFrame with an index, speaker id, concatenated text,
    and a timestamp marker that appears only for the first row of each minute.

    The resulting DataFrame is printed and saved as a pipe-delimited file
    named 'output_transcript.txt'.
    """
    # Open the input file and read non-empty lines, stripping surrounding whitespace
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Split the lines into blocks. Each block begins with a timestamp header line
    # that starts with "00:" or "01:" (hour prefixes used in this transcript).
    blocks = []
    current_block = []

    for line in lines:
        # Start a new block when we encounter a header line (timestamp beginning)
        if line.startswith("00:") or line.startswith("01:"):
            if current_block:
                blocks.append(current_block)
                current_block = []
        current_block.append(line)

    # Append the final block if present
    if current_block:
        blocks.append(current_block)

    rows = []
    last_minute = None  # used to only show the timestamp marker when minute changes

    # Iterate over blocks and parse header + text
    for i, block in enumerate(blocks):
        if len(block) < 2:
            # skip incomplete blocks that don't have both header and text
            continue

        header = block[0]
        # Join any subsequent lines in the block into a single text field
        text = " ".join(block[1:])

        # Expected header format: HH:MM:SS Speaker N
        match = re.match(r"(\d{2}):(\d{2}):(\d{2})\s+Speaker\s+(1|2)", header)
        if match:
            hh, mm, ss, speaker_id = match.groups()
            timestamp = f"{hh}:{mm}:{ss}"
            minute = int(mm)
            speaker_id = int(speaker_id)

            # Column 3: include a timestamp marker like "[HH:MM:SS]"
            # only if this is the first row or the minute has changed since the last row.
            if i == 0 or minute != last_minute:
                col3 = f"[{timestamp}]"
                last_minute = minute
            else:
                col3 = ""

            # Use a 1-based index for the "Index" column
            index = i + 1
            rows.append([index, speaker_id, text, col3])

    # Build DataFrame with explicit column names
    df = pd.DataFrame(rows, columns=["Index", "Speaker", "Text", "Timestamp Marker"])
    print(df)

    # Save to a pipe-delimited file without the DataFrame index
    df.to_csv("output_transcript.txt", sep="|", index=False, encoding="utf-8")
    print("✅ Pipe-delimited file saved as output_transcript.txt")

# Example usage: call the function with the transcript filename
build_dataframe_with_index("erp.txt")
