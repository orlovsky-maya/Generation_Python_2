# n = int(input())
# my_list = []
# for i in range(1, n + 1):
#     my_list.append(list(range(1, i + 1)))
# print(* my_list, sep='\n')



n = int(input())


elem = [list(range(1, i + 1)) for i in range(1, n + 1)]
print(* elem, sep='\n')




