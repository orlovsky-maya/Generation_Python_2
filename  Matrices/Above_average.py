n = int(input())
matrix = []
result = []
for i in range(n):
    tmp_result = 0
    row = [int(num) for num in input().split()]
    summa = sum(row)
    average = summa / n
    matrix.append(row)
    for j in range(n):
        if matrix[i][j] > average:
            tmp_result += 1
    result.append(tmp_result)
print(* result, sep='\n')

n = int(input())
matrix = []




for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)