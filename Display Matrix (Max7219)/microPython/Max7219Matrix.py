import sys
if sys.platform != 'rp2': # raspian pico
    print(40 * "-")
    print(">>>>>> Demo for Respberry Pi Pico <<<<<<")
    print(40 * "-")
    quit()
    
"""
    about   : Max7219Matrix is IDisplay inherrited class for displaying
              on a max 7219 matrix connected to a pico
    Version : 1.0.0
    Date    : 10 April 2024
    
    MAX7219 driver: https://github.com/mcauser/micropython-max7219
    Note: this driver is designed for 4-in-1 MAX7219 modules.
"""

from machine import Pin, SPI
from utime import sleep
from Max7219 import Matrix8x8

PIXELS_MODULE_WIDTH: int = 8
PIXELS_MODULE_HEIGHT:int = 8
PIXELS_HEIGHT = PIXELS_MODULE_WIDTH
PSI_CHANNEL = 0
SCROLL_DELAY = 50  # MAX7219 display scrolling speed (ms)
SLEEP_ANIMATION = .5
PIXEL_ON = 1
PIXEL_OFF = 0

_pin_sck = 2
_pin_mosi = 3
_pin_cs = 5
_brightness = 4
number_of_modules_x = 4
number_of_modules_y = 1
_width  = number_of_modules_x * PIXELS_MODULE_WIDTH
_height = number_of_modules_y * PIXELS_MODULE_HEIGHT

spi = SPI(PSI_CHANNEL, sck=Pin(pin_sck), mosi=Pin(pin_mosi))
cs = Pin(pin_cs, Pin.OUT)
display = Matrix8x8(spi, cs, number_of_modules_x * number_of_modules_y)
display.brightness(_brightness)

display.text("Hoi", 2, 1)
display.show()

