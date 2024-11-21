# Instruction encoding map
instruction_encoding = {
    # <mnemonic>: (<opcode>, <funct3>, <funct7>)
    # R-type instructions: have opcode, funct3, and funct7
    # I-type instructions: have opcode and funct3
    # S-type instructions: have opcode and funct3
    # SB-type instructions: have opcode and funct3
    # U-type instructions: have opcode
    # UJ-type instructions: have opcode
    "add": ("0000000", "000", "0000000"),
    "addu": ("0010000", "000", "0000000"),
    "sub": ("0000000", "001", "0000000"),
    "subu": ("0010000", "001", "0000000"),
    "mul": ("0000000", "010", "0000000"),
    "mulu": ("0010000", "010", "0000000"),
    "mulh": ("0000000", "011", "0000000"),
    "mulhu": ("0010000", "011", "0000000"),
    "div": ("0000000", "100", "0000000"),
    "divu": ("0010000", "100", "0000000"),
    "rem": ("0000000", "101", "0000000"),
    "remu": ("0010000", "101", "0000000"),
    "seq": ("0000100", "000", "0000000"),
    "slt": ("0000100", "001", "0000000"),
    "sltu": ("0001100", "001", "0000000"),
    "sle": ("0000100", "010", "0000000"),
    "sleu": ("0001100", "010", "0000000"),
    "sgt": ("0000100", "011", "0000000"),
    "sgtu": ("0001100", "011", "0000000"),
    "sge": ("0001100", "100", "0000000"),
    "sgeu": ("0001100", "100", "0000000"),
    "not": ("0001000", "000", "0000000"),
    "and": ("0001000", "001", "0000000"),
    "or": ("0001000", "010", "0000000"),
    "xor": ("0001000", "011", "0000000"),
    "nand": ("0001000", "100", "0000000"),
    "nor": ("0001000", "101", "0000000"),
    "xnor": ("0001000", "110", "0000000"),
    "sll": ("0011100", "000", "0000000"),
    "srl": ("0011100", "001", "0000000"),
    "sla": ("0011100", "010", "0000000"),
    "sra": ("0011100", "011", "0000000"),
    "   ": ("0000001", "000", "-1"),
    "subi": ("0000001", "001", "-1"),
    "muli": ("0000001", "010", "-1"),
    "divi": ("0000001", "100", "-1"),
    "remi": ("0000001", "101", "-1"),
    "seqi": ("0000101", "000", "-1"),
    "slti": ("0000101", "001", "-1"),
    "sltui": ("0001101", "001", "-1"),
    "slei": ("0000101", "010", "-1"),
    "sleui": ("0001101", "010", "-1"),
    "sgti": ("0000101", "011", "-1"),
    "sgtui": ("0001101", "011", "-1"),
    "sgei": ("0000101", "100", "-1"),
    "sgeui": ("0001101", "100", "-1"),
    "noti": ("0001001", "000", "-1"),
    "andi": ("0001001", "001", "-1"),
    "ori": ("0001001", "010", "-1"),
    "xori": ("0001001", "011", "-1"),
    "nandi": ("0001001", "100", "-1"),
    "nori": ("0001001", "101", "-1"),
    "xnori": ("0001001", "110", "-1"),
    "slli": ("0011101", "000", "-1"),
    "srli": ("0011101", "001", "-1"),
    "srai": ("0011101", "011", "-1"),
    "beq": ("0000110", "000", "-1"),
    "bne": ("0000110", "111", "-1"),
    "blt": ("0000110", "001", "-1"),
    "bltu": ("0001110", "001", "-1"),
    "ble": ("0000110", "010", "-1"),
    "bleu": ("0001110", "010", "-1"),
    "bgt": ("0000110", "011", "-1"),
    "bgtu": ("0001110", "011", "-1"),
    "bge": ("0000110", "100", "-1"),
    "bgeu": ("0001110", "100", "-1"),
    "j": ("0000011", "-1", "-1"),
    "jal": ("0000111", "-1", "-1"),
    "jalr": ("0001011", "-1", "-1"),
    "lui": ("0001111", "-1", "-1"),
    "auipc": ("0010011", "-1", "-1"),
}

