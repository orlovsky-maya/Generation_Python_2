first_word = list(input())
second_word = list(input())

first_dict = {}
second_dict = {}
for c in first_word:
    first_dict[c] = first_dict.get(c, 0) + 1

for c in second_word:
    second_dict[c] = second_dict.get(c, 0) + 1

if first_dict == second_dict:
    print('YES')
else:
    print('NO')

#  reference solution

d = {}
for c in input().lower():
    d[c] = d.get(c, 0) + 1
for c in input().lower():
    d[c] = d.get(c, 0) - 1

print(('NO', 'YES')[set(d.values()) == {0}])
