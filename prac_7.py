#GND - 6, VCC - 2, IN1 - 26, IN2 - 24, IN3 - 21
"""
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
relay_pin=26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin,GPIO.OUT)
GPIO.output(relay_pin,1)
try:
    while True:
        GPIO.output(relay_pin,0)
        sleep(5)
        GPIO.output(relay_pin,1)
        sleep(5)
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
"""
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
relay_pin1=26
relay_pin2=24
relay_pin3=21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin1,GPIO.OUT)
GPIO.setup(relay_pin2,GPIO.OUT)
GPIO.setup(relay_pin3,GPIO.OUT)
GPIO.output(relay_pin1,1)
GPIO.output(relay_pin2,1)
GPIO.output(relay_pin3,1)
try:
    while True:
        GPIO.output(relay_pin1,0)
        sleep(5)
        GPIO.output(relay_pin2,0)
        sleep(5)
        GPIO.output(relay_pin3,0)
        sleep(5)
        GPIO.output(relay_pin1,1)
        sleep(5)
        GPIO.output(relay_pin2,1)
        sleep(5)
        GPIO.output(relay_pin3,1)
        sleep(5)
except KeyboardInterrupt:
    pass
    GPIO.cleanup()