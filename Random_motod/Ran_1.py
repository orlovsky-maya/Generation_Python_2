import random

n = int(input())
for i in range(n):
    answer = random.randint(0, 1)
    if answer == 0:
        print('Орел')
    else:
        print('Решка')

from random import randint

COIN = ['Орел', 'Решка']

for _ in range(int(input())):
    print(COIN[randint(0, 1)])

import random

for i in range(int(input())):
    print(('Орел', 'Решка')[random.randint(0, 1)])