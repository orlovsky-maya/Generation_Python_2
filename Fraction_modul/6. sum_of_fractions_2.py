from fractions import Fraction as F
from math import factorial
n = int(input())
result = F(sum([F(1, factorial(i)) for i in range(1, n + 1)]))
print(result)