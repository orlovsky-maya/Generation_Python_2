text = [s for s in input().split()]
result_dict = {}
for c in text:
    counter = result_dict.get(c, 0)
    result_dict[c] = result_dict.get(c, 0) + 1
    if counter == 0:
        print(c, end=' ')
    else:
        print(str(c) + '_' + str(counter), end=' ')
