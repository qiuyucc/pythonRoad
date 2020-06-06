#requests是一个基于HTTP协议来使用网络的第三库，其官方网站有这样的一句介绍它的话：
# “Requests是唯一的一个非转基因的Python HTTP库，人类可以安全享用。”简单的说，使用requests库可以非常方便的使用HTTP，
# 避免安全缺陷、冗余代码以及“重复发明轮子”（行业黑话，通常用在软件工程领域表示重新创造一个已有的或是早已被优化過的基本方法）



from time import time
from threading import Thread

import requests

# inheriten Thread class to create Thread
class DownloadHandler(Thread):

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfin('/')+1:]
        resp = requests.get(self.url)

def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    print(data_model)
    # for mm_dict in data_model['newslist']:
    #     url = mm_dict['picUrl']
    #     # 通过多线程的方式实现图片下载
    #     DownloadHandler(url).start()


if __name__ == '__main__':
    main()