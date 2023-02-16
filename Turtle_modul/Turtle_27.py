# from turtle import *
#
# begin_fill()
# for _ in range(2):
#     forward(60)
#     left(90)
#     forward(200)
#     left(90)
# end_fill()
#
# colours = ('green', 'yellow', 'red')
#
#
# def draw_circle(x, y, r, i):
#     penup()
#     goto(x, y)
#     pendown()
#     color = colours[i]
#     fillcolor(color)
#     begin_fill()
#     circle(r)
#     end_fill()
#     speed(0)
#
#
# x, y = 30, -40
#
# for i in range(3):
#     y += 60
#     draw_circle(x, y, 20, i)
#

from turtle import *

begin_fill()
for _ in range(2):
    forward(70)
    left(90)
    forward(200)
    left(90)
end_fill()

colours = ('green', 'yellow', 'red')

x, y = 35, 30

for i in range(3):
    penup()
    goto(x, y)
    pendown()
    colour = colours[i]
    fillcolor(colour)
    begin_fill()
    circle(20)
    end_fill()
    y += 60


