from functools import reduce


def evaluate(coefficients, x):
    degree = reversed(range(len(coefficients)))
    map_result = list(map(lambda num, d: num * x ** d, coefficients, degree))
    return reduce(lambda x, y: x + y, map_result, 0)


coefficients = [int(i) for i in input().split()]
x = int(input())

print(evaluate(coefficients, x))

