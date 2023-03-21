num1 = set(input())
num2 = set(input())
if num1.isdisjoint(num2):
    print('NO')
else:
    print('YES')

#  reference solution
print(("YES", "NO")[set(input()).isdisjoint(input())])