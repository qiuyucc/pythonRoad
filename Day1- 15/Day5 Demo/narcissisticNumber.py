# 水仙花数
# narcissistic number

number = int(input('Type your number: '))
s = str(number)
sum_num = 0
for i in s:
    print('char at ', i)
    sum_num += int(i) ** 3
if sum_num == number:
    print('%d is a narcissistic number' % number)
