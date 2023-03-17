list_numbers = [int(i) for i in input().split()]
counter = 1
for j in range(1, len(list_numbers)):
    if list_numbers[j] != list_numbers[j - 1]:
        counter += 1
print(counter)