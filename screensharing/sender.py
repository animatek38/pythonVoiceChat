from vidstream import ScreenShareClient
import threading
import socket
import time

#ip = socket.gethostbyname(socket.gethostname())
ip = '127.0.0.1'
port = 6969

sender = ScreenShareClient(ip, port)

t = threading.Thread(target=sender.start_stream)

print("[!] - The receiver needs to put your ip to receive")

while input("") != 'STOP':
    time.sleep(3)
    print("[*] - Sending", port,"...")
    continue

sender.stop_stream()

while True:
    try:
        t.start()
    except:
        continue
    break
    