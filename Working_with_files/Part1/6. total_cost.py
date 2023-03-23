file = open('prices.txt')
result_summa = 0
for line in file:
    summa = int(line.split()[2]) * int(line.split()[1])
    result_summa += summa
print(result_summa)

#  reference solution
file = open('prices.txt')
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()