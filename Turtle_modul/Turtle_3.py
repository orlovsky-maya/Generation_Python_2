import turtle


def square(side):
    angle = 30
    for _ in range(3):
        turtle.setheading(angle)
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        angle += 15


square(int(input()))
