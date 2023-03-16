files_list = [input() for i in range(int(input()))]
with open('output.txt', 'a') as output:
    for name_file in files_list:
        file = open(name_file).read()
        output.write(file)

#Good solution

# with open('output.txt', 'w') as out:
#     for i in range(int(input())):
#         with open(input()) as f:
#             out.write(f.read())