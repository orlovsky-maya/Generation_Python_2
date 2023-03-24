with open('ledger.txt') as file:
    num = [int((n.lstrip('$')).strip()) for n in file.readlines()]
    print('$' + str(sum(num)))

#  reference solution

with open('ledger.txt') as f:
    print(f'${sum([int(i.strip()[1:]) for i in f.readlines()])}')