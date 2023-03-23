with open('numbers.txt') as file:
    lls = list(map(str.split, file.readlines()))
    for l in lls:
        print(sum(map(int, l)))

#  reference solution
with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))

