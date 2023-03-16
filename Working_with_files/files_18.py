with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    input_list = input_file.readlines()
    for index, item in enumerate(input_list, 1):
        output_file.write(f'{index}) {item}')

with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)