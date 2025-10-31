from machine import Pin
from time import sleep

# Define the GPIO pin connected to the relay module input
relay = Pin(15, Pin.OUT)

# Active LOW relay logic
def relay_on():
    relay.value(0)   # turn ON (LOW signal)
    print("Relay ON")

def relay_off():
    relay.value(1)   # turn OFF (HIGH signal)
    print("Relay OFF")

# Initialize with relay off
relay_off()

# Test loop
while True:
    relay_on()
    sleep(2)
    relay_off()
    sleep(2)