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

#  reference solution
import random
for _ in range(100):
    print(random.randint(1000000, 9999999))

#  reference solution
from random import sample as r

print(*r(range(int(1e6), int(1e7)), 100), sep='\n')