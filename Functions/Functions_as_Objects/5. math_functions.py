from math import *


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def root(num):
    return sqrt(num)


def modulus(num):
    return abs(num)


def sine(num):
    sin(num)


commands = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': modulus, 'синус': sin}
n = int(input())
com = input()
print(commands[com](n))

#  reference solution
import math

def pwr(p):
  def numpower(n):
    return n**p
  return numpower

commands = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), "модуль": abs, "синус": math.sin}

n = int(input())
command = input()
print(commands[command](n))