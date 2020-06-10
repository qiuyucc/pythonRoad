"""
双色球随机选号

"""
from random import randint, sample


def display(red_ball):
    for index, ball in enumerate(red_ball):
        if index == len(red_ball) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()


def select_ball():
    ball_poll = [x for x in range(1, 34)]
    red_ball = sample(ball_poll, 6)
    red_ball.sort()
    red_ball.append(randint(1, 10))
    return red_ball


n = int(input('How many sets: '))
for _ in range(n):
    display(select_ball())
