import unittest
from LeastSquares import LeastSquares
from List import List


class TestList(unittest.TestCase):
    def test_sub(self):
        a = List([1, 2, 3])
        b = List([2, 3, 4])
        c = a - b
        right_result = List([-1, -1, -1])
        self.assertEqual(c, right_result)

    def test_mul(self):
        a = List([1, 2, 3])
        b = List([2, 3, 4])
        c = a * b
        right_result = List([2, 6, 12])
        self.assertEqual(c, right_result)

    def test_truediv(self):
        a = List([10, 30, 4])
        b = List([2, 3, 4])
        c = a / b
        right_result = List([5.0, 10.0, 1.0])
        self.assertEqual(c, right_result)

    def test_pow(self):
        a = List([1, 2, 3])
        b = 2
        c = a ** b
        right_result = List([1, 4, 9])
        self.assertEqual(c, right_result)

    def test_abs(self):
        a = List([-1, 2, -3])
        c = abs(a)
        right_result = List([1, 2, 3])
        self.assertEqual(c, right_result)


def beautiful_result(result):
    tmp = [round(el, 3) for el in result]
    return tuple(tmp)


class TestLeastSquares(unittest.TestCase):
    def test_1(self):
        x = [1, 2, 3]
        y = [2, 4, 6]
        sigma = [0.1, 0.1, 0.1]
        obj = LeastSquares(x, y, sigma)
        result = beautiful_result(obj.get_result())
        right_result = (2.0, 0.0, 0.005, 0.023, 1.0)
        self.assertEqual(result, right_result)

    def test_2(self):
        x = [1, 2]
        y = [2, 4]
        sigma = [0.1, 0.1]
        obj = LeastSquares(x, y, sigma)
        result = beautiful_result(obj.get_result())
        right_result = (2.0, 0.0, 0.02, 0.05, 1.0)
        self.assertEqual(result, right_result)

    def test_3(self):
        x = [1, 2, 3, 4, 5, 6]
        y = [2, 1, 2, 3, 2, 3]
        sigma = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        obj = LeastSquares(x, y, sigma)
        result = beautiful_result(obj.get_result())
        right_result = (0.257, 1.267, 0.001, 0.009, 0.71)
        self.assertEqual(result, right_result)


if __name__ == "__main__":
    unittest.main()


'''
coverage run -m pytest tests.py
coverage report -m
'''
