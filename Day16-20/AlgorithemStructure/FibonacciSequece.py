# F(1)=1，F(2)=1, F(n)=F(n - 1)+F(n - 2)

"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""


def fib(num, temp={}):
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]




def fibonacci_tool(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_tool(n-1) + fibonacci_tool(n-2)

def fibonacci(n):
    result_list = []
    for i in range(1,n+1):result_list.append(fibonacci_tool(i))
    return result_list

print(fibonacci(12))