def summa(num):
    return sum(num)


numbers = [[int(j) for j in i] for i in input().split()]
numbers.sort(key=summa)
for i in numbers:
    print(*i, sep='', end=' ')
