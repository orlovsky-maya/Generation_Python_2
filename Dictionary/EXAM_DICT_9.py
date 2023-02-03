n = int(input())
mydict = {}
for i in range(n):
    sername, item, count = input().split()
    if sername not in mydict:
        mydict[sername] = {item: int(count)}
    else:
        mydict[sername][item] = mydict[sername].get(item, 0) + int(count)
for name in sorted(mydict):
    print(name, ':', sep='')
    for key, value in sorted(mydict[name].items()):
        print(key, value)



