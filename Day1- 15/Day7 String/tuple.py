# tuple
# similiar with list, but tuple can not changed

def main():
    # define a tuples
    t = ('brook', 38, True, 'china')
    print(t)
    # get  elements in tuple
    print(t[0])
    print(t[3])

    # iterate all the value in tuple
    for member in t:
        print(member)

    # assign new value to tuple
    # t[0] = 'qiuyu' #typeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('de', 20, True, 'yunnai')
    print(t)
    # change tuple to list
    person = list(t)
    print(person)
    # list can change values
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # covert list to tuple
    fruiteList = ['number', 'number2', 'number3']
    tupleFruite = tuple(fruiteList)
    print(tupleFruite)


if __name__ == '__main__':
    main()

# 元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象
# （一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；
# 另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。
# 一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，
# 当然如果一个方法要返回多个值，使用元组也是不错的选择。

# 相对于列表，元祖所占用的内存小很多，import sys 去证明