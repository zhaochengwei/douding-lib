import RPi.GPIO as GPIO
import json
import serial
LED1_PIN=37
LED2_PIN=38
GPIO.setwarnings(False) 	#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering format
GPIO.setup(LED1_PIN, GPIO.OUT)	#set GPIO as output
GPIO.setup(LED2_PIN, GPIO.OUT)	#set GPIO as output
ser = serial.Serial("/dev/rfcomm0",9600,timeout=0.5)
buffer_string=''
while True:
    try:
        
        buffer_string = buffer_string + ser.read(ser.inWaiting()).decode('utf-8')
        if '}' in buffer_string:
            lines = buffer_string.split('}"') # Guaranteed to have at least 2 entries
            buffer_string=lines[0]
            print('I am recv:',buffer_string)
            recv_parsed=json.loads(buffer_string)
            GPIO.output(recv_parsed["p"],recv_parsed["v"])
            buffer_string=''
    except Exception as e:
        print(e)

