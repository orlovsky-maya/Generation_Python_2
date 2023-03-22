def merge(values):  # values - это список словарей
    my_dict = {}
    for di in values:
        for key, value in di.items():
            my_dict[key] = my_dict.get(key, set())
            my_dict.get(key).add(value)
    return my_dict

#  reference solution
def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res

#  reference solution
def merge(values):
    result = {}
    for i in values:
        for key, value in i.items():
            result[key] = result.get(key, {value}) | {value}
    return result

# input
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)
# output
result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}