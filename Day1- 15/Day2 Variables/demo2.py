# caculate perimeter and prportion of circle by radius

import math

radius = float(input("Input the radius: "))
perimeter = math.pi * 2 * radius
area = math.pi * radius * radius
print('perimeter: %.1f' % perimeter)
print('area: %.1f' % area)