list_numbers = [int(i) for i in input().split()]
list_numbers.insert(0, list_numbers[-1])
del list_numbers[-1]
print(* list_numbers)