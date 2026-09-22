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
    
  
  
  
  
  
