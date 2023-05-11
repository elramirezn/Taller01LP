class ControlUnit:
    def __init__(self, memory, registers, AU):
        self.IC = "0" * 16 # init Reg Instrucción en curso
        self.CP = "0" * 10 # init Mem Contador de programa
        self.memory = memory
        self.registers = registers
        self.AU = AU # arithmetic unit

    def run(self, CP):
        self.CP = CP
        running = True
        while running:
            self.IC = self.memory.read(self.CP)
            self.CP = format(int(self.CP, 2) + 1, "010b")
            self.executeInstruction(self.IC)

    def executeInstruction(self, ins):
        if ins == "0000000000000000":
            self.parar()
        elif ins[0:4] == "0001":
            self.cargar(ins[4:6],ins[6:])
        elif ins[0:4] == "0010":
            self.cargarValor(ins[ins[4:6], ins[6:]])
        elif ins[0:4] == "0011":
            self.almacenar(ins[4:6], ins[6:])
        elif ins[0:6] == "010000":
            self.saltarSiCero(ins[6:])
        elif ins[0:6] == "010001":
            self.saltarSiNeg(ins[6:])
        elif ins[0:6] == "010010":
            self.saltarSiPos(ins[6:])
        elif ins[0:6] == "010011":
            self.saltarSiDes(ins[6:])
        elif ins[0:6] == "010100":
            self.saltar(ins[6:])
        elif ins[0:12] == "011000000000":
            self.copiar(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000001":
            self.sumar(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000010":
            self.restar(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000011":
            self.mult(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000100":
            self.div(ins[12:14], ins[14:])    
        elif ins[0:12] == "011000000101":
            self.EstadoDeProcedimiento(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000101":
            self.Conjuncion(ins[12:14], ins[14:])
        elif ins[0:12] == "011000000101":
            self.Disyuncion(ins[12:14], ins[14:])
        elif ins[0:12] == "011000001000":
            self.noAutorizo(ins[12:14], ins[14:])
        elif ins[0:14] == "01110000000000":
            self.entrada(ins[14:])
        elif ins[0:14] == "01110000000001":
            self.EntradaEntero(ins[14:])
        elif ins[0:14] == "01110000000010":
            self.salida(ins[14:])
        elif ins[0:14] == "01110000000011":
            self.salidaDetallada(ins[14:])
        elif ins[0:16] == "0000000000000001":
            self.Estado()
        elif ins[0:14] == "01110000000101":
            self.incrementar(ins[14:])
        elif ins[0:14] == "01110000000110":
            self.decrementar(ins[14:])
    
    def findRegister (self, id):
        return self.registers[int(id, 2)]

    #Microinstructions
    def parar(self):
        exit()

    def cargar(self, R, M):
        self.registers[int(R, 2)] = self.memory.read(M)

    def cargarValor(self, R, V):
        self.registers[int(R, 2)] = format(int(V, 2), "016b")

    def almacenar(self, R, M):
        reg=self.findRegister(R)
        self.memory.write(M, reg)

    def saltarSiCero(self, M):
        if self.AU.c == 1:
            self.CP = M

    def saltarSiNeg(self, M):
        if self.AU.n == 1:
            self.CP = M

    def saltarSiPos(self, M):
        if self.AU.p == 1:
            self.CP = M

    def saltarSiDes(self, M):
        if self.AU.d == 1:
            self.CP = M

    def saltar(self, M):
        self.CP = M

    def copiar (self, R, R_):
        if R == R_:
            pass        
        else:
            self.registers[int(R_, 2)] = self.registers[int(R, 2)]

    def sumar(self, R, R_):
        self.registers[int(R, 2)] = self.AU.sum(self.registers[int(R, 2)], self.registers[int(R_, 2)])

    def restar(self, R, R_):
        self.registers[int(R, 2)] = self.AU.res(self.registers[int(R, 2)], self.registers[int(R_, 2)])

    def mult(self, R, R_):
        self.registers[int(R, 2)] = self.AU.mul(self.registers[int(R, 2)], self.registers[int(R_, 2)])

    def div(self, R, R_):
        self.registers[int(R, 2)], self.registers[int(R_, 2)] = self.AU.div(self.registers[int(R, 2)], self.registers[int(R_, 2)])

        # Ampliación

    def EstadoDeProcedimiento(self, R, S):
        self.cargar(R, self.IC)
        self.cargarValor(R, self.CP)

    def Conjuncion(self, R, R_):
        self.registers[int(R, 2)] = format(int(self.registers[int(R, 2)], 2) & int(self.registers[int(R_, 2)], 2), "016b")

    def Disyuncion(self, R, R_):
        self.registers[int(R, 2)] = format(int(self.registers[int(R, 2)], 2) | int(self.registers[int(R_, 2)], 2), "016b")

    def noAutorizo(self, R, R_):
        self.registers[int(R, 2)] = format(int(self.registers[int(R, 2)], 2) - int(self.registers[int(R_, 2)], 2), "016b")

    def entrada(self, R):
        bits = ("Ingrese una cadena de 16 bits: ")
        self.cargarValor(R, bits[0:16])

    def EntradaEntero(self,R):
        value = int(input("Ingrese un entero ∊ [-32768, 32767]: "))
        self.cargarValor(R, format(value, "016b"))

    def salida(self, R):
        print(self.registers[int(R, 2)])

    def salidaDetallada(self, R):
        print("Id de registro:", int(R, 2))
        print("Contenido binario de registro:", self.registers[int(R, 2)])
        print("Valor entero del contenido:", int(self.registers[int(R, 2)], 2))

    def Estado(self):
        print("C:", self.AU.c)
        print("P:", self.AU.p)
        print("N:", self.AU.n)
        print("D:", self.AU.d)

    def incrementar(self, R):
        self.sumar(R,format(1, "016b"))

    def decrementar(self, R):
        self.restar(R,format(1, "016b"))

