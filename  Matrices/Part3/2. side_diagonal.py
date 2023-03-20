n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][n - i - 1] = 1
        if i > n - 1 - j:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
