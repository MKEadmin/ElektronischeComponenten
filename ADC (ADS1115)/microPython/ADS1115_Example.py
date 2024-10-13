from ADS1115 import ADC
from machine import I2C, Pin

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
ADDRESS = i2c.scan()[0]

adc = ADC(i2c, ADDRESS)


print(f"Voltage : {adc.readVolts(ADC.A0)} Volt")
print(f"decimal : {adc.readValue(ADC.A0)}")