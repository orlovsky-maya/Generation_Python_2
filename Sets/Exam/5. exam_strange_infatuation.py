first = {int(i) for i in input().split()}
second = {int(i) for i in input().split()}
common_digits = first & second
if len(common_digits) > 0:
    print(*sorted(common_digits, reverse=True))
else:
    print('BAD DAY')


#  reference solution
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

if set1.isdisjoint(set2):
    print('BAD DAY')
else:
    print(*sorted(set1 & set2, reverse=True))