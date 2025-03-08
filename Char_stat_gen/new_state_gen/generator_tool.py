import random


def randominus(a=50, start=10) -> int:  # Видає характериcтику
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
    with open('last_id.txt', 'r') as f:
        _id = str(format(int(f.read(), 16) + 1, 'x'))
        _id = '0' * (16 - len(_id)) + _id
    with open('last_id.txt', 'w') as f:
        f.write(_id)
    return _id

#######################################################################################################################
if __name__ is '__main__':
    pass
