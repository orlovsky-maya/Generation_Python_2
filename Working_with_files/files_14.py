with open('population.txt') as file:
    l_str = list(map(str.rstrip, file.readlines()))
    l_list = dict(list(map(lambda x: x.split('\t'), l_str)))
    result = list(filter(lambda item in point.items(): item[0].startswith('G') and int(item[1]) > 500000, l_list))
    print(l_str)
    print(l_list)
    # print(result)