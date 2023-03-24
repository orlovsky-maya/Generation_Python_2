with open('forbidden_words.txt', 'r', encoding='utf-8') as f_file, open(input(), 'r', encoding='utf-8') as txt_file:
    f_file = f_file.read().split()
    txt_file = txt_file.read()
    txt_file_str_lower = txt_file.lower()
    for fob_word in f_file:
        txt_file_str_lower = txt_file_str_lower.replace(fob_word, '*' * len(fob_word))
    for i in range(len(txt_file)):
        if txt_file_str_lower[i] == '*':
            print('*', end='')
        else:
            print(txt_file[i], end='')

