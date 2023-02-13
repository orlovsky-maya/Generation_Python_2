n, z_1, z_2 = int(input()), complex(input()), complex(input())
print(z_1 ** n + z_2 ** n + z_1.conjugate() ** n + z_2.conjugate() ** (n + 1))
