import adafruit_sdcard
import busio
import digitalio
import board
import storage
from analogio import AnalogIn
import time

# Connect to the card and mount the filesystem.
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Use the filesystem
with open("/sd/test.txt", "w") as f:
    f.write("Hello world\n")


# measure A0
analog_in = AnalogIn(board.A0)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2

while True:
    print((get_voltage(analog_in),))
    time.sleep(0.5)
