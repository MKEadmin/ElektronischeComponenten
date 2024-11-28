# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-bme280-micropython/
from machine import Pin, I2C
from time import sleep
from BME280 import BME280

# Initialize I2C communication
i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=40000)

# Initialize BME280 sensor
bme = BME280(i2c=i2c)
        
while True:
    try:
        # Print sensor readings
        print("--------------------------------------")
        print(f"Temperature: {bme.getTemperature()[0]:10.2f}")
        print(f"Humidity   : {bme.getHumidity()[0]:10.2f}")
        print(f"Pressure   : {bme.getPressure()[0]:10.2f}")
        
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(5)

