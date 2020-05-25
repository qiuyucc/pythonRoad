# calculate if the input year is leap year or not

year = int(input('Input the year: '))

print("This year is leap year [True or false]: ", (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
