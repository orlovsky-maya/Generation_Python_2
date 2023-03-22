from random import choice as c, randrange as r
import string
def generate_index():
    return f'{c(string.ascii_uppercase)}{c(string.ascii_uppercase)}{r(100)}_{r(100)}' \
           f'{c(string.ascii_uppercase)}{c(string.ascii_uppercase)}'


print(generate_index())
