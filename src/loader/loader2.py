import os
def parse_memory_file(memory_file="memory.txt"):
    """
    Parses the memory.txt file to extract the existing .text section and identify section boundaries.

    Args:
        memory_file (str): Path to the memory file.

    Returns:
        text_lines (list): Lines of the existing .text section.
        last_text_address (int): Last memory address used in the .text section.
        data_start_line (int): Starting line number of the .data section.
    """
    text_lines = []
    last_text_address = -1
    data_start_line = 1000  # Default start line for .data section if not found

    if os.path.exists(memory_file):
        with open(memory_file, "r") as mem_file:
            lines = mem_file.readlines()

            in_text_section = False
            for i, line in enumerate(lines):
                # Check for section headers
                if line.startswith("# .text Section"):
                    in_text_section = True
                elif line.startswith("# .data Section"):
                    in_text_section = False
                    data_start_line = i  # Mark the line where .data section starts
                    break

                # Capture lines and the last address in the .text section
                if in_text_section and line.strip():
                    text_lines.append(line.strip())
                    parts = line.split()
                    if len(parts) > 1:  # Ensure valid line
                        try:
                            address = int(parts[0], 16)
                            last_text_address = max(last_text_address, address)
                        except ValueError:
                            pass  # Ignore invalid lines

    return text_lines, last_text_address, data_start_line


def load_sections_and_registers_from_bin(executable_file, memory_file="memory.txt", register_file="register.txt"):
    """
    Reads the .bin file, appends .text and .data sections, and updates memory and register files.

    Args:
        executable_file (str): Path to the .bin file.
        memory_file (str): Path to the memory file.
        register_file (str): Path to the register file.
    """
    # Parse memory.txt to get existing .text content and boundaries
    existing_text, last_text_address, data_start_line = parse_memory_file(memory_file)

    # Read the .bin file
    with open(executable_file, "r") as bin_file:
        lines = bin_file.readlines()

    # Parse entry point and sections from the binary file
    entry_point = None
    text_binary = []
    data_binary = []
    reading_text = False
    reading_data = False

    for line in lines:
        line = line.strip()

        # Extract entry point
        if line.startswith("ENTRY"):
            entry_point = line.split()[1]
            print(f"Entry point found: {entry_point}")
        elif line.startswith(".text"):
            reading_text = True
            reading_data = False
        elif line.startswith(".data"):
            reading_text = False
            reading_data = True
        elif reading_text:
            text_binary.append(line)
        elif reading_data:
            data_binary.append(line)

    if entry_point is None:
        raise ValueError("Error: Entry point not found in .bin file.")

    # Prepare updated memory content
    memory = []

    # Preserve existing .text section and append new instructions
    memory.append("# .text Section")
    memory.extend(existing_text)  # Keep the existing .text section

    # Start new instructions from the next available address
    current_text_address = last_text_address + 1 if last_text_address >= 0 else 0
    for instruction in text_binary:
        memory.append(f"{current_text_address:04X} {instruction}")
        current_text_address += 1

    # Add padding to align .data section to line 1000 if needed
    while len(memory) < data_start_line:
        memory.append("")

    # Append .data section
    memory.append("# .data Section")
    current_data_address = data_start_line
    for data in data_binary:
        memory.append(f"{current_data_address:04X} {data}")
        current_data_address += 1

    # Write updated memory to memory.txt
    with open(memory_file, "w") as mem_file:
        mem_file.write("\n".join(memory))
    print(f"Memory updated in {memory_file}")

    # Handle register file
    registers = []
    if not os.path.exists(register_file):
        # Create register file if it doesn't exist
        registers.append(f"PC {entry_point}\n")
        for i in range(1, 32):
            registers.append(f"R{i} 0000\n")
        print(f"{register_file} created with PC set to {entry_point} and registers initialized.")
    else:
        # Update existing registers
        with open(register_file, "r") as reg_file:
            registers = reg_file.readlines()

        pc_updated = False
        for i, line in enumerate(registers):
            if line.startswith("PC"):
                registers[i] = f"PC {entry_point}\n"
                pc_updated = True
                break

        if not pc_updated:
            registers.insert(0, f"PC {entry_point}\n")

    # Write updated registers to register.txt
    with open(register_file, "w") as reg_file:
        reg_file.writelines(registers)
    print(f"PC register updated or initialized in {register_file}")


# Example usage
executable_file = "test1.bin"
load_sections_and_registers_from_bin(executable_file)
