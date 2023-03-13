from random import *

file = open('lines.txt', encoding='utf-8')
text = choice(file.readlines())
print(text.rstrip())
file.close()