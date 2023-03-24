with open('words.txt') as file:
    data_list = file.read().split()
    largest = max(list(map(len, data_list)))
    for word in data_list:
        if len(word) == largest:
            print(word)

#  reference solution
with open('words.txt') as f:
    lst = f.read().split()
longest = len(max(lst, key=len))
print(*filter(lambda x: len(x) == longest, lst), sep='\n')