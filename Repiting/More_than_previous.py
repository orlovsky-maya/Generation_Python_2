list_of_numbers = [int(i) for i in input().split()]
counter = 0
j = 0
while j < len(list_of_numbers) - 1:
    if list_of_numbers[j] < list_of_numbers[j + 1]:
        counter += 1
    j += 1
print(counter)
