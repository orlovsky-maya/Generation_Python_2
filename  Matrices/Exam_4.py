n = int(input())
matrix = [['.'] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = '*'
    matrix[i][n - 1 - i] = '*'
    matrix[n // 2][i] = '*'
    matrix[i][n // 2] = '*'
for row in matrix:
    print(*row)
