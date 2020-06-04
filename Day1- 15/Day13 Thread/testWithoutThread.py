# sum 1~100000000

from time import time


def main():
    total = 0
    number_lists = [x for x in range(1, 100000001)]
    start = time()
    for number in number_lists:
        total += number
    end = time()
    print('Execution Time: %.2f second' % (end - start))


if __name__ == '__main__':
    main()
