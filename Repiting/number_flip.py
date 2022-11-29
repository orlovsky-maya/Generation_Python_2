number = input()
if len(number) == 5:
    print(int(number[::-1]))
if len(number) == 6:
    print(int(number[0] + number[6:0:-1]))