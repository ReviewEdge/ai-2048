import random


def get_move():
    m = random.randint(0,3)

    if m==0:
        return "w"
    elif m==1:
        return "a"
    elif m==2:
        return "s"
    return "d"