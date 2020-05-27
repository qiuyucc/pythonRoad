from random import randint


def roll_dice(n=2):
    """

    :param n: number of dices
    :return: sum of dices
    """

    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

print('\n')
print('\n')
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数

def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(2))
print(add(1, 2))
print(add(3))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))