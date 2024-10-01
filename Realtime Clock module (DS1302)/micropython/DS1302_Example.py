from machine import Pin
from time import sleep
from ds1302 import DS1302

PIN_CLK = 0
PIN_DIO = 1
PIN_CS  = 2

# Initialize DS1302 RTC with specified pins (clk, dio, cs)
ds = DS1302(Pin(PIN_CLK),Pin(PIN_DIO),Pin(PIN_CS))

# Set the date and time on the RTC
ds.year  (2024)
ds.month (12)
ds.day   (31)
ds.hour  (23)
ds.minute(59)
ds.second(50)

# Print the date and time
while True:
    print( f"Date={ds.month():2}/{ds.day():2}/{ds.year():4} Time={ds.hour():02}:{ds.minute():02}:{ds.second():02}")
    sleep(1)

