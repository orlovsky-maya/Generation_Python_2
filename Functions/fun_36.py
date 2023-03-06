R = 2
abscissas, ordinates, applicates = [[float(num) for num in input().split()] for _ in range(3)]

for x, y, z in zip(abscissas, ordinates, applicates):
    sum = x ** 2 + y ** 2 + z ** 2
    result = list(map(lambda x, y, z: True if sum <= R ** 2 else False, abscissas, ordinates, ordinates))

print(all(result))


abscissas, ordinates, applicates=(map(float, input().split()) for _ in range(3))
print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))

abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())

result = all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates))
print(result)