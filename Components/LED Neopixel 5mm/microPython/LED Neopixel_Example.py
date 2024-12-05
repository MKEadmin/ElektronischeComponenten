import machine
import neopixel

# Configuration
NUM_PIXELS = 2  # Number of LEDs in the NeoPixel strip
PIN_NUM = 15    # GPIO pin connected to the NeoPixel's DIN

# Initialize NeoPixel
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

np[0] = (255,   0,   0)  # Set the color for each LED
np[1] = (  0, 255,   0)  # Set the color for each LED
np.write()  # Send the data to the LEDs