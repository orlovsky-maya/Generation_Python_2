n = int(input())
mydict = {}
for i in range(n):
    stroka = input().split()
    for c in stroka:
        mydict[c] = mydict.get(c, 0) + 1
mylist = [(value, key) for key, value in mydict.items()]
mylist = sorted(mylist, key=lambda x: x[1])
mylist = sorted(mylist, reverse=True, key=lambda x: x[0])
for i in range(len(mylist)):
    print(mylist[i][1])
