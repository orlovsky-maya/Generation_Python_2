from turtle import *

def circle_turtle(count, side):
    shape('turtle')
    stamp()

    for _ in range(count):
        penup()
        forward(side)
        stamp()
        backward(side)
        left(360 // count)


n, s = int(input()), int(input())
circle_turtle(n, s)