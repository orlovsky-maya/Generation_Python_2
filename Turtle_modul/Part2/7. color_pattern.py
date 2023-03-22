from turtle import *

colours = ('green', 'BlueViolet', 'orange', 'red', 'blue', 'yellow')
size = 1
step = 2
for i in range(6):
    for j in range(6):
        pensize(size)
        pencolor(colours[j])
        left(45)
        forward(step)
        step += 2
    size += 2

#  reference solution
colours = ((0, 0, 255), (255, 255, 0), (0, 134, 0), (166, 0, 128), (246, 182, 0), (234, 0, 0))

from turtle import *
colours = ('blue', 'yellow', 'green', 'BlueViolet', 'orange', 'red')

size = 1
step = 2
for i in range(8):
    for j in range(6):
        pensize(size)
        pencolor(colours[j])
        left(45)
        forward(step)
        step += 2
    size += 2

#  reference solution
from turtle import *

length, width = 10, 0.5
colors = ('blue', 'yellow', 'green', 'purple', 'orange', 'red')

for i in range(44):
  pencolor(colors[i % 6])
  pensize(width)
  left(45)
  forward(length)
  length += 2.7
  width += 0.7

#  reference solution

from turtle import *
colours = ('blue', 'yellow', 'green', 'BlueViolet', 'orange', 'red')

size = 1
step = 1
pensize(size)
pencolor(colours[step])
forward(step)

for i in range(7):
    for j in range(6):
        pensize(size)
        pencolor(colours[j])
        left(45)
        forward(step)
        step += 0.7
    size += 0.7
