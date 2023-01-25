# a = set(int(n) for n in input().split())
# b = set(int(n) for n in input().split())
#
# print(*sorted(a & b))


print(*sorted(set(int(n) for n in input().split()) & set(int(n) for n in input().split())))


