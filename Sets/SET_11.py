# number = int(input())
#
# attempt = set([num for num in input().split()])
# result_set = attempt
# while attempt != {'HELP'}:
#     answer = input()
#     if answer == "YES":
#         result_set.intersection_update(attempt)
#     else:
#         result_set.difference_update(attempt)
#     attempt = set([num for num in input().split()])
# print(*sorted(result_set))


n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))
