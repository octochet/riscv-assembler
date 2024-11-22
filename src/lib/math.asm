.section
.data
.section
.text
jal x30,__abs
__abs:
sw x1,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
sw x2,0(x5)
addi x6,x2,40
lui x5,2
addi x5,x5,12
sw x2,0(x5)
addi x2,x2,60
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE6
jal x30,__IF_FALSE6
__IF_TRUE6:
addi x5,x0,-1
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_0_loop:
            beq x29,x0,__mul_0_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_0_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_0_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_0_loop
            
            __mul_0_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
jal x30,__IF_END6
__IF_FALSE6:
__IF_END6:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
__exp:
sw x1,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
sw x2,0(x5)
addi x6,x2,40
lui x5,2
addi x5,x5,12
sw x2,0(x5)
addi x2,x2,60
lui x7,260096
addi x7,x7,0
addi x7,x7,0
fmv.w.x f3,x7
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
lui x7,260096
addi x7,x7,0
addi x7,x7,0
fmv.w.x f3,x7
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
fsw f3,0(x6)
addi x5,x0,1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
__L4:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,20
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__end_#L4_no
__end_#L4_no:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
div x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_1_loop:
            beq x29,x0,__mul_1_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_1_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_1_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_1_loop
            
            __mul_1_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
fcvt.s.w f3,x5
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
fsw f3,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
addi x5,x0,1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
sub x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
jal x30,__L4
__end___L4:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
__power:
sw x1,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
sw x2,0(x5)
addi x6,x2,40
lui x5,2
addi x5,x5,12
sw x2,0(x5)
addi x2,x2,60
lui x7,260096
addi x7,x7,0
addi x7,x7,0
fmv.w.x f3,x7
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE7
jal x30,__IF_FALSE7
__IF_TRUE7:
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
__L5:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__end_#L5_no
__end_#L5_no:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_2_loop:
            beq x29,x0,__mul_2_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_2_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_2_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_2_loop
            
            __mul_2_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
jal x30,__L5
__end___L5:
jal x30,__IF_END7
__IF_FALSE7:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE8
jal x30,__IF_FALSE8
__IF_TRUE8:
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
__L6:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,-1
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_3_loop:
            beq x29,x0,__mul_3_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_3_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_3_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_3_loop
            
            __mul_3_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__end_#L6_no
__end_#L6_no:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_4_loop:
            beq x29,x0,__mul_4_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_4_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_4_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_4_loop
            
            __mul_4_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
jal x30,__L6
__end___L6:
lui x7,260096
addi x7,x7,0
addi x7,x7,0
fmv.w.x f3,x7
fsw f3,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
div x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
flw f3,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
fsw f3,0(x6)
jal x30,__IF_END7
__IF_FALSE8:
__IF_END7:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
__mod:
sw x1,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
sw x2,0(x5)
addi x6,x2,40
lui x5,2
addi x5,x5,12
sw x2,0(x5)
addi x2,x2,60
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE8
jal x30,__IF_FALSE8
__IF_TRUE8:
addi x5,x0,-1
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
jal x30,__IF_END8
__IF_FALSE8:
__IF_END8:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
div x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
            # Multiplication of x6 and x5
            addi x26,x0,0     # Initialize result
            addi x27,x0,0     # Initialize counter
            add x28,x6,x0  # Copy multiplicand
            add x29,x5,x0  # Copy multiplier
            
            __mul_5_loop:
            beq x29,x0,__mul_5_done
            andi x30,x29,1    # Check LSB
            beq x30,x0,__mul_5_shift
            add x26,x26,x28   # Add multiplicand to result
            
            __mul_5_shift:
            slli x28,x28,1    # Shift multiplicand left
            srli x29,x29,1    # Shift multiplier right
            bge x0,x0,__mul_5_loop
            
            __mul_5_done:
            add x5,x26,x0   # Move result to destination
        sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
sub x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
sw x5,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE9
jal x30,__IF_FALSE9
__IF_TRUE9:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
sw x5,0(x6)
jal x30,__IF_END9
__IF_FALSE9:
__IF_END9:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
flw f3,0(x5)
fsw f3,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,__IF_TRUE10
jal x30,__IF_FALSE10
__IF_TRUE10:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
add x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
sw x5,0(x6)
jal x30,__IF_END10
__IF_FALSE10:
__IF_END10:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
__gcd:
sw x1,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
sw x2,0(x5)
addi x6,x2,40
lui x5,2
addi x5,x5,12
sw x2,0(x5)
addi x2,x2,60
__L7:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x5,x0,0
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x6,x0,1
beq x5,x6,___L0
jal x30,__end___L7
___L0:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,8
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
addi x2,x2,-4
lw x6,0(x2)
rem x5,x6,x5
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,8
sw x5,0(x6)
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,4
add x6,x6,x8
lw x6,0(x6)
addi x6,x6,4
sw x5,0(x6)
jal x30,__L7
__end___L7:
lui x5,2
addi x5,x5,4
add x5,x5,x8
lw x5,0(x5)
addi x5,x5,4
lw x5,0(x5)
sw x5,0(x2)
addi x2,x2,4
addi x2,x2,-4
lw x5,0(x2)
lui x6,2
addi x6,x6,8
lw x6,0(x6)
sw x5,0(x6)
lui x5,2
addi x5,x5,4
lw x2,0(x5)
lw x5,-8(x2)
lui x6,2
addi x6,x6,16
sw x5,0(x6)
lw x5,-12(x2)
lui x6,2
addi x6,x6,12
sw x5,0(x6)
lw x7,-16(x2)
lw x5,-20(x2)
lui x6,2
addi x6,x6,4
sw x5,0(x6)
lw x5,-4(x2)
lui x6,2
addi x6,x6,8
lw x2,0(x6)
addi x2,x2,4
lui x6,2
addi x6,x6,8
sw x7,0(x6)
jalr x0,x1,0
jal x30,__END__
__type_check:
addi x25,x0,1
beq x23,x25,__type_int
addi x25,x0,2
beq x23,x25,__type_float
addi x25,x0,3
beq x23,x25,__type_char
addi x25,x0,4
beq x23,x25,__type_bool
__type_int:
addi x24,x0,4
jalr x0,x1,0
__type_float:
addi x24,x0,4
jalr x0,x1,0
__type_char:
addi x24,x0,1
jalr x0,x1,0
__type_bool:
addi x24,x0,1
jalr x0,x1,0
__array_out_of_bounds:
nop
__END__:
nop
