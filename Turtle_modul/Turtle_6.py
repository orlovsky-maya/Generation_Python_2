import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)
        for _ in range(6):
            turtle.forward(side)
            turtle.left(60)


hexagon(50)
