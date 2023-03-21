n, m = [int(num_1) for num_1 in input().split()]
matrix_1 = [[int(num_1) for num_1 in input().split()] for _ in range(n)]

input()

m_2, k = [int(num_2) for num_2 in input().split()]
matrix_2 = [[int(num_2) for num_2 in input().split()] for _ in range(m)]

matrix_multi = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(m):
        for q in range(k):
            matrix_multi[i][q] = matrix_multi[i][q] + matrix_1[i][j] * matrix_2[j][q]

for row in matrix_multi:
    print(*row)
