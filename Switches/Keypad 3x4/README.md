## Switch Keypad Hard

<img src="Keypad_Photo.jpg" alt="Photo of the component">
<img src="Keypad_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description
see <a href="https://learn.adafruit.com/matrix-keypad/pinouts">here </a> for pinout of the keypad

## Order
<a href="https://www.otronic.nl/nl/3x4-matrix-keypad-zwart.html">https://www.otronic.nl/nl/3x4-matrix-keypad-zwart.htm</a>
<img src="Keypad_Order.jpg" alt="Photo of the Order">


## Wiring to Raspberry Pi Pico
<img src="Keypad_Wiring.jpg" alt="Wiring" >

## Installation libraries
copy the next files to the pico
```bash
 numlock3x4.py
```

## Example code
```python
from numlock3x4 import read_key #Libary for the numlock
from utime import sleep

user_Code = []
while True: 
    key = read_key()	#reads numpad inputs
    print(key)
    sleep(.1)


```



