color = [int(i) for i in input().split()]
color_opposite = list(map(lambda color: 255 - color, color))

print(*color_opposite)