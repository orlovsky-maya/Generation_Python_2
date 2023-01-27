# n = int(input())
# prog_list = [input() for _ in range(n)]
# m = int(input())
# words = [input().lower() for _ in range(m)]
#
# for i in range(len(prog_list)):
#     prog_list[i] = prog_list[i].split(': ')
# for j in range(len(prog_list)):
#     for k in range(len(prog_list)):
#         prog_list[k][0] = prog_list[k][0].lower()
#
# prog_dict = dict(prog_list)
#
# for c in words:
#     print(prog_dict.get(c, 'Не найдено'), sep='\n')


mydict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key.lower()] = value

for _ in range(int(input())):
    print(mydict.get(input().lower(), 'Не найдено'))
