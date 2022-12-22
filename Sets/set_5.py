n = input()
if len(n) != len(set(n)):
    print('NO')
else:
    print('YES')


a = input()
print(('NO', 'YES')[len(a) == len(set(a))])

