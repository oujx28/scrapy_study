# -*- coding:utf-8 -*-
import socket

HOST = 'agps.u-blox.com'
PORT = 46434

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'user=mike.jiang@pashine.cn;pwd=Xugwp;cmd=full;lat=30.604186;lon=114.303220;pacc=3000000000')
    data = s.recv(1024)
    print(data)

