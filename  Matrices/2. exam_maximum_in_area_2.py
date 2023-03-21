n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]
largest = matrix[0][n - 1]
for i in range(1, n):
    for j in range(n - i - 1, n):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
print(largest)
