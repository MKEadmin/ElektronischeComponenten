## LED Neopixel 5mm

<img src="LED Neopixel_Photo.jpg" alt="Photo of the component">
<img src="LED Neopixel_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description
NeoPixel LEDs are smart RGB LEDs that can be individually controlled for color and brightness using a single data line. They are based on WS2812B or similar ICs, which integrate the LED and the controller into one package. These LEDs are popular for projects that require complex lighting effects, as they allow for easy chaining and require minimal wiring.

DIN -> Connect to the digital Pin
DOUT -> Connect to the DIN of the next neo pixel
VDD -> 5 V
VSS/GROUND -> Connect to ground

Key Features of NeoPixel LEDs:

	1.	Integrated Controller:
	•	Each LED has its own controller chip.
	•	Colors are specified using an 8-bit value for each channel (Red, Green, Blue), resulting in 24-bit color depth.
	2.	Single-Wire Communication:
	•	All LEDs are connected in series, requiring only one data line to control the entire strip or matrix.
	3.	Chaining Capability:
	•	LEDs can be daisy-chained, meaning the data from one LED is passed to the next.
	4.	Precise Timing:
	•	NeoPixels require precise timing signals for communication, typically using a microcontroller.

How to Use NeoPixel LEDs with a Raspberry Pi Pico

The Raspberry Pi Pico can control NeoPixels using libraries such as MicroPython’s neopixel module or Adafruit’s CircuitPython.

1. Materials Needed
```
	•	Raspberry Pi Pico.
	•	NeoPixel LED strip or individual NeoPixel LEDs.
	•	Resistor (330 ohms, optional but recommended).
	•	Capacitor (1000 µF, optional but recommended for stability).
	•	External power supply (if powering many LEDs).
```
2. Circuit Setup
```
	1.	Connect Power:
	•	Connect the NeoPixel strip’s VCC (usually 5V) to an external 5V power source.
	•	If the Pico is powering a small number of LEDs (e.g., <10), you can connect VCC to the Pico’s VSYS pin (if the Pico is powered via USB).
	2.	Connect Ground:
	•	Connect the NeoPixel strip’s GND to the power supply’s ground.
	•	Also connect the power supply’s ground to the Pico’s GND.
	3.	Connect Data:
	•	Connect the NeoPixel strip’s DIN (data in) to a GPIO pin on the Pico (e.g., GPIO 15).
	•	Place a 330-ohm resistor between the GPIO pin and the NeoPixel’s DIN pin to protect against voltage spikes.
	4.	Add Capacitor (Optional but Recommended):
	•	Place a 1000 µF capacitor across the NeoPixel’s VCC and GND to stabilize the voltage.
```
3. Install MicroPython’s NeoPixel Library
```
	•	The neopixel module is included in MicroPython for the Raspberry Pi Pico.
```
4. Write Code to Control the NeoPixels

At the end of this page is an example using MicroPython.

5. Explanation of the Code
```
	1.	neopixel.NeoPixel():
	•	Initializes the NeoPixel object, specifying the GPIO pin and the number of LEDs.
	2.	np[i] = (r, g, b):
	•	Sets the color for a specific LED using RGB values (0–255).
	3.	np.write():
	•	Sends the updated color data to the LEDs.
```
6. Tips for Using NeoPixels
```
	•	Power Considerations:
	•	Each NeoPixel LED can draw up to 60 mA at full brightness (white, 255,255,255). Ensure your power supply can handle the total current.
	•	Voltage Level:
	•	NeoPixels are typically 5V devices, but the Pico operates at 3.3V. Most NeoPixels will still accept 3.3V data, but if you encounter issues, use a logic level shifter.
	•	Heat Dissipation:
	•	If using many LEDs at high brightness, consider heat dissipation as they can get warm.
```

7. Advanced Features
```
	•	Animations: Create effects like chasing, fading, or rainbow patterns.
	•	Individual Control: Control each LED in the strip for custom effects:
```

```python
np[0] = (255, 0, 0)  # First LED Red
np[1] = (0, 255, 0)  # Second LED Green
np.write()
```
	•	Libraries for Complex Effects: Use libraries like Adafruit CircuitPython for advanced effects.

## Order
<a href="https://nl.aliexpress.com/item/1005006140674321.html">https://nl.aliexpress.com/item/1005006140674321.html</a>
<img src="LED Neopixel_Order.jpg" alt="Photo of the Order">

##  Versions

<img src="LED Neopixel_Wiring.jpg" alt="Wiring" >

## Python example code

```python
import machine
import neopixel
import time

# Configuration
NUM_PIXELS = 8  # Number of LEDs in the NeoPixel strip
PIN_NUM = 15    # GPIO pin connected to the NeoPixel's DIN

# Initialize NeoPixel
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

# Function to set all LEDs to a color
def set_color(r, g, b):
    for i in range(NUM_PIXELS):
        np[i] = (r, g, b)  # Set the color for each LED
    np.write()  # Send the data to the LEDs

# Example: Cycle through colors
while True:
    set_color(255, 0, 0)  # Red
    time.sleep(1)
    set_color(0, 255, 0)  # Green
    time.sleep(1)
    set_color(0, 0, 255)  # Blue
    time.sleep(1)
```
