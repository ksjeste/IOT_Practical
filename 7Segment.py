import sys
import time
import datetime
import RPi.GPIO as GPIO
import tml1637

GPIO.setmode(GPIO.BCM)

Display=tml1637.TM1637()
Display.Clear()
Display.SetBrightness(1)
while True:
    now=datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    #currenttime=[int(hour/10),hour%10,int(minute/10),minute%10] OR
    currenttime=[int(minute/10),minute%10,int(second/10),second%10]
    
    Display.Show(currenttime)
    Display.ShowDoublepoint(second%2)
    
    time.sleep(1)
