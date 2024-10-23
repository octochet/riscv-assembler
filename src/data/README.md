# Data Files

## reg_map.dat

This file contains the register mappings of mnemonics to the actual riscv registers.

## instr_data.dat

This file contains the instruction encodings of different types of riscv instruction which will run on our processor.

Currently we have done the encodings for R, I, S and U type formats.

- R-Type format: \<instr mnemonic> \<opcode> \<funct3> \<funct7>
  - Line nos. 1-32
- I-Type format: \<instr mnemonic> \<opcode> \<funct3>
  - Line nos. 33-56
- S-Type format: \<instr mnemonic> \<opcode> \<funct3>
  - Line nos. 57-66
- U-Type format: \<instr mnemonic> \<opcode>
  - Line nos. 67-71
