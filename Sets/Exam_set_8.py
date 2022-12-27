m = int(input())
n = int(input())
mat_set = {input() for i in range(m)}
inf_set = {input() for j in range(n)}
only_one = mat_set ^ inf_set
if len(only_one) > 0:
    print(len(only_one))
else:
    print('NO')
