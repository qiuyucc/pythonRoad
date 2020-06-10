# def can_form_triangle(a, b, c):
#     print(f'a = {a}, b = {b}, c = {c}')
#     return a + b > c and b + c > a and a + c > b
#
#
# # 调用函数传入参数不指定参数名按位置对号入座
# print(can_form_triangle(1, 2, 3))
# # 调用函数通过“参数名=参数值”的形式按顺序传入参数
# print(can_form_triangle(a=1, b=2, c=3))
# # 调用函数通过“参数名=参数值”的形式不按顺序传入参数
# print(can_form_triangle(c=3, a=1, b=2))

# 调用函数时，如果希望函数的调用者必须以参数名=参数值的方式传参，可以用命名关键字参数取代位置参数。
# 所谓命名关键字参数，是在函数的参数列表中，写在*之后的参数
def can_form_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# print(is_valid_for_triangle(3, 4, 5))
# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_form_triangle(a=3, b=4, c=5))
print(can_form_triangle(c=5, b=4, a=3))


# *args并不能处理带参数名的参数。我们在设计函数时，如果既不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名
# 那么同时使用可变参数和关键字参数。关键字参数会将传入的带参数名的参数组装成一个字典，参数名就是字典中键值对的键，而参数值就是字典中键值对的值
def calc(*args, **kwargs):
    result = 0
    print(args, '\n', kwargs)
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc())  # 0
print(calc(1, 2, 3))  # 6
print(calc(a=1, b=2, c=3))  # 6
print(calc(1, 2, c=3, d=4))  # 10


# Advanced method
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# 其中init_value代表运算的初始值，op代表二元运算函数。经过改造的calc函数不仅仅可以实现多个参数的累加求和

def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))

# Python内置函数中有不少高阶函数，我们前面提到过的filter和map函数就是高阶函数，前者可以实现对序列中元素的过滤，
# 后者可以实现对序列中元素的映射，例如我们要去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表，
# 就可以直接使用这两个函数来做到
#
# def is_even(num):
#     return num % 2 == 0
#
#
# def square(num):
#     return num ** 2
#
#
# numbers1 = [35, 12, 8, 99, 60, 52]
# numbers2 = list(map(square, filter(is_even, numbers1)))
# print(numbers2)    # [144, 64, 3600, 2704]

# numbers1 = [35, 12, 8, 99, 60, 52]
# numbers2 = [x ** 2 for x in numbers1 if x % 2 == 0]
# print(numbers1)

# Lambda 函数 匿名函数
# lambda 参数 ： 函数本身
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)  # [144, 64, 3600, 2704]


def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# 调用calc函数，使用init_value和op的默认值
print(calc(1, 2, 3, x=4, y=5))  # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))  # 120

import operator, functools

# 一行代码定义求阶乘的函数
face = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5)) + 1))

print(face(10))
print(is_prime(9))

# Python中的函数可以使用可变参数*args和关键字参数**kwargs来接收任意数量的参数，而且传入参数时可以带上参数名也可以没有参数名，可变参数会被处理成一个元组，
# 而关键字参数会被处理成一个字典。Python中的函数也是对象，所以函数可以作为函数的参数和返回值，也就是说，
# 在Python中我们可以使用高阶函数。如果我们要定义的函数非常简单，只有一行代码且不需要名字，可以将函数写成Lambda函数（匿名函数）的形式。