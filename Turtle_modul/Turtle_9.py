import turtle

def star(side):
    for _ in range(12):
        turtle.forward(side)
        turtle.backward(side)
        turtle.left(30)


star(100)