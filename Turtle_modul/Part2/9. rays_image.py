from turtle import *

Screen().setup(640, 480)
pencolor('red')
dot(10)
X = 200
for i in range(10):
    goto(X, -200)
    pencolor('SteelBlue')
    dot(10)
    pencolor('aquamarine')
    goto(0, 0)
    X -= 40
