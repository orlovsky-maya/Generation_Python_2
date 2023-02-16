from turtle import *

for _ in range(3):
    forward(100)
    left(120)


coord = ((50, -30), (100, 70), (0, 70))

pencolor('white')
fillcolor('white')
begin_fill()

for i in range(3):
    penup()
    goto(coord[i])
    pendown()
    dot(30, 'black')
goto(50, -30)
end_fill()


