from machine import Pin, PWM
import time

# Set up PWM for each color
red = PWM(Pin(15))
green = PWM(Pin(14))
blue = PWM(Pin(13))

# Set PWM frequency
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Function to set RGB color
def set_color(r, g, b):
    # Set duty cycle (0–65535)
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# Example: Fade colors
while True:
    for i in range(0, 65536, 256):  # Gradually increase intensity
        set_color(i, 0, 0)  # Red
        time.sleep(0.01)
    for i in range(0, 65536, 256):
        set_color(0, i, 0)  # Green
        time.sleep(0.01)
    for i in range(0, 65536, 256):
        set_color(0, 0, i)  # Blue
        time.sleep(0.01)