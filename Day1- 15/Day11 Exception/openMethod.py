# open method python
# 通过Python内置的open函数，我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象

# r- read by default
# w- write 先截断以前的内容
# x -写入，如果文件已经存在会产生异常
# a -追加，将内容写在已有文件的末端
# b - 二进制模式
# t - 文本模式（默认）
# + 更新(既可以读 又可以写）

# 读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），
# 然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码），
# 如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败。

# def main():
#     f = open('树.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()
#
#


# 如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。
# 为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理，
def main():
    f = None
    try:
        f = open('树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
