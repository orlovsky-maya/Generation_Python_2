num = [int(n) for n in input().split()]
n = num[0]
m = num[1]
matrix = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 != 0:
            matrix[i][j] = '*'
        if i % 2 != 0 and j % 2 == 0:
            matrix[i][j] = '*'
for row in matrix:
    print(*row)


n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)
