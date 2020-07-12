import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
    id, text = reader.read()
    print(id)
    text_b=bytes(text,encoding='windows-1252')
    text=text_b.decode('gbk') 
    print(text)
finally:
    GPIO.cleanup()