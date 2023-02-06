import random
def generate_ip():
    ip_adress = []
    for i in range(4):
        ip_adress.append(str(random.randint(0, 255)))
    return '.'.join(ip_adress)


print(generate_ip())

from random import choice
def generate_ip():
    s = range(0, 256)
    return f"{choice(s)}.{choice(s)}.{choice(s)}.{choice(s)}"




from random import randrange as r

def generate_ip():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

