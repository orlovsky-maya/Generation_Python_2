from turtle import *
def builds(size):
    width, height = size
    pencolor('Blue')
    fillcolor('Blue')
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
builds((70, 300))