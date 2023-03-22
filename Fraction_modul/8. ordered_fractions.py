from fractions import Fraction as F
from math import gcd

n = int(input())
result = []
z = n
while z > 1:
    for i in range(1, n + 1):
        if gcd(i, z) == 1 and i < z:
            result.append(F(i, z))
    z -= 1

print(*sorted(result), sep='\n')


#  reference solution
from fractions import Fraction

numbers = set()

for i in range(2, int(input()) + 1):
    for j in range(1, i):
        numbers.add(Fraction(j, i))

print(*sorted(numbers), sep='\n')