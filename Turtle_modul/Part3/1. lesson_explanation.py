# Создание нескольких черепашек

import turtle
turtle.Screen().bgcolor('yellow')  #  устанавливаем цвет фона

tim = turtle.Turtle()    # создаем первую черепашку и устанавливаем ее свойства
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)


alex = turtle.Turtle()    # создаем вторую черепашку и устанавливаем ее свойства
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

# Черепашек можно сохранить в списке, а затем в цикле обрабатывать его.


import turtle
from random import randrange

def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turt.tracer(25, 0)
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)


# Отслеживание нажатия клавиш

import turtle


def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + 5)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - 5)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - 5, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + 5, y)


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.shape('turtle')
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо


# Давайте теперь сделаем так, чтобы по нажатию на пробел черепашка скрывалась и переставала оставлять след.
# Также добавим возможность увеличивать скорость перемещения черепашки по нажатию на клавиши клавиатуры q и w.

import turtle

speed = 5


def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + speed)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - speed)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - speed, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + speed, y)


def change():  # функция обратного вызова
    if turtle.isvisible():
        turtle.up()
        turtle.hideturtle()
    else:
        turtle.down()
        turtle.showturtle()


def speed_increase():  # функция обратного вызова
    global speed
    speed += 1


def speed_decrease():  # функция обратного вызова
    global speed
    speed -= 1


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')


# Отслеживание нажатия мыши


import turtle
from random import randrange


def random_color():
  return randrange(256), randrange(256), randrange(256)



def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)



def left_mouse_click(x, y):
    draw_circle(x, y, 10)



turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()