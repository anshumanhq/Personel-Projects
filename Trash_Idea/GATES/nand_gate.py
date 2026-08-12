#This is NAND Gate
from and_gate import and_gate
from not_gate import not_gate

def nand_gate(A:bool,B:bool)->bool:
    AND=and_gate(A,B)
    result=not_gate(AND)
    return result
