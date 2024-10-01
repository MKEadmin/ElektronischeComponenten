from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

PIN_DHT = 28
pin_dht = Pin(PIN_DHT, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin_dht)

while True:
    time.sleep(5)
    print(f"Temperature: {sensor.temperature}, Humidity: {sensor.humidity}")
