# regular expression

# https://github.com/qiuyucc/Python-100-Days/blob/master/Day01-15/12.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md''

import re


def main():
    username = input('type your username: ')
    password = input('type your number:')

    m1 = re.match(r'^\w{6,20}$', username)
    if not m1:
        print('please type right username')

    m2 = re.match(r'^[1-9]\d{4,11}$', password)
    if not m2:
        print('please type right password')
    if m1 and m2:
        print('successfully')


if __name__ == '__main__':
    main()
