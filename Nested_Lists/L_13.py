s = input().split()
result_list = [[]]
n = 1
while n != len(s) + 1:
    for i in range(0, len(s) - (n - 1)):
        result_list.append(s[i:i + n])
    n += 1
print(result_list)

