# 客户端
from inspect import ArgSpec
import socket
import threading
import cv2
import numpy as np
from PIL import ImageGrab
from pynput.mouse import Button, Controller

m = Controller()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 2052
    server.connect((host, port))

    conn_str = server.recv(1024)
    print(conn_str.decode('utf-8'))

    # t = threading.Thread(target = receive_screen, args = (server,))
    # t.start()
    while True:
        # recv_msg = server.recv(102400)

        f = open("out.txt", 'rb')
        recv_msg = f.read()

        msg_str = np.fromstring(recv_msg, np.uint8)
        img_decode = cv2.imdecode(msg_str, cv2.IMREAD_COLOR)
        
        cv2.imshow('Client', img_decode)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()