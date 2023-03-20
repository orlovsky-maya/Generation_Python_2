n = int(input())
m = int(input())
matrix = [[_ for _ in input().split()] for _ in range(n)]
numbers = [int(num) for num in input().split()]
i = numbers[0]
j = numbers[1]
for r in range(n):
    matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()


# #  reference solution
#
# n, m = int(input()), int(input())
# matrix = [input().split() for _ in range(n)]
# col1, col2 = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
#
# for row in matrix:
#     print(*row)