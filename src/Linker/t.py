def process_input(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    text_section = []
    data_section = []
    is_data_section = False

    # Separate .text and .data sections
    for line in lines:
        line = line.strip()
        if line == ".text":
            is_data_section = False
        elif line == ".data":
            is_data_section = True
        elif is_data_section:
            data_section.append(line)
        else:
            text_section.append(line)

    return text_section, data_section


def write_output(text_section, data_section, output_file):
    with open(output_file, 'w') as f:
        f.write("Linked .text section:\n")
        for line in text_section:
            f.write(f"{line}\n")
        
        f.write("\nLinked .data section:\n")
        for line in data_section:
            f.write(f"{line}\n")


if __name__ == "__main__":
    input_file = "input_file.txt"  # Change this to your input file
    output_file = "final_output.txt"
    
    # Process the input file
    text_section, data_section = process_input(input_file)
    
    # Write to the output file
    write_output(text_section, data_section, output_file)
