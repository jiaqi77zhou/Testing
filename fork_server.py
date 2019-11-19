"""
fork_server.py  fork多进程网络并发
重点代码

流程思路:
   创建监听套接字
   等待接收客户端请求
   客户端连接,创建新的进程处理客户端请求
   原进程继续等待其他客户端连接
   如果客户端退出，则销毁对应的进程
"""

from socket import *
import os
import signal

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

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888...")
# 循环等待客户端链接
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)   # 处理客户端具体请求
        os._exit(0)  # 处理完客户端请求后子进程退出
    else:
        c.close()
