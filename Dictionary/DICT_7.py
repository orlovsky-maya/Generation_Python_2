n = int(input())
mydict = {}
for i in range(n):
    country, *cities = input().split()
    mydict[country] = cities
m = int(input())
for j in range(m):
    city = input()
    for key, value in mydict.items():
        if city in value:
            print(key)

motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
print(motherland)

for i in range(int(input())):
    print(motherland[input()])