def summa(num):
    n = [int(j) for j in str(num)]
    return sum(n)


numbers = sorted([int(i) for i in input().split()])
numbers.sort(key=summa)

print(*numbers, sep=' ', end=' ')
