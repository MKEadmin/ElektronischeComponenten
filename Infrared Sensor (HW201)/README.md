## HW201 - LCD display with i2c module
<img src="HW201_Photo.jpg" alt="Photo of the component">
<img src="HW201_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Where stored
Cupboard __1__ Drawer __2__  position __A3__

## Description
The HW-201 is a simple and affordable hall effect magnetic sensor module that detects the presence or absence of a magnetic field. It is commonly used in embedded electronics projects to detect the proximity of magnetic objects, measure magnetic fields, or as a switch that activates when a magnet is nearby. This sensor is primarily used for non-contact sensing applications, such as proximity switches, motor speed detection, and other magnetic field sensing tasks.

Key Features

	•	Hall Effect Sensor: Based on a hall effect sensor that detects changes in a magnetic field.
	•	Digital Output: Provides a binary (high or low) output signal based on the presence of a magnetic field.
	•	Sensitivity: High sensitivity to magnetic fields.
	•	Operating Voltage: Typically operates between 3.3V and 5V, making it compatible with microcontrollers like Arduino and Raspberry Pi.
	•	Adjustable Sensitivity: Some modules may include a potentiometer to adjust the sensitivity of the magnetic field detection.
	•	Indicator LED: An onboard LED indicates when a magnetic field is detected.
	•	Compact Size: Small and easy to integrate into various projects.

Working Principle

The HW-201 module works using the hall effect principle. When the sensor is placed in a magnetic field, it generates a voltage (the Hall voltage) that is proportional to the strength of the magnetic field. This voltage is then processed and converted into a digital signal (either high or low) that can be easily read by a microcontroller.

	•	Output Low (Active): When a magnetic field of sufficient strength is detected, the sensor’s output pin goes LOW (0V or close to 0V), and the onboard LED turns on.
	•	Output High (Inactive): When no magnetic field is detected, the sensor’s output pin goes HIGH (typically 3.3V or 5V), and the onboard LED remains off.

Pin Configuration

The HW-201 sensor module typically has 3 pins:

	1.	VCC: Power supply pin, usually connected to a 3.3V or 5V source.
	2.	GND: Ground pin.
	3.	OUT: Digital output pin that provides either HIGH or LOW based on magnetic field detection.

Operating Specifications

	•	Operating Voltage: 3.3V to 5V (typically 5V).
	•	Output Type: Digital (high or low).
	•	Magnetic Sensitivity: Varies based on the hall sensor used; generally, it can detect a magnetic field strength of around 10 to 100 mT.
	•	Indicator LED: Lights up when the sensor detects a magnetic field.

Applications

The HW-201 magnetic sensor module is used in a wide range of applications where magnetic field detection is required, including:

	1.	Proximity Sensing: Detects the proximity of a magnetic object, such as a door or window.
	2.	Speed Measurement: In motors, the sensor can be used to detect the rotation speed by measuring the number of magnetic poles passing by.
	3.	Position Detection: Measures the position of objects that have embedded magnets, such as in robotics or automotive applications.
	4.	Contactless Switches: Acts as a contactless switch that activates when a magnet is brought close to the sensor.
	5.	Magnetic Field Detection: Measures changes in magnetic fields for scientific or experimental purposes.

Example Code for Arduino

Here’s a simple example of how to use the HW-201 sensor module with an Arduino:

```cpp
int hallSensorPin = 2;  // The pin where the sensor is connected
int sensorState = 0;    // Variable to store the sensor's state

void setup() {
  pinMode(hallSensorPin, INPUT);  // Set the sensor pin as input
  Serial.begin(9600);             // Initialize serial communication
}

void loop() {
  // Read the state of the hall effect sensor
  sensorState = digitalRead(hallSensorPin);
  
  if (sensorState == LOW) {  // Magnetic field detected
    Serial.println("Magnet detected!");
  } else {                   // No magnetic field
    Serial.println("No magnet detected.");
  }
  
  delay(500);  // Delay for half a second
}
```

In this code:

	•	digitalRead() is used to read the state of the sensor (LOW when a magnetic field is detected, HIGH when no field is present).
	•	The Serial Monitor is used to display the sensor status in real time.

Advantages

	•	Low Cost: Inexpensive and easy to source for hobby projects and prototyping.
	•	Simple to Use: Provides a simple digital output, making it easy to interface with microcontrollers.
	•	Non-Contact Sensing: Can detect magnetic fields without needing physical contact with the magnet, making it ideal for non-intrusive sensing applications.
	•	Compact and Portable: Small size and lightweight, making it easy to integrate into various projects.

Limitations

	•	Limited Sensing Distance: The sensing distance is limited to the proximity of the magnet (usually a few millimeters to a centimeter), meaning it needs to be close to the magnetic source for detection.
	•	No Analog Output: The sensor only provides a binary (high or low) output, so it cannot measure the strength of the magnetic field directly. For applications requiring analog field strength measurement, an analog hall effect sensor would be better.
	•	Magnet Dependent: Requires the presence of a magnetic field to operate; will not work in environments without magnets.

Conclusion

The HW-201 Hall Effect Magnetic Sensor Module is a simple and effective tool for detecting the presence or absence of a magnetic field. With its straightforward digital output and low cost, it is an ideal choice for beginners and hobbyists working on proximity sensors, contactless switches, or other magnetic detection applications. The module’s ease of use and compatibility with popular microcontrollers like Arduino and Raspberry Pi make it a versatile component for a wide range of DIY electronics projects.

## Order
<a href="https://nl.aliexpress.com/item/1005006385279953.html">https://nl.aliexpress.com/item/1005006385279953.html</a>
<img src="HW201_Order.jpg" alt="Photo of the Order">

## Wiring to Raspberry Pi Pico
<img src="HW201_Wiring.jpg" alt="Wiring" >

## Installation libraries
Copy next files to the Raspberry Pi Pico

```bash

```

## Example code
```python


```




