text = input().split()
mydict = {}
for word in text:
    counter = mydict.get(word, 0)
    mydict[word] = mydict.get(word, 0) + 1
    if counter == 0:
        print(0, end=' ')
    else:
        print(counter,  end=' ')

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

text = input().split()
words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 0
    print(words[word], end=' ')