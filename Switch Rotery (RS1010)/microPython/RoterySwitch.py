from machine import Pin
from utime import sleep

class RoterySwitch:
    _moveUp = None #callback when moving up
    _moveDown = None #callback when moving up
    
    def __init__(self, pinA, pinB, callbackUp, callbackDown, pinButton, callbackPressed, debug = False):
        self._pinA 		 = Pin(pinA, Pin.IN )#, Pin.PULL_UP) 
        self._pinB 		 = Pin(pinB, Pin.IN )#, Pin.PULL_UP)
        self._pinPressed = Pin(pinButton, Pin.IN )
        self._debug = debug
        self._callbackUp = callbackUp
        self._callbackDown = callbackDown
        self._callbackPressed = callbackPressed
        
        if callbackUp != None or callbackDown != None:
            self._pinA.irq(trigger=Pin.IRQ_FALLING, handler=self.rotate)
        if callbackPressed != None:
            self._pinPressed.irq(trigger=Pin.IRQ_FALLING, handler=self._pressed)
    
    def _pressed(self, pin):
        self._pinPressed.irq(handler=None)
        self._callbackPressed()
        sleep(0.3)
        if self._debug:
            print("Pressed", self._pinPressed.value())
        self._pinPressed.irq(handler=self._pressed)
        
            
    def rotate(self, pin):
        if self._pinB.value() == 1:
            if self._debug:
                print("Up")
            if self._callbackUp != None:
                self._callbackUp()
        else:
            if self._debug:
                print("Down")
            if self._callbackDown != None:
                self._callbackDown()

if __name__ == "__main__":
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

    changer    = RoterySwitch(14, 15, prevValue, nextValue, 22, pressed, False)
        
    while True:
        machine.idle() # Delay to prevent excessive CPU usage
    
            
            
            