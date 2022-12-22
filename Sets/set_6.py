first = {int(num) for num in input()}
second = {int(num) for num in input()}
answer = 'YES'
for i in range(10):
    if i not in first and i not in second:
        answer = "NO"
        break
print(answer)


print(('NO', 'YES')[len(set(input() + input())) == 10])