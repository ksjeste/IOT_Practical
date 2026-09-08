"""one LED
#import RPi.GPIO as GPIO
import time
numTimes=int(input("Enter total number of times to blink: "))
speed=float(input("Enter length of each blink(seconds): "))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)	#using physical pin numbers
GPIO.setup(11, GPIO.OUT)	#LED1
def Blink(numTimes,speed):
    for i in range(numTimes):
            print("Iteration:", i+1)
            GPIO.output(11,True)  #LED1 ON
            time.sleep(speed)
            GPIO.output(11,False)  #LED1 OFF
            time.sleep(speed)
Blink(numTimes,speed)
GPIO.cleanup()
print("Done")
"""

#2 LED
"""import RPi.GPIO as GPIO
import time
numTimes=int(input("Enter total number of times to blink: "))
speed=float(input("Enter length of each blink(seconds): "))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)	#using physical pin numbers
GPIO.setup(11, GPIO.OUT)	#LED1
GPIO.setup(3,GPIO.OUT)		#LED2
def Blink(numTimes,speed):
    for i in range(numTimes):
            print("Iteration:", i+1)
            GPIO.output(11,True)  #LED1 ON
            time.sleep(speed)
            GPIO.output(3,False)  #LED2 OFF
            time.sleep(speed)
            GPIO.output(3,True)  #LED2 ON
            time.sleep(speed)
            GPIO.output(11,False)  #LED1 OFF
            time.sleep(speed)
Blink(numTimes,speed)
GPIO.cleanup()
print("Done")
"""
#4 LED
import RPi.GPIO as GPIO
import time
numTimes=int(input("Enter total number of times to blink: "))
speed=float(input("Enter length of each blink(seconds): "))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)	#using physical pin numbers
GPIO.setup(11, GPIO.OUT)	#LED1
GPIO.setup(3,GPIO.OUT)#LED2
GPIO.setup(31,GPIO.OUT)#LED3
GPIO.setup(40,GPIO.OUT)#LED4
def Blink(numTimes,speed):
    for i in range(numTimes):
            print("Iteration:", i+1)
            GPIO.output(11,True)  #LED1 ON
            time.sleep(speed)
            GPIO.output(3,True)  #LED2 ON
            time.sleep(speed)
            GPIO.output(31,False) #LED3 OFF
            time.sleep(speed)
            GPIO.output(40,False)  #LED4 OFF
            time.sleep(speed)
            GPIO.output(11,False)  #LED1 ON
            time.sleep(speed)
            GPIO.output(3,False)  #LED2 ON
            time.sleep(speed)
            GPIO.output(31,True) #LED3 OFF
            time.sleep(speed)
            GPIO.output(40,True)  #LED4 OFF
            time.sleep(speed)
            
Blink(numTimes,speed)
GPIO.cleanup()
print("Done")




