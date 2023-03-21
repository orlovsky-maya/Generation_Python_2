text = input().split()
answer = 'YES'
for i in range(1, len(text)):
    if set(text[i]) != set(text[i - 1]):
        answer = 'NO'
        break
print(answer)

a, b, c = input().split()
print(['NO', "YES"][set(a) == set(b) == set(c)])