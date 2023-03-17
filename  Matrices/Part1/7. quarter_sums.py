n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in  input().split()]
    matrix.append(row)
top = 0
right = 0
lower = 0
left = 0
for i in range(n):
    for j in range(n):
        if j > i < n - 1 - j:
            top += matrix[i][j]
        if j > i > n - 1 - j:
            right += matrix[i][j]
        if j < i > n - 1 - j:
            lower += matrix[i][j]
        if j < i < n - 1 - j:
            left += matrix[i][j]
print('Верхняя четверть:', top)
print('Правая четверть:', right)
print('Нижняя четверть:', lower)
print('Левая четверть:', left)
