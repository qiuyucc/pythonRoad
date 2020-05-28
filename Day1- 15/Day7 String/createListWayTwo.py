# creat list by different statement

import sys


def main():
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    f = [x ** 2 for x in range(1, 10000)]
    print(sys.getsizeof(f))  # check memory comsumtion for this varible
    print(f)
    #generate variable to store value,
    # use generator to get value, it won't take much memory space
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
