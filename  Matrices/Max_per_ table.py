n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
largest = matrix[0][0]
row_number = 0
col_number = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            row_number = i
            col_number = j
print(row_number, col_number, sep=' ')

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j

print(row, col)