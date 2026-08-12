"""
This is Combinational Circuit

FOR HALF ADDER
It need two inputs(A,B) and it will give two output(Sum and Carry)
Sum=A XOR B
Carry=A AND B

FOR FULL ADDER
It need three inputs(A,B,C) and it will give output(Sum and Carry-out)
Sum= A XOR B XOR Carry_in
Carry-out=(A AND B) OR (B AND Carry_in) OR (A AND Carry_in)
"""
from gates import XOR, AND, OR, validate_input, XNOR

# Half Adder
def half_adder(A,B):
    return XOR(A,B),AND(A,B)


# Full Adder
def full_adder(A,B,Carry_in):
    Sum=XOR(A,B,Carry_in)
    Carry_out=OR(AND(A,B),AND(B,Carry_in),AND(A,Carry_in))
    return  Sum, Carry_out

# Multiplexer
def MUX(D0,D1,D2,D3,S0,S1):
    validate_input(D0,D1,D2,D3,S0,S1)
    S0_=not(S0)
    S1_=not(S1)
    and0=AND(D0,S1_,S0_)
    and1=AND(D1,S1_,S0)
    and2=AND(D2,S1,S0_)
    and3=AND(D3,S1,S0)
    result=OR(and0,and1,and2,and3)
    return result

# Decoder
def decoder(A,B):
    validate_input(A,B)
    A_=not(A)
    B_=not(B)
    Y0,Y1,Y2,Y3=AND(A_,B_),AND(A_,B),AND(A,B_),AND(A,B)
    return Y0,Y1,Y2,Y3

# Encoder
def encoder(D0, D1, D2, D3):
    validate_input(D0, D1, D2, D3)
    A=OR(D2,D3)
    B=OR(D1,D3)
    return A,B

#Comparator
def comparator(A0,A1,B0,B1):
    X1=XNOR(A1,B1)
    X0=XNOR(A0,B0)
    A_equal_B = AND(X1, X0)
    A_greater_B = OR( AND(A1, NOT(B1)), AND(X1, AND(A0, NOT(B0))) )
    A_less_B = OR( AND(NOT(A1), B1), AND(X1, AND(NOT(A0), B0)) )










    
