from vidstream import AudioReceiver

import threading
import socket


#ip = input('what is the ip')
#port input('and the port')
ip = '92.157.93.242'
port1 = 6969

receiver = AudioReceiver('localhost', port1)
receive_thread = threading.Thread(target=receiver.start_server)

receive_thread.start()
