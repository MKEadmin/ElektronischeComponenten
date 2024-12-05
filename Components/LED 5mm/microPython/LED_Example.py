from machine import Pin
import time

# Set up GPIO pin 15 as an output
led = Pin(15, Pin.OUT)

# Blink the LED
while True:
    led.on()  # Turn the LED on
    time.sleep(1)  # Wait for 1 second
    led.off()  # Turn the LED off
    time.sleep(1)  # Wait for 1 second