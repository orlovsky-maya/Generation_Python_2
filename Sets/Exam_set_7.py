m = int(input())
n = int(input())
mat_set = {input() for i in range(m)}
inf_set = {input() for j in range(n)}
only_mat = mat_set - inf_set
print(len(only_mat))