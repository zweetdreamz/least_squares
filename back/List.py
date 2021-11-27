class List(list):
    def __init__(self, arr):
        super().__init__(arr)

    def __sub__(self, other):
        if len(self) != len(other):
            raise RuntimeError("Error: arrays have different lengths")
        tmp = self.copy()
        for i in range(len(tmp)):
            tmp[i] -= other[i]
        return List(tmp)

    def __mul__(self, other):
        if len(self) != len(other):
            raise RuntimeError("Error: arrays have different lengths")
        tmp = self.copy()
        for i in range(len(tmp)):
            tmp[i] *= other[i]
        return List(tmp)

    def __truediv__(self, other):
        if len(self) != len(other):
            raise RuntimeError("Error: arrays have different lengths")
        tmp = self.copy()
        for i in range(len(tmp)):
            tmp[i] /= other[i]
        return List(tmp)

    def __pow__(self, power, modulo=None):
        tmp = self.copy()
        for i in range(len(tmp)):
            tmp[i] **= power
        return List(tmp)

    def __abs__(self):
        tmp = self.copy()
        for i in range(len(tmp)):
            tmp[i] = abs(tmp[i])
        return List(tmp)
