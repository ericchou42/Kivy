import socket
import time

# 創建socket
host = '172.17.75.2'  # 指定IP地址
port = 100             # 指定端口號

# 創建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))  # 連接到伺服器

# 持續讀取數據
while True:
    data = sock.recv(1024).decode('utf-8').strip()  # 從socket接收數據
    if data:
        print(f"{data}")
    else:
        time.sleep(0.1)  # 如果沒數據，稍微等待一段時間

sock.close()  # 關閉socket