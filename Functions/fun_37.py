number_ip = list(map(str, input().split('.')))
number_ip_digit = list(filter(lambda x: x.isdigit(), number_ip))

if len(number_ip_digit) == 4:
    print(all(map(lambda x: True if int(x) <= 255 else False, number_ip_digit)))
else:
    print(False)


print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, input().split('.'))))