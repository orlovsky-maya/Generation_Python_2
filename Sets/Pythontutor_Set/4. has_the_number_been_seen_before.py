numbers_list = [int(num) for num in input().split()]
numbers_set = set()
for n in numbers_list:
    if n not in numbers_set:
        print('NO')
        numbers_set.add(n)
    else:
        print('YES')