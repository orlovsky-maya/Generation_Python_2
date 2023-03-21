n, m = [int(num) for num in input().split()]
matrix_1 = []
for _ in range(n):
    row = [int(num) for num in input().split()]
    matrix_1.append(row)
input()
matrix_2 = []
for _ in range(n):
    row = [int(num) for num in input().split()]
    matrix_2.append(row)

matrix_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = (matrix_1[i][j] + matrix_2[i][j])

for r in matrix_sum:
    print(*r)


#  reference solution

n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrixC:
    print(*row)