#This is NOR Gate

from or_gate import *
from not_gate import *

def nor_gate(A:bool,B:bool)->bool:
    OR=or_gate(A,B)
    result=not_gate(OR)
    return result
