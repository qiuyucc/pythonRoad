# for-in loop
# iteration in a collection

sum = 0
for x in range(101):
    sum += x
print(sum)

# range(101)可以产生一个0到100的整数序列。
# range(1, 100)可以产生一个1到99的整数序列。
# range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

# sum even number 1-100

sum2 = 0
for x in range(2, 101, 2):
    sum2 += x
print(sum2)

# second way
sum3 = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum3 += x
print(sum3)
