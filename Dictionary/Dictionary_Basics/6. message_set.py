keyboard = {(' ',): '0',
            ('.', ',', '?', '!', ':'): '1',
            ('A', 'B', 'C'): '2',
            ('D', 'E', 'F'): '3',
            ('G', 'H', 'I'): '4',
            ('J', 'K', 'L'): '5',
            ('M', 'N', 'O'): '6',
            ('P', 'Q', 'R', 'S'): '7',
            ('T', 'U', 'V'): '8',
            ('W', 'X', 'Y', 'Z'): '9'}

text = input().upper()
for c in '";()-+*':
    if c in text:
        text = text.replace(c, '')

digits = ''

for letter in text:
    for key in keyboard:
        if letter in key:
            position = key.index(letter)
            digits += keyboard[key] * (position + 1)
            break
print(digits)



#  reference solution
keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for letter in input().upper():
    for key, value in keyboard.items():
        if letter in value:
            print(key * (value.index(letter) + 1), end="")