from vidstream import AudioSender

import threading
import socket


ip = input('what is the ip : ')
port1 = 6969

sender = AudioSender(ip, port1)
sender_thread = threading.Thread(target=sender.start_stream)

sender_thread.start()
