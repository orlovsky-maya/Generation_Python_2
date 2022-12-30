s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
    'barley '
s_list = s.split()

s_dict = {}
for word in s_list:
    s_dict[word] = s_dict.get(word, 0) + 1

counter = 0
word = ''

for key, value in s_dict.items():
    if value > counter:
        counter = value
        word = key
    elif value == counter:
        word = min(key, word)
print(word)
