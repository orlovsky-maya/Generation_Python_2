text = input().lower()
symbols = ".,;:-?!"
for c in symbols:
    if c in text:
        text = text.replace(c, '')
text_set = set(text.split())
print(len(text_set))


words = [word.lower().strip('.,;:-?!') for word in input().split()]

print(len(set(words)))