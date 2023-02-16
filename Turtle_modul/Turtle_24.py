from turtle import *
from random import *

Screen().setup(640, 480)
Screen().bgcolor('cyan')


def snowflake(size, colour, posit):
    step = size // 4
    pencolor(colour)
    x, y = posit
    angle = 0
    for i in range(8):
        left(angle)
        for j in range(3):
            forward(step)
            left(45)
            forward(step)
            backward(step)
            right(90)
            forward(step)
            backward(step)
            left(45)
        forward(step)
        goto(x, y)
        angle += 45


colors = ('red', 'green', 'blue', 'yellow', 'orange', 'violet', 'pink', 'black', 'brown')
coordinates = ((0, 0), (100, -100), (-100, 100), (100, 100), (-100, -100))
speed(0)
for k in range(5):
    penup()
    goto(coordinates[k])
    dot()
    pendown()
    snowflake(randrange(10, 150), choice(colors), coordinates[k])




