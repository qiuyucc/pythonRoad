from socket import socket
from json import loads
from base64 import b64encode


def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
    # define a varible to store binary data
    in_data = bytes()
    # receive 1024 every time
    data = client.recv(1024)
    while data:
        # combine the data
        in_data += data
        data = client.recv(1024)
    # convert json to dictionary
    # using loads to convert
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # convert base64 data to binary data and write into file
        f.write(b64encode(filedata))
    print('pic has been saved')


if __name__ == '__main__':
    main()
