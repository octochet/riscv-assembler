import struct

def read_binary(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(12)  # Example header: 4 bytes each for `.text`, `.data`, `.bss` sizes
        text_size, data_size, bss_size = struct.unpack('III', header)
        text_section = f.read(text_size).hex()  # Convert to hex for readability
        data_section = f.read(data_size).hex()
        return {'text': text_section, 'data': data_section, 'bss': bss_size}

def link_binaries_to_txt(input_files, output_txt):
    combined_text = ""
    combined_data = ""
    bss_total = 0

    for idx, file in enumerate(input_files, start=1):
        binary = read_binary(file)
        combined_text += f"// Text Section from {file}\n{binary['text']}\n\n"
        combined_data += f"// Data Section from {file}\n{binary['data']}\n\n"
        bss_total += binary['bss']

    with open(output_txt, 'w') as out:
        # Write metadata and sections in human-readable format
        out.write("=== LINKED BINARY OUTPUT ===\n")
        out.write(f"Total BSS Size: {bss_total} bytes\n\n")
        out.write("=== COMBINED TEXT SECTION ===\n")
        out.write(combined_text)
        out.write("\n=== COMBINED DATA SECTION ===\n")
        out.write(combined_data)

# Example usage
link_binaries_to_txt(['input_0.bin', 'input_1.bin'], 'linked_output.txt')
