from vidstream import StreamingServer
import threading
import socket
import time

ip = input("what ip : ")
port = 6969

receiver = StreamingServer(ip, port)

t = threading.Thread(target=receiver.start_server)
t.start()

while ip == ip:
    time.sleep(3)
    t.start()
    print("[*] - Listening on","'",ip,"'","port","'",port,"'","...")

while input("") != 'STOP':
    continue

receiver.stop_server()