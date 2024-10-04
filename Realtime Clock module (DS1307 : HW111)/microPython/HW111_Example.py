from machine import Pin, I2C
from time import sleep
from hw111 import HW111

# Initialize I2C on Raspberry Pi Pico
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialize HW111 RTC with the I2C object
rtc = HW111(i2c)

# Set the date and time on the RTC
rtc.set_datetime(year=2024, month=12, day=31, hour=23, minute=59, second=50)

# Print the date and time in a loop
while True:
    dt = rtc.get_datetime()
    print(f"Date={dt['month']:02}/{dt['day']:02}/{dt['year']:4} Time={dt['hour']:02}:{dt['minute']:02}:{dt['second']:02}")
    sleep(1)
