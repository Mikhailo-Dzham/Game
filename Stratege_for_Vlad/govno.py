from turtle import *
import random


def trade_ai(n):
    k = random.randint(-5, 12)
    n = n + (n * k) / 100
    return n


def draw_circle(k = 1):
    down()
    speed(100)
    for i in range(45):
        left(4 * k)
        forward(2)
    speed(1)

def statege():
    up()
    goto(-130, -230)
    draw_circle()
    forward(150)
    draw_circle()
    forward(150)
    left(90)
    forward(60)
    up()
    left(180)
    forward(30)
    left(90)
    forward(15)
    down()
    forward(15)
    up()
    left(180)
    forward(230)
    draw_circle()
    draw_circle()
    draw_circle(-1)
    draw_circle(-1)




up()
goto(-100, -200)
down()
p = 1
x = -100
for i in range(200):
    p = trade_ai(p)
    goto(x, p - 200)
    x += 1
statege()


mainloop()

