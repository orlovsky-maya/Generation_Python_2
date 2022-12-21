n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
sea = n - x
village = m - x - y
mountain = k - y
result = sea + village + mountain + x + y + z
print(result)


n, m, k, x, y, z = [int(input()) for _ in range(6)]

print(n + m + k - x - y + z)