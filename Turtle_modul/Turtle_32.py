from turtle import *
from random import *


def star_5(side, col):
    pencolor(col)
    fillcolor(col)
    begin_fill()
    for _ in range(5):
        right(144)
        forward(side)
    end_fill()


speed(0)
Screen().colormode(255)
for i in range(200):
    coord = randrange(-200, 200), randrange(-200, 200)
    colour = randrange(256), randrange(256), randrange(256)
    size = randrange(10, 50)
    penup()
    goto(randrange(-200, 200), randrange(-200, 200))
    pendown()
    star_5(size, colour)
done()

