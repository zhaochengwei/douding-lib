import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522
import json
reader = SimpleMFRC522()
try:
    user_name = input('用户名:')
    user_id = input('id:')
    print("Now place your tag to write")
    data={"n":user_name,'d':user_id}
    reader.write(json.dumps(data))
    print("Written")
finally:
    GPIO.cleanup()