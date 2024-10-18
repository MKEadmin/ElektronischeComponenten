from RoterySwitch import RoterySwitch

PIN_PREV = 14
PIN_NEXT = 15
PIN_PRESSED = 22


value = 0
def prevValue():
    global value
    value -= 1
    print("Prev", value)
    
def nextValue():
    global value
    value += 1
    print("Next", value)
    
def pressed():
    print("Pressed")


changer = RoterySwitch(PIN_PREV, PIN_NEXT, prevValue, nextValue, PIN_PRESSED, pressed, False)
    
while True:
    machine.idle() # Delay to prevent excessive CPU usage

