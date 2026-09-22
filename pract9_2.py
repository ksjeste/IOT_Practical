import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Setup I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)

print("--- NFC Writer ---")

text_to_write = input("Enter a small message to save to the card: ")

# Data must be exactly 16 bytes for a single block
data = text_to_write.ljust(16).encode()

print("Now, place your white card on the reader...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is not None:
        try:
            # Use block 4 (Sector 1)
            key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

            if pn532.mifare_classic_authenticate_block(uid, 4, 0x60, key):
                pn532.mifare_classic_write_block(4, data)
                print(f"Success! '{text_to_write}' written to card.")
                break
            else:
                print("Authentication failed!")

        except Exception as e:
            print(f"Error: {e}")
            break