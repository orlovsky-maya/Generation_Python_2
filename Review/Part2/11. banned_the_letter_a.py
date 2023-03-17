def delete_letter(text, letter):
    while letter in text:
        text.remove(letter)
    return text


word = list(input() + ' ' + 'запретил букву')

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in range(len(alphabet)):
    if alphabet[i] in word:
        print(' '.join(''.join(word).split()), ' ', alphabet[i], sep='')
        delete_letter(word, alphabet[i])


word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()