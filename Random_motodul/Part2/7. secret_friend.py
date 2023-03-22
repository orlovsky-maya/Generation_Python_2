import random
n = int(input())
in_list = [input() for _ in range(n)]
select = in_list.copy()
out_list = []

for i in range(len(in_list)-1):
    e = select.pop(0)
    choice = random.choice(select)
    out_list.append(choice)
    select.remove(choice)
    select.append(e)

out_list.append(select[0])
if in_list[-1] == out_list[-1]:
    out_list[-2], out_list[-1] = out_list[-1], out_list[-2]

result_dict = dict(zip(in_list, out_list))

for key, value in result_dict.items():
    print(key, '-', value)


#  reference solution
from random import choice

names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
for name in names.copy():
    if names == {name}:
        rel[tmp], rel[name] = name, rel[tmp]
    else:
        rand_name = choice(list(names - {name}))
        rel[name] = rand_name
        names -= {rand_name}
        tmp = name
[print(k, '-', v) for k, v in rel.items()]