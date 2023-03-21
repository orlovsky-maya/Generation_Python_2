s1, s2 = [set([int(i) for i in input().split()])for _ in range(2)]
print(*sorted(s1.difference(s2)))

#  reference solution
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())

print(*sorted(set1 - set2))