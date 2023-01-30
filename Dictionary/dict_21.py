word = input()
n = int(input())
alf_dict = dict([input().split(': ') for _ in range(n)])

for key, value in alf_dict.items():
    for i in range(len(word)):
        if word.count(word[i]) == int(value):
            word = word.replace(word[i], key)
print(word)