# Register mapping
register_mapping = {
    "zero": "00000", "x0": "00000",
    "ra": "00001", "x1": "00001",
    "sp": "00010", "x2": "00010",
    "gp": "00011", "x3": "00011",
    "tp": "00100", "x4": "00100",
    "t0": "00101", "x5": "00101",
    "t1": "00110", "x6": "00110",
    "t2": "00111", "x7": "00111",
    "s0": "01000", "fp": "01000", "x8": "01000",
    "s1": "01001", "x9": "01001",
    "a0": "01010", "x10": "01010",
    "a1": "01011", "x11": "01011",
    "a2": "01100", "x12": "01100",
    "a3": "01101", "x13": "01101",
    "a4": "01110", "x14": "01110",
    "a5": "01111", "x15": "01111",
    "a6": "10000", "x16": "10000",
    "a7": "10001", "x17": "10001",
    "s2": "10010", "x18": "10010",
    "s3": "10011", "x19": "10011",
    "s4": "10100", "x20": "10100",
    "s5": "10101", "x21": "10101",
    "s6": "10110", "x22": "10110",
    "s7": "10111", "x23": "10111",
    "s8": "11000", "x24": "11000",
    "s9": "11001", "x25": "11001",
    "s10": "11010", "x26": "11010",
    "s11": "11011", "x27": "11011",
    "t3": "11100", "x28": "11100",
    "t4": "11101", "x29": "11101",
    "t5": "11110", "x30": "11110", 
    "t6": "11111", "x31": "11111" 
}

R_instr = [
    "add", "addu", "sub" , "subu" ,
    "mul", "mulu", "mulh", "mulhu",
    "div", "divu", "rem" , "remu" ,
    "seq", 
    "slt", "sltu", 
    "sle", "sleu",
    "sge", "sgeu",
    "not", "and" , "or"  , "xor" , "nand",  "nor", "xnor",
    "sll", "srl"
]

I_instr = [
    "addi" ,  "subi",  "muli",  "divi",
    "remi" ,  "seqi",
    "slti" , "sltui",  "slei", "sleui",
    "sgti" , "sgtui",  "sgei", "sgeui",
    "noti" , 
    "andi" ,   "ori",  "xori",
    "nandi",  "nori", "xnori",
    "slli" ,  "srli", "srai" , 
]

S_instr = [
    "beq", "bne", 
    "blt", "bltu", 
    "ble", "bleu", 
    "bgt", "bgtu", 
    "bge", "bgeu"
]

U_instr = [
    "j", "jal", "jalr",
    "lui", "auipc"
]

class SymbolTable:
    def __init__(self):
        self.label_addresses = {}  # For text section
        self.data_labels = {}  # For data section
        self.next_text_address = 0
        self.next_data_address = 0

    def add_text_label(self, label):
        if label not in self.label_addresses:
            self.label_addresses[label] = self.next_text_address
            self.next_text_address += 4  # Increment by 4 bytes for each instruction

    def add_data_label(self, label):
        if label not in self.data_labels:
            self.data_labels[label] = self.next_data_address
            self.next_data_address += 4  # Increment by 4 bytes for each data item

    def get_text_address(self, label):
        return self.label_addresses.get(label, None)

    def get_data_address(self, label):
        return self.data_labels.get(label, None)

    def print_symbol_table(self):
        print("Symbol Table:")
        print("Label                Address (Hex)")
        print("-" * 30)
        for label, address in self.label_addresses.items():
            print(f"{label:<20} {address:#04x}")
        for label, address in self.data_labels.items():
            print(f"{label:<20} {address:#04x}")
        print("-" * 30)

