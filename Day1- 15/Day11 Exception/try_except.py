# try代码块后面可以跟上一个或者多个except来捕捉可能出现的异常状况。 例如在上面读取文件的过程中。

# 。例如在上面读取文件的过程中，文件找不到会引发FileNotFoundError，指定了未知的编码会引发LookupError，
# 而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，我们在try后面跟上了三个except分别处理这三种不同的异常状况。
# 最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，由于finally块的代码不论程序正常还是异常都会执行到
# （甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常）
# 因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作
# 如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

def main():
    try:
        with open('树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('cunt open file')
    except LookupError:
        print('unknown encoding')
    except UnicodeDecodeError:
        print('read file wrong')


if __name__ == '__main__':
    main()
