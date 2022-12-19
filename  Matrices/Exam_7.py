coord_col, coord_row = input()
n = 8
ind_col = ord(coord_col) - 97
ind_row = n - int(coord_row)
matrix = [['.'] * n for _ in range(n)]

for i in range(8):
    for j in range(8):
        if abs(ind_row - i) == abs(ind_col - j) or ind_row == i or ind_col == j:
            matrix[i][j] = '*'
matrix[ind_row][ind_col] = 'Q'
for row in matrix:
    print(*row)