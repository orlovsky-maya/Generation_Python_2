numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
           53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
           37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]


filter_result = list(filter(lambda num: num % 2 == 0 or num < 47, numbers))
map_result = list(map(lambda num: num // 2 if num % 2 == 0 else num, filter_result))
print(*map_result)


# filter_result = list(filter(lambda num: False if (num % 2 != 0 and num > 47) else True, numbers))

print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))