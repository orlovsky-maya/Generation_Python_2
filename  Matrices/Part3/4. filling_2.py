n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    number = i + 1
    for j in range(m):
        matrix[i][j] = number
        number += n
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#  reference solution
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()