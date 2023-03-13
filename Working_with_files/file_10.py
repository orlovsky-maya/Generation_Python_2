with open('numbers.txt') as file:
    file = list(map(str.split, file.readlines()))
    for i in range(len(file)):
        print(sum(map(int, file[i])))


with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))