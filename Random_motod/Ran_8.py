from random import randrange as r
bilets = set()
while len(bilets) != 100:
    num = []
    num.append(r(1, 10))
    for i in range(6):
        num.append(r(9))
    bilets.add(tuple(num))

for i in bilets:
    print(*i, sep='')


import random
for _ in range(100):
    print(random.randint(1000000, 9999999))