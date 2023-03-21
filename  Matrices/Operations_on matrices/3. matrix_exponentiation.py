def mul_matrix(matrix_a, matrix_b):
    n_row_col = len(matrix_a)
    matrix_multi = [[0] * n_row_col for _ in range(n_row_col)]
    for i in range(n_row_col):
        for j in range(n_row_col):
            for q in range(n_row_col):
                matrix_multi[i][q] = matrix_multi[i][q] + matrix_a[i][j] * matrix_b[j][q]
    return matrix_multi


def matrix_degree(matrix_a, m_degree):
    matrix_r = matrix_a.copy()
    counter = 1
    while counter < m_degree:
        matrix_r = mul_matrix(matrix_r, matrix_a)
        counter += 1
    return matrix_r


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
m = int(input())


for row in matrix_degree(matrix, m):
    print(*row)
