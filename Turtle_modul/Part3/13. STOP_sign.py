from turtle import *


def angle_7(size, pen_size, colour):
    pensize(pen_size)
    fillcolor(colour)
    begin_fill()
    for _ in range(8):
        forward(size)
        left(45)
    end_fill()


angle_7(90, 4, 'white')
penup()
goto(5, 11)
angle_7(80, 0, 'red')

hideturtle()
penup()
goto(-43, 60)
pencolor('white')
write('STOP', align='left', font=('Arial', 50, 'bold'))
done()


#  reference solution
from turtle import *


def angle_7(size, pen_size, colour):
    pensize(pen_size)
    fillcolor(colour)
    begin_fill()
    for _ in range(8):
        forward(size)
        left(45)
    end_fill()

speed(8)
angle_7(90, 4, 'white')
penup()
goto(5, 11)
angle_7(80, 0, 'red')

hideturtle()
penup()
goto(-50, 80)
fillcolor('white')
write('STOP', align='left', font=('Arial', 44, 'bold'))
done()
