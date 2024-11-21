'''
High Priority TODO:
- Reads the assembly code from the file
- Tokenizes the code, removing comments and empty lines
    - Identify the labels and their addresses
    - Identify the functions, registers and variables
- Converts the code to machine code
Output to text, bin or console

Low Priority TODO:
- pseudo instructions (e.g. swap, etc)
'''
import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from assembler import Assembler

#read filname from command line
file_path = sys.argv[1]

# file_path = "tests/test1.asm"
with open(file_path, "r") as file:
    asm_code = file.read()

assembler = Assembler()
assembler.first_pass(asm_code)

assembler.symbol_table.print_symbol_table()
assembler.second_pass()

# Print the symbol table, binary data dumps, and binary text dumps
assembler.print_binary_data_section()
assembler.print_binary_text_section()

# binary_file_path = "output.bin"
# with open(binary_file_path, "wb") as bin_file:
#     for instruction in assembler.binary_instructions:
#         # Assuming each instruction is a 32-bit binary string
#         bin_file.write(int(instruction, 2).to_bytes(4, byteorder='big'))

# text file output to be same filename but with .txt extension and placed in the out directory
text_file_path = os.path.join("out", os.path.basename(file_path).replace(".asm", ".bin"))


#Print "ENTRY 0000" in the file
with open(text_file_path, "w") as text_file:
    text_file.write("ENTRY 0000\n")
    text_file.write(".text\n")
    for instruction in assembler.binary_instructions:
        text_file.write(instruction + "\n")
    text_file.write(".data\n")
    for data in assembler.binary_data:
        text_file.write(data + "\n")

