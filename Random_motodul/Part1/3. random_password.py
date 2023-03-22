import random

length = int(input())
for i in range(length):
    print(((chr(random.randint(65, 90)), chr(random.randint(97, 122)))[random.randint(0, 1)]), end='')

#  reference solution
import random

length = int(input())    # длина пароля

for i in range(length):
    print(chr(random.randint(65, 90) or random.randint(97, 122)), end='')