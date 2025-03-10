from turtle import *

def trade_ai(n):
    k = random.randint(-5, 12)
    n = n + (n * k) / 100
    return n
def draw_lines():
    down()

    for i in range(500,-200,-100):
        goto(-100,i)
        goto(-110,i)
        write((i+200)*100000)
        goto(-90,i)

        goto(-100,i)
    for i in range(-100,600,100):
        goto(i,-200)
        goto(i, -210)
        write((i+200) * 100)
        goto(i, -190)
        goto(i, -200)

def draw_circle(k = 1):
    down()
    speed(1000)
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
    left(155)
    forward(45)

    write('Nastya Urus', font = ('Arial',24,'normal'))



up()
goto(-100, -200)
down()
p = 1
x = -100
draw_lines()
for i in range(200):
    p = trade_ai(p)
    goto(x, p - 200)
    x += 1
    if p > 500:
        break
statege()


mainloop()
