import turtle


def rhombus(side):
    for _ in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)


rhombus(int(input()))
