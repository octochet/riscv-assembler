def read_bin_file(filename):
    with open(filename, 'rb') as f:
        return f.read().decode('utf-8').splitlines()

def link_files(file1, file2):
    text_sections = []
    data_sections = []

    for file in [file1, file2]:
        lines = read_bin_file(file)
        is_data_section = False

        for line in lines:
            if line == ".text":
                is_data_section = False
            elif line == ".data":
                is_data_section = True
            elif is_data_section:
                data_sections.append(line)
            else:
                text_sections.append(line)

    return text_sections, data_sections

def write_output(text_sections, data_sections, output_file):
    with open(output_file, 'w') as f:
        f.write("Linked .text section:\n")
        for line in text_sections:
            f.write(f"{line}\n")

        f.write("\nLinked .data section:\n")
        for line in data_sections:
            f.write(f"{line}\n")

if __name__ == "__main__":
    input_file1 = "input_0.bin"
    input_file2 = "input_1.bin"
    output_file = "final_output.txt"

    text_sections, data_sections = link_files(input_file1, input_file2)
    write_output(text_sections, data_sections, output_file)