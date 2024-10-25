from machine import Pin, SPI
from Max7219 import Matrix8x8

PSI_CHANNEL = 0 # Sets SPI channel to 0
PIN_SCK = 2     # shows to which pin it needs to be connected on the Raspberry pi pico
PIN_MOSI = 3    # shows to which pin it needs to be connected on the Raspberry pi pico
PIN_CS = 5      # shows to which pin it needs to be connected on the Raspberry pi pico

BRIGHTNESS = 4  		 # Select the brightness of the screen(ranges from 0-15)
number_of_modules_x = 4  # The number of Screens connected in the X access(width)
number_of_modules_y = 1  # The number of screens conencted in the Y access(height)

spi = SPI(PSI_CHANNEL, sck=Pin(PIN_SCK), mosi=Pin(PIN_MOSI))
cs = Pin(PIN_CS, Pin.OUT)

display = Matrix8x8(spi, cs, number_of_modules_x * number_of_modules_y)
display.brightness(BRIGHTNESS)

display.text("hi!!", 2, 1)  # Enter the text you wish to display
display.show()  			# This actualy shows the text on the display