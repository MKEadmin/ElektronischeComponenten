## DAC (MCP4725)

<img src="MCP4725_Photo.jpg" alt="Photo of the component">
<img src="MCP4725_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description
The MCP4725 is a 12-bit Digital-to-Analog Converter (DAC) with non-volatile memory (EEPROM), manufactured by Microchip Technology. It is commonly used in microcontroller-based projects and systems to generate an analog output from a digital signal. Here’s a detailed description:

Key Features

	•	12-bit Resolution DAC: Provides a 12-bit resolution, meaning the digital input can range from 0 to 4095, resulting in fine granularity for the output voltage.
	•	Output Voltage Range: The analog output voltage ranges from 0V to VDD (usually 3.3V or 5V, depending on the supply voltage).
	•	EEPROM (Non-Volatile Memory): Allows the DAC output to retain its value even after power is removed and restored.
	•	I2C Interface: Communicates via the I2C protocol, making it easy to interface with microcontrollers like Arduino, Raspberry Pi, and others.
	•	Two I2C Addresses: You can select between two I2C addresses, allowing for two devices on the same I2C bus (using the A0 address pin).
	•	Fast Update Rate: Can update the analog output quickly (up to 3.4 MHz I2C speed).
	•	Low Power Consumption: Typical active current is about 0.33 mA, and standby current is as low as 0.06 µA.

Package Types

	•	Available in small, surface-mount packages such as SOT-23-6.

Pin Description

	1.	VDD: Power supply pin (typically 3.3V or 5V).
	2.	GND: Ground pin.
	3.	SCL: I2C clock line (connects to the SCL line of the microcontroller or host).
	4.	SDA: I2C data line (connects to the SDA line of the microcontroller or host).
	5.	VOUT: The DAC analog output pin (produces an analog voltage based on the digital input).
	6.	A0: I2C address selection pin. It allows you to configure the I2C address by connecting it to GND (address 0x60) or VDD (address 0x61).

Block Diagram Overview

The MCP4725 consists of three main sections:

	1.	12-bit DAC Core: Converts the digital input from the I2C bus into an analog voltage.
	2.	Reference and Power Supply: Provides the voltage reference for the DAC output, which can be the VDD supply voltage.
	3.	EEPROM Memory: Stores the DAC value for non-volatile operation. This ensures that even if the device loses power, the output voltage will return to the saved value upon restart.

Communication Protocol

The MCP4725 uses the I2C (Inter-Integrated Circuit) protocol, which allows multiple devices to communicate with a microcontroller using only two lines (SCL and SDA). It supports the following features:

	•	I2C Speed: Up to 3.4 MHz (high-speed mode), though commonly used at 100 kHz or 400 kHz.
	•	7-bit Address: The default I2C address is 0x60 when A0 is connected to GND, or 0x61 when A0 is connected to VDD.
	•	I2C Commands: The microcontroller writes to the DAC register by sending I2C commands with a 12-bit digital value, which sets the output voltage.

Operating Modes

	1.	Normal Mode: The DAC continuously converts the digital input to analog output.
	2.	Power-Down Modes: The DAC can enter low-power states to save energy, reducing current consumption to microamps when the DAC output is not needed.

Using MCP4725 in a Project

	•	Input Range: The 12-bit DAC input takes values between 0 and 4095. This input determines the output voltage as a fraction of the reference voltage (usually the supply voltage VDD). For example:
￼
Where:
	•	￼ is the analog output voltage.
	•	￼ is the 12-bit digital value (0-4095).
	•	￼ is the supply voltage (typically 3.3V or 5V).
	•	EEPROM Programming: You can store a DAC output value in EEPROM using I2C commands, allowing the MCP4725 to retain this value after a power cycle.

Applications

	•	Analog Signal Generation: Useful in audio signal processing, waveform generation, and other systems that require converting digital data into an analog signal.
	•	Control Systems: Often used to control actuators, such as motors and valves, where an analog signal is needed.
	•	Sensor Calibration: Can provide precise analog voltages for sensor calibration.
	•	Function Generators: Combined with microcontroller programming, it can create various waveforms (sine, triangle, square) for testing and signal processing.
	•	Voltage Reference: In precision applications where an adjustable reference voltage is needed.

Advantages

	•	High Accuracy: 12-bit resolution means fine control over the output voltage.
	•	Non-Volatile Memory: The integrated EEPROM allows the DAC output to be restored after power loss, which is particularly useful for systems that need to maintain state after a reboot.
	•	I2C Simplicity: The I2C protocol requires only two pins, reducing the number of microcontroller I/O pins needed for communication.
	•	Low Power: Suitable for battery-powered and low-power applications.

Typical Circuit Connection

To use the MCP4725 with a microcontroller like an Arduino or Raspberry Pi:

	•	VDD → 3.3V or 5V
	•	GND → Ground
	•	SCL → I2C Clock (Arduino pin A5 for I2C)
	•	SDA → I2C Data (Arduino pin A4 for I2C)
	•	A0 → Either GND or VDD (to select the I2C address)
	•	VOUT → The generated analog output

Example Code (Arduino)

```C
#include <Wire.h>
#include <Adafruit_MCP4725.h>
Adafruit_MCP4725 dac;

void setup()
{
  Serial.begin(9600);
  dac.begin(0x60);  // Initialize DAC at I2C address 0x60
}

void loop()
{
  for (uint16_t i = 0; i < 4096; i++)
  {
    dac.setVoltage(i, false);  // Set the DAC output voltage
    delay(1);  // Small delay to see the output change
  }
}
```

Limitations

	•	Fixed Output Reference: The DAC uses the supply voltage (VDD) as the reference voltage, so its output precision depends on the stability of the power supply.
	•	Single Channel: Only one output channel, which limits its use in multi-channel applications.

Conclusion

The MCP4725 is a versatile and easy-to-use 12-bit DAC with built-in EEPROM and I2C interface. It is ideal for applications requiring analog signal generation, precision voltage control, and systems that need to retain DAC output values after power cycles. Its small size, low power consumption, and high resolution make it popular in both hobbyist projects and professional designs.

## Order
<a href="https://nl.aliexpress.com/item/1005006459299143.html">https://nl.aliexpress.com/item/1005006459299143.htm</a>
<img src="MCP4725_Order.jpg" alt="Photo of the Order">


## Wiring to Raspberry Pi Pico
<img src="MCP4725_Wiring.jpg" alt="Wiring" >

## Installation libraries
Copy next files to the Raspberry Pi Pico

```bash

```

## Example code
```python



```



