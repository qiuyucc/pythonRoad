def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

print(fac(5))

# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120

# 函数调用会通过内存中称为“栈”（stack）的数据结构来保存当前代码的执行现场，函数调用结束后会通过这个栈结构恢复之前的执行现场。
# 栈是一种先进后出的数据结构，这也就意味着最早入栈的函数最后才会返回，而最后入栈的函数会最先返回。
# 例如调用一个名为a的函数，函数a的执行体中又调用了函数b，函数b的执行体中又调用了函数c，那么最先入栈的函数是a，最先出栈的函数是c。
# 每进入一个函数调用，栈就会增加一层栈帧（stack frame），栈帧就是我们刚才提到的保存当前代码执行现场的结构；
# 每当函数调用结束后，栈就会减少一层栈帧。通常，内存中的栈空间很小，因此递归调用的次数如果太多，会导致栈溢出（stack overflow），
# 所以递归调用一定要确保能够快速收敛。我们可以尝试执行fac(5000)，看看是不是会提示RecursionError错误，
# 错误消息为：maximum recursion depth exceeded in comparison（超出最大递归深度），其实就是发生了栈溢出。

# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)



def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# 打印前20个斐波那契数
for i in range(1, 21):
    print(fib(i))



