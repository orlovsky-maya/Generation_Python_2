first_word, second_word = input().lower(), input().lower()
first_dict = {}
second_dict = {}

for c in first_word:
    if c in '.,!?:;-':
        first_word.replace(c, '')
    else:
        first_dict[c] = first_dict.get(c.strip(), 0) + 1

for c in second_word:
    if c in '.,!?:;-':
        second_word.replace(c, '')
    else:
        second_dict[c] = second_dict.get(c.strip(), 0) + 1

print(('NO', 'YES')[first_dict == second_dict])

#  reference solution
def make_dict(word):
    mydict = {}

    for c in word:
        if c in '.,!?:;-':
            word.replace(c, '')
        else:
            mydict[c] = mydict.get(c.strip(), 0) + 1
    return mydict


first_dict = make_dict(input().lower())
second_dict = make_dict(input().lower())

print(('NO', 'YES')[first_dict == second_dict])


#  reference solution
def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res


print(("NO", "YES")[s(input()) == s(input())])