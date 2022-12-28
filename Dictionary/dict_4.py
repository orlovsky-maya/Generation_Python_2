# digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
#           9: 'nine'}
# num = [int(i) for i in input()]
# result = []
# for c in num:
#     result.append(digits[c])
# print(*result)

digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
          9: 'nine'}
num = [digits[int(i)] for i in input()]
print(*num)