# text = input().lower()
# for c in '.,!?:;-':
#     if c in text:
#         text = text.replace(c, '')
# text = text.split()
# dict_text = {}
# for i in text:
#     dict_text[i] = dict_text.get(i, 0) + 1
#
# counter = len(text)
# word = ''
# for key, value in dict_text.items():
#     if value < counter:
#         counter = value
#         word = key
#     elif value == counter:
#         word = min(key, word)
# print(word)


dct = {}
lst = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in lst:
    dct[word] = dct.get(word, 0) + 1
lst = [(value, key) for key, value in dct.items()]
lst.sort()
print(lst[0][1])