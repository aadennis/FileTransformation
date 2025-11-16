import re

def convert_transcript_to_pipe(input_file, output_file):
    """
    Reads a timestamped transcript and writes it as a pipe-delimited file.
    Format: timestamp | speaker | text
    """
    pattern = re.compile(r"^(\d{2}:\d{2}:\d{2})\s+(Speaker\s+\d+)\s+(.*)")

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            match = pattern.match(line)
            if match:
                timestamp, speaker, text = match.groups()
                outfile.write(f"{timestamp} | {speaker} | {text}\n")
            else:
                # Handle continuation lines (no timestamp/speaker)
                outfile.write(f"    |    | {line}\n")

    print(f"Converted transcript saved to: {output_file}")

# Example usage
convert_transcript_to_pipe("input_transcript.txt", "output_transcript.txt")


