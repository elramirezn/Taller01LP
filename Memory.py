class Memory:
    def __init__(self, size):
        self.size = size
        self.cells = ["0"*16] * self.size 
    
    def read(self, dir_):
        return self.cells[int(dir_, 2)]

    def write(self, dir_, R):
        self.cells[int(dir_, 2)] = R
        return
