with open('data.txt') as file:
    file_list = file.readlines()[::-1]
    for line in file_list:
        print(line.rstrip())
