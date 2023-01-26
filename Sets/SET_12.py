# number = int(input())
# all_num = set(range(1, number + 1))
# result_set = all_num
#
# while True:
#     attempt = input()
#     if attempt == 'HELP':
#         break
#     attempt = {int(num) for num in attempt.split()}
#     if len(attempt) == len(result_set) / 2:
#         print('NO')
#         result_set &= all_num - attempt
#     else:
#         temp_result_set_NO = result_set & all_num - attempt
#         temp_result_set_YES = result_set & attempt
#         if len(temp_result_set_NO) >= len(temp_result_set_YES):
#             print('NO')
#             result_set &= all_num - attempt
#         else:
#             print('YES')
#             result_set &= attempt
# print(*sorted(result_set))

n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible_nums & guess) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= guess
    else:
        print('NO')
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))