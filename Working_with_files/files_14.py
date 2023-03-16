# with open('population.txt') as file:
#     l_list = list(map(lambda x: x.split('\t'), map(str.rstrip, file.readlines())))
#     result = list(filter(lambda point: point[0].startswith('G') and int(point[1]) > 500000, l_list))
#     for elem in result:
#         print(elem[0])


with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)