# while
# guess game from 1-100

# import random
#
# answer = random.randint(1, 100)
# counter = 0
# print(answer)
# while True:
#     counter += 1
#     number = int(input('please have a guess: '))
#     if number < answer:
#         print('guess bigger number')
#     elif number > answer:
#         print('guess smaller number')
#     else:
#         print('congraz')
#         break
# print('Total guess %d number' % counter)
# if counter > 7:
#     print('Bad perform')

# break, terminate this loop.
# continue,continue to next round.

# nested for loop
for i in range(1, 10):
    print(end='\n')
    for j in range(1, i + 1):
        print('%d * %d =%d' % (i, j, i * j), end='\t')
