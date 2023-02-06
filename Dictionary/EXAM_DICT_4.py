text = input().split()
mydict = {}
for word in text:
    counter = mydict.get(word, 1)
    mydict[word] = mydict.get(word, 1) + 1
    if counter == 1:
        print(1, end=' ')
    else:
        print(counter,  end=' ')

s = input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
    print(d[i], end = ' ')