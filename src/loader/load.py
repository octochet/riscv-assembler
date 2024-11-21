import os

def load_binary_to_memory_and_registers(bin_file_path, memory_file_path="memory.txt", register_file_path="register.txt"):
    try:
        # Initialize variables for `.text` and `.data` section positions
        text_end = 0
        data_start = 1000
        entry_point = None

        # Read the existing memory file (if it exists) to determine current positions
        try:
            with open(memory_file_path, 'r') as memory_file:
                memory_lines = memory_file.readlines()
                
                # Determine where the `.text` and `.data` sections end
                for i, line in enumerate(memory_lines):
                    if line.strip():  # Non-empty line
                        if i < 1000:
                            text_end = max(text_end, i + 1)  # End of `.text`
                        else:
                            data_start = max(data_start, i + 1)  # End of `.data`
        except FileNotFoundError:
            # If the memory file doesn't exist, start fresh
            memory_lines = []

        # Parse the binary file to extract `.text`, `.data`, and the entry point
        with open(bin_file_path, 'r') as bin_file:
            lines = bin_file.readlines()
        
        text_section = []
        data_section = []
        is_data_section = False

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith("ENTRY"):
                entry_point = stripped_line.split()[1]
            elif stripped_line == ".data":
                is_data_section = True
                continue
            elif stripped_line == ".text":
                is_data_section = False
                continue
            
            if is_data_section:
                data_section.append(stripped_line)
            elif stripped_line and not stripped_line.startswith("ENTRY"):
                text_section.append(stripped_line)

        if entry_point is None:
            raise ValueError("Error: Entry point not found in the binary file.")

        # Prepare updated memory content
        with open(memory_file_path, 'w') as memory_file:
            # Write existing `.text` content
            for i, line in enumerate(memory_lines[:text_end]):
                memory_file.write(line)
            
            # Append new `.text` content
            for line in text_section:
                memory_file.write(line + '\n')
            
            # Add empty lines to align `.data` section if necessary
            lines_to_add = max(1000 - text_end, 0) - len(text_section)
            memory_file.write('\n' * lines_to_add)
            
            # Write existing `.data` content
            for i, line in enumerate(memory_lines[data_start:]):
                memory_file.write(line)
            
            # Append new `.data` content
            for line in data_section:
                memory_file.write(line + '\n')

        print(f"Binary file '{bin_file_path}' successfully loaded into '{memory_file_path}'!")

        # Update or create the register file
        registers = []
        if not os.path.exists(register_file_path):
            # Create a new register file with all registers initialized
            registers.append(f"PC {entry_point}\n")  # Set PC to entry point
            for i in range(1, 32):  # Assuming 32 general-purpose registers
                registers.append(f"R{i} 0000\n")
            print(f"Register file '{register_file_path}' created with PC set to {entry_point}.")
        else:
            # Update the existing register file
            with open(register_file_path, 'r') as reg_file:
                registers = reg_file.readlines()
            
            # Update the PC register
            pc_updated = False
            for i, line in enumerate(registers):
                if line.startswith("PC"):
                    registers[i] = f"PC {entry_point}\n"
                    pc_updated = True
                    break
            
            # If PC does not exist, add it
            if not pc_updated:
                registers.insert(0, f"PC {entry_point}\n")

        # Write updated registers to the file
        with open(register_file_path, 'w') as reg_file:
            reg_file.writelines(registers)

        print(f"Register file '{register_file_path}' updated with PC set to {entry_point}.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
bin_file_path = "test1.bin"  # Path to the binary file
memory_file_path = "memory.txt"
register_file_path = "register.txt"

# Load binary file into memory and update registers
load_binary_to_memory_and_registers(bin_file_path, memory_file_path, register_file_path)
