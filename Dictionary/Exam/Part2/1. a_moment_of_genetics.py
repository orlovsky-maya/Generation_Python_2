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


#  reference solution
d = {'ACGT'[i]: 'UGCA'[i] for i in range(4)}
for i in input():
    print(d[i], end='')

#  reference solution
d = dict(zip('GCTA', 'CGAU'))
print(*[d[i] for i in input()], sep = '')