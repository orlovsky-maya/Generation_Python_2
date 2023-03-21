n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            matrix[i][j] = j - i
        else:
            matrix[i][j] = i - j
        matrix[i][i] = 0
for row in matrix:
    print(*row)