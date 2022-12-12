coordinats = list(input())
colomns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['8', '7', '6', '5', '4', '3', '2', '1', '0']
row = int(rows.index(coordinats[1]))
col = int(colomns.index(coordinats[0]))
matrix = [['.'] * 8 for i in range(8)]
matrix[row][col] = 'N'
for r in range(8):
    for c in range(8):
        if abs(col - c) * abs(row - r) == 2:
            matrix[r][c] = '*'
for row in matrix:
    print(*row)


x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)
