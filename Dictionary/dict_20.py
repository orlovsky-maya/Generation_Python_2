# n = int(input())
# mydict = {}
#
# for _ in range(n):
#     num, name = input().lower().split()
#     mydict[num] = name
#
# m = int(input())
#
# for _ in range(m):
#     name_frends = input().lower()
#     num_list = []
#     if name_frends in mydict.values():
#         for key_num, value_name in mydict.items():
#             if name_frends == value_name:
#                 num_list.append(key_num)
#         print(*num_list)
#     else:
#         print('абонент не найден')



dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))