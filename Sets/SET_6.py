n = int(input())
union = set()
for i in range(n):
    stroka = set(input().split())
    union |= stroka
print(len(union))


# words = set()
# for _ in range(int(input())):
#     words.update(input().split())
# print(len(words))