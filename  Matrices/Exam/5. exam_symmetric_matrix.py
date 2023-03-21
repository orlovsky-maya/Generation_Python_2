n = int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]
answer = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            answer = 'NO'
            break
print(answer)