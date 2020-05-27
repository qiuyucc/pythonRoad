# Fibonacci Sequence

numMax = int(input('please input a maxnumber: '))

def flibsOne(numMax):
    c = []
    a, b = 0, 1
    while a < numMax:
        a, b = b, a + b
        c.append(a)
    c.remove(c[-1])
    print(c)
