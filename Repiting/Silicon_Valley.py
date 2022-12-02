def is_anton(name):
    key_word = ''
    for c in 'anton':
        ind = name.find(c)
        if ind > -1:
            key_word += c
            name = name[ind:]
    if key_word == 'anton':
        return True
    return False


list_names = [input() for _ in range(int(input()))]
numbers_refr = []
for i in range(len(list_names)):
    if is_anton(list_names[i]):
        numbers_refr.append(i + 1)
print(* numbers_refr)
