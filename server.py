# Remote desktop
import socket
import threading
import numpy as np
import cv2
import os
from PIL import ImageGrab
from pynput.mouse import Button, Controller
# from vidgear.gears import VideoGear

# 发送屏幕内容
def send_screen(client):
    img_quality = 25; # 图像质量
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), img_quality]
    while True:
        img = ImageGrab.grab(bbox = (0, 0, 500, 500))
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) # 转为opencv的BGR格式
        img_cv = cv2.resize(img_cv, (1000, 1000))
        img_encode = cv2.imencode(".jpg", img_cv, encode_param)[1]
        data_encode = np.array(img_encode)
        str_encode = data_encode.tobytes()
        # print(f"str_encode len = {len(str_encode)}")

        client.send(str(len(str_encode)).zfill(12).encode('utf-8') + str_encode)

def main():
    listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 2052
    listen.bind((host, port))
    listen.listen(5)
    client, addr = listen.accept()
    client.send('成功连接到服务器'.encode('utf-8'))
    #开启一个线程向客户端发送屏幕内容
    t = threading.Thread(target = send_screen, args = (client,))
    t.start()

if __name__ == '__main__':
    main()