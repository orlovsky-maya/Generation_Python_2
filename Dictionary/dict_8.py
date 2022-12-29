result = dict({(i, i ** 2) for i in range(1, 16)})
print(result)


result = {}
for i in range(1, 16):
    result[i] = i * i