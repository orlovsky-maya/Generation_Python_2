import random
numbers = set()
while len(numbers) != 7:
    numbers.add(random.randint(1, 49))
print(*sorted(numbers))