def merge(values):  # values - это список словарей
    my_dict = {}
    for di in values:
        for key, value in di.items():
            my_dict[key] = my_dict.get(key, set())
            my_dict.get(key).add(value)
    return my_dict


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)