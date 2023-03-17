n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
largest = matrix[0][0]
for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j and largest < matrix[i][j]:
            largest = matrix[i][j]
        if i <= j and i >= n - 1 - j and largest < matrix[i][j]:
            largest = matrix[i][j]
print(largest)