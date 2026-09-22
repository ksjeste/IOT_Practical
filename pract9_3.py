import board
import busio
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)

print("Waiting for card to read stored data...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is not None:
        key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

        if pn532.mifare_classic_authenticate_block(uid, 4, 0x60, key):
            data = pn532.mifare_classic_read_block(4)

            if data is not None:
                print(f"Stored Data: {data.decode().strip()}")
                break