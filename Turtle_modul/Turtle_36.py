from turtle import *
Screen().setup(680, 450)

names = ('Солнце', 'Меркурий', 'Венера', 'Земля', 'Марс', 'Юптер', 'Сатурн', 'Уран', 'Нептун', 'Плутон')
colours = ('light yellow', 'orange', 'orange', 'light green', 'red', 'orange', 'orange', 'light blue',
           'blue', 'orange')
size = (100, 30, 50, 30, 20, 70, 70, 65, 60, 10)
coord = ((-490, -100), (-350, -30), (-250, -50), (-150, -30), (-80, -20), (20, -70), (190, -70),
         (350, -65), (480, -60), (570, -10))
speed(10)
for i in range(10):
    penup()
    goto(coord[i])
    pendown()
    fillcolor(colours[i])
    begin_fill()
    circle(size[i])
    end_fill()

for j in range(len(coord)):
    x, y = coord[j]
    penup()
    goto(x, y - 20)
    write(names[j], align='center')

done()
