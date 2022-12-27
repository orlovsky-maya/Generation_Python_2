first = {int(i) for i in input().split()}
second = {int(i) for i in input().split()}
common_digits = first & second
if len(common_digits) > 0:
    print(*sorted(common_digits, reverse=True))
else:
    print('BAD DAY')