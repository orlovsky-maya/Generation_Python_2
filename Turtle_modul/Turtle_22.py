from turtle import *

colours = ('blue', 'black', 'red', 'yellow', 'green')
pensize(5)
X = -100
Y = 0
for i in range(3):
    pencolor(colours[i])
    penup()
    goto(X, Y)
    pendown()
    circle(50)
    X += 100
X = -50
Y = -48
for j in range(2):
    pencolor(colours[j + 3])
    penup()
    goto(X, Y)
    pendown()
    circle(50)
    X += 100


import turtle as t

pos = [[0, 0],[-62, 0],[62, 0],[-31,-40],[31,-40]]
cols = ["black","cyan","red","yellow","green"]
t.pensize(3)
for i in range(5):
  t.penup()
  t.goto(pos[i])
  t.pendown()
  t.color(cols[i])
  t.circle(30)