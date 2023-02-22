def mean(*args):
    s = sum([float(args[i]) for i in range(len(args)) if type(args[i]) is float or type(args[i]) is int])
    le = len([float(args[j]) for j in range(len(args)) if type(args[j]) is float or type(args[j]) is int])
    if le == 0:
        return 0.0
    else:
        return s / le


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))




def mean(*args):
    s = [float(i) for i in args if type(i) in (int, float)]
    if len(s) > 0:
        return sum(s)/len(s)
    else:
        return 0.0



