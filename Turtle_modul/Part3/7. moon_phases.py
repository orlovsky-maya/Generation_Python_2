from turtle import *

Screen().setup(640, 480)
Screen().bgcolor('Blue')
pencolor('Blue')
hideturtle()

turtle_orange = Turtle()
turtle_orange.hideturtle()
turtle_orange.dot(200, 'orange')

turtle_blue = Turtle()
turtle_blue.hideturtle()
turtle_blue.penup()

for i in range(200, -201, -1):
    turtle_blue.goto(i, 0)
    turtle_blue.dot(200, 'Blue')
    turtle_blue.speed(5)
    tracer(3, 30)
    turtle_blue.clear()

done()
