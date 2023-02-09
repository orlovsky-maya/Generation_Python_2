from fractions import Fraction as F
num_1, num_2 = input(), input()
print(f'{num_1} + {num_2} = {F(num_1) + F(num_2)}')
print(f'{num_1} - {num_2} = {F(num_1) - F(num_2)}')
print(f'{num_1} * {num_2} = {F(num_1) * F(num_2)}')
print(f'{num_1} / {num_2} = {F(num_1) / F(num_2)}')

