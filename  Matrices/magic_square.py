n = int(input())
matrix = [[int(_) for _ in input().split()] for _ in range(n)]
numbers = [int(_) for _ in range(1, n ** 2 + 1)]
numbers_of_matrix = []
numbers_of_matrix.sort()
result = 'YES'

for i in range(len(numbers)):
    for j in range(n):
        if numbers[i] in matrix[j]:
            numbers_of_matrix.append(numbers[i])
            break

if numbers != numbers_of_matrix:
    result = 'NO'

main_diagonal = 0
secondary_diagonal = 0

if result == 'YES':

    for i in range(n):
        for j in range(n):
            if i == j:
                main_diagonal += matrix[i][j]
            if j == n - i - 1:
                secondary_diagonal += matrix[i][j]

    if main_diagonal != secondary_diagonal:
        result = 'NO'

    for i in range(1, n):
        if sum(matrix[i]) != sum(matrix[i - 1]) or sum(matrix[i]) != main_diagonal:
            result = 'NO'
            break

    new_matrix = [[0] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            new_matrix[c][r] = matrix[r][c]

    for r in range(n):
        for c in range(n):
            if sum(new_matrix[r]) != sum(new_matrix[r - 1]) or sum(new_matrix[r]) != main_diagonal:
                result = 'NO'

print(result)
