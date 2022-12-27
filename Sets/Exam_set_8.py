m = int(input())
n = int(input())
mat_set = {input() for i in range(m)}
inf_set = {input() for j in range(n)}
only_one = mat_set ^ inf_set
if len(only_one) > 0:
    print(len(only_one))
else:
    print('NO')


m, n = int(input()), int(input())
math = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
result = len(math ^ inf)

if result:
    print(result)
else:
    print('NO')