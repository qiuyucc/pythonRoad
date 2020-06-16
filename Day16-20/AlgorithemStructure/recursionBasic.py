import sys
from functools import lru_cache
# by default: the limitation of recursion for python is 1000

sys.setrecursionlimit(10000)
total = 0


def fac(num):
    if num == 0:
        return 1
    return num * fac(num - 1)

#
# def climb(num):
#     global total
#     if num == 0:
#         total += 1
#         return 1
#     elif num < 0:
#         return 0
#     else:
#         climb(num - 1)
#         climb(num - 2)
#         climb(num - 3)
#     return total
# 上面的递归函数性能会非常的差，因为时间复杂度是几何级数级的。
@lru_cache()
def climb(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    return climb(num - 1) + climb(num - 2) + climb(num - 3)

# sometimes we are unnecessary to use recursion
def climb2(num):
    a,b,c =1,2,4
    for _ in range(num-1):
        a,b,c = b,c,a+b+c
    return a

if __name__ == '__main__':
    print(fac(10))
    print(climb(10))
    print(climb2(4))
