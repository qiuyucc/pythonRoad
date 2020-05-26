# dice the number

from random import randint

face = randint(1, 6)
if face == 1:
    result = 'Singing a song'
elif face == 2:
    result = 'Dance'
elif face == 3:
    result = 'bark'
elif face == 4:
    result = 'push up'
else:
    result = 'joke'
print(result)
