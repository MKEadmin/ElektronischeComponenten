import machine
import neopixel
import time

# Configuration
NUM_PIXELS = 8  # Number of LEDs in the NeoPixel strip
PIN_NUM = 15    # GPIO pin connected to the NeoPixel's DIN

# Initialize NeoPixel
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

# Function to set all LEDs to a color
def set_color(r, g, b):
    for i in range(NUM_PIXELS):
        np[i] = (r, g, b)  # Set the color for each LED
    np.write()  # Send the data to the LEDs

# Example: Cycle through colors
while True:
    set_color(255, 0, 0)  # Red
    time.sleep(1)
    set_color(0, 255, 0)  # Green
    time.sleep(1)
    set_color(0, 0, 255)  # Blue
    time.sleep(1)