n, m, k, p = [int(input()) for _ in range(4)]
answer = n - ((m - p) + (k - p) + p)
print(answer)