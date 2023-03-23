def print_products(*args):
    prod = [i for i in args if type(i) is str and len(i) > 0]
    if len(prod) == 0:
        print('Нет продуктов')
    else:
        for i in range(len(prod)):
            print(f'{i + 1}) {prod[i]}')

# # input
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')
# # output
# 1) Бананы
# 2) Яблоки
# 3) Макароны
# Нет продуктов