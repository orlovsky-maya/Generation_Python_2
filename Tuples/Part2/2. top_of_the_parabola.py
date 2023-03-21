def coord_parabola(a, b, c):
    first_coord = b / - (2 * a)
    second_coord = (4 * a * c - (b ** 2)) / (4 * a)
    return first_coord, second_coord


a, b, c, = int(input()), int(input()), int(input())
print(coord_parabola(a, b, c))
