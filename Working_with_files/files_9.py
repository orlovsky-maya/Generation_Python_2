# with open('lines.txt') as file:
#     file = file.readlines()
#     maximum = len(max(file, key=len))
#     result_file = list(filter(lambda line: len(line) == maximum, file))
#     for line in result_file:
#         print(line.rstrip())

with open('lines.txt') as file:
    file = file.readlines()
    maximum = len(max(file, key=len))
    result_file = list(filter(lambda line: len(line) == maximum, file))
print(*result_file, sep='')

