n = int(input())
m = int(input())
matrix = []
row = []
for i in range(n):
    for j in range(m):
        cols = input()
        row.append(cols)
    matrix.append(row)
    row = []
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
    print()
