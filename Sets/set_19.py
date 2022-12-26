stud1, stud2, stud3 = [{int(i) for i in input().split()} for _ in range(3)]
print(*sorted((stud1 & stud2) - stud3, reverse=True))



set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set1 & set2 - set3, reverse=True))