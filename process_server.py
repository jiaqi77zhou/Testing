from socket import *
from multiprocessing import Process
import sys,signal

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
        sys.exit('服务退出')
    except Exception as e:
        print(e)
        continue

    # 创建进程处理客户端请求
    p = Process(target=handle,args=(c,))
    p.daemon = True # 父进程服务结束,子进程也退出服务
    p.start()

