# read method
# use for-in loop or realines  to read file

import time


def main():
    # read the whole document
    with open('树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # for-in
    with open('树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # read file by line and store them into a list
    with open('树.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
