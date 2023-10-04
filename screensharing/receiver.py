from vidstream import StreamingServer
import threading
import socket
import time

ip = input("what ip : ")
port = 6969

receiver = StreamingServer(ip, port)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    time.sleep(3)
    print("[*] - Listening on", port,"...")
    continue

receiver.stop_server()