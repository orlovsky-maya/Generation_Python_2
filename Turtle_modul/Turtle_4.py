import turtle


def square(side):
    angle = 0
    for _ in range(8):
        turtle.setheading(angle)
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        angle += 45


square(int(input()))

