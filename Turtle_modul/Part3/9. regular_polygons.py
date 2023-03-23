from turtle import *
from random import *
from math import *

Screen().colormode(255)
Screen().setup(680, 420)


def form(count, angl, length, colour):
    pencolor(colour)
    fillcolor(colour)
    begin_fill()
    for _ in range(count):
        forward(length)
        right(angl)
    end_fill()


s = 200
x, y = -325, 325
for _ in range(5):
    for _ in range(5):
        count_angel = randrange(3, 8)
        angle = 360 / count_angel
        side = sqrt(s * 4 * tan(radians(180) / count_angel))
        color = randrange(256), randrange(256), randrange(256)
        penup()
        goto(x, y)
        form(count_angel, angle, side, color)
        x += 70
    x = -325
    y -= 70

done()

#  reference solution
from turtle import *
from random import *
from math import *

Screen().colormode(255)
Screen().setup(680, 420)

speed(0)
def form(count, angl, length, colour):
    pencolor(colour)
    fillcolor(colour)
    begin_fill()
    for _ in range(count):
        forward(length)
        right(angl)
    end_fill()


s = 400
x, y = -200, 200
for _ in range(5):
    for _ in range(5):
        count_angel = randrange(3, 8)
        angle = 360 / count_angel
        side = sqrt(s * 4 * tan(radians(180) / count_angel))
        color = randrange(256), randrange(256), randrange(256)
        penup()
        goto(x, y)
        form(count_angel, angle, side, color)
        x += 70
    x = -200
    y -= 70

done()
