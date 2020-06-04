# 接下来我们将重点放在如何实现两个进程间的通信。我们启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个。
# 听起来很简单吧，但是如果这样写可是错的哦。


from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.1)


def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()

if __name__ == '__main__':
    main()