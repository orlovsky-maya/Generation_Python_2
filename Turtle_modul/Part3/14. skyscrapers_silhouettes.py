from turtle import *
from random import *

Screen().bgcolor('Dark Blue')
Screen().setup(640, 480)
speed(0)


def stars():
    for i in range(100):
        coord = randrange(-200, 200), randrange(-200, 200)
        size = randrange(1, 6)
        penup()
        goto(coord)
        pencolor('yellow')
        fillcolor('yellow')
        begin_fill()
        pendown()
        circle(size)
        end_fill()


def builds(size):
    width, height = size
    pencolor('Blue')
    fillcolor('Blue')
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def windows():
    pencolor('yellow')
    fillcolor('yellow')
    begin_fill()
    for _ in range(4):
        forward(20)
        left(90)
    end_fill()

#  reference solution
coord_build = ((-320, -250), (-240, -250), (-160, -250), (-10, -250), (60, -250), (140, -250),
               (200, -250), (270, -250), (340, -250))
size = ((80, 300), (80, 360), (150, 450), (70, 320), (80, 400), (60, 370), (70, 280), (50, 200))

stars()
for i in range(8):
    x, y = coord_build[i]
    penup()
    goto(x, y)
    pendown()
    builds(size[i])

coord_widow = ((-310, 10), (-150, 160), (-150, 120), (-50, 50), (-100, -100), (75, 40))

for j in range(6):
    penup()
    goto(coord_widow[j])
    pendown()
    windows()

done()
