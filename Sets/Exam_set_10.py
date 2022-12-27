m = int(input())
n = int(input())
common_list = [input() for i in range(m + n)]
common_set = set(common_list)
if len(common_list) == len(common_set):
    print(n + m)
else:
    if len(common_set) - (len(common_list) - len(common_set)) > 0:
        print(len(common_set) - (len(common_list) - len(common_set)))
    else:
        print('NO')
