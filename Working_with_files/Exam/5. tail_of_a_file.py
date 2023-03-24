with open(input()) as file:
    lines_list = file.readlines()[-10:]
    print(*lines_list, sep='')