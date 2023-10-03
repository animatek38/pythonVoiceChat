import time

from vidstream import AudioReceiver

import threading
import socket


#ip = input('what is the ip')
#port input('and the port')


ip = ''
port1 = 6969

receiver = AudioReceiver(ip, port1)
receive_thread = threading.Thread(target=receiver.start_server)

receive_thread.start()

while True:
    time.sleep(1)
    print("Server is running...")