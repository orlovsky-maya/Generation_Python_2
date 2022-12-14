n, m = [int(n) for n in input().split()]
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        num = (i + j + 1) % m
        if num == 0:
            matrix[i][j] = m
        else:
            matrix[i][j] = num
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()