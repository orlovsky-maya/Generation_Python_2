numbers = [int(num) for num in input().split()]
numbers_set = set()
length = 0
for c in numbers:
    numbers_set.add(c)
    if length != len(numbers_set):
        print('NO')
        length = len(numbers_set)
    else:
        print('YES')


#  reference solution
numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)