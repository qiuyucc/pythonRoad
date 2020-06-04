# Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，
# 但是子进程拥有自己的PID。fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，
# 而子进程中的返回值永远都是0。Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，
# 可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的封装，
# 例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。

from random import randint
from time import time, sleep


def download_task(filename):
    print('start to download %s ..' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download completed, use %d second' % (filename, time_to_download))


def main():
    start = time()
    download_task('python 100 days.pdf')
    download_task('Peking Hot.avi')

    end = time()
    print('Overall time spend %.2f second' % (end - start))


if __name__ == '__main__':
    main()
