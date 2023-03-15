with open('file.txt') as file:
    alfabet_result = 0
    for line in file.readlines():
        alfabet_result += len(''.join(list(filter(str.isalpha, (map(str.strip, line))))))
    file.seek(0)

    word_result = 0
    for line in file.readlines():
        word_result += len(line.split())
    file.seek(0)

    str_result = len(file.readlines())

    print(f'Input file contains:\n{alfabet_result} letters\n{word_result} words\n{str_result} lines')


with open('lines.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')