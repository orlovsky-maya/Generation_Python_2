import turtle


def star_5(side):
    turtle.forward(side // 2)

    for _ in range(5):
        turtle.left(216)
        turtle.forward(side)


star_5(100)

#  reference solution
from turtle import *
for _ in range(5):
    right(144)
    forward(100)
done()
