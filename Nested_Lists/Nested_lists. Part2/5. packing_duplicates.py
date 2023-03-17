s = input().split()
result_list = []
row = [s[0]]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        row.append(s[i])
    else:
        result_list.append(row)
        row = [s[i]]
result_list.append(row)
print(result_list)
