from random import *

with open('random.txt', 'w', encoding='utf-8') as file:
    for i in range(25):
        file.write(str(randint(111, 777)))
        file.write('\n')

#  reference solutions
from random import*
with open('random.txt', 'w', encoding='utf-8') as file:
    for i in range(25):
        file.write(str(randint(111,777))+'\n')

from random import randrange
with open('random.txt','w') as out:
    print(*[randrange(111,778) for _ in range(25)],sep='\n',file=out)
