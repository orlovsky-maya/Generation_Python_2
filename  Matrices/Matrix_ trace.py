n = int(input())
matrix = []
for i in range(n):
    row = [int(num) for num in input().split()]
    matrix.append(row)
summa = 0
for i in range(n):
    summa += matrix[i][i]
print(summa)


res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)