list = [i for i in input().split()]
n = int(input())
list_result = []
for i in range(n):
    list_inter = []
    for j in range(i, len(list), n):
        list_inter.append(list[j])
    list_result.append(list_inter)
print(list_result)