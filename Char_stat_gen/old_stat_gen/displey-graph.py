from turtle import *

with open('teg_sum_stats', 'r') as f:
    stats = f.read()
    sum_stat = stats.split()

dic = {}
for i in range(50):
    dic[i] = 0

for char in sum_stat:
    char = int(char)
    char -=50
    dic[char] +=1

print(dic)


down()
for key in dic.keys():
    down()
    value = dic[key] // 1000
    goto(key, value)
# for stat in sum_stat:
#     stat = (int(stat) -50)*20 - 100
#     goto(x, stat)
#     x +=1

mainloop()