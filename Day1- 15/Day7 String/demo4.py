# def for return the biggest and the scond biggest number in the list


import random


def returnNumber(list):
    max1, max2 = 0, 0
    for number in list:
        if number > max1:
            max1 = number
        elif max2 < number < max1:
            max2 = number
        else:
            continue
    return max1, max2


if __name__ == '__main__':
    list = (random.randint(1, 100) for x in range(1, 50))
print('the biggest number:%d , the second biggest number: %d' % returnNumber(list))
