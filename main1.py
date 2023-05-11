from ControlUnit import ControlUnit
from ArithmeticUnit import ArithmeticUnit
from Memory import Memory

memory = Memory(1024)
registers = ["0"*16] * 4
arithmeticUnit = ArithmeticUnit()
controlUnit = ControlUnit(memory, registers, arithmeticUnit)
 

## Ejemplo 2
instructions =["0111000000000100","0111000000000101","0111000000000110"
               ,"0110000000110001","0110000001000010","0111000000001100"
               ,"0111000000001110","0000000000000000"]
 
 
memory.cells[256:256 + len(instructions)] = instructions
 
controlUnit.run(format(256, "010b"))
