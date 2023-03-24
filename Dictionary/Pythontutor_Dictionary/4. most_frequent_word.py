n = int(input())
medict = {}
for i in range(n):
    text = input().split()
    for word in text:
        medict[word] = medict.get(word, 0) + 1

largest = 0
result_word = ''
for key, value in medict.items():
    if value > largest:
        largest = value
        result_word = key
    elif value == largest:
        if key < result_word:
            result_word = key
print(result_word)

#  reference solution
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))