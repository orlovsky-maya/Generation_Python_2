from decimal import *

s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 ' \
    '7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 ' \
    '3.86 5.56 1.43 8.36 6.29 5.13'

numbers = [Decimal(i) for i in s.split()]
numbers_copy = numbers.copy()
max_list = []

for j in range(5):
    m = max(numbers_copy)
    max_list.append(m)
    numbers_copy.remove(m)

print(sum(numbers))
print(*max_list)

#  reference solution
from decimal import Decimal as D

s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'

nums = [D(x) for x in s.split()]

print(sum(nums))
print(*sorted(nums, reverse=True)[:5])

