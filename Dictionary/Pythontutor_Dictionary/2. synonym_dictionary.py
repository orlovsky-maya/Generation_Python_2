n = int(input())
mydict = dict([input().split() for num in range(n)])
word = input()
for key, value in mydict.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)
