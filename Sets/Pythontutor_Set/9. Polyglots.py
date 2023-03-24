n = int(input())
language_sets = [{input() for _ in range(int(input()))} for _ in range(n)]
result_set_1 = language_sets[0].copy()
result_set_2 = language_sets[0].copy()
for i in range(1, len(language_sets)):
    result_set_1 &= language_sets[i]
    result_set_2 |= language_sets[i]

print(len(result_set_1))
print(*sorted(result_set_1), sep='\n')
print(len(result_set_2))
print(*sorted(result_set_2), sep='\n')


#  reference solution
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')