'''
consists of various instr classes and their formats and converts them to 
'''

from pathlib import Path
from bitstring import BitArray
import math

all = ['R_instr', 'I_instr', 'S_instr', 'U_instr', 'R', 'I', 'S', 'U']

class Instruction:
    def compute_instr(self, *args):
        raise NotImplementedError('Method not implemented')
    
    def __call__(self, *args, **kwds):
        return self.compute_instr(*args, **kwds)
    
    def check_instr_valid(self, x, instr_set):
        assert x in instr_set, f'Invalid instruction: {x}'
        return x
    
class _R(Instruction):
    def __repr__(self):
        return "R instruction"
    
    def compute_instr(self, instr, rs1, rs2, rd):
        instr = super.check_instr_valid(instr, R_instr)
        opcode, funct3, funct7 = 0, 1, 2

        return "".join([
            instr_map[instr][funct7], #to implement instr_map will be a dict of instr encodings

        ])


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