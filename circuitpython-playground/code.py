import adafruit_sdcard
import busio
import digitalio
import board
import storage
from analogio import AnalogIn
import time
import supervisor
import interaction

mode, r = interaction.wait_for_input()  

# Connect to the card and mount the filesystem.
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

sampling_rate = 10



# Use the filesystem
with open("/sd/ee392d_samples.txt", "a") as f:
    f.write("-" * 20)
    f.write("\n" + mode + "\n")
    f.write("-" * 20)

    # measure A0 and A2
    analog_in0 = AnalogIn(board.A0)
    analog_in2 = AnalogIn(board.A2)

    def get_voltage(pin):
        return ((pin.value * 3.3) / 65536)

    def get_current(pin):
        return ((pin.value * 3.3) / 65536)

    for _ in range(r):

        measurementsA0 = []
        measurementsA2 = []
        for _ in range(sampling_rate):
            measurementsA0.append(get_voltage(analog_in0))
            measurementsA2.append(get_current(analog_in2))
            time.sleep(1 / sampling_rate)
        mA0 = sum(measurementsA0) / len(measurementsA0)
        mA2 = sum(measurementsA2) / len(measurementsA2)
        print("Time: " + str(time.monotonic()))
        print("Voltage: " + str(mA0*2,))
        print("")
        f.write("\n" + str(time.monotonic())+", " + str(mA0*2,))
    f.write("\n")
