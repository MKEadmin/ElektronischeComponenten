'''TC74_VARIANT:
    A0 = 0x48
    A1 = 0x49
    A2 = 0x4A
    A3 = 0x4B
    A4 = 0x4C
    A5 = 0x4D
    A6 = 0x4E
    A7 = 0x4F'''

from machine import Pin, I2C
from time import sleep

i2c_interface = 0
sdapin = Pin(16)
sclpin = Pin(17)
i2c = I2C(i2c_interface, scl = sclpin, sda = sdapin, freq=100000)
#tc74address = 0x48 #we gebruiken tc74 A0 en A3 in de opstelling!
tc74address = 0x4B

while True:
    data = i2c.readfrom(tc74address, 1, True)
    
    temp = int.from_bytes(data, "big")
    print('Temperature: %3.1f C' %temp)
    
    sleep(1)
    
# def ReadTemperature():
#     data = i2c.readfrom(tc74address, 1, True)
#     temp1 = int.from_bytes(data, "big")
#     return temp1