from vidstream import StreamingServer
import threading
import socket

ip = input("what ip : ")
port = 6969

receiver = StreamingServer(ip, port)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()