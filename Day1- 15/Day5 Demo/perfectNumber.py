# perfect number

number = int(input('Enter your number: '))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += i
if number == sum:
    print('The %d is perfect number ' % number)
else:
    print('The %d is not a perfect number ' % number)