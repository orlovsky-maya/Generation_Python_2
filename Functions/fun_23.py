func = lambda txt: txt.lower()[0] == 'a' and txt.lower()[-1] == 'a'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))


func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')