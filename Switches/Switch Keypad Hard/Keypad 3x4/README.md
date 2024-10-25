## Switch Keypad Hard

<img src="Keypad_Photo.jpg" alt="Photo of the component">
<img src="Keypad_QR_code.jpg" alt="QR code to this page" width="80" height="80">

## Description

## Order
<a href="https://www.otronic.nl/nl/3x4-matrix-keypad-zwart.html">https://www.otronic.nl/nl/3x4-matrix-keypad-zwart.htm</a>
<img src="Keypad_Order.jpg" alt="Photo of the Order">


## Wiring to Raspberry Pi Pico
<img src="Keypad_Wiring.jpg" alt="Wiring" >

## Installation libraries
```bash
Copy numlock_3x4 to the Raspberry Pico
```

## Example code
```python
from numlock_3x4 import read_key		#Libary for the numlock

user_Code = []
while True: 
    key = read_key()	#reads numpad inputs
    if key != None:
        user_Code.append(key)
        if key == "#":
            print(user_Code)
            user_Code = []
```



