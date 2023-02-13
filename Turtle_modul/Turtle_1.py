import turtle


def rectangle(width, height):
    for _ in range(2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)


w, h = 50, 150
rectangle(w, h)


