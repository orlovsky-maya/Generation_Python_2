n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]

min_n = 0
max_n = n - 1
min_m = 0
max_m = m - 1
counter = 1
while counter <= n * m:
    for i in range(min_n + 1):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = counter
                counter += 1
    for i in range(1, n):
        for j in range(max_m, m):
            if matrix[i][j] == 0:
                matrix[i][j] = counter
                counter += 1
    for i in range(max_n, n):
        for j in range(max_m - 1, -1, -1):
            if matrix[i][j] == 0:
                matrix[i][j] = counter
                counter += 1
    for i in range(max_n - 1, 0, -1):
        for j in range(min_m + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = counter
                counter += 1
    min_n += 1
    max_n -= 1
    min_m += 1
    max_m -= 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()