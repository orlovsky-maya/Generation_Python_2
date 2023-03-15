from random import *

with open('first_names.txt') as first_names, open('last_names.txt') as last_names:
    for i in range(3):
        first_name = choice(first_names.readlines()).rstrip()
        last_name = choice(last_names.readlines()).rstrip()
        print(first_name, last_name)
        first_names.seek(0)
        last_names.seek(0)
