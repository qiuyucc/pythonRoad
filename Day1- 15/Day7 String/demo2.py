#

import random


def generate_code(n):
    """
       生成指定长度的验证码

       :param code_len: 验证码的长度(默认4个字符)

       :return: 由大小写英文字母和数字构成的随机验证码
    """

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''

    for _ in range(n):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    number = random.randint(3, 10)
    print(number)
    print( generate_code(number))
