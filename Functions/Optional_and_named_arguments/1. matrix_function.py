def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]


print(matrix(3, 4, 9))

# input

# print(matrix())                   # матрица 1 × 1 из 0
# print(matrix(3))                  # матрица 3 × 3 из 0
# print(matrix(2, 5))               # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))            # матрица 3 × 4 из 9

# output

# [[0]]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]