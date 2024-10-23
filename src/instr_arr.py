'''
consists of various instr classes and their formats and converts them to 
'''

from pathlib import Path
from bitstring import BitArray
import math

all = ['R_instr', 'I_instr', 'S_instr', 'U_instr', 'pseudo_instr', 'JUMP', 'R', 'I', 'S', 'U', 'Rp', 'Ip', 'Sp', 'Up', 'Psp']

class Instruction:
    def compute_instr(self, *args):
        raise NotImplementedError('Method not implemented')
    
    def __call__(self, *args, **kwds):
        return self.compute_instr(*args, **kwds)
    
    def check_instr_valid(self, x, instr_set):
        assert x in instr_set, f'Invalid instruction: {x}'
        return x
    
    @staticmethod
    def reg(x):
        return format(int(x[1:]), '05b')
    
    @staticmethod
    def immediate(x):
        raise NotImplementedError('Method not implemented')
    
class _R(Instruction):
    def __repr__(self):
        return "R instruction"
    
    def compute_instr(self, instr, rs1, rs2, rd):
        instr = super().check_instr_valid(instr, R_instr)
        opcode, funct3, funct7 = 0, 1, 2

        return "".join([
            instr_map[instr][funct7], #to implement instr_map will be a dict of instr encodings
            super().reg(rs2),
            super().reg(rs1),
            instr_map[instr][funct3],
            super().reg(rd),
            instr_map[instr][opcode]
        ])
    
class _I(Instruction):
    def __repr__(self):
        return "I instruction"
    
    def compute_instr(self, instr, rs1, imm, rd):
        instr = super().check_instr_valid(instr, I_instr)
        opcode, funct3 = 0, 1
        
        return "".join([
            format(((1 << 12) - 1) & int(imm), '012b'),
            super().reg(rs1),
            instr_map[instr][funct3],
            super().reg(rd),
            instr_map[instr][opcode]
        ])
    
class _S(Instruction):
    def __repr__(self):
        return "S instruction"
    
    def compute_instr(self, instr, rs1, rs2, imm):
        instr = super().check_instr_valid(instr, S_instr)
        opcode, funct3 = 0, 1
        
        return "".join([
            _S.immediate(imm, 1),
            super().reg(rs2),
            super().reg(rs1),
            instr_map[instr][funct3],
            _S.immediate(imm, 2),
            instr_map[instr][opcode]
        ])
    
    @staticmethod
    def immediate(imm, n):
        mod_imm = format(((1 << 12)-1)&int(imm), '012b')
        if n == 1:
            return mod_imm[0] + mod_imm[12-10:12-4]
        return mod_imm[12-4:12-0] + mod_imm[1]

class _U(Instruction):
	def __repr__(self):
		return "U instruction"

	def compute_instr(self, instr, imm, rd):
		instr = super().check_instr_valid(instr, U_instr)
		opcode = 0

		return "".join([
			_U.immediate(imm),
			super().reg(rd),
			instr_map[instr][opcode]
		])

	@staticmethod
	def immediate(imm):
		return format(int(imm) >> 12, '013b')
     
class InstructionParser:
	def organize(self, *args):
		raise NotImplementedError()

	def __call__(self, *args):
		return self.organize(*args)
     
class _R_parse(InstructionParser):

	def __repr__(self):
		return "R Parser"

	def __str__(self):
		return "R Parser"

	def organize(self, tokens):
		instr, rs1, rs2, rd = tokens[0], reg_map[tokens[2]], reg_map[tokens[3]], reg_map[tokens[1]]
		return R(instr, rs1, rs2, rd)
     
class _I_parse(InstructionParser):

	def __repr__(self):
		return "I Parser"

	def __str__(self):
		return "I Parser"

	def organize(self, tokens):
		line_num, code = tokens[-2], tokens[-1]
		instr, rs1, imm, rd = tokens[0], None, None, None
		if instr == "jalr":
			if len(tokens) == 4:
				rs1, imm, rd = reg_map[tokens[2]], JUMP(tokens[3], line_num, code), reg_map[tokens[1]]
			else:
				rs1, imm, rd = reg_map[tokens[1]], 0, reg_map["x1"]
		elif instr == "lw":
			rs1, imm, rd = reg_map[tokens[3]], tokens[2], reg_map[tokens[1]]
		else:
			rs1, imm, rd = reg_map[tokens[2]], tokens[3], reg_map[tokens[1]]

		return I(instr, rs1, imm, rd)

class _S_parse(InstructionParser):

	def __repr__(self):
		return "S Parser"

	def __str__(self):
		return "S Parser"

	def organize(self, tokens):
		instr, rs1, rs2, imm = tokens[0], reg_map[tokens[3]], reg_map[tokens[1]], tokens[2]
		return S(instr, rs1, rs2, imm)
	
class _U_parse(InstructionParser):

	def __repr__(self):
		return "U Parser"

	def __str__(self):
		return "U Parser"

	def organize(self, tokens):
		instr, imm, rd = tokens[0], tokens[1], reg_map[tokens[2]]
		return U(instr, imm, rd)

def JUMP(x : str, line_num : int, code: list) -> int:
	# search forward
	skip_labels = 0
	for i in range(line_num, len(code)):
		if x+":" == code[i]:
			jump_size = (i - line_num - skip_labels) * 4 # how many instructions to jump ahead
			return jump_size

		if code[i][-1] == ':':
			skip_labels += 1

	# search backward
	skip_labels = 0
	for i in range(line_num, -1, -1):
		# substruct correct label itself
		if code[i][-1] == ':':
			skip_labels += 1

		if x+":" == code[i]:
			jump_size = (i - line_num + skip_labels) * 4 # how many instructions to jump behind
			return jump_size

	raise Exception("Address not found!")

class _Pseudo_parse(InstructionParser):
	def __repr__(self):
		return "Pseudo Parser"

	def __str__(self):
		return "Pseudo Parser"

	def organize(self, tokens):
		instr = tokens[0]
		if instr == "neg":
			rs1, rs2, rd = reg_map["x0"], reg_map[tokens[2]], reg_map[tokens[1]]
			return R("sub", rs1, rs2, rd)

		return BadInstructionError() # type: ignore
         
def register_map():
    path = Path(__file__).parent / 'data/reg_map.dat'
    reg_map = {}
    
    f = open(path, 'r')
    line = f.readline()
    while line!="":
        entry = line.split()
        reg_map[entry[0]] = entry[1]
        line = f.readline()
    f.close()
    return reg_map

def instruction_map():
    path = Path(__file__).parent / 'data/instr_data.dat'
    instr_map = {}
    
    f = open(path, 'r')
    line = f.readline()
    while line!="":
        entry = line.split()
        instr_map[entry[0]] = entry[1:]
        line = f.readline()
    f.close()
    return instr_map


R, I, S, U = _R(), _I(), _S(), _U()
Rp, Ip, Sp, Up, Psp = _R_parse(), _I_parse(), _S_parse(), _U_parse(), _Pseudo_parse()
reg_map, instr_map = register_map(), instruction_map()

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

pseudo_instr = [
    "neg"
]