n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]
counter = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                counter += 1
                matrix[i][j] = counter
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# n, m = map(int, input().split())
# mt = [[''] * m for i in '1'* n]
# d = 1
# for k in range(1, n + m + 1):
#     for i in range(n):
#         for j in range(m):
#             if i + j + 1 == k:
#                 mt[i][j] = str(d).ljust(3)
#                 d += 1
# [print(*r, sep='') for r in mt]