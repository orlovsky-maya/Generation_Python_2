stud1, stud2, stud3 = [set(int(i) for i in input().split()) for _ in range(3)]
grades = set(range(11))
print(*sorted(grades - (stud1 | stud2 | stud3)))