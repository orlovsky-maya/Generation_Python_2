def sq_sum(*args):
    summa = 0
    for i in range(len(args)):
        summa += args[i] ** 2
    return summa

# # input
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# # output
# 0
# 4
# 8.5
# 14
# 385