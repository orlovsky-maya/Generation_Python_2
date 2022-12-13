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
else:
    result = 'YES'
print(result)


