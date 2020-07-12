# coding=utf-8                   #让Python可以识别中文
# 加载 GPIO 库、time 库
import RPi.GPIO as GPIO  # 引入库
import time  # 引入库
# import cs

# 定义 GPIO 引脚
GPIO.setmode(GPIO.BOARD)  # 使用GPIO.BOARD模式，采用物理地址对GPIO引脚进行编号
GPIO.setwarnings(False)
SCLK = 36
RCLK = 38
DIO = 40

# 设置 GPIO 引脚为输出
LED_PINS = [36, 38, 40]
for led_pin in LED_PINS:
    GPIO.setup(led_pin, GPIO.OUT)
# 定义字模
LED_Library = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90, 0x8C,
               0xBF, 0xC6, 0xA1, 0x86, 0x8E, 0xbf]


def Show(i_data):
    while i_data > 10000:  # 限制数据大小
        i_data = i_data - 10000
    if (i_data >= 1000):
        i_show1 = i_data // 1000  # 确定千位
        i_data -= 1000 * i_show1
    else:
        i_show1 = 0
    if (i_data >= 100):
        i_show2 = i_data // 100  # 确定百位
        i_data -= 100 * i_show2
    else:
        i_show2 = 0
    if (i_data >= 10):
        i_show3 = i_data // 10  # 确定十位
        i_data -= 10 * i_show3
    else:
        i_show3 = 0
    i_show4 = i_data  # 确定个位
    LED4_Display(i_show1, 0x08)  # 显示个位
    time.sleep(0.001)
    LED4_Display(i_show2, 0x04)  # 显示十位
    time.sleep(0.001)
    LED4_Display(i_show3, 0x02)  # 显示百位
    time.sleep(0.001)
    LED4_Display(i_show4, 0x01)  # 显示千位
    time.sleep(0.001)


def LED4_Display(i_index, hx_location):  # 定义显示数字的函数
    LED_OUT(LED_Library[i_index])  # 输出字模
    LED_OUT(hx_location)  # 输出位地址
    GPIO.output(RCLK, GPIO.LOW)  # 在 RCLK 输出向上脉冲
    GPIO.output(RCLK, GPIO.HIGH)  # 在 RCLK 输出向下脉冲


def LED_OUT(X):
    for i in range(0, 8):
        if (X & 0x80):  # X与0x80与操作，判断第一位是否为1
            GPIO.output(DIO, GPIO.HIGH)  # 在 DIO 输出向上脉冲
        else:

            GPIO.output(DIO, GPIO.LOW)   # 在 DIO 输出向下脉冲
        GPIO.output(SCLK, GPIO.LOW)  # 在 SCLK 输出向上脉冲
        GPIO.output(SCLK, GPIO.HIGH)  # 在 SCLK 输出向下脉冲
        X <<= 1  # X左移一位

# while True:
#     Show(2020)
#     cs.getdis()
#     time.sleep(0.000002)
#     Show(cs.data)
#     # time.sleep(0.000002)
