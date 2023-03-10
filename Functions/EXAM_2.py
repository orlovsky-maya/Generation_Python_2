# def pretty_print(data, side='-', delimiter='|'):
#     first_delimiter = delimiter
#     delimiter = ' ' + delimiter + ' '
#     lenght = len(data) * 5
#     print(' ', side * lenght, ' ')
#     print(first_delimiter.strip(' | '), *data, sep=delimiter, end=delimiter)
#     print()
#     print(' ', side * lenght, ' ')

from functools import reduce


# def pretty_print(*data, side='-', delimiter='|'):
#     s = str(data)
#
#     mylist = list(map(lambda x: delimiter + ' ' + str(x) + ' ', *data))
#     lenght = len(str(mylist))
#     print(*mylist, end=delimiter)
#     print()
#     print(' ' + (lenght - 20) * side + ' ')
#     print()
#     print(lenght)
#     print(s)
#


def pretty_print(*data, side='-', delimiter='|'):
    s = list(map(lambda x: str(x), *data))
    s_1 = '   '.join(s)
    lenght = len(s_1)
    print(' ' + (lenght - 2) * side + ' ')
    mylist = list(map(lambda x: delimiter + ' ' + str(x) + ' ', *data))
    print(*mylist, end=delimiter)
    print()
    print(' ' + (lenght - 2) * side + ' ')
    print(s)
    print(s_1)
    # print(lenght)


    # mylist = list(map(lambda x: delimiter + ' ' + str(x) + ' ', *data))
    # lenght = len(str(mylist))
    # print(*mylist, end=delimiter)
    # print()
    # print(' ' + (lenght - 20) * side + ' ')
    # print()
    # print(lenght)
    # print(s)




pretty_print([1, 2, 10, 23, 123, 3000])


# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')