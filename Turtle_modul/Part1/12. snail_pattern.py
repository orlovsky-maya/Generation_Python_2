import turtle


def snail(side):
    for _ in range(24):
        turtle.left(90)
        turtle.forward(side)
        side += 15
        turtle.left(90)
        turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

snail(20)


#  reference solution
import turtle


def snail(side, count, st):
    for _ in range(n):
        turtle.left(90)
        turtle.forward(side)
        side += st
        turtle.left(90)
        turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


n = int(input())
s = int(input())
step = int(input())
snail(s, n, step)

#  reference solution

from turtle import *


def pyramid(side, n, s):
    for i in range(n):
        left(90)
        forward(side + i * s)


side, n, s = int(input('Наименьшая сторона:')), int(input('Количество витков:')), int(input('Шаг:'))

pyramid(side, n, s)

#  reference solution
import turtle as t
side = 10
for i in range(20):
  for j in range(2):
    t.left(90)
    t.forward(side)
  side += 10