import subprocess
import time

NAME = "Manisha"  # Put your name here
last_uid = None

try:
    while True:
        output = subprocess.getoutput("nfc-list")

        if "UID" in output:
            for line in output.splitlines():
                if "UID" in line:
                    uid = line.split(":")[1].strip().replace(" ", "")

                    if uid != last_uid:
                        print(f"{NAME}: {uid}")
                        last_uid = uid
                        break

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped")
    
  
  
  
  
  
  
  
  
  
  
  
  
  
sudo raspi-config
manisha@raspberrypi:~ $ pip3 install adafruit-circuitpython-pn532 --break-system-packages
manisha@raspberrypi:~ $ sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools
sudo nano /etc/nfc/libnfc.conf


