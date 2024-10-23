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

from assemble import AssemblyConverter as AC
from parser import Parser
from pathlib import Path

if __name__=="__main__":
    cnv = AC()
    path = str(Path(__file__).parent / 'tests/test1.s')
    res = cnv(path)
    print(res)