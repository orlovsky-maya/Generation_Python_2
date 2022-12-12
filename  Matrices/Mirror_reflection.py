n = int(input())
matrix = [input().split() for _ in range(n)]


for i in range(n):
    for j in range(n):
        if i < n // 2:
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
for row in matrix:
    print(*row)


n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)