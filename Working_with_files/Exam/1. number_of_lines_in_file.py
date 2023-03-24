name = input()
with open(name) as file:
    file_data = file.readlines()
    print(len(file_data))