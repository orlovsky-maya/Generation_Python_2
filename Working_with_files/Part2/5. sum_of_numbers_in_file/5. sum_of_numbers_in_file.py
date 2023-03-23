# draft
with open('nums.txt') as file:
    file = file.read()

    digits = []
    for i in range(len(file)):
        if file[i].isdigit():
            digits.append(file[i])
        else:
            digits.append(' ')
    digits_str = ''.join(digits)
    numbers_str = digits_str.split(' ')
    res = 0
    for n in numbers_str:
        if n:
            res += int(n)

    print(res)


with open('nums.txt') as file:
    file = file.read()

    digits = []
    for elem in file:
        if elem.isdigit():
            digits.append(elem)
        else:
            digits.append(' ')
    digits_str = ''.join(digits)
    numbers_str = digits_str.split(' ')
    result = sum((map(lambda x: int(x) if x else int(0), numbers_str)))
    print(result)


#  reference solutions
with open('numbers.txt', encoding='utf-8') as file:
    row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(sum(map(int, row.split())))


with open('nums.txt') as file:
    temp = ''
    n = 0
    for c in file.read():
        if c.isdigit():
            temp += c
        elif temp != '':
            n += int(temp)
            temp = ''
    print(n)