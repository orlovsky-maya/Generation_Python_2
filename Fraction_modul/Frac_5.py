from fractions import Fraction as F
n = int(input())

result = 0
for i in range(1, n + 1):
    num = F(1, i ** 2)
    result += num
print(result)


from fractions import Fraction as F

print(sum([F(1, i**2) for i in range(1, int(input()) + 1)]))