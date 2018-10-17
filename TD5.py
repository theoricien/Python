class SystemeEquations:
    def __init__ (self, A=[[0]]):
        self.A = A

    def __repr__ (self):
        return str(self.A)

    def __str__ (self):
        return str(self.A)
    
    def echange (self, i, j):
        try:
            self.A[i],self.A[j] = self.A[j],self.A[i]
        except:
            raise IndexError("Argument too high")

    def prod_scalaire (self, i, x):
        if x == 0:
            raise ValueError("x cannot be 0")
        for j in range(len(self.A[i])):
            self.A[i][j] *= x

    def comb_lin (self, i, j, x):
        self.A[i] = [self.A[i][k] + x*self.A[j][k] for k in range(len(self.A[i]))]
            
    def resoudre (self):
        for row in range(len(self.A)):
            for column in range(len(self.A[0])-1):
                if column == row:
                    continue
                coeff = self.A[column][row] / self.A[row][row]
                self.comb_lin(column, row, -coeff)
