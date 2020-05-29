# exercise
# string come and go

import os
import time


def main():
    content = 'Welcome to python demo section....'
    while True:
        # clean terminal content
        os.system('cls')
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
