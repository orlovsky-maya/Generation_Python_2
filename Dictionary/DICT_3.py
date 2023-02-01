n = int(input())
mydict = {}
for s in range(n):
    name, voice = input().split()
    mydict[name] = mydict.get(name, 0) + int(voice)
for name in sorted(mydict):
    print(name, mydict[name])