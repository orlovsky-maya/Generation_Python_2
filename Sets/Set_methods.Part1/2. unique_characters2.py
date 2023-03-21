n = int(input())
mylist = [list(input().lower()) for _ in range(n)]
myset = set()

for i in range(n):
    for j in range(len(mylist[i])):
        myset.add(mylist[i][j])
print(len(myset))

#  reference solution
n = int(input())
symbols = set()

for _ in range(n):
    for c in input().lower():
        symbols.add(c)

print(len(symbols))