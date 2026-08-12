"""
There are 7 basic logic ggates that used to create any  Combinational Circuits or Sequential Circuits
We are use to this file populate all the basic gates in this single module file
"""

# Utils functions
def validate_input(A,B,*extra):
    data=list(extra)
    data.append(A)
    data.append(B)
    allowed=(True,False,0,1)
    for i in data:
        if i not in allowed:
            raise TypeError("Input must be bool or 0 or 1")
    return data
        

# AND Gate multi-input
def AND(A,B,*extra):
    data=validate_input(A,B,*extra)

    for i in data:
        if i is False or i==0:
            return False
    return True

# OR Gate multi-input
def OR(A,B,*extra):
    data=validate_input(A,B,*extra)

    for i in data:
        if i is True or i==1:
            return True
    return False

# NOT Gate  single input
def NOT(A):
    validate_input(A,B=0)
    return  not(A)

# NAND Gate multi input
def NAND(A,B,*extra):
    data=AND(A,B,*extra)
    return not(data)

# NOR Gate multi input
def NOR(A,B,*extra):
    data=OR(A,B,*extra)
    return not(data)

# XOR Gate multi-input
def XOR(A,B,*extra):
    data=validate_input(A,B,*extra)
    count_1=0
    for i in data:
        if i is True or i==1:
            count_1+=1
    if count_1%2==1:
        return True
    else:
        return False

# XNOR Gate
def XNOR(A,B,*extra):
    data= XOR(A,B,*extra)
    return not(data)



    
