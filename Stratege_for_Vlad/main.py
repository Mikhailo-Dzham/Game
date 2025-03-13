import turtle
from turtle import *
from draw_lib import *
turtle.tracer(2, 10)
for x_main in range(-200, 401, 270):
    for y_main in range(300, -301, -120):
        penis(x_main, y_main)
        print(x_main,y_main)
turtle.update()




mainloop()