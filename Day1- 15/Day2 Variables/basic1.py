# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


# int()：将一个数值或字符串转换成整数，可以指定进制。
# float()：将一个字符串转换成浮点数。
# str()：将指定的对象转换成字符串形式，可以指定编码。
# chr()：将整数转换成该编码对应的字符串（一个字符）。
# ord()：将字符串（一个字符）转换成对应的编码（整数）。

#use input() to get input from keyboard
#use int() to convert datatype

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

#Using operator
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
print("a = ", a)
a -= c
print("a = ", a)
a *= d
print("a = ", a)
a /= e
print("a = ", a)

flag1 = 3>2
flag2 = 2<1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1

print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)