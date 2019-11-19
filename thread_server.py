"""
thread_server.py
重点代码

思路:
    创建监听套接字
    循环接收客户端连接请求
    当有新的客户端连接创建线程处理客户端请求
    主线程继续等待其他客户端连接
    当客户端退出，则对应分支线程退出
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 与客户端交互,处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")
# 循环等待客户端链接
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务退出')
    except Exception as e:
        print(e)
        continue

    # 创建线程处理客户端请求
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True) # 主线程服务结束,分支线程也退出服务
    t.start()











