from turtle import *


def draw_circle(k=1, degc=45, deg=4, f=2):
    down()
    speed(10)
    for i in range(degc):
        left(deg * k)
        forward(f)
    speed(1)

def penis(x, y):
    up()
    goto(x, y)
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
    left(155)
    forward(45)


if __name__ is '__main__':
    pass
