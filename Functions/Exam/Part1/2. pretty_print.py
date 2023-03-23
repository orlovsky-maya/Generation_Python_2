def pretty_print(data, side='-', delimiter='|'):
    s = f' {delimiter} '.join(map(str, data))
    lenght = len(s)
    print(' ' + (lenght + 2) * side + ' ')
    print(delimiter, s, delimiter)
    print(' ' + (lenght + 2) * side + ' ')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

