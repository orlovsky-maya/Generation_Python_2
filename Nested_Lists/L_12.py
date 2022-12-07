def chunked(s, n):
    result_list = []
    row = []
    for elem in s:
        if len(row) < n:
            row.append(elem)
        else:
            result_list.append(row)
            row = [elem]
    result_list.append(row)
    return result_list


stroka = input().split()
num = int(input())
print(chunked(stroka, num))


def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))