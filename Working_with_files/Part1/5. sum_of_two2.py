file = open('nums.txt')
result = file.read().split()
print(sum(map(int, result)))
file.close()