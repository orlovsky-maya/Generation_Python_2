from fractions import Fraction as F
n = int(input())
result = 0
for i in range(1, n // 2 + 1):
    num = F(i, n - i)
    if sum(num.as_integer_ratio()) == n:
        if num > result:
            result = num
print(result)


# Second solution
from fractions import Fraction as F
n = int(input())
result = 0
for i in range(1, n // 2 + 1):
    num = F(i, n - i)
    if num.numerator + num.denominator == n:
        if num > result:
            result = num
print(result)

#  reference solution
from fractions import Fraction as F
from math import gcd

n = int(input())
a = n // 2
b = n - a
while gcd(a, b) != 1:
    a -= 1
    b += 1
print(F(a, b))