class Assembler:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.instructions = []
        self.data_section = []
        self.binary_data = []  # To store binary representation of data
        self.binary_instructions = []  # To store binary representation of instructions

    def first_pass(self, asm_code):
        lines = asm_code.splitlines()
        current_section = None

        for line in lines:
            line = line.strip()

            if line.startswith('.data'):
                current_section = 'data'
                continue
            elif line.startswith('.text'):
                current_section = 'text'
                continue
            elif line.startswith('.globl'):
                continue  # Ignore global directive

            if current_section == 'data':
                if line.endswith(":"):
                    label = line[:-1]
                    self.symbol_table.add_data_label(label)
                elif line:  # Non-empty line
                    # Assuming .asciz is a single string for simplicity
                    if ".asciz" in line:
                        # Extract the string between the double quotes
                        string = line.split('"')[1]
                        # Convert the string to a list of ASCII values
                        ascii_values = [ord(char) for char in string]
                        # Append a null terminator
                        ascii_values.append(0)
                        # Convert the ASCII values to binary
                        binary_data = [format(value, '08b') for value in ascii_values]
                        # Combine the binary values into a single string
                        binary_data = ''.join(binary_data)
                        # Append the binary data to the list
                        self.binary_data.append(binary_data)

            elif current_section == 'text':
                if line.endswith(":"):
                    label = line[:-1]
                    self.symbol_table.add_text_label(label)
                elif line:  # Non-empty line
                    self.instructions.append(line)

    def second_pass(self):
        for instruction in self.instructions:
            # instruction format: <mnemonic> <rd>,<rs1>,<rs2/imm>
            # no spaces between registers and comma separated
            # print(instruction)
            parts = [instruction.split()[0]] #mnemonic
            if parts[0] == 'nop' or parts[0] == 'ecall':
                continue
            parts.extend(instruction.split()[1].split(","))
            mnemonic = parts[0]
            if mnemonic in instruction_encoding:
                encoding = instruction_encoding[mnemonic]
                opcode = encoding[0]
                funct3 = encoding[1]
                funct7 = encoding[2]

                if mnemonic in R_instr:
                    rd = register_mapping[parts[1]]
                    rs1 = register_mapping[parts[2]]
                    rs2 = register_mapping[parts[3]]
                    self.binary_instructions.append(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
                elif mnemonic in I_instr:
                    rd = register_mapping[parts[1]]
                    rs1 = register_mapping[parts[2]]
                    # immediate value is an int in decimal
                    imm_val = int(parts[3])
                    if imm_val < 0:
                        imm = format((1 << 12) + imm_val, '012b')
                    else:
                        imm = format(imm_val, '012b')
                    self.binary_instructions.append(f"{imm}{rs1}{funct3}{rd}{opcode}")
                elif mnemonic in S_instr:
                    rs1 = register_mapping[parts[1]]
                    rs2 = register_mapping[parts[2]]
                    # parts[3] is the immediate label
                    # get address of the label from the symbol table
                    imm = self.symbol_table.get_text_address(parts[3])
                    imm = format(imm, '012b')
                    self.binary_instructions.append(f"{imm[5:12]}{rs2}{rs1}{funct3}{imm[:5]}{opcode}")
                elif mnemonic in U_instr:
                    if mnemonic == "lui":
                        rd = register_mapping[parts[1]]
                        imm = format(int(parts[2]), '020b')
                        self.binary_instructions.append(f"{imm}{rd}{opcode}")
                    else:
                        rd = register_mapping[parts[1]]
                        imm = self.symbol_table.get_text_address(parts[2])
                        imm = format(imm, '020b')
                        self.binary_instructions.append(f"{imm}{rd}{opcode}")
                

    def print_binary_data_section(self):
        print("Data Section Binary Dump:")
        for label in self.symbol_table.data_labels:
            address = self.symbol_table.get_data_address(label)
            # Check if the index exists in binary_data
            if address // 4 < len(self.binary_data):
                binary_value = self.binary_data[address // 4]
                print(f"{label} (Address: {address:#04x}): {binary_value}")
            else:
                print(f"{label} (Address: {address:#04x}): No binary data available.")

    def print_binary_text_section(self):
        print("Text Section Binary Dump:")
        for label in self.symbol_table.label_addresses:
            address = self.symbol_table.get_text_address(label)
            # Check if the index exists in binary_instructions
            if address // 4 < len(self.binary_instructions):
                instruction = self.binary_instructions[address // 4]
                print(f"{label} (Address: {address:#04x}): {instruction}")
            else:
                print(f"{label} (Address: {address:#04x}): No instruction available.")

# Example usage

# file_path = "tests/test.asm"
# with open(file_path, "r") as file:
#     asm_code = file.read()

# asm_code = """
# .data
# string_array:
#     .asciz "Hello"
# prompt:
#     .asciz "Enter a number: "

# .text
# .globl main
# main:
#     addi a2 a3 34
# """

# assembler = Assembler()
# assembler.first_pass(asm_code)
# assembler.second_pass()

# # Print the symbol table, binary data dumps, and binary text dumps
# assembler.symbol_table.print_symbol_table()
# assembler.print_binary_data_section()
# assembler.print_binary_text_section()

# Example usage:
lines ="""
.section
.data
__main__data0:
	.asciz "ABCD"
.section
.text
jal x30,main
main:
add x3,x4,x5

"""

assembler = Assembler()
assembler.first_pass(lines)
assembler.symbol_table.print_symbol_table()
assembler.second_pass()
assembler.print_binary_data_section()
assembler.print_binary_text_section()