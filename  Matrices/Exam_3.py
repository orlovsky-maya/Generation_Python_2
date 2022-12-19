n = int(input())
matrix = [[i for i in input().split()] for i in range(n)]
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    print(*row)