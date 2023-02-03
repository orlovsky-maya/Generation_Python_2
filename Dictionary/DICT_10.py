# mydict = {}
# while True:
#     sername, item, count = input().split()
#     for key, value in mydict:
#         if sername not in mydict:
#             mydict[sername] = {item: count}
#         else:
#             mydict[sername][item] += count
#             print(mydict)


# mydict = {}
# for i in range(6):
#     sername, item, count = input().split()
#     if sername not in mydict:
#         mydict[sername] = {item: int(count)}
#     else:
#         mydict[sername][item] = mydict[sername].get(item, 0) + int(count)
#
# for key, value in sorted(mydict.items(), key = lambda x: x[1]):
#     print(key, ':', *value)

mydict = {sername: {item: count for item, count in range(3)} for sername in input().split('\n')}

print(mydict)
#     sername, item, count = input().split()
#     if sername not in mydict:
#         mydict[sername] = {item: int(count)}
#     else:
#         mydict[sername][item] = mydict[sername].get(item, 0) + int(count)
#
# for key, value in sorted(mydict.items(), key = lambda x: x[1]):
#     print(key, ':', *value)



