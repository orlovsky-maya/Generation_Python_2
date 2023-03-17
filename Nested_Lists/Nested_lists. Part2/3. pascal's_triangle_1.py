n = int(input())

my_list = []
for i in range(n + 1):
    temp_list = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
    my_list.append(temp_list)

print(my_list[n])


