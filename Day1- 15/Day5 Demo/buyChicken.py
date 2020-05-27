# bai ji bai qian
# female chicken 3 aud
# male chicken 5 aud
# little chicken 1 aud
# you now have 100 aud, how many female chicken, male chicken and little chicken you can buy

# female x, male y , little 100-x-y
# 3x+5y+ (100-x-y)/3 = 100
# 9x+15y+(100-x-y) =300   300-100+x+y
# x & y should be integer

for x in range(0, 100):
    for y in range(0, 100):
        if 14 * y + 8 * x - 200 == 0 and 100 - x - y >= 0:
            print('female chicken: ', x, 'male chicken: ', y, 'little: ', 100 - x - y)
