n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
maximum = matrix[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
print(maximum)


# reference solution
# n = int(input())
# matrix = []
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# largest = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > largest:
#             largest = matrix[i][j]
#
# print(largest)