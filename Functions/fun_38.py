a, b = int(input()), int(input())

diapazon = list(filter(lambda x: '0' not in str(x), list(range(a, b + 1))))

result_list = []
for num in diapazon:
    result = all(map(lambda x: True if num % int(x) == 0 else False, str(num)))
    if result:
        result_list.append(num)
print(*result_list)


def check(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))

a, b = int(input()), int(input())
seq = range(a, b + 1)
print(*list(filter(lambda x: check(x), seq)))