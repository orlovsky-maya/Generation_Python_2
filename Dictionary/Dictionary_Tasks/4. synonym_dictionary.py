n = int(input())
mydict = {}

for i in range(n):
    key, value = input().split()
    mydict[key] = value

word = input()

for key, value in mydict.items():
    if word == key:
        print(mydict[word])
    elif word == value:
        print(key)

#  reference solution
words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])