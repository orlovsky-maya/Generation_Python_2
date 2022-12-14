n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()