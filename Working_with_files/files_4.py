file = open('numbers.txt')
numbers = file.readlines()
print(int(numbers[0].rstrip()) + int(numbers[1].rstrip()))
file.close()

file = open('numbers.txt')

print(sum(map(int, file)))

file.close()
