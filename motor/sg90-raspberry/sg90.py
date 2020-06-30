import RPi.GPIO as GPIO
import time

class sg90():
    def __init__(self, motor_pin):
        self.motor_pin = motor_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motor_pin, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(motor_pin, 50)  # 50HZ
        self.p.start(0)

    def get_duty_cycle(self, angle):
        if angle < 0 or angle > 180:
            return -1
        return 2.5 + 10 * angle / 180

    def set_angle(self, angle):
        self.p.ChangeDutyCycle(self.get_duty_cycle(angle))
        time.sleep(1)
        self.p.ChangeDutyCycle(0)

    def reset_angle(self):
        self.p.ChangeDutyCycle(self.get_duty_cycle(0))
        time.sleep(1)
        self.p.ChangeDutyCycle(0)


motor1=sg90(26)
while(1):
    motor1.set_angle(90)
    motor1.set_angle(0)
    pass
