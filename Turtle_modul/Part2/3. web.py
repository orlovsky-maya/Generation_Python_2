from turtle import *


def web(count, side):
    angle = 0
    dot(10)
    shape('arrow')
    for _ in range(count):
        setheading(angle)
        forward(side)
        stamp()
        backward(side)
        angle += 360 // count


n, s = int(input()), int(input())
web(n, s)
