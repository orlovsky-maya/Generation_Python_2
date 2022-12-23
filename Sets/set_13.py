s1, s2 = [set(input().split()) for _ in range(2)]
s3 = s1.intersection(s2)
print(len(s3))