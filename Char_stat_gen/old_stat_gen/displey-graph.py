from turtle import *

with open('teg_sum_stats', 'r') as f:
    stats = f.read()
    sum_stat = stats.split()

up()
goto((-100), 0)
down()
x = -100
for stat in sum_stat:
    stat = (int(stat) -50)*20 - 100
    goto(x, stat)
    x +=1

