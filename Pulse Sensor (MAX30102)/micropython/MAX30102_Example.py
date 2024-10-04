from machine import Pin, I2C
import time
from max30102 import MAX30102

# Initialiseer I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialiseer MAX30102 sensor
sensor = MAX30102(i2c=i2c)

while True:
    # Lees de hartslag en SPO2 waarde uit
    sensor.read_sensor()
    heart_rate = sensor.ir_value  # Lees de IR waarde voor hartslag
    spo2 = sensor.red_value       # Lees de rode LED waarde voor SPO2

    print("Hartslag: ", heart_rate)
    print("SpO2: ", spo2)

    time.sleep(1)

