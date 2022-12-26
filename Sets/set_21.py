stud1, stud2, stud3 = [set(int(i) for i in input().split()) for _ in range(3)]
print(*sorted((stud3 - stud1 - stud2), reverse=True))