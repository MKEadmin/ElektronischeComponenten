from machine import Pin
import utime as time
import dht

sensor = dht.DHT22(Pin(28))

while True:
    time.sleep(5)
    print(f"Temperature: {sensor.temperature}, Humidity: {sensor.humidity}")
