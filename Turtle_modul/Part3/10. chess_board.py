from turtle import *

Screen().setup(680, 420)
speed(0)

def square(side, colour):
    fillcolor(colour)
    begin_fill()
    for _ in range(4):
        forward(side)
        left(90)
    end_fill()


penup()
goto(-250, -250)
pendown()
square(500, 'white')

s = 100
x, y = -250, -250

for _ in range(3):
    for _ in range(3):
        penup()
        goto(x, y)
        pendown()
        square(s, 'black')
        x += 200
    x = -250
    y += 200

x, y = -150, -150

for _ in range(2):
    for _ in range(2):
        penup()
        goto(x, y)
        pendown()
        square(s, 'black')
        x += 200
    x = -150
    y += 200
done()
