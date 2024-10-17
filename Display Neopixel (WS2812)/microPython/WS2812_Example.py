import random
from machine import Pin
import neopixel

PIN_DIN = 28
PIXELS_X = 16
PIXELS_Y = 16
PIXELS = PIXELS_X * PIXELS_Y

positions = []
for x in range(PIXELS):
    positions.append(x)

_np = neopixel.NeoPixel(Pin(PIN_DIN), PIXELS)


def clear():
    for x in positions:
        _np[x] = (0, 0, 0)
    _np.write()


def showPixel(p, color):
    _np[p] = color
    _np.write()


clear()
while True:
    x = random.choice(positions)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    showPixel(x, (r, g, b))
    showPixel(x, (0, 0, 0))
