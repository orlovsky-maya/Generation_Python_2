n = int(input())
all_class = []


def check_class(school_class):
    return any(map(lambda x: int(x[1]) == 5, school_class))


for i in range(n):
    k = int(input())
    school_class = [input().split() for j in range(k)]
    all_class.append(check_class(school_class))

if all(all_class):
    print('YES')
else:
    print('NO')



# cl = [['Васечкин', '4'], ['Илюшин', '5']]
# all_class.append(check_class(cl))
# print(check_class(cl))
# print(all_class)