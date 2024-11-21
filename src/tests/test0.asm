.section
.data
.section
.text
add x3,x4,x5
sub x5,x6,x15
mul x1,x1,x2
mulh x2,x3,x4
mulhu x1,x2,x3
mulhsu x6,x7,x8
div x3,x6,x9
divu x4,x8,x10
rem x2,x12,x13
remu x3,x4,x5
slt x2,x3,x4
sltu x3,x9,x12
and x3,x9,x21
or x3,x4,x6
xor x4,x5,x6
sll x2,x3,x1
srl x3,x2,x1
sra x4,x8,x11
addi x5,x5,32
slti x4,x4,32
sltiu x3,x3,32
andi x1,x1,1
ori x9,x9,2
xori x7,x7,3
slli x8,x8,1
srli x13,x13,1
srai x2,x2,3
lw x5,0(x2)
sw x5,50(x2)
lui x6,2
auipc x5,3
jal x4,__X
__X:
beq x2,x3,__Next
add x2,x2,x2
__Next:
bne x2,x3,__NNext
sub x2,x2,x2
__NNext:
blt x2,x3,__NNN
mul x3,x3,x0
__NNN:
bltu x4,x5,__NMM
div x3,x3,x3
__NMM:
bge x7,x8,__NML
rem x1,x4,x4
__NML:
bgeu x2,x3,__L0
addi x1,x1,1
__L0:
jalr x0,x0,0
