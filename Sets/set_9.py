n = int(input())
mylist = [input().lower() for elem in range(n)]
for c in mylist:
    print(len(set(c)))


for _ in range(int(input())):
    print(len(set(input().lower())))