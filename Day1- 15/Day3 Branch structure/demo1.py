# convert inch with celimeter

value = float(input('type the length: '))
unit = input('type the unit: ')
if unit == 'cm':
    print('%.1f cm = %.1f inch' % (value, value / 2.54))
elif unit == 'inch':
    print('%.1f inch = %.1f cm' % (value, value * 2.54))
else:
    print('please type the right unit!')
