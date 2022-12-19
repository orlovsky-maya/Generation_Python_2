n = int(input())
matrix_1 = [[int(i) for i in input().split()] for i in range(n)]
numbers = [int(_) for _ in range(1, n + 1)]
matrix_2 = [[matrix_1[r][c] for r in range(n)] for c in range(n)]
answer = 'YES'

for row in range(n):
    for num in range(n):
        if numbers[num] not in matrix_1[row] or numbers[num] not in matrix_2[row]:
            answer = 'NO'
            break
print(answer)

