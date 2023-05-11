from ControlUnit import ControlUnit
from ArithmeticUnit import ArithmeticUnit
from Memory import Memory

memory = Memory(1024)
registers = ["0"*16] * 4
arithmeticUnit = ArithmeticUnit()
controlUnit = ControlUnit(memory, registers, arithmeticUnit)
 

## Ejemplo 1
instructions = ["0001001000000000","0001011000000001","0110000000000010","0110000000101001"
               ,"0100000100001010","0100010100001000","0110000000100001","0101000100000010"
               ,"0110000000100100","0101000100000010","0011001000000010","0111000000001100"
               ,"0000000000000000"]


memory.cells[512] = format(18, "016b") # a = 18
memory.cells[513] = format(14, "016b") # b = 9
 
memory.cells[256:256 + len(instructions)] = instructions
 
controlUnit.run(format(256, "010b"))


