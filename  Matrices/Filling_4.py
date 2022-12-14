n = int(input())
matrix = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j:
            matrix[i][j] = 0
        if i > j and i < n - 1 - j:
            matrix[i][j] = 0
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()