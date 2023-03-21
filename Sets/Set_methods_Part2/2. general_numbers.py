s1, s2 = [set([int(i) for i in input().split()])for _ in range(2)]
print(*sorted(s1 & s2))
