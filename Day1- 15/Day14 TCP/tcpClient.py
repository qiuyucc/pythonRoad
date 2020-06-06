# TCP 客户端

from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4 和 TCP 协议
    client = socket()
    # 2.connect to server (IP and port)
    client.connect(('192.168.1.2', 6789))
    # 3.receive data from server
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
