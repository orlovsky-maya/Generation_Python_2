# Complete the given code1
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
comp = 1
for elem in numbers:
    comp *= elem
print(comp)

# Complete the given code2
data = 'Python для продвинутых!'
date_tup = tuple(data)
print(date_tup)

# Complete the given code3
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = poet_data[:-1] + ('Москва',)
print(poet_data)

# Complete the given code4
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
list_result = []
for elem in numbers:
    aver = sum(elem) / len(elem)
    list_result.append(aver)
print(list_result)

# Complete the given code5
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
list_result = [sum(elem) / len(elem) for elem in numbers]
print(list_result)

