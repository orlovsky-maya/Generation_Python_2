import random
from random import choice as c, sample as s
import string

symbols_upper = string.ascii_uppercase
symbols_lower = string.ascii_lowercase
symbols_digit = string.digits
for i in 'lI1oO0':
    if i in symbols_upper:
        symbols_upper = symbols_upper.replace(i, '')
    elif i in symbols_digit:
        symbols_digit = symbols_digit.replace(i, '')
    elif i in symbols_lower:
        symbols_lower = symbols_lower.replace(i, '')
symbols_all = symbols_upper + symbols_lower + symbols_digit


def generate_password(length):
    password = list(c(symbols_upper)) + list(c(symbols_lower)) + list(c(symbols_digit)) + s(symbols_all, length - 3)
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())

generate_passwords(n, m)



from string import ascii_uppercase, ascii_lowercase, digits
from random import sample, shuffle
letters_lower = [i for i in ascii_lowercase if i not in 'lo']
letters_upper = [i for i in ascii_uppercase if i not in 'IO']
digits = list(digits[2:])
all_symbol = letters_lower + letters_upper + digits


def generate_password(length):
    password = sample(letters_lower, 1) + sample(letters_upper, 1) + sample(digits, 1) + sample(all_symbol, length-3)
    shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for i in range(count)]


n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')