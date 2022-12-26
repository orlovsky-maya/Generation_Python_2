stud1, stud2, stud3 = [{int(i) for i in input().split()} for _ in range(3)]
print(*sorted((stud1 | stud2 | stud3) - (stud1 & stud2 & stud3)))