import random
n = 5
my_list = list(set(random.sample(range(1, 76), n * n)))
matrix = [[0] * n for i in range(n)]

for r in range(n):
    for c in range(n):
        matrix[r][c] = my_list[r * n + c]

for r in range(n):
    for c in range(n):
        if r == 2 and c == 2:
            matrix[r][c] = 0
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()


from random import sample

numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()