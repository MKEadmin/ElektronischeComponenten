from machine import Pin, I2C
from time import sleep
from HW111 import HW111  # Assuming you name the file hw111.py

# Initialize I2C bus (adjust the pins as per your hardware setup)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialize HW111 RTC with I2C
rtc = HW111(i2c)

# Set the current date and time: (year, month, day, weekday, hour, minute, second, subseconds)
rtc.datetime((2024, 10, 11, 5, 11, 18, 30, 0))

# Loop to print the current datetime every second
while True:
    dt = rtc.datetime()
    print(f"Date={dt[1]:02}/{dt[2]:02}/{dt[0]:4} Time={dt[4]:02}:{dt[5]:02}:{dt[6]:02}")
    sleep(1)

