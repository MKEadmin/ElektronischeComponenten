from machine import Pin
import utime

#https://www.youtube.com/watch?v=7-PoXmxeCmQ&t=116s

# Create a map between keypad buttons and characters
MATRIX_KEYS = (('1', '2', '3', 'A'),
               ('4', '5', '6', 'B'),
               ('7', '8', '9', 'C'),
               ('*', '0', '#', 'D'))

# Define PINs according to cabling
GPIO_KEYPAD_Y = (6,7,8,9) 
GPIO_KEYPAD_X = (2,3,4,5) 

PIN_X = []
PIN_Y = []
def init():
    for gpio in GPIO_KEYPAD_Y:
        PIN_Y.append(Pin(gpio, Pin.OUT))
    for gpio in GPIO_KEYPAD_X:
        PIN_X.append(Pin(gpio, Pin.IN, Pin.PULL_DOWN))
    for pin in PIN_Y:
        pin.value(0)
    for pin in PIN_X:
        pin.value(0)
    
"""
    return the coordinates of the key pressed
"""
def keyPressed():
    for y in range( len( PIN_Y)  ):
        PIN_Y[y].high() # set the rows high one by one
        for x in range( len( PIN_X) ): 
            if PIN_X[x].value() == 1: # check which col is checked
                return (y, x), MATRIX_KEYS[x][y]    
        PIN_Y[y].low()
    return None, None

init()

if "__main__" == __name__:
    while True:
        key = keyPressed()
        utime.sleep(0.2)
        if key[0] != None:
            print(key[0], key[1])
        
        
        
        
