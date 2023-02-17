from turtle import *

Screen().setup(640, 480)
Screen().bgcolor('DarkBlue')
pencolor('DarkBlue')
penup()
goto(0, -100)
pendown()

fillcolor('orange')
begin_fill()
circle(150)
end_fill()

forward(40)
fillcolor('DarkBlue')
begin_fill()
circle(150)
end_fill()
