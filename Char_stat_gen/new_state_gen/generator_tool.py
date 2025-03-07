import random


def randominus(a=50, start=10) -> int:  # Видає характеритику
    finish = start
    a = 100 // a - 1
    while True:
        r = random.randint(0, a)
        if r == 1:
            finish += 1
        else:
            break
    return finish


def id_generator():
    with open('history_id', 'r') as f:
        f = f.read()



#######################################################################################################################
if __name__ is '__main__':
    pass
