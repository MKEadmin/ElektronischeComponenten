## LED RGB 5mm

<img src="LED RGB_Photo.jpg" alt="Photo of the component">
<img src="LED RGB_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description
What is an RGB LED?

An RGB LED is a single LED package that contains three smaller LEDs: Red, Green, and Blue. These three LEDs can be combined in various ways to produce different colors.

Types of RGB LEDs:
	1.	Common Cathode: All three LEDs share a single cathode (negative) pin, and each color has its own anode (positive) pin.
	2.	Common Anode: All three LEDs share a single anode (positive) pin, and each color has its own cathode (negative) pin.

Pins in an RGB LED:
	•	4 pins: One common pin and three separate pins for Red, Green, and Blue.
	•	The longest pin is usually the common pin (cathode or anode).

How to Use an RGB LED with a Raspberry Pi Pico and PWM

The Raspberry Pi Pico can control the brightness and color of an RGB LED using Pulse Width Modulation (PWM). PWM allows you to control the intensity of each color channel by varying the duty cycle of the signal.

1. Materials Needed

	•	Raspberry Pi Pico.
	•	RGB LED (common cathode or anode).
	•	Resistors (220–330 ohms, one for each LED channel).
	•	Breadboard and jumper wires.

2. Circuit Setup

	1.	Identify the RGB LED Pins:
	•	Determine if your RGB LED is common cathode or common anode. This information is crucial for wiring.
	2.	Connect Resistors:
	•	Attach a 220–330 ohm resistor to each color pin (R, G, B).
	3.	Connect the Common Pin:
	•	For common cathode: Connect the longest pin (common cathode) to the Pico’s GND.
	•	For common anode: Connect the longest pin (common anode) to the Pico’s 3.3V.
	4.	Connect the Color Pins:
	•	Connect each of the color pins (via the resistor) to separate GPIO pins on the Pico that support PWM. For example:
	•	Red to GPIO 15.
	•	Green to GPIO 14.
	•	Blue to GPIO 13.

3. Write Code to Control the RGB LED with PWM

You can use MicroPython to control the RGB LED using PWM.
Example code at the end of this page.

4. Explanation of the Code

	•	PWM Setup: The PWM object is initialized for each GPIO pin connected to the RGB LED.
	•	Frequency: PWM frequency is set to 1000 Hz for smooth control.
	•	Duty Cycle: The duty_u16() function sets the intensity for each color, with values ranging from 0 (off) to 65535 (full brightness).
	•	set_color Function: Adjusts the intensity of Red, Green, and Blue independently.

5. Tips and Troubleshooting

	•	Check Resistor Values: Ensure the resistors match the specifications of your RGB LED.
	•	Color Mixing: Combine different intensities of Red, Green, and Blue to create various colors. For example:
	•	Yellow: Red = 65535, Green = 65535, Blue = 0.
	•	Cyan: Red = 0, Green = 65535, Blue = 65535.
	•	Magenta: Red = 65535, Green = 0, Blue = 65535.
	•	Common Cathode vs. Anode: If the LED doesn’t light up, check whether you’ve wired it for the correct type (common cathode or anode).

## Order
<a href="https://nl.aliexpress.com/item/1005006140674321.html">https://nl.aliexpress.com/item/1005006140674321.html</a>
<img src="LED RGB_Order.jpg" alt="Photo of the Order">

##  Versions

<img src="LED RGB_Wiring.jpg" alt="Wiring" >

##  Versions

<img src="LED_Wiring.jpg" alt="Wiring" >

## Python example code

```python
from machine import Pin, PWM
import time

# Set up PWM for each color
red = PWM(Pin(15))
green = PWM(Pin(14))
blue = PWM(Pin(13))

# Set PWM frequency
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Function to set RGB color
def set_color(r, g, b):
    # Set duty cycle (0–65535)
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# Example: Fade colors
while True:
    for i in range(0, 65536, 256):  # Gradually increase intensity
        set_color(i, 0, 0)  # Red
        time.sleep(0.01)
    for i in range(0, 65536, 256):
        set_color(0, i, 0)  # Green
        time.sleep(0.01)
    for i in range(0, 65536, 256):
        set_color(0, 0, i)  # Blue
        time.sleep(0.01)
```
