from turtle import *


def draw_circle(k=1, degc=15, deg=12, f=6):
    down()
    speed(0)
    for i in range(degc):
        left(deg * k)
        forward(f)
    speed(10)

def penis(x, y, size = 1, p_len = 150):
    speed(10)
    up()
    goto(x, y)
    draw_circle()
    forward(150)
    draw_circle()
    forward(150)
    left(90)
    forward(58)
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
    left(180)
    up()



