from turtle import *
from math import *

t = 0
pencolor('red')
fillcolor('red')
begin_fill()
for _ in range(600):
    x = 128*sin(t)**3
    y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
    penup()
    goto(x, y)
    t += 0.01
end_fill()

done()