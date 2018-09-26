from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 发起链接
server_addr=('0.0.0.0',8888)
sockfd.connect(server_addr)


# 消息发送接收
while True:
    data = input('发送>>')
    if not data:
        break
    sockfd.send(data.encode())
    # 消息接收
    data = sockfd.recv(1024)
    print('接收到:',data.decode())

# 关闭套接字
sockfd.close()



