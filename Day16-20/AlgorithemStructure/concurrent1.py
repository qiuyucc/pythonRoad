'''
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
'''

import glob
import os
import threading

from PIL import Image

PREFIX='thumbnails'

def generate_thumbnail(infile,size,format='PNG'):
    '''generate thumbnail for specific pic'''