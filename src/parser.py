from src.instr_arr import *
from types import FunctionType as function
from os.path import exists

class _Parser:

    '''
    Procedure:
        1. Open and read the input assembly file
            1.1 If the file does not exist or is empty, raise an error
            1.2 handle inline comments
            1.3 determine type of instruction -> return appropriate function
        2. Parse the file line by line
            2.1 If the line is empty, skip it
            2.2 If the line is a label, add it to the symbol table
            2.3 If the line is an instruction, parse it
        3. Return the symbol table and the instruction array
    '''

    def __call__(self, *args) -> list:
        if exists(*args):
            return _Parser.interpret_arr(_Parser.read_file(*args))
		#return [_Parser.interpret(_Parser.tokenize(x)) for x in args[0].split("\n") if len(_Parser.tokenize(x)) > 0]
        elif type(args[0]) == str:
            return _Parser.interpret_arr(args[0].split('\n'))
        return _Parser.interpret_arr(*args)
    
    @staticmethod
    def valid_line(x: str, allow_colon: bool = False) -> bool:
        if len(x) == 0:
            return False
        if x[0][0]=="#" or x[0][0]=="\n" or x[0][0]=="" or x[0][0]==".":
            return False
        
        if not allow_colon and x[-1]==":":
            return False
        return True
    
    @staticmethod
    def handle_inline_comments(x: str) -> str:
        if '#' in x:
            pos = x.index('#')
            if pos!=0 and pos!=len(x)-1:
                return x[:pos].replace(',', ' ')
        return x.replace(',', ' ')
    
    @staticmethod
    def handle_specific_instr(x: list) -> list:
        # for sw, lw, lb, lh, sb, sh
        if len(x[0])==2 and (x[0] in S_instr or x[0] in I_instr):
            y = x[-1].split('('); y[1] = y[1].replace(')', '')
            return x[:-1] + y
        elif 'requires jump' == 5:
            ...
        return x
    
    @staticmethod
    def read_file(file: str) -> list:
        with open(file, 'r') as f:
            return [x.strip() for x in f.readlines() if x!='\n']
        
    @staticmethod
    def interpret_arr(code: list) -> list:
        int_code = []
        for line_num, line in enumerate(code):
            tokens = _Parser.tokenize(line, line_num, code)
            int_code += [_Parser.interpret(tokens) for _ in range(1) if len(tokens)!=0]

        return int_code
    
    @staticmethod
    def tokenize(line: str, line_num: int=None, code: list=None) -> list:
        line = line.strip()
        if len(line)>0 and _Parser.valid_line(line):
            tokens = _Parser.handle_inline_comments(line).split()
            tokens = _Parser.handle_specific_instr(tokens)
            return tokens + [line_num, code] if line_num!=None and code!=None else tokens
        return []
    
    @staticmethod
    def interpret(tokens: list) -> str:
        f = _Parser.determine_type(tokens[0])
        return f(tokens)
    
    @staticmethod
    def determine_type(tk: str) -> function:
        instr_sets = [R_instr, I_instr, S_instr, U_instr, pseudo_instr]
        parsers = [Rp, Ip, Sp, Up, Psp]
        for i in range(len(instr_sets)):
            if tk in instr_sets[i]:
                return parsers[i]
        raise Exception("Invalid instruction Provided: " + tk + "!")
    
Parser = _Parser()