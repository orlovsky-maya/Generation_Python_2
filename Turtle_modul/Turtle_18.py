# from turtle import *
#
#
# def turtle_snail(count):
#     shape('turtle')
#     penup()
#     Screen().bgcolor('LightGreen')
#
#     for i in range(1, count, 3):
#         forward(i)
#         right(30)
#         stamp()
#
#
# n = int(input())
# turtle_snail(n)


from turtle import *
Screen().bgcolor('LightGreen')
shape("turtle")
stamp()
for i in range(35):
  right(25)
  penup()
  forward(i)
  stamp()