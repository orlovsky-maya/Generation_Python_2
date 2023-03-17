n = int(input())
converted_n = []
counter = 0
while n != 0:
    last_digit = n % 10
    counter += 1
    converted_n.append(last_digit)
    if counter == 3:
        converted_n.append(',')
        counter -= 3
    n //= 10
if converted_n[-1] == ',':
    del converted_n[-1]
converted_n.reverse()
print(* converted_n, sep='')

# better solution

# num = input()
# for idx in range(len(num) - 3, 0, -3):
#     num = num[:idx] + ',' + num[idx:]
# print(num)

# print(f'{int(input()):,}')
#
# a = int(input())
# print(f'{a:,}')