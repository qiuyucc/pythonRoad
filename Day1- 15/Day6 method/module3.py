def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__

# 作为脚本才会被执行，作为import 不可以被执行
# 可以理解为程序的主入口

if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
