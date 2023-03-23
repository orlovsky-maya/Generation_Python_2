def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def func_apply(fun, items):
    return map(fun, items)


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))