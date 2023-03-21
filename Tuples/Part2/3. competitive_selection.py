n = int(input())
list_all = []
list_more_3 = []
for i in range(n):
    elem = tuple(input().split())
    list_all.append(elem)
    if int(elem[1]) > 3:
        list_more_3.append(elem)
for elem in list_all:
    print(*elem)
print()
for elem in list_more_3:
    print(*elem)

#  reference solution
students = [tuple(input().split()) for _ in range(int(input()))]

for student in students:
    print(*student)

print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)




