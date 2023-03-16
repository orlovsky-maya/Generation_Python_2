# with open('goats.txt') as colours, open('answer.txt', 'w') as goats:
#     all_list = colours.readlines()
#     colour_list = []
#     i = 1
#     while all_list[i].rstrip() != 'GOATS':
#         colour_list.append(all_list[i])
#         i += 1
#     goats_list = all_list[i - 1:]
#     length = len(goats_list)
#     result_list = []
#     for c in colour_list:
#         color_count = ''.join(goats_list).count(c)
#         if color_count * 100 / length > 7:
#             result_list.append(c)
#     goats.writelines(sorted(result_list))


with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)
