import turtle


def rectangle(width, height):
    for _ in range(2):
        turtle.dot(10)
        turtle.forward(height)
        turtle.dot(10)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)


w, h = int(input()), int(input())
rectangle(w, h)
