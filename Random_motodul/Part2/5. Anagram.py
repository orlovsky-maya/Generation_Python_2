import random
text = list(input())
random.shuffle(text)
print(*text, sep='')

