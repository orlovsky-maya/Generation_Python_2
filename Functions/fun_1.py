def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]


print(matrix(3, 4, 9))