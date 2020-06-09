# 常见数据结构列表

# 我们先给大家一个编程任务，将一颗色子掷6000次，统计每个点数出现的次数。这个任务对大家来说应该是非常简单的，我们可以用1到6均匀分布的随机数来模拟掷色子，然后用6个变量分别记录每个点数出现的次数，

import random

# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0
# for _ in range(6000):
#     number = random.randint(1, 6)
#     if number == 1:
#         f1 += 1
#     elif number == 2:
#         f2 += 1
#     elif number == 3:
#         f3 += 1
#     elif number == 4:
#         f4 += 1
#     elif number == 5:
#         f5 += 1
#     else:
#         f6 += 1
#
# print(f'1点出现了{f1}次')
# print(f'2点出现了{f2}次')
# print(f'3点出现了{f3}次')
# print(f'4点出现了{f4}次')
# print(f'5点出现了{f5}次')
# print(f'6点出现了{f6}次')

items1 = [35, 12, 99, 68, 55, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
print(items1)
print(items2)

# 列表的运算符号
items3 = items1 + items2
print(items3)

# 列表的重复
items4 = ['hello'] * 3
print(items4)

# 列表的成员运算
print(100 in items3)
print('hello' in items4)

# 获取列表的长度
size = len(items3)
print(size)

# 列表的索引
print(items3[0], items3[-size])
items3[-1] = 100
print(items3[size - 1], items3[-1])

# 列表的切片
print(items3[:5])  # [35, 12, 99, 68, 55]
print(items3[4:])  # [55, 87, 45, 8, 100]
print(items3[-5:-7:-1])  # [55, 68]
print(items3[::-2])  # [100, 45, 55, 99, 35]

# 列表的比较运算
items5 = [1, 5, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)  # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)  # True

# 列表元素的遍历
# way1:
items = ['Python', 'Java', 'Go', 'Kotlin']
for index in range(len(items)):
    print(items[index])

# way2:
for item in items:
    print(item)

# 修改统计点数的代码

couters = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    couters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{couters[face - 1]}次')

# 列表的方法
# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)

items.insert(2, 'SQL')
print(items)

# delete the specific elements:
items.remove('Java')
print(items)
items.pop(0)
items.pop(len(items) - 1)
print(items)
# clear the list
items.clear()
print(items)
# 需要提醒大家，在使用remove方法删除元素时，如果要删除的元素并不在列表中，会引发ValueError异常，错误消息是：list.remove(x): x not in list。
# 在使用pop方法删除元素时，如果索引的值超出了范围，会引发IndexError异常，错误消息是：pop index out of range。

items10 = ['Python', 'Java', 'GO', 'Kotlin', 'Python']
del items10[1]
print(items10)

items6 = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
print(items6.index('Python'))
print(items6.index('Python', 2))
#print(items.index('Java', 3))      # ValueError: 'Java' is not in list

#查找元素出现的次数
print(items6.count('Python'))
print(items6.count('Go'))
print(items6.count('Swift'))

#元素的排列和反转
items6.sort()
print(items6)
items6.reverse()
print(items6)

# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)

# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

#嵌套列表
#嵌套的列表可以用来表示表格或数学上的矩阵，例如：我们想保存5个学生3门课程的成绩，可以定义一个保存5个元素的列表保存5个学生的信息，
# 而每个列表元素又是3个元素构成的列表，分别代表3门课程的成绩
socres = [[0]*3]*5
print(socres)
#如果输入第一个学生的第一个成绩
socres[0][0] = 95
print(socres) #发现列表里其他学生的第一个成绩也是95
##正确方法嵌套
right= [[0]*3 for _ in range(5)]
right[0][0] =95
print(right)

