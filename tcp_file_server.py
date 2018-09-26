from socket import *
import os
import sys

class Myftp():
    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST,self.PORT)

    def my_sf(c):
        while True:
            data = c.recv(2048)
            if data.decode() == 1:
                ftp_chakan()
            elif data.decode() == 2:
                ftp_xiazai(c)
            elif data.decode() == 3:
                ftp_shangchuan()

    def ftp_xiazai(c):
        data = c.recv(2048)
        f = open(data.decode())

HOST = ''
PORT = 8888
ADDR = (HOST,PORT)


def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    while True:
        try:
            c,addr = self.s.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print('Error:',e)
            continue

        pid = os.fork()

        if pid == 0:
            s.close()
            my_sf(c)
        else:
            c.close()
            continue 








