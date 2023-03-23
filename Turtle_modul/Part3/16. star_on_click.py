from turtle import *
from random import *

Screen().bgcolor('black')
Screen().colormode(255)
Screen().setup(640, 480)

def random_size():
    return randrange(5, 40)
def random_count():
    return randrange(5, 14, 2)
def random_color():
    return (randrange(256), randrange(256), randrange(256))



def drown_star(x, y):
    size = random_size()
    count = random_count()
    color = random_color()
    penup()
    goto(x, y - count)
    pencolor(color)
    fillcolor(color)
    begin_fill()
    pendown()
    for _ in range(count):
        right(180 - 180 / count)
        forward(size)
    end_fill()


def mouse_click(x, y):
    drown_star(x, y)


hideturtle()
Screen().onclick(mouse_click)
Screen().listen()
done()
