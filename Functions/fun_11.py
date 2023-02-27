def comparator(point):
    return point[sort_set[num] - 1]


athletes = [('Дима', 10, 130, 35), ('Рустам', 10, 128, 30), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
            ('Матвей', 17, 168, 68), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Петя', 15, 190, 90)]
sort_set = {1: 1, 2: 2, 3: 3, 4: 4}
num = int(input())
athletes.sort(key=comparator)
for c in athletes:
    print(*c)
