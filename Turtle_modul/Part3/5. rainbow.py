from turtle import *

colours = ('red', 'orange', 'yellow', 'green', 'light green', 'Cyan', 'RoyalBlue', 'blue', 'magenta', 'DeepPink')
speed(0)
hideturtle()
r = 200
x, y = 0, -200
for i in range(10):
    penup()
    goto(x, y)
    pendown()
    fillcolor(colours[i])
    begin_fill()
    circle(r)
    end_fill()
    y += 20
    r -= 20


