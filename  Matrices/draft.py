n = int(input())
matrix_1 = [[int(i) for i in input().split()] for i in range(n)]
matrix_2 = [[matrix_1[r][c] for r in range(n)] for c in range(n)]
print(matrix_2)