// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @i
    M=0 // i=0
    @2
    M=0 // suma=0
(LOOP)
    @i
    D=M // D=i
    @1
    D=D-M // D=i-R1
    @END
    D;JGE // Si D >= 0 ir a END
    @0
    D=M // D=R0
    @2
    M=D+M // suma=R0+suma
    @i
    M=M+1 // i=i+1
    @LOOP
    0;JMP // ir a LOOP
(END)
    @END
    0;JMP
