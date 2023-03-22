from turtle import *

for i in range(2):
    circle(100 - i * 40)
for j in range(2):
    penup()
    goto(-45 + j * 90, 120)
    dot(20)
for k in range(2):
    penup()
    goto(-70 + k * 140, 180)
    pendown()
    circle(30)

penup()
goto(0, 10)
pendown()
goto(0, 80)
circle(10)