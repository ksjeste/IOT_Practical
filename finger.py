 fingerprint program starts

import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

print("Successfully imported fingerprint module")

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
except Exception as e:
    print('Exception Message: ' + str(e))
    exit(1)


def enrollFinger():
    print('Enrolling Finger')
    time.sleep(3)

    print('Place Finger')
    while f.readImage() == False:
        pass

    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print('Template already exists at position #' + str(positionNumber))
        time.sleep(2)
        return

    print('Remove finger')
    time.sleep(2)

    print('Place same finger again')
    while f.readImage() == False:
        pass

    f.convertImage(0x02)

    if f.compareCharacteristics() == 0:
        print('Fingers do not match')
        time.sleep(2)
        return

    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully')
    print('Stored at position: ' + str(positionNumber))
    time.sleep(2)


def searchFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            pass

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(2)
            return False
        else:
            print('Found template at position ' + str(positionNumber))
            time.sleep(2)
            return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)


def deleteFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            pass

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(2)
            return False
        else:
            if f.deleteTemplate(positionNumber):
                print('Finger Deleted')
                time.sleep(2)
                return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)


time.sleep(1)

print('Start')

while True:
    i = int(input("\nEnter:\n1. Enroll\n2. Search\n3. Delete\n4. Exit\n"))

    if i == 1:
        enrollFinger()
    elif i == 2:
        searchFinger()
    elif i == 3:
        deleteFinger()
    elif i == 4:
        break
    else:
        print("Invalid option! Enter Correct")

# fingerprint program ends