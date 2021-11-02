from List import List


class LeastSquares:
    def __init__(self, x_cord, y_cord, sigma_y=None):
        if len(x_cord) != len(y_cord) and len(x_cord) != len(sigma_y):
            raise RuntimeError("Error: arrays have different lengths")
        self.X = List(x_cord)
        self.Y = List(y_cord)
        self.Sy = List(sigma_y)
        self.n = len(x_cord)
        self.r = None

    def calculate(self):
        delta = sum((self.X ** 2) / (self.Sy ** 2)) * sum(self.Sy ** (-2)) - (sum(self.X / (self.Sy ** 2))) ** 2
        delta_a = sum((self.X * self.Y) / (self.Sy ** 2)) * sum(self.Sy ** (-2)) - sum(self.X / (self.Sy ** 2)) * sum(self.Y / (self.Sy ** 2))
        delta_b = sum((self.X ** 2) / (self.Sy ** 2)) * sum(self.Y / (self.Sy ** 2)) - sum(self.X / (self.Sy ** 2)) * sum((self.X * self.Y) / (self.Sy ** 2))
        self.a = delta_a/delta
        self.b = delta_b/delta
        self.s_a = sum(self.Sy ** (-2)) / delta
        self.s_b = sum((self.X ** 2) / (self.Sy ** 2)) / delta

        X_avg = List([sum(self.X) / self.n for i in range(self.n)])
        Y_avg = List([sum(self.Y) / self.n for i in range(self.n)])
        s_x = sum((self.X - X_avg) ** 2) / (self.n - 1)
        s_y = sum((self.Y - Y_avg) ** 2) / (self.n - 1)
        self.r = sum(abs((self.X - X_avg) * (self.Y - Y_avg))) / ((self.n - 1) * (s_x * s_y)**(1/2))

    def get_result(self):
        if self.r is None: self.calculate()
        return self.a, self.b, self.s_a, self.s_b, self.r


if __name__ == "__main__":
    obj = LeastSquares([1, 2, 3], [2, 4, 6], [0.1, 0.1, 0.1])
    print(obj.get_result())
