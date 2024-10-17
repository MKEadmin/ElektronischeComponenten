from machine import I2C, Pin
import time
import bme280  # Assuming you've uploaded a 'bme280.py' driver file

# Initialize I2C interface
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

# Initialize BME280 sensor
sensor = bme280.BME280(i2c=i2c)

while True:
    # Read temperature, pressure, and humidity
    temperature, pressure, humidity = sensor.read_compensated_data()

    # Convert temperature to Celsius
    temperature = temperature / 100
    pressure = pressure / 256  # Convert pressure to hPa
    humidity = humidity / 1024  # Convert humidity to percentage

    # Print values
    print("Temperature: {:.2f}°C".format(temperature))
    print("Pressure: {:.2f} hPa".format(pressure))
    print("Humidity: {:.2f}%".format(humidity))

    # Sleep for 1 second before the next read
    time.sleep(1)
