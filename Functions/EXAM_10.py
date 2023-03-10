from operator import *


def arithmetic_operation(operation):
    operation_dict = {'+': add, '-': sub, '*': mul, '/': truediv}
    return lambda x, y: operation_dict[operation](x, y)

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))