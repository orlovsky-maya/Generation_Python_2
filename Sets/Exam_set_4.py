m = int(input())
n = int(input())
home_set = {input() for i in range(m)}
summer_list = [input() for j in range(n)]
for book in summer_list:
    if book in home_set:
        print('YES')
    else:
        print('NO')