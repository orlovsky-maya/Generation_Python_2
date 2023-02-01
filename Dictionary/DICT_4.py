n = int(input())
medict = {}
for i in range(n):
    text = input().split()
    for word in text:
        medict[word] = medict.get(word, 0) + 1

largest = 0
result_word = ''
for key, value in medict.items():
    if value > largest:
        largest = value
        result_word = key
    elif value == largest:
        if key < result_word:
            result_word = key
print(result_word)