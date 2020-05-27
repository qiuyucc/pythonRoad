def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()

    # 在bar函数的内部并没有定义a和b两个变量，那么a和b是从哪里来的。
    # 我们在上面代码的if分支中定义了一个变量a，这是一个全局变量（global variable），属于全局作用域，因为它没有定义在任何一个函数中。
    # 在上面的foo函数中我们定义了变量b，这是一个定义在函数中的局部变量（localvariable），属于局部作用域，
    # 在foo函数的外部并不能访问到它；但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的。bar函数中的变量c属于局部作用域，
    # 在bar函数之外是无法访问的。
    # 事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些隐含标识符min、len等都属于内置作用域）。