list_numbers = [int(input()) for _ in range(int(input()))]
prod_number = int(input())
flag = False
for i in range(len(list_numbers)):
    for j in range(i + 1, len(list_numbers)):
        if list_numbers[i] * list_numbers[j] == prod_number:
            flag = True
            break
if flag is True:
    print('ДА')
else:
    print('НЕТ')
