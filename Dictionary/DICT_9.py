n = int(input())
mydict = {}
for i in range(n):
    word = input()
    if word.lower() not in mydict:
        mydict[word.lower()] = [word]
    else:
        mydict[word.lower()].append(word)

text = input().split()
counter = 0
#
for j in text:
    if j.lower() in mydict:
        if j not in mydict[j.lower()]:
            counter += 1
    else:
        if j.islower():
            counter += 1
        else:
            count_upper = 0
            for k in j:
                if k.isupper():
                    count_upper += 1
            if count_upper > 1:
                counter += 1
print(counter)


n = int(input())
accents = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)

errors = 0
sent = input().split()
for word in sent:
    base_form = word.lower()
    if (base_form in accents and word not in accents[base_form]
            or len([l for l in word if l.isupper()]) != 1):
        errors += 1
print(errors)




