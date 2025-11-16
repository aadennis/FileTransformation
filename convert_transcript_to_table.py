def print_transcript_blocks(input_file):
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

    for block in blocks:
        print(block)

# Example usage
print_transcript_blocks("input_transcript.txt")
