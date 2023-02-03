gen_dict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'}

dnk = input()
pnk = ''
for c in dnk:
    pnk = pnk + gen_dict[c]
print(pnk)

