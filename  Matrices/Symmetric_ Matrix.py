n = int(input())
matrix = [[_ for _ in input().split()] for _ in range(n)]
symmertric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmertric = False
            break
if symmertric == True:
    print('YES')
else:
    print('NO')


n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)
