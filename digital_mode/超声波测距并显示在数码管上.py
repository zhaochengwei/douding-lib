# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import LED2
import threading
import queue

import random

TRIG = 3
ECHO = 5
# data=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def checkdist():
    global show_queue
    global TRIG
    global ECHO
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    # 超声波模块的读取时序为给定一定时间的高电平，然后检测输出引脚的电平跳变并计时，根据时间计算距离
    GPIO.output(TRIG, GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    t1 = time.time()
    while GPIO.input(ECHO):
        pass
    t2 = time.time()
    show_queue.put((t2-t1)*34000/2)  # 得到距离，单位mm
    threading.Timer(1, checkdist).start()

def random_gen():
    global show_queue
    data1=random.randint(1, 1000)
    print(data1)
    show_queue.put(data1)
    threading.Timer(1, random_gen).start()

show_queue = queue.Queue()
threading.Timer(1, checkdist).start()
show_data=0
while True:
    # global data
    # data = round(checkdist(),1)*10    #将得到的距离保存在data里，单位是m
    if not show_queue.empty():
        show_data=int(show_queue.get())
    LED2.Show(show_data)
    # data = int(checkdist())
    # print(data)
    # LED2.Show((data))
    # print('距离为： ',data,' mm')
    # time.sleep(1)
