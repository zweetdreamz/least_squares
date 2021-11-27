import time
from random import randint

from LeastSquares import LeastSquares


def test_generate(n):
    x, y, sigma = [], [], []
    for i in range(n):
        x.append(randint(1, 100))
        y.append(randint(2, 200))
        sigma.append(1)
    return x, y, sigma


def some_test():
    n = randint(1, 10**5)
    x, y, sigma = test_generate(n)
    obj = LeastSquares(x, y, sigma)
    result = obj.get_result()
    return n


def main():
    for i in range(10):
        start = time.time()
        n = some_test()
        finish = time.time()
        print(f"Run #{i} test; number points: {n}; time test: {round(finish-start,5)}s.")


if __name__ == "__main__":
    main()
