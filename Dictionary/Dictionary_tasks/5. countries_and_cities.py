n = int(input())

mydict = {}
for _ in range(n):
    mylist = input().split()
    dict_temp = dict.fromkeys(mylist[1:], mylist[0])
    mydict.update(dict_temp)
m = int(input())

for _ in range(m):
    print(mydict[input()])

#  reference solution
d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    d.update(dict.fromkeys(cities, country))
for _ in range(int(input())):
    print(d[input()])