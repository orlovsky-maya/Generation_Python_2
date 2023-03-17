s = input()
counter_max = 0
counter_tails = 0
for i in range(len(s)):
    if s[i] == 'Р':
        counter_tails += 1
    else:
        if counter_max < counter_tails:
            counter_max = counter_tails
        counter_tails = 0
if counter_max < counter_tails:
    counter_max = counter_tails
print(counter_max)

# better solution

# s = input().split('О')
# print(len(max(s)))