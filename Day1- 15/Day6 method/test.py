# python 中没有函数重载的概念
# 那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的


# from module1 import foo
#
# # 输出hello, world!
# foo()
#
# from module2 import foo
#
# # 输出goodbye, world!
# foo()

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
import module3