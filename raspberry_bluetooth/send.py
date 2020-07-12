import RPi.GPIO as GPIO
import json
import serial

ser = serial.Serial("/dev/ttyUSB0",9600)
while True:
    try:
        pin_sel = input("请输入要控制的LED管脚：");
        pin_value = input("请输入设置值：");
        data={"p":int(pin_sel),"v":int(pin_value)}
        send_str=json.dumps(data).replace(' ', '')
        print("准备发送 {}".format(send_str))
        ser.write(send_str.encode('utf-8'))
    except Exception as e:
        print(e)