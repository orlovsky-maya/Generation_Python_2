# Последовательность Трибоначчи

n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, sep=' ', end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3


