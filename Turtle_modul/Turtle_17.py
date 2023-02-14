from turtle import *


def circle_turtle(count, side):
    shape('turtle')
    stamp()

    for _ in range(count):
        penup()
        forward(side)
        stamp()
        backward(20)
        pendown()
        backward(30)
        penup()
        backward(side - 50)
        left(360 // count)


n, s = int(input()), int(input())
circle_turtle(n, s)