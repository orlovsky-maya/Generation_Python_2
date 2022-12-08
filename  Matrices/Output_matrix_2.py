n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
print()
for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()