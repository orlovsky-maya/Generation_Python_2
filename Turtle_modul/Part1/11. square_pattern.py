import turtle


def square(side):
    for _ in range(4):
        turtle.backward(side)
        turtle.right(90)


s = 300
for _ in range(30):
    square(s)
    s -= 10


#  reference solution
import turtle
def squares(side, n, step):
    for _ in range(n):
        side += step
        for _ in range(4):
            turtle.left(90)
            turtle.forward(side)
side = int(input('Введите длину стороны квадрата:\n'))
n = int(input('Введите количество квадратов:\n'))
step = int(input('Введите шаг:\n'))
squares(side, n, step)