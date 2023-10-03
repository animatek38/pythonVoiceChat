from vidstream import ScreenShareClient
import threading
import socket


#ip = socket.gethostbyname(socket.gethostname())
ip = '127.0.0.1'
port = 6969

sender = ScreenShareClient(ip, port)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()