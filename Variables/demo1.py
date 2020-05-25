# convert Fahrenheit to centigrade degree

# F =1.8C+32

f = float(input('Type fahrenheit degree: '))
c = (f-32)/1.8
# place holder,%[(name)][flags][width].[precision] typecode + content

# flags          可选，可供选择的值有:
# +       右对齐；正数前加正好，负数前加负号；
# -        左对齐；正数前无符号，负数前加负号；
# 空格    右对齐；正数前加空格，负数前加负号；
# 0        右对齐；正数前无符号，负数前加负号；用0填充空白处
# width         可选，占有宽度
# .precision   可选，小数点后保留的位数
# typecode    必选
# s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
# r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
# c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
# o，将整数转换成八进制表示，并将其格式化到指定位置
# x，将整数转换成十六进制表示，并将其格式化到指定位置
# d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
# e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
# E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
# f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
# F，同上
# g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
# G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
# %，当字符串中存在格式化标志时，需要用 %%表示一个百分号

print('%.1f fahrenheit= %.3f centigrade' % (f, c))

