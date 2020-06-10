# 元组也是多个元素按照一定的顺序构成的序列。元组和列表的不同之处在于，元组是不可变类型，
# 这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。

# define a tuple
t1 = (30, 10, 55)

t2 = ('Brook', 40, True, '四川成都')

# check the tuple type
print(type(t1), type(t2))

print(len(t1), len(t2))

# index search
print(t1[0], t1[-3])
print(t2[3], t2[-1])

for member in t2:
    print(member)

print(100 in t1)
print(40 in t2)

t3 = t1 + t2
print(t3)

# 切片
print(t3[::3])
# compare operator
print(t1 == t2)
print(t1 >= t3)
print(t1 < (30, 11, 55))

# 一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。
# 需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号
# ，所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。我们可以通过下面的代码来加以验证。

# 空元组
a = ()
print(type(a))  # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
# 一元组
d = ('hello',)
print(type(d))  # <class 'tuple'>
e = (100,)
print(type(e))  # <class 'tuple'>

# tuple application
# ：打包和解包操作
a = 1, 10, 100
print(type(a), a)
i, j, k = a
#在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常，
# 错误信息为：too many values to unpack（解包的值太多）或not enough values to unpack（解包的值不足）。
print(i, j, k)

#有一种解决变量个数少于元素的个数方法，就是使用星号表达式，我们之前讲函数的可变参数时使用过星号表达式。有了星号表达式，我们就可以让一个变量接收多个值，
# 代码如下所示。需要注意的是，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。还有在解包语法中，星号表达式只能出现一次。

a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)          # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)          # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)          # [1, 10] 100 1000
*i, j = a
print(i, j)             # [1, 10, 100] 1000
i, *j = a
print(i, j)             # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)       # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)    # 1 10 100 1000 []

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

#现在我们可以反过来思考一下函数的可变参数，可变参数其实就是将多个参数打包成了一个元组
def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    return total


add(1, 10, 20)        # <class 'tuple'> (1, 10, 20)
add(1, 2, 3, 4, 5)


#让函数返回多个值
def find_max_and_min(items):
    """找出列表中最大和最小的元素
    :param items: 列表
    :return: 最大和最小元素构成的二元组
    """
    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one, min_one