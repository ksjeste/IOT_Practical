from collections import deque
import time
import board
import busio
import numpy as np
import matplotlib.pyplot as plt
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation

#=======================SETTINGS============================
DURATION = 10 #SECONDS SHOWN ON THE SCREEN
SAMPLE_RATE = 128
GAIN = 1
CHANNEL = 0
I2C_ADDRESS = 0X48
#===========================================================
#I2C SETUP
i2c = busio.I2C(board.SCL,board.SDA)
ads = ADS1115(i2c,address=I2C_ADDRESS)
ads.data_rate = SAMPLE_RATE
ads.gain = GAIN
chan = AnalogIn(ads,CHANNEL)
#Buffer
num_samples = SAMPLE_RATE * DURATION
x = np.linspace(0,DURATION,num_samples)
y = deque([0.0]*num_samples,maxlen=num_samples)

#Plot
fig, ax = plt.subplots()
ax.set_xlim(0,DURATION)
ax.set_ylim(-4.2,4.2)
ax.set_xlabel("Time[s]")
ax.set_ylabel("Voltage[V]")
ax.set_title("ADS1115 Software Oscilloscope")
ax.grid(True)

line, =ax.plot(x,y,lw=1)

#Update loop
def update(frame):
    try:
        voltage = chan.voltage
    except Exception:
        voltage=0.0
    y.append(voltage)
    line.set_ydata(y)
    return line,

#animation
ani=FuncAnimation(
    fig,
    update,
    interval=1000/SAMPLE_RATE,
    blit=True
    )

plt.show()