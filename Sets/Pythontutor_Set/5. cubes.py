n, m = [int(num) for num in input().split()]
anna = set(int(input()) for _ in range(n))
biris = set(int(input()) for _ in range(m))
print(len(anna.intersection(biris)))
print(*sorted(anna.intersection(biris)))
print(len(anna.difference(biris)))
print(*sorted(anna.difference(biris)))
print(len(biris.difference(anna)))
print(*sorted(biris.difference(anna)))