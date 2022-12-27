m = int(input())
myset = {input() for _ in range(int(input()))}
for i in range(m - 1):
    myset_next = {input() for _ in range(int(input()))}
    myset &= myset_next
print(*sorted(myset), sep='\n')


# s = set()
# s_2 = {1, 2, 3}
# print(s_2 & s)