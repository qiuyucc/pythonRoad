# check 3 input number can form a trangile or not, if then caculate the area

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and a + c > b:
    print('The perimeter for the circle is: ', a + b + c)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Area: %f' % (area))
else:
    print('it is not a triangle')
