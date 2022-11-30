list_of_numbers = [i for i in input().split()]
j = 0
while j < len(list_of_numbers) - 1:
    list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
    j += 2
print(* list_of_numbers)
