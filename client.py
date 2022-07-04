# Local
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

    recv_bytes = bytes()
    header_size = 12

    # 在主线程中接收服务器屏幕内容
    while True:
        # recv_msg = server.recv(102400)
        # TODO 分包
        # f = open("out.txt", 'rb')
        # recv_msg = f.read()

        recv_bytes += server.recv(1024)
        if len(recv_bytes) == 0:
            continue
        len_bytes = int(recv_bytes[:header_size])
        if len(recv_bytes) - header_size < len_bytes:
            continue
        msg_str = np.frombuffer(recv_bytes[header_size : header_size + len_bytes], np.uint8)
        img_decode = cv2.imdecode(msg_str, cv2.IMREAD_COLOR)
        recv_bytes = recv_bytes[header_size + len_bytes:]

        cv2.namedWindow('client', 0)
        cv2.resizeWindow('client', 500, 500)
        # cv2.startWindowThread()
        cv2.imshow('client', img_decode)

        if cv2.waitKey(100) & 0xff == ord('q'):
            break
        # cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()