# String usage

def main():
    str1 = 'hello, world!'
    # len function to get the length of str1
    print(len(str1))

    # capitalize the string
    print(str1.capitalize())

    # uppercase all the letter
    print(str1.upper())

    # find the position of specific text
    print(str1.find('or'))
    print(str1.find('shit'))
    # find the index of specific text, if can not find, show error
    print(str1.index('or'))
    # print(str1.index('shit'))

    # check if the text starts at specific text
    print(str1.startswith('He'))  # false
    print(str1.startswith('hel'))  # true
    # check if string end with
    print(str1.endswith('!'))
    # put string in center with specific width and fill specific character
    print(str1.center(80, '*'))
    # fill specific character on right side
    print(str1.rjust(50, '$'))

    # the first index:0, the index of the last element is -1
    str2 = 'abc123456'
    print(str2[2])

    print(str2[2:5])
    print(str2[2:])
    # from 2 to end, get 2,4,6...
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])  # reverse
    print(str2[-3:-1])

    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


#
# string[:]  # 提取从开头到结尾的整个字符串
#
# string[start:]  # 从start提取到结尾
#
# string[:end]  # 从开头提取到end - 1
#
# string[start:end]  # 从start提取到end - 1
#
# string[::step]  # 每step个字符提取一个
#
# string[start::step]  # 从start开始到结尾，每step个字符提取一个
#
# string[:end:step]  # 从开始到end - 1，每step个字符提取一个
#
# string[start:end:step]  # 从start提取到end - 1，每step个字符提取一个

if __name__ == '__main__':
    main()
