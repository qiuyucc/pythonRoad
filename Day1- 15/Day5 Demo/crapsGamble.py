# craps gamble python implmentation

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
sum_num = dice1 + dice2
print(dice1, ' ', dice2)
count = 0
game = True
while game:
    if count == 0:
        if sum_num == 7 or sum_num == 11:
            print('player win')
            break
        elif sum_num == 2 or sum_num == 3 or sum_num == 12:
            print('player lose')
            break
        else:
            count += 1
    else:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1, ' ', dice2)
        if dice1 + dice2 == sum_num:
            print('player win')
            break
        elif dice1 + dice2 == 7:
            print('player lose')
            break
        else:
            count += 1
