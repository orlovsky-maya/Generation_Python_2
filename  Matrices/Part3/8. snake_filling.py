n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]
number = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = number
        number += 1
for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

#  reference solution
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()