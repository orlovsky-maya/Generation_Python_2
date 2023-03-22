import random
import string


def generate_password(length):
    symbols = string.ascii_letters + string.digits
    for s in 'lI1oO0':
        if s in symbols:
            symbols = symbols.replace(s, '')
    return ''.join(random.sample(symbols, length))


def generate_passwords(length):
    return generate_password(length)


n, m = int(input()), int(input())

for i in range(n):
    print(generate_passwords(m))



#  reference solution

from string import *
from random import sample

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    return ''.join(sample(LETTER, length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')





from string import ascii_letters, digits
from random import sample

def generate_password(lenght):
    return ''.join(sample(letter, lenght))


def generate_passwords(count, lenght):
    for _ in range(count):
        print(generate_password(lenght))


n, m = int(input()), int(input())
letter = list((set(ascii_letters) | set(digits)) - set('lLiI1oO0'))

generate_passwords(n, m)