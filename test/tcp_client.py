"""
tcp_client.py
tcp客户端流程
"""

from socket import *

while True:
    # 创建tcp套接字
    sockfd = socket() # 默认参数就是tcp

    # 链接服务端
    server_addr = ('172.40.91.205',8888)
    sockfd.connect(server_addr)

# # 发消息
# while True:
#     data = input(">>")
#     if not data:
#         break
#     sockfd.send(data.encode()) # 发送字节串
#     # if data == '##':
#     #     break
#     msg = sockfd.recv(1024)
#     print("Server:",msg.decode())    # 服务端回复内容
#
# #关闭套接字
# sockfd.close()









