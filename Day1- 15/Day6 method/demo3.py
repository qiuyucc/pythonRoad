#实现计算求最大公约数和最小公倍数的函数。

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False