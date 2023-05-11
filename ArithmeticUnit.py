class ArithmeticUnit:
    def __init__(self):
        pass

    # cada vez que oopera inicializa las banderas Estado
    def initFlags(self):
        (self.c, self.p, self.n, self.d) = ("0","0","0","0")

    def sum(self, R, S):
        self.initFlags()
        valR = int(R, 2)
        valS = int(S, 2)
        valSum = valR + valS
        self.verifyResult(valSum)
        sum_ = format(valSum, "016b")
        return sum_
    
    def res(self,R,S):
        self.initFlags()
        valR = int(R, 2)
        valS = int(S, 2)
        valRes = valR - valS
        self.verifyResult(valRes)
        res = format(valRes, "016b")
        return res
    
    def mul(self,R,S):
        self.initFlags()
        valR = int(R, 2)
        valS = int(S, 2)
        valMul = valR * valS
        self.verifyResult(valMul)
        mul_ = format(valMul, "016b")
        return mul_

    def div(self,R,S):
        self.initFlags()
        valR = int(R, 2)
        valS = int(S, 2)
        valDiv = valR // valS
        self.verifyResult(valDiv)
        div_ = format(valDiv, "016b")
        valDiv = valR % valS
        self.verifyResult(valDiv)
        res_ = format(valDiv, "016b")
        return div_, res_ 
 
    def verifyResult(self, res):
        if res == 0:
            self.c = 1
        elif res > 0:
            self.p = 1
        elif res < 0:
            self.n = 1
        if res < -32768 or res > 32767:
            self.d =1

