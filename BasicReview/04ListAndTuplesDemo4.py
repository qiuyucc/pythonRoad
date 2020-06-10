# lucky woman

# 有15个男人和15个女人乘船在海上遇险，为了让一部分人活下来，不得不将其中15个人扔到海里，有个人想了个办法让大家围成一个圈，
# 由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到将15个人扔到海里。
# 最后15个女人都幸免于难，15个男人都被扔到了海里。问这些人最开始是怎么站的，哪些位置是男人，哪些位置是女人。

person = [True] * 30
counter, index, number = 0, 0, 0
while counter <15:
    if person[index]:
        number += 1
        if number == 9:
            person[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30
for person in person:
    print('woman' if person else 'man', end=' ')
