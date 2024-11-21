import os

def load_sections_and_registers_from_bin(executable_file, memory_file="memory.txt", register_file="register.txt"):
    """
    Reads the .bin file, extracts entry point, loads .text and .data sections into memory,
    and updates the PC register in registers. Creates files if they do not exist.

    Args:
        executable_file (str): Path to the .bin file.
        memory_file (str): Output memory file name.
        register_file (str): Register file name (to update PC).
    """
    # Read the binary file
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

        # Extract entry point (Assumed format: ENTRY <address>)
        if line.startswith("ENTRY"):
            entry_point = line.split()[1]
            print(f"Entry point found: {entry_point}")
        
        # Identify .text section
        elif line.startswith(".text"):
            reading_text = True
            reading_data = False

        # Identify .data section
        elif line.startswith(".data"):
            reading_text = False
            reading_data = True

        # Store binary code
        elif reading_text:
            text_binary.append(line)
        
        elif reading_data:
            data_binary.append(line)

    # Ensure entry point is found
    if entry_point is None:
        raise ValueError("Error: Entry point not found in .bin file.")

    # Prepare memory data
    memory = []

    # Load .text section
    memory.append("# .text Section")
    for i, instruction in enumerate(text_binary):
        address = i  # .text starts from address 0x0000
        memory.append(f"{address:04X} {instruction}")

    # Add padding to align .data section to line 1000
    while len(memory) < 1000:
        memory.append("")  # Blank lines

    # Load .data section
    memory.append("# .data Section")
    for i, data in enumerate(data_binary):
        address = 0x1000 + i  # .data starts from address 0x1000
        memory.append(f"{address:04X} {data}")

    # Write memory to memory.txt
    with open(memory_file, "w") as mem_file:
        mem_file.write("\n".join(memory))
    print(f"Memory loaded into {memory_file}")

    # Handle register file
    registers = []
    if not os.path.exists(register_file):
        # Create register file if it doesn't exist
        registers.append(f"PC {entry_point}\n")  # Initialize PC to entry point
        for i in range(1, 32):  # Assuming 32 registers
            registers.append(f"R{i} 0000\n")  # Initialize other registers to 0
        print(f"{register_file} created with PC set to {entry_point} and registers initialized.")
    else:
        # Read existing registers
        with open(register_file, "r") as reg_file:
            registers = reg_file.readlines()

        # Update PC register
        pc_updated = False
        for i, line in enumerate(registers):
            if line.startswith("PC"):
                registers[i] = f"PC {entry_point}\n"  # Update PC to entry point
                pc_updated = True
                break

        # If PC doesn't exist, add it
        if not pc_updated:
            registers.insert(0, f"PC {entry_point}\n")  # Add PC at the beginning

    # Write updated or new registers to register.txt
    with open(register_file, "w") as reg_file:
        reg_file.writelines(registers)
    print(f"PC register updated or initialized in {register_file}")


# Example usage
executable_file = "test1.bin"  # Replace with the path to your .bin file
load_sections_and_registers_from_bin(executable_file)
