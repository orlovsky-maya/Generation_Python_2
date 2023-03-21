n = int(input())
numbers = [set(input()) for i in range(n)]
myset = numbers[0]
for i in range(1, n):
    myset = myset.intersection(numbers[i])

print(*sorted(myset))

#  reference solution
n = int(input())
numbers = [input() for _ in range(n)]

num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))