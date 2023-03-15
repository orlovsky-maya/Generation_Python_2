from random import *

with open('first_names.txt') as first_names, open('last_names.txt') as last_names:
    for i in range(3):
        first_name = choice(first_names.readlines()).rstrip()
        last_name = choice(last_names.readlines()).rstrip()
        print(first_name, last_name)
        first_names.seek(0)
        last_names.seek(0)


import random as r

with open('first_names.txt') as fn, open('last_names.txt') as ln:
    first_name = fn.read().split()
    last_name = ln.read().split()

[print(*i) for i in list(zip(r.sample(first_name, 3), r.sample(last_name, 3)))]