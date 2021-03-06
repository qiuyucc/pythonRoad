# lottery demo

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 36)]
    selected_balls = []
    selected_balls = sample(red_balls, 7)
    #selected_balls.sort()
    selected_balls.append(randint(1, 20))
    return selected_balls


def main():
    n = int(input('How many set: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
