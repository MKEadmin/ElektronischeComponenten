## ADC (ADS1115)

<img src="ADS1115_Photo.jpg" alt="Photo of the component">
<img src="ADS1115_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description
The **ADS1115** is a 16-bit analog-to-digital converter (ADC) from Texas Instruments. It features a programmable gain amplifier (PGA) and communicates via an I²C interface, making it ideal for precision measurement applications requiring small package size and low power consumption.

### Key Features:
- **16-bit resolution**: Provides highly accurate digital conversions from analog signals.
- **4 input channels**: Can be used as four single-ended inputs or two differential inputs.
- **Programmable Gain Amplifier (PGA)**: Adjustable gain settings allow amplification of smaller signals, with gain options ranging from ±0.256V to ±6.144V.
- **I²C interface**: Enables easy communication with microcontrollers or other I²C devices. It supports standard (100 kHz), fast (400 kHz), and high-speed (3.4 MHz) modes.
- **Data rates**: Selectable data rates from 8 to 860 samples per second (SPS), allowing a trade-off between speed and precision.
- **Low power consumption**: Ideal for battery-operated devices, with a current consumption of just 150 µA during conversions and 0.5 µA in power-down mode.
- **Internal voltage reference** and **clock**: No need for external components for precision timing or reference voltage.
- **Operating voltage**: Typically operates at 2.0V to 5.5V, making it compatible with a wide range of systems.
- **Size**: Available in small packages like the MSOP-10 and VSSOP-10.

### Common Applications:
- Sensor measurements (temperature, light, pressure)
- Data acquisition systems
- Portable instrumentation
- Industrial monitoring

Its high resolution, versatility in input channels, and ease of integration make the ADS1115 a popular choice for projects that require accurate analog-to-digital conversion with low power demands.

## Order
<a href="https://nl.aliexpress.com/item/1005006143923238.html">https://nl.aliexpress.com/item/1005006143923238.htm</a>
<img src="ADS1115_Order.jpg" alt="Photo of the Order">

## Wiring to Raspberry Pi Pico
<img src="ADS1115_Wiring.jpg" alt="Wiring" >

## Installation libraries
Copy next files to the Raspberry Pi Pico

```bash
ADS1115.py
```

## Example code
```python
from ADS1115 import ADC
from machine import I2C, Pin

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
ADDRESS = i2c.scan()[0]

adc = ADC(i2c, ADDRESS)


print(f"Voltage : {adc.readVolts(ADC.A0)} Volt")
print(f"decimal : {adc.readValue(ADC.A0)}")
```



