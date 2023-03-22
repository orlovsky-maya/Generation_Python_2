import turtle


def rhombus(side):
    angle = 15
    for _ in range(10):
        turtle.setheading(angle)
        for _ in range(2):
            turtle.forward(side)
            turtle.left(60)
            turtle.forward(side)
            turtle.left(120)
        angle += 35


rhombus(100)
