# def product_of_odds(data):
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result


from functools import reduce


def product_of_odds(data):
    fltered_list = list(filter(lambda x: x % 2 == 1, data))
    redused_list = reduce(lambda x, y: x * y, fltered_list, 1)
    return redused_list


print(product_of_odds([1, 2, 3, 4, 5]))
