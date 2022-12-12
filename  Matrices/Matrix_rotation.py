n = int(input())
matrix = [input().split() for _ in range(n)]
matrix.reverse()
for c in range(n):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
